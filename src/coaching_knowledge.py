"""
Comprehensive Dota 2 coaching knowledge and terminology
Master module that imports all specialized coaching knowledge
"""

try:
    from .hero_guides import get_all_hero_guides
    from .matchup_analysis import get_all_matchup_analysis
    from .mmr_coaching import get_all_mmr_coaching
    from .draft_strategy import get_all_draft_strategy
    from .advanced_strategy import get_all_advanced_strategy
    from .web_scraping import get_all_scraped_knowledge
except ImportError:
    from hero_guides import get_all_hero_guides
    from matchup_analysis import get_all_matchup_analysis
    from mmr_coaching import get_all_mmr_coaching
    from draft_strategy import get_all_draft_strategy
    from advanced_strategy import get_all_advanced_strategy
    from web_scraping import get_all_scraped_knowledge

def get_advanced_coaching_examples():
    """Return advanced coaching examples covering all aspects of Dota 2"""
    
    return [
        # Advanced Mechanics
        {
            "instruction": "What is animation canceling in Dota 2? How do I practice it?",
            "output": "Animation canceling means stopping your attack/spell animation after the damage/effect triggers. Right-click to move immediately after attack lands, or use stop command. Practice with Shadow Fiend - cancel backswing after each raze. Improves DPS and repositioning speed."
        },
        {
            "instruction": "What is creep aggro and how do I manipulate it?",
            "output": "Creep aggro means enemy creeps targeting you. Right-click enemy heroes within 500 range to draw creeps, then immediately click away. Use this to pull creeps for easier last hits, deny enemy farm, or reset lane equilibrium. Aggro lasts 2-3 seconds."
        },
        {
            "instruction": "What does 'orb walking' mean in Dota 2?",
            "output": "Orb walking means using attack modifiers (orb effects) that don't trigger creep aggro, like Drow's Frost Arrows or Viper's Poison Attack. Manually cast these spells to harass enemies without drawing creep aggro. Essential for laning dominance."
        },
        
        # Roles and Responsibilities
        {
            "instruction": "What are the 5 positions in Dota 2? Explain each role.",
            "output": "Position 1 (Hard Carry): Safe lane, highest farm priority, late game focus. Position 2 (Mid): Solo mid, levels + farm, tempo control. Position 3 (Offlaner): Hard lane, initiator/space creator. Position 4 (Soft Support): Roaming, ganking, early game impact. Position 5 (Hard Support): Ward bitch, selfless, enables team."
        },
        {
            "instruction": "How do I play position 4 support effectively?",
            "output": "Focus on early ganks, stacking neutrals, and roaming between lanes. Buy smokes, coordinate with pos 5, and transition to utility items mid-game. Unlike pos 5, you can take some farm and levels. Key items: Boots, Wand, Force Staff, Glimmer Cape."
        },
        
        # Game Phases and Strategy  
        {
            "instruction": "What are the different phases of a Dota 2 game?",
            "output": "Laning Phase (0-10 min): Focus on farm, levels, and early advantages. Mid Game (10-30 min): Teamfights, objectives, map control. Late Game (30+ min): High ground pushes, big teamfights, buyback management. Each phase requires different priorities and strategies."
        },
        {
            "instruction": "When should I group up with my team vs farm alone?",
            "output": "Group when you have key items for teamfight, enemy is grouped, or objectives are available (towers, Roshan). Farm alone when you need key items, team lacks initiation, or enemies can't catch you. Carries should farm until ready to fight effectively."
        },
        
        # Advanced Items and Builds
        {
            "instruction": "What is the difference between Linken's Sphere and BKB?",
            "output": "Linken's blocks one targeted spell every 13 seconds, good vs single target lockdown like Doom or Hex. BKB provides magic immunity for 5-10 seconds, better vs AoE disable/damage. Choose based on enemy lineup - Linken's vs targeted spells, BKB vs magic damage/AoE."
        },
        {
            "instruction": "When should I buy Aghanim's Scepter vs other items?",
            "output": "Buy Aghs when the upgrade significantly improves your impact - like better teamfight, farming, or survivability. Priority depends on hero and game state. Some heroes (Invoker, Tinker) rush it, others buy it as luxury. Check if Aghs Shard (cheaper) gives better value first."
        },
        
        # Vision and Map Control
        {
            "instruction": "Where should I place wards in Dota 2? Best ward spots?",
            "output": "Key spots: Rune wards (both sides), jungle entrances, Roshan pit, enemy triangle, high ground near towers. Aggressive wards in enemy jungle when ahead, defensive wards near your base when behind. Always have detection vs invis heroes. Deward enemy vision."
        },
        {
            "instruction": "What is smoke ganking? How do I coordinate smoke ganks?",
            "output": "Smoke of Deceit makes your team invisible until near enemies or 35 seconds. Use for ganks, Roshan attempts, or team positioning. Coordinate in voice chat, target isolated enemies, and have disable/burst ready. Smoke breaks 1025 units from enemies, so approach carefully."
        },
        
        # Team Fighting
        {
            "instruction": "How do I improve my team fighting in Dota 2?",
            "output": "Focus on positioning, target priority, and ability timing. Supports initiate/save, cores follow up with damage. Target enemy supports first, then cores. Use high ground, trees, and chokepoints. Don't chase kills - take objectives after winning fights."
        },
        {
            "instruction": "What is 'kiting' in Dota 2? How do I kite effectively?",
            "output": "Kiting means maintaining distance while dealing damage, using movement and range advantage. Attack-move repeatedly, use slows/mobility spells, and maintain maximum attack range. Essential for ranged cores vs melee enemies. Force Staff and Hurricane Pike help with kiting."
        },
        
        # Psychology and Mindset
        {
            "instruction": "How do I deal with toxic teammates in Dota 2?",
            "output": "Mute immediately if they're being toxic - focus on your own gameplay. Communicate with pings and chat wheel. Don't argue or tilt - it only makes things worse. Play your best regardless of team attitude. Use /mute all if needed for mental health."
        },
        {
            "instruction": "How do I avoid tilting in Dota 2? Mental game tips?",
            "output": "Take breaks after losses, focus on improvement over winning, and accept that some games are unwinnable. Review replays to learn from mistakes. Don't blame teammates - focus on your own play. Set small goals each game (CS targets, ward placements)."
        },
        
        # Advanced Concepts
        {
            "instruction": "What is 'networth timing' in Dota 2?",
            "output": "Networth timing refers to power spikes when heroes complete key items. Examples: AM with Battlefury (12-15 min), Invoker with Aghs (18-20 min). Teams should fight when their cores hit timings, avoid fights when enemies are stronger. Track enemy item progression."
        },
        {
            "instruction": "What does 'tempo' mean in Dota 2?",
            "output": "Tempo refers to the pace and momentum of the game. High tempo means constant fighting and objectives, low tempo means farming and late game focus. Mid heroes often control tempo with ganks and rotations. Tempo controllers: QoP, Puck, Storm Spirit."
        },
        
        # Patch Knowledge and Meta
        {
            "instruction": "How do I adapt to new Dota 2 patches?",
            "output": "Read patch notes carefully, focus on hero changes and item updates. Test changes in demo mode, watch pro players/streamers adapt. Meta shifts take 1-2 weeks to stabilize. Experiment with buffed heroes, avoid nerfed ones initially. Stay flexible with builds and strategies."
        },
        
        # Communication and Leadership
        {
            "instruction": "How do I shot-call and lead my team in Dota 2?",
            "output": "Communicate objectives clearly: 'Smoke gank mid', 'Take Roshan after', 'Defend high ground'. Use specific timings and locations. Be positive and decisive. Don't micromanage - give overall strategy. Leading supports often shot-call due to map awareness and vision control."
        }
    ]

def get_dota_terminology():
    """Return Dota 2 specific terminology and slang"""
    
    return [
        {
            "instruction": "What does 'CS' mean in Dota 2?",
            "output": "CS means 'Creep Score' - the number of last hits (creeps killed) you have. Good CS benchmarks: 50 by 10 minutes for supports, 80+ for cores. CS directly translates to gold and experience, making it crucial for item timings."
        },
        {
            "instruction": "What does 'gank' mean in Dota 2?",
            "output": "Gank means coordinated attack by multiple heroes to kill an enemy, usually someone farming alone. Successful ganks require disable, burst damage, and vision control. Mid heroes often gank side lanes after hitting level 6."
        },
        {
            "instruction": "What does 'feed' mean in Dota 2?",
            "output": "Feed means dying unnecessarily and giving the enemy gold/experience. 'Feeding' can be intentional (griefing) or accidental (poor positioning). Avoid feeding by playing safely, warding, and not overextending without vision."
        },
        {
            "instruction": "What does 'carry' mean in Dota 2?",
            "output": "Carry refers to heroes that scale heavily with items and levels, becoming very powerful late game. They 'carry' the team to victory through damage output. Examples: Anti-Mage, Phantom Assassin, Spectre. Carries need farm priority and protection early game."
        },
        {
            "instruction": "What does 'support' mean in Dota 2?",
            "output": "Support heroes enable their team through utility, healing, and vision rather than damage. They have low farm priority but high early game impact. Buy wards, stack camps, and save teammates. Examples: Crystal Maiden, Dazzle, Lion."
        },
        {
            "instruction": "What does 'mid' mean in Dota 2?",
            "output": "Mid refers to the middle lane and the hero playing there (position 2). Mid heroes get solo experience and farm, reaching power spikes quickly. They often control game tempo through ganks and map presence. Examples: Invoker, Queen of Pain, Puck."
        },
        {
            "instruction": "What does 'offlane' mean in Dota 2?",
            "output": "Offlane is the hard lane (top for Radiant, bottom for Dire) where position 3 heroes play. It's called 'offlane' because it's far from your team's safe areas. Offlaners are usually tanky initiators who create space. Examples: Axe, Tidehunter, Mars."
        },
        {
            "instruction": "What does 'jungle' mean in Dota 2?",
            "output": "Jungle refers to neutral creep camps between the lanes. Heroes can farm jungle for gold/experience when lanes are dangerous. Some heroes can jungle from level 1, but it's generally less efficient than laning. Use jungle to supplement lane farm."
        },
        {
            "instruction": "What does 'roam' mean in Dota 2?",
            "output": "Roaming means moving between lanes to gank, ward, or help teammates instead of staying in one lane. Position 4 supports excel at roaming. Effective roaming requires map awareness, timing, and coordination with teammates."
        },
        {
            "instruction": "What does 'split push' mean in Dota 2?",
            "output": "Split pushing means one hero pushes a side lane while the team groups elsewhere, forcing enemies to choose between defending or fighting. Creates map pressure and space. Heroes with escape mechanisms (AM, QoP) excel at split pushing."
        }
    ]

def get_comprehensive_coaching_knowledge():
    """Get all coaching knowledge from all modules"""
    all_knowledge = []
    
    # Add all specialized modules
    all_knowledge.extend(get_all_hero_guides())
    all_knowledge.extend(get_all_matchup_analysis())
    all_knowledge.extend(get_all_mmr_coaching())
    all_knowledge.extend(get_all_draft_strategy())
    all_knowledge.extend(get_all_advanced_strategy())
    
    # Add web-scraped community knowledge
    all_knowledge.extend(get_all_scraped_knowledge())
    
    # Add original coaching knowledge
    all_knowledge.extend(get_advanced_coaching_examples())
    all_knowledge.extend(get_dota_terminology())
    
    print(f"Loaded comprehensive coaching knowledge: {len(all_knowledge)} examples")
    return all_knowledge