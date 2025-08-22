"""
Comprehensive hero-specific guides for Dota 2
Covers builds, combos, timings, and strategies for popular heroes
"""

def get_carry_guides():
    """Position 1 carry heroes guides"""
    return [
        # Anti-Mage
        {
            "instruction": "How do I play Anti-Mage effectively? What's the build and timing?",
            "output": "Early: Quelling Blade, Tangos, Poor Man's Shield. Rush Battle Fury by 12-15 minutes. Skill build: Max Blink and Mana Break first. Mid game: Manta Style (18-20 min), then BKB or Butterfly. Late: Abyssal Blade, Heart. Farm aggressively, avoid fights until 3+ items. Split push with Manta illusions. Use Mana Void on mana-dependent heroes in teamfights."
        },
        {
            "instruction": "What are Anti-Mage's key power spikes and timings?",
            "output": "Battle Fury (12-15 min): Farming accelerates massively. Manta Style (18-20 min): Can fight and split push safely. BKB + Butterfly (25-30 min): Peak fighting window. Focus on farming until Manta + 1 item, then look for pickoffs on supports."
        },
        
        # Phantom Assassin
        {
            "instruction": "How do I play Phantom Assassin? What items should I build?",
            "output": "Core items: Phase Boots, BKB, Desolator/Daedalus. Luxury: Satanic, Abyssal Blade, Divine Rapier. Max Dagger first for harass, then Blur. Use Dagger to secure last hits and harass. BKB timing is crucial - buy when enemies have key disables. Late game, position carefully due to lack of escape."
        },
        {
            "instruction": "How do I deal with PA counters like MKB and Silver Edge?",
            "output": "Against MKB: Build more HP (Satanic, Heart), focus positioning over evasion. Against Silver Edge: Buy detection, stay with team, consider Linken's Sphere. Ghost Scepter on supports counters your physical damage - build Nullifier or focus other targets first."
        },
        
        # Faceless Void
        {
            "instruction": "How do I play Faceless Void? Chronosphere tips?",
            "output": "Build: Mask of Madness → Maelstrom → BKB → Mjolnir → Butterfly. Chrono tips: Catch 2+ enemies, position so allies can follow up. Don't waste on single supports late game. Use Time Walk aggressively with Chrono backup. MoM + Maelstrom accelerates farm massively."
        },
        
        # Juggernaut  
        {
            "instruction": "How do I play Juggernaut effectively? Spell usage tips?",
            "output": "Build: Phase Boots → Yasha → Manta/S&Y → Butterfly → Abyssal. Omnislash tips: Use on isolated targets, can dodge spells during animation. Healing Ward: Use in fights for sustain, protect it with positioning. Blade Fury: Dispels debuffs, use for escapes or early aggression. Very versatile carry - can fight early and scale late."
        },
        
        # Spectre
        {
            "instruction": "How do I play Spectre? When do I use Haunt?",
            "output": "Build: Radiance rush (16-20 min) → Manta → Heart/Butterfly. Haunt usage: Join teamfights globally, clean up low HP enemies, scout for ganks. Early game: Focus on survival and farm. Spectre peaks very late - avoid fights until Radiance + 1 item. Dispersion makes you tankier in big fights."
        },
        
        # Luna
        {
            "instruction": "How do I play Luna? Eclipse positioning tips?",
            "output": "Build: Dragon Lance → Manta → BKB → Butterfly. Eclipse: Use in narrow spaces (trees, uphill), combine with BKB for safety. Glaives accelerate farming - stack ancients. Lunar Blessing helps team early. Peak timing around 20-25 minutes with core items. Very fast farmer but needs good positioning."
        },
        
        # Terrorblade
        {
            "instruction": "How do I play Terrorblade effectively? Metamorphosis usage?",
            "output": "Build: Dragon Lance → Manta → BKB → Butterfly → Skadi. Metamorphosis: Use for farming/pushing when safe, save for fights when needed. Sunder: Emergency heal or finishing low enemies. Create pressure with illusions while farming jungle. Very strong split pusher but fragile early game."
        }
    ]

