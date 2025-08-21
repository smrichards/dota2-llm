#!/usr/bin/env python3
"""
Script to collect Dota 2 training data from OpenDota API
Usage: python scripts/collect_data.py [--matches NUM] [--api-key KEY]
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_collection import OpenDotaCollector, TrainingDataGenerator
import config

def main():
    parser = argparse.ArgumentParser(description="Collect Dota 2 training data")
    parser.add_argument("--matches", type=int, default=config.DEFAULT_NUM_MATCHES,
                       help="Number of matches to process")
    parser.add_argument("--api-key", type=str, default=config.OPENDOTA_API_KEY,
                       help="OpenDota API key")
    parser.add_argument("--output", type=str, default=str(config.TRAINING_DATA_FILE),
                       help="Output file path")
    parser.add_argument("--delay", type=float, default=config.API_DELAY,
                       help="Delay between API requests")
    
    args = parser.parse_args()
    
    print("=== Dota 2 LLM Data Collection ===")
    print(f"Target matches: {args.matches}")
    print(f"API Key: {'Yes' if args.api_key else 'No (Free tier)'}")
    print(f"Output file: {args.output}")
    
    # Initialize collector
    collector = OpenDotaCollector(api_key=args.api_key, delay=args.delay)
    
    # Test API connection
    print("\nTesting API connection...")
    test_heroes = collector.get_heroes()
    if not test_heroes:
        print("Failed to connect to OpenDota API")
        return 1
    print(f"✓ Connected successfully, found {len(test_heroes)} heroes")
    
    # Initialize data generator
    generator = TrainingDataGenerator(collector)
    
    # Collect training data
    print(f"\nStarting data collection...")
    training_data = generator.collect_training_data(args.matches)
    
    if training_data:
        # Save the data
        generator.save_training_data(training_data, args.output)
        
        # Show sample data
        print(f"\nSample training examples:")
        for i, example in enumerate(training_data[:3]):
            print(f"\n--- Example {i+1} ---")
            print(f"Q: {example['instruction']}")
            print(f"A: {example['output'][:100]}...")
    
    print(f"\n=== Data Collection Complete ===")
    print(f"Generated {len(training_data)} training examples")
    return 0

if __name__ == "__main__":
    sys.exit(main())