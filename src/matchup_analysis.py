"""
Comprehensive matchup analysis and counter-picking knowledge for Dota 2
Covers hero counters, lane matchups, and strategic counters
"""

def get_counter_picking_guides():
    """Counter-picking knowledge for draft phase"""
    return [
        # Anti-Meta Counters
        {
            "instruction": "How do I counter Anti-Mage? What heroes and items work?",
            "output": "Heroes: Bloodseeker (Rupture through Blink), Storm Spirit (gap close), Lion (instant disable). Items: Orchid/Bloodthorn (silence), Scythe of Vyse, Abyssal Blade. Strategy: End game before 30 minutes, pressure early teamfights, ward his jungle, pick fights when he's farming."
        },
        {
            "instruction": "How do I counter Pudge? Positioning and items?",
            "output": "Heroes: Lifestealer (Magic Immunity), Queen of Pain (Blink escape), Puck (Phase Shift). Strategy: Stay behind creeps, ward rotation paths, buy Force Staff for hook saves. Items: Linken's Sphere, Lotus Orb. Never walk alone without vision vs Pudge."
        },
        {
            "instruction": "How do I counter Invoker? Early game pressure?",
            "output": "Heroes: Storm Spirit (gap close), Queen of Pain (mobility), Pudge (catch him out). Strategy: Gank mid frequently, pressure before Aghs timing, interrupt his farming. Items: Pipe vs magical damage, BKB vs combos. Don't let him free farm - Invoker needs levels and gold."
        },
        {
            "instruction": "How do I counter Phantom Assassin? True strike and magic damage?",
            "output": "Heroes: Tinker (pure damage), Lion (instant burst), Lina (magic damage). Items: MKB (true strike), Silver Edge (break evasion), Ghost Scepter (avoid physical). Strategy: Focus her early before BKB, use magic damage and disables."
        },
        {
            "instruction": "How do I counter Techies? Detection and movement?",
            "output": "Heroes: Zeus (True Sight), Bounty Hunter (Track vision), Nature's Prophet (summons tank mines). Items: Sentries, Gem, Force Staff, Boots of Travel. Strategy: Push with creeps, buy detection constantly, avoid common mine spots, group up for high ground."
        },
        
        # Carry Counters
        {
            "instruction": "What counters Spectre? Early game pressure heroes?",
            "output": "Heroes: Phantom Lancer (outcarry late), Lycan (early push), Chen (early teamfights). Strategy: End before 35 minutes, pressure her weak laning, pick fights during her Radiance timing window (16-20 min). Don't let the game go ultra-late."
        },
        {
            "instruction": "How do I counter Faceless Void? Chronosphere counters?",
            "output": "Heroes: Lifestealer (Rage immunity), Juggernaut (Omnislash), Invoker (Ghost Walk). Items: Linken's Sphere, Aeon Disk, BKB before chrono. Strategy: Spread out in fights, bait chrono on one hero, save key abilities for post-chrono."
        },
        {
            "instruction": "What counters Terrorblade? Burst damage and illusion clear?",
            "output": "Heroes: Lina (pure damage), Lion (burst), Ember Spirit (cleave). Items: Mjolnir (illusion clear), Silver Edge (break), Dagon (burst). Strategy: Focus him before Metamorphosis, clear illusions quickly, pressure his weak early game."
        },
        
        # Mid Counters
        {
            "instruction": "How do I counter Queen of Pain mid? Gap closing and sustain?",
            "output": "Heroes: Storm Spirit (equal mobility), Pudge (hook through blink), Invoker (outscale). Items: Orchid (silence), Linkens (block scream), BKB (magic immunity). Strategy: Match her mobility, sustain through harass, ward rune spots."
        },
        {
            "instruction": "What counters Puck mid? Instant lockdown?",
            "output": "Heroes: Lion (instant hex), Lina (long range), Invoker (Tornado setup). Items: Orchid (silence), Nullifier (dispel), Scythe (instant disable). Strategy: Save instant disables for Phase Shift, pressure early game, don't let him escape freely."
        },
        {
            "instruction": "How do I counter Storm Spirit? Mana burn and silence?",
            "output": "Heroes: Anti-Mage (mana burn), Invoker (EMP), Silencer (silence). Items: Orchid/Bloodthorn, Diffusal Blade, Scythe. Strategy: Drain his mana, silence before Ball Lightning, pressure his Bloodstone timing. Storm is weak without mana."
        },
        
        # Support Counters
        {
            "instruction": "How do I counter Crystal Maiden? Gap closing and burst?",
            "output": "Heroes: Pudge (hook), Storm Spirit (zip), Queen of Pain (blink). Strategy: Focus her first in fights, interrupt Freezing Field channeling, exploit her lack of mobility. Buy Blink Dagger to gap close. She dies very easily."
        },
        {
            "instruction": "What counters Oracle? Dispel and burst damage?",
            "output": "Heroes: Invoker (Tornado dispel), Pudge (displacement), Lion (instant burst). Items: Nullifier (dispel), Lotus Orb (reflect), BKB (immunity). Strategy: Dispel False Promise, burst through his heals, pressure early game."
        },
        {
            "instruction": "How do I counter Rubick? Positioning and spell priority?",
            "output": "Heroes: Storm Spirit (mobility), Queen of Pain (gap close), Anti-Mage (spell resistance). Strategy: Don't use big ultimates near him, position spells carefully, focus him first to prevent steals. Save key spells until he's dead."
        },
        
        # Offlane Counters
        {
            "instruction": "How do I counter Axe? Ranged harassment and kiting?",
            "output": "Heroes: Invoker (range), Queen of Pain (mobility), Lina (range + stun). Items: Force Staff (escape), Hurricane Pike (distance), Silver Edge (break). Strategy: Kite him, don't group up vs Call, pressure before Blink timing."
        },
        {
            "instruction": "What counters Mars? High ground and spell immunity?",
            "output": "Heroes: Invoker (Tornado), Storm Spirit (zip over arena), Lifestealer (Rage). Items: BKB (immunity), Force Staff (escape), Hurricane Pike (range). Strategy: Stay on high ground vs spear, spread out vs Arena, use spell immunity."
        },
        {
            "instruction": "How do I counter Tidehunter? Spread positioning and dispel?",
            "output": "Heroes: Invoker (Tornado dispel), Oracle (immunity), Naga Siren (song counter). Items: Manta Style (dispel), Linken's Sphere (block), BKB (immunity). Strategy: Don't group up, bait Ravage on one hero, use spell immunity or dispels."
        }
    ]