def get_mid_guides():
    """Position 2 mid heroes guides"""
    return [
        # Invoker
        {
            "instruction": "How do I play Invoker? What combos should I learn first?",
            "output": "Quas-Exort build: Max Exort first for damage. Essential combos: Cold Snap + Forge Spirit (QE basic), Eul's → Meteor → Deafening Blast → Cold Snap (advanced), Tornado → EMP → Meteor → Deafening Blast (teamfight). Practice in demo mode daily. Items: Boots → Eul's → Aghs → BKB → Refresher."
        },
        {
            "instruction": "What are the different Invoker builds and when to use them?",
            "output": "Quas-Exort: Best for farming and damage, use vs most matchups. Quas-Wex: Better vs mobile heroes, more utility with EMP/Tornado. Exort-Wex: Rare, for pure damage builds. QE is standard - provides farming with Forge Spirits and fighting with combos."
        },
        
        # Queen of Pain
        {
            "instruction": "How do I play Queen of Pain effectively? Positioning tips?",
            "output": "Build: Bottle → Boots → Orchid/Bloodstone → BKB → Linken's/Refresher. Use Blink aggressively for kills but always have escape plan. Scream of Pain farms waves fast. Sonic Wave hits hard - use in teamfights or to finish enemies. Very mobile - abuse positioning to get pickoffs."
        },
        
        # Puck
        {
            "instruction": "How do I play Puck? Phase Shift and Orb usage?",
            "output": "Build: Bottle → Boots → Blink → Eul's → BKB/Linken's. Phase Shift: Dodge spells, wait for cooldowns, bait enemy abilities. Orb: Initiation, escape, or gap closing. Dream Coil: Use in chokepoints, catch multiple enemies. Very elusive - focus on initiation and escape rather than damage."
        },
        
        # Storm Spirit
        {
            "instruction": "How do I play Storm Spirit? Ball Lightning mana management?",
            "output": "Build: Bottle → Arcane Boots → Bloodstone → BKB → Linken's/Orchid. Ball Lightning: Short hops to dodge spells, long jumps for ganks. Manage mana carefully - Bloodstone charges are crucial. Overload procs maximize damage. Peak around Bloodstone timing, falls off if behind."
        },
        
        # Pudge Mid
        {
            "instruction": "How do I play Pudge mid effectively? Hook techniques?",
            "output": "Build: Bottle → Boots → Blink → Force Staff → Aghs. Hook prediction: Aim where enemies will be, use fog/uphill advantage. Rot: Helps secure hooks, use for farming. Dismember: Channeling disable - position safely. Roam to side lanes after level 6. Very team-dependent but high impact when played well."
        },
        
        # Shadow Fiend
        {
            "instruction": "How do I play Shadow Fiend? Raze techniques and soul management?",
            "output": "Build: Bottle → Boots → Dragon Lance → BKB → Butterfly. Raze practice: Learn all 3 ranges, use for farming and harass. Souls: Maintain 36+ for damage, stack jungle camps. Requiem: Use defensively when dying or offensively in teamfights. Very farm-dependent - prioritize CS and stacks."
        }
    ]

def get_support_guides():
    """Position 4 and 5 support guides"""
    return [
        # Crystal Maiden
        {
            "instruction": "How do I play Crystal Maiden effectively? Positioning and ultimate usage?",
            "output": "Items: Tranquil Boots → Force Staff → Glimmer Cape → BKB. Positioning: Stay max range, use trees/fog. Freezing Field: Use when enemies are locked down or distracted. Frostbite: Combo with allies' stuns. Crystal Nova: Initiation and wave clear. Very fragile - positioning is everything."
        },
        
        # Dazzle
        {
            "instruction": "How do I play Dazzle? Shallow Grave timing?",
            "output": "Items: Boots → Force Staff → Glimmer → Aghs → Solar Crest. Shallow Grave: Use just before allies die, not when they're full HP. Poison Touch: Max first for harass. Shadow Wave: Heals allies and damages nearby enemies. Bad Juju cooldown reduction is very powerful late game."
        },
        
        # Lion
        {
            "instruction": "How do I play Lion effectively? Earth Spike vs Hex priority?",
            "output": "Items: Tranquil Boots → Force Staff → Blink → Aghs. Earth Spike: AoE disable, use for initiation. Hex: Single target, use on key enemies. Finger of Death: Execute low enemies, damage scales with kills. Mana Drain: Lane sustain and mana burn. Very burst-heavy support."
        },
        
        # Rubick
        {
            "instruction": "How do I play Rubick? What spells should I prioritize stealing?",
            "output": "High priority steals: Black Hole, Ravage, Reverse Polarity, RP. Medium: Stuns, nukes, heals. Low: Passives, weak spells. Position safely to steal key spells. Telekinesis: Great setup for spell steal. Null Field: Reduces magic damage for team. Practice spell combinations in demo mode."
        },
        
        # Oracle
        {
            "instruction": "How do I play Oracle effectively? False Promise usage?",
            "output": "Items: Boots → Force Staff → Glimmer → Aghs. False Promise: Use on allies about to die, combine with healing. Fortune's End: Dispels and stuns, can target allies to dispel debuffs. Fate's Edict: Makes allies magic immune but unable to attack. Very complex hero - practice combos extensively."
        }
    ]

def get_offlane_guides():
    """Position 3 offlane heroes guides"""
    return [
        # Axe
        {
            "instruction": "How do I play Axe offlane? Berserker's Call usage?",
            "output": "Build: Stout Shield → Vanguard → Blink → Blade Mail → Shiva's. Berserker's Call: Use to initiate teamfights, interrupt channeling, force BKB usage. Counter Helix: Proc chance increases with attackers. Culling Blade: Execute threshold increases with levels - use on low enemies to reset cooldown."
        },
        
        # Mars
        {
            "instruction": "How do I play Mars effectively? Arena usage and spear combos?",
            "output": "Build: Phase Boots → Blink → BKB → Assault Cuirass. Spear: Combo with Arena for guaranteed hits, use walls/trees for stuns. Arena: Trap enemy cores, block projectiles, control teamfights. God's Rebuke: Crit and armor reduction. Very strong teamfight initiator."
        },
        
        # Tidehunter
        {
            "instruction": "How do I play Tidehunter? Ravage timing and positioning?",
            "output": "Build: Arcane Boots → Blink → Refresher → Shiva's. Ravage: Wait for enemy grouping, use Blink for positioning. Anchor Smash: Reduces enemy damage, use in teamfights. Kraken Shell: Dispels debuffs at damage thresholds. Very teamfight dependent - make Ravage count."
        },
        
        # Centaur Warrunner
        {
            "instruction": "How do I play Centaur Warrunner? Double Edge usage?",
            "output": "Build: Vanguard → Blink → Pipe → Heart. Double Edge: High damage nuke, damages self - use Heart Stopper for sustain. Hoof Stomp: AoE stun for initiation. Stampede: Global mobility for team, use for ganks or escapes. Very tanky initiator with global presence."
        },
        
        # Underlord
        {
            "instruction": "How do I play Underlord effectively? Dark Rift usage?",
            "output": "Build: Arcane Boots → Pipe → Crimson Guard → Shiva's. Firestorm: Percentage-based damage, great vs tanky heroes. Pit of Malice: Root in area, use for teamfight control. Dark Rift: Global teleport for team, use for ganks or defense. Very defensive offlaner focused on team utility."
        }
    ]

def get_all_hero_guides():
    """Combine all hero guides"""
    guides = []
    guides.extend(get_carry_guides())
    guides.extend(get_mid_guides())
    guides.extend(get_support_guides())
    guides.extend(get_offlane_guides())
    return guides