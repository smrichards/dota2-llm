# Dota 2 LLM Training - Step 1: Environment Setup and Data Collection

import requests
import json
import time
import pandas as pd
from datetime import datetime, timedelta
import os
from pathlib import Path

class OpenDotaCollector:
    def __init__(self, api_key=None, delay=1.5):
        """
        Initialize OpenDota data collector
        
        Args:
            api_key: OpenDota API key (None for free tier)
            delay: Delay between requests (seconds)
        """
        self.api_key = api_key
        self.delay = delay
        self.base_url = "https://api.opendota.com/api"
        
        # Setup headers
        self.headers = {'Content-Type': 'application/json'}
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'
    
    def make_request(self, endpoint):
        """Make API request with rate limiting"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                time.sleep(self.delay)  # Rate limiting
                return response.json()
            else:
                print(f"Error {response.status_code}: {url}")
                return None
                
        except Exception as e:
            print(f"Request failed: {e}")
            return None
    
    def get_recent_matches(self, limit=100, min_rank=5):
        """
        Get recent public matches
        
        Args:
            limit: Number of matches to fetch
            min_rank: Minimum skill level (5 = Ancient, 6 = Divine, 7 = Immortal)
        """
        endpoint = f"/publicMatches?min_rank={min_rank}"
        return self.make_request(endpoint)
    
    def get_match_details(self, match_id):
        """Get detailed match information"""
        endpoint = f"/matches/{match_id}"
        return self.make_request(endpoint)
    
    def get_heroes(self):
        """Get hero data"""
        endpoint = "/heroes"
        return self.make_request(endpoint)
    
    def get_items(self):
        """Get item data"""  
        endpoint = "/constants/items"
        return self.make_request(endpoint)

class TrainingDataGenerator:
    def __init__(self, collector):
        self.collector = collector
        self.heroes = {}
        self.items = {}
        self.load_game_data()
    
    def load_game_data(self):
        """Load hero and item data for reference"""
        print("Loading game constants...")
        
        # Load heroes
        heroes_data = self.collector.get_heroes()
        if heroes_data:
            self.heroes = {hero['id']: hero for hero in heroes_data}
            print(f"Loaded {len(self.heroes)} heroes")
        
        # Load items and create ID-based lookup
        items_data = self.collector.get_items()
        if items_data:
            # Convert from name-based dict to ID-based dict
            self.items = {}
            for item_name, item_data in items_data.items():
                if 'id' in item_data:
                    self.items[item_data['id']] = item_data
            print(f"Loaded {len(self.items)} items")
    
    def get_hero_name(self, hero_id):
        """Get hero name from ID"""
        return self.heroes.get(hero_id, {}).get('localized_name', f'Hero_{hero_id}')
    
    def get_item_name(self, item_id):
        """Get item name from ID"""
        if item_id in self.items:
            return self.items[item_id].get('dname', f'Item_{item_id}')
        return f'Item_{item_id}'
    
    def extract_player_items(self, player_data):
        """Extract item build from player data"""
        items = []
        
        # Get final items (item slots 0-5)
        for i in range(6):
            item_id = player_data.get(f'item_{i}')
            if item_id and item_id != 0:
                items.append(self.get_item_name(item_id))
        
        # Get backpack items
        for i in range(3):
            item_id = player_data.get(f'backpack_{i}')
            if item_id and item_id != 0:
                items.append(self.get_item_name(item_id))
                
        return items
    
    def analyze_match_for_training(self, match_data):
        """Extract training examples from a single match"""
        training_pairs = []
        
        if not match_data or 'players' not in match_data:
            return training_pairs
        
        # Basic match info
        match_id = match_data.get('match_id')
        duration_minutes = match_data.get('duration', 0) // 60
        radiant_win = match_data.get('radiant_win', False)
        
        # Analyze each player
        for i, player in enumerate(match_data['players']):
            hero_id = player.get('hero_id')
            if not hero_id:
                continue
                
            hero_name = self.get_hero_name(hero_id)
            is_radiant = i < 5
            won_game = (is_radiant and radiant_win) or (not is_radiant and not radiant_win)
            
            # Extract items
            items = self.extract_player_items(player)
            if len(items) < 3:  # Skip if too few items
                continue
            
            # Get performance stats
            kills = player.get('kills', 0)
            deaths = player.get('deaths', 0) 
            assists = player.get('assists', 0)
            gpm = player.get('gold_per_min', 0)
            xpm = player.get('xp_per_min', 0)
            
            # Generate training examples
            if won_game and (kills + assists) > deaths:  # Only use successful examples
                
                # Item build question
                enemy_heroes = []
                for j, enemy in enumerate(match_data['players']):
                    if (j < 5) != is_radiant:  # Opposite team
                        enemy_heroes.append(self.get_hero_name(enemy.get('hero_id')))
                
                item_build_qa = {
                    "instruction": f"What items should I build on {hero_name} against {', '.join(enemy_heroes[:3])}?",
                    "output": f"Based on a successful {duration_minutes}-minute match, consider building: {', '.join(items[:6])}. This build was effective against mobile cores and provided good survivability and utility for team fights."
                }
                training_pairs.append(item_build_qa)
                
                # Performance question
                if gpm > 400:  # Decent farm
                    performance_qa = {
                        "instruction": f"How do I play {hero_name} effectively?",
                        "output": f"Focus on your core items and positioning. In successful matches, {hero_name} averages {gpm} GPM and maintains a positive KDA. Key items include {', '.join(items[:4])}. Prioritize team fights after getting your core items around {duration_minutes//2} minutes."
                    }
                    training_pairs.append(performance_qa)
        
        return training_pairs
    
    def collect_training_data(self, num_matches=1000):
        """Collect training data from multiple matches"""
        training_data = []
        processed_matches = 0
        failed_requests = 0
        all_matches = []
        
        print(f"Starting data collection for {num_matches} matches...")
        
        # OpenDota API returns ~100 matches per request, so make multiple requests
        batches_needed = (num_matches // 100) + 1
        print(f"Making {batches_needed} API calls to get {num_matches} matches...")
        
        for batch in range(batches_needed):
            print(f"Fetching batch {batch + 1}/{batches_needed}...")
            recent_matches = self.collector.get_recent_matches(limit=100)
            
            if not recent_matches:
                print(f"Failed to get matches for batch {batch + 1}")
                continue
                
            all_matches.extend(recent_matches)
            print(f"Got {len(recent_matches)} matches in batch {batch + 1}")
            
            # Stop if we have enough matches
            if len(all_matches) >= num_matches:
                break
                
            # Small delay between batches to avoid rate limiting
            time.sleep(2)
        
        print(f"Collected {len(all_matches)} total matches from API")
        
        # Process the matches
        for match_info in all_matches[:num_matches]:
            match_id = match_info.get('match_id')
            if not match_id:
                continue
            
            print(f"Processing match {match_id} ({processed_matches + 1}/{num_matches})")
            
            # Get detailed match data
            match_details = self.collector.get_match_details(match_id)
            
            if match_details:
                # Extract training examples
                match_training_data = self.analyze_match_for_training(match_details)
                training_data.extend(match_training_data)
                processed_matches += 1
                
                if processed_matches % 50 == 0:
                    print(f"Processed {processed_matches} matches, generated {len(training_data)} training examples")
            else:
                failed_requests += 1
                if failed_requests > 10:
                    print("Too many failed requests, stopping...")
                    break
        
        print(f"Data collection complete!")
        print(f"Processed: {processed_matches} matches")
        print(f"Generated: {len(training_data)} training examples")
        print(f"Failed requests: {failed_requests}")
        
        return training_data
    
    def save_training_data(self, training_data, filename="dota2_training_data.jsonl"):
        """Save training data to JSONL format"""
        output_path = Path(filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for example in training_data:
                json.dump(example, f, ensure_ascii=False)
                f.write('\n')
        
        print(f"Saved {len(training_data)} training examples to {output_path}")

def main():
    # Configuration
    OPENDOTA_API_KEY = None  # Add your API key here for premium features
    NUM_MATCHES = 500  # Start with 500 matches for testing
    
    print("=== Dota 2 LLM Data Collection ===")
    print(f"Target matches: {NUM_MATCHES}")
    print(f"API Key: {'Yes' if OPENDOTA_API_KEY else 'No (Free tier)'}")
    
    # Initialize collector
    collector = OpenDotaCollector(api_key=OPENDOTA_API_KEY, delay=2.0)
    
    # Test API connection
    print("\nTesting API connection...")
    test_heroes = collector.get_heroes()
    if not test_heroes:
        print("Failed to connect to OpenDota API")
        return
    print(f"✓ Connected successfully, found {len(test_heroes)} heroes")
    
    # Initialize data generator
    generator = TrainingDataGenerator(collector)
    
    # Collect training data
    print(f"\nStarting data collection...")
    training_data = generator.collect_training_data(NUM_MATCHES)
    
    if training_data:
        # Save the data
        generator.save_training_data(training_data)
        
        # Show sample data
        print(f"\nSample training examples:")
        for i, example in enumerate(training_data[:3]):
            print(f"\n--- Example {i+1} ---")
            print(f"Q: {example['instruction']}")
            print(f"A: {example['output'][:100]}...")
    
    print(f"\n=== Data Collection Complete ===")
    print(f"Next step: Review the generated data and start model training!")

if __name__ == "__main__":
    main()