def get_lane_matchup_guides():
    """Specific lane matchup knowledge"""
    return [
        # Mid Lane Matchups
        {
            "instruction": "How do I play Invoker vs Queen of Pain mid? Laning strategy?",
            "output": "Stay back, use Forge Spirits for last hits and harass. Cold Snap when she blinks aggressively. Rush Eul's for setup and mana. She wins trades early but you outscale. Ward runes, call missing frequently. Focus on farming until combo items."
        },
        {
            "instruction": "How do I play Storm Spirit vs Invoker mid? Trading and all-ins?",
            "output": "Trade with Remnant + Overload, use Ball Lightning for short escapes. Pre-Bloodstone, manage mana carefully. Look for kill potential at level 6 with full combo. He outscales you late, so pressure early-mid game. Bottle crow for sustain."
        },
        {
            "instruction": "How do I play Pudge vs Queen of Pain mid? Hook opportunities?",
            "output": "Use Rot to farm and sustain, hook when she's aggressive or going for runes. Ward her escape routes, coordinate with supports for ganks. She can harass you easily, so focus on farming and looking for hook opportunities. Post-6, roam for easier targets."
        },
        
        # Carry vs Carry
        {
            "instruction": "How do I play Anti-Mage vs Phantom Assassin late game?",
            "output": "Build Butterfly early for evasion vs evasion. Mana Burn counters her small mana pool. Use Manta to dispel her slow. Avoid manfighting - use Blink for positioning. She spikes earlier, you scale better with items. Farm until you have advantage."
        },
        {
            "instruction": "How do I play Terrorblade vs Anti-Mage? Split push vs farm speed?",
            "output": "You spike earlier with Metamorphosis. Pressure his jungle with illusions, force fights before his 3-item timing. Use Sunder aggressively in fights. He outfarms you late game, so create pressure mid-game with your stronger illusions."
        },
        
        # Support vs Support
        {
            "instruction": "How do I play Crystal Maiden vs Lion in teamfights?",
            "output": "Position further back, use Freezing Field after his combo. Frostbite can cancel his channeling spells. Both are squishy - whoever initiates first usually wins. Ward defensively, don't face-check alone. Save BKB for his combo."
        },
        {
            "instruction": "How do I play Dazzle vs Oracle? Healing competition?",
            "output": "Shallow Grave beats False Promise in most cases. Poison Touch for constant pressure. His dispels can remove your abilities - time them carefully. Both excel at keeping cores alive - focus on positioning and timing over direct dueling."
        }
    ]

def get_team_composition_counters():
    """Counter strategies for team compositions"""
    return [
        {
            "instruction": "How do I counter a heavy teamfight lineup? Split push strategy?",
            "output": "Pick split pushers: Anti-Mage, Queen of Pain, Nature's Prophet. Avoid grouping, force rotations, take objectives while they group. Items: Boots of Travel, Manta Style. Don't take 5v5 fights - create map pressure instead."
        },
        {
            "instruction": "How do I counter a split push strategy? Catching and grouping?",
            "output": "Pick gap closers: Storm Spirit, Queen of Pain, Pudge. Force teamfights, group as 5, ward their escape routes. Items: Smokes, detection, lockdown items. Don't chase the split pusher - force objectives or catch them rotating."
        },
        {
            "instruction": "How do I counter heavy magic damage? Magic resistance and immunity?",
            "output": "Items: Pipe of Insight, BKB, Lotus Orb, Glimmer Cape. Heroes: Pudge (high HP), Anti-Mage (spell resistance), Lifestealer (magic immunity). Strategy: Rush magic resistance, group for Pipe, use spell immunity timing."
        },
        {
            "instruction": "How do I counter high physical damage? Armor and evasion?",
            "output": "Items: Assault Cuirass, Shiva's Guard, Butterfly, Ghost Scepter. Heroes: Invoker (Alacrity), Dazzle (armor), Omniknight (immunity). Strategy: Stack armor auras, use ghost forms, kite with slows and disables."
        },
        {
            "instruction": "How do I counter invisible heroes? Detection and area damage?",
            "output": "Items: Sentry Wards, Dust, Gem of True Sight. Heroes: Zeus (True Sight), Bounty Hunter (Track), Bloodseeker (Thirst). Strategy: Constant detection, group movement, area damage abilities. Never walk alone without detection."
        }
    ]

def get_all_matchup_analysis():
    """Combine all matchup analysis"""
    analysis = []
    analysis.extend(get_counter_picking_guides())
    analysis.extend(get_lane_matchup_guides())
    analysis.extend(get_team_composition_counters())
    return analysis