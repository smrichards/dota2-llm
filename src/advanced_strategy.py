"""
Advanced decision making, laning mastery, farming optimization, and ward strategy
Comprehensive high-level Dota 2 knowledge
"""

def get_decision_making_scenarios():
    """Real-time decision making for complex game situations"""
    return [
        {
            "instruction": "It's 25 minutes, we're ahead 10k gold. Should we take Roshan or push high ground?",
            "output": "Take Roshan first if: 1) You have vision control around pit. 2) Enemy can't contest (dead/low). 3) You have Roshan-taking abilities. Then use Aegis for safer high ground push. If enemies are all alive and defending, pressure side lanes to force rotations, then Roshan when they split."
        },
        {
            "instruction": "Enemy carry is farming our jungle. Should we fight or ignore and farm elsewhere?",
            "output": "Fight if: You have numbers advantage, key abilities ready, can kill quickly. Ignore if: He has escape, you lack lockdown, he's stronger than you. Alternative: Force objectives elsewhere, smoke gank his team. Don't waste time chasing if you can't secure the kill. Map pressure > kill hunting."
        },
        {
            "instruction": "We're behind 15k gold at 35 minutes. What's our comeback strategy?",
            "output": "1) Defend high ground patiently. 2) Smoke gank isolated enemies. 3) Force favorable fights (2v1, 3v2). 4) Ward defensively, deward aggressively. 5) Look for enemy mistakes. 6) Use buyback strategically. 7) One good teamfight can close 15k gap. Patience and precision over desperation."
        },
        {
            "instruction": "Enemy team is Roshing and we have no vision. Should we contest or get objectives?",
            "output": "Contest if: You can teamfight favorably, have AoE abilities, enemy is low. Get objectives if: You lack vision/initiation, they're ahead, risky to face-check. Alternative options: Ward approaches, smoke from behind, pressure their base. Don't face-check into 5 enemies without information."
        },
        {
            "instruction": "Our carry is splitpushing but enemy is grouping as 5. What should we do?",
            "output": "Defend 4v5 if: You have wave clear, defensive abilities, high ground advantage. Join carry if: You can't defend, they're too strong. Alternative: Pressure different objective, force them to choose. Communicate with carry about timing. Split push only works with team coordination."
        },
        {
            "instruction": "Enemy has buybacks, we just won a fight. Push or back?",
            "output": "Push if: You have Aegis, significant numbers advantage, fast push abilities. Back if: Low HP/mana, no sustain, risky without Aegis. Consider: Enemy respawn timings, your ability to disengage, objective value. Don't throw advantage by overextending. Secure what you can safely."
        },
        {
            "instruction": "We need one more item to fight but enemy is pressuring. Farm or join team?",
            "output": "Join if: Team will lose 4v5, you can make impact without item, objective is critical. Farm if: Team can defend, item timing is crucial (BKB, Blink), safe farming available. Communicate timing to team. Sometimes one crucial item > joining early teamfight."
        },
        {
            "instruction": "Enemy carry is stronger but we have better teamfight. How do we play?",
            "output": "Force 5v5 teamfights, avoid isolated pickoffs, group with team, use smokes to find favorable engagements. Don't let their carry free farm or split push. Control vision around objectives. Your window is mid-game before their carry peaks. Coordinate teamfight timing."
        }
    ]

def get_laning_mastery():
    """Advanced laning phase knowledge and techniques"""
    return [
        {
            "instruction": "How do I manipulate creep aggro for better last hitting?",
            "output": "Right-click enemy hero within 500 range, then immediately click away. Creeps will move toward you for easier last hits. Use between :00-:03 seconds for best effect. Practice timing: Aggro → move → last hit → reset. This pulls creeps into better positions and away from enemy."
        },
        {
            "instruction": "What is creep equilibrium and how do I control it?",
            "output": "Equilibrium = where creeps meet and fight. Control by: 1) Only last hitting (pushes toward enemy). 2) Denying creeps (keeps equilibrium). 3) Aggro pulling (brings toward you). 4) Attacking enemy creeps (pushes away). Ideal: Creeps fight near your tower but not under it."
        },
        {
            "instruction": "When should I pull creeps and how do I do it effectively?",
            "output": "Pull when: Lane is pushing toward enemy, you want to deny XP, reset equilibrium. Timing: Attack neutral creeps at :53 seconds. Stack-pull: Clear small camp first. Chain-pull: Connect multiple camps. Benefits: Denies enemy XP/gold, gives supports farm, resets lane position."
        },
        {
            "instruction": "How do I trade effectively in lane? When to be aggressive?",
            "output": "Trade when: Enemy goes for last hits, your abilities are ready, you have creep advantage, support rotation incoming. Avoid: Trading under enemy tower, when low on regen, against superior harass. Use: High ground advantage, fog of war, ability combos. Win trades through positioning and timing."
        },
        {
            "instruction": "What are advanced deny mechanics and why are they important?",
            "output": "Deny at <50% HP, gives 25% XP to enemies (vs 100% if they last hit). Advanced: Deny your own creeps to control equilibrium, deny siege creeps (worth more XP), deny neutrals when jungling. Denying = XP advantage = level advantage = lane control. Practice deny timing like last hitting."
        },
        {
            "instruction": "How do I play against heavy harassment in lane?",
            "output": "Buy more regen, use creep aggro to get safe last hits, trade back when possible, call for support rotation, consider pulling to get farm. Items: Extra tangoes, salve, magic stick. Don't just take harassment - either trade back or get out of range. Sustain through superior regen."
        },
        {
            "instruction": "When should I abandon my lane to help team?",
            "output": "Leave when: Tower is lost/under siege, better opportunities elsewhere, carry can farm alone safely. TP to: Defensive situations, profitable ganks, tower pushes. Don't: Leave carry alone vs aggressive dual lane, abandon farm for uncertain ganks. Communicate timing with team."
        }
    ]

def get_farm_optimization():
    """Farming patterns and efficiency guides"""
    return [
        {
            "instruction": "What are efficient farming patterns for carries?",
            "output": "Triangle farming: Lane → large camp → medium camp → ancient camp → lane. Timing: Clear waves quickly, then jungle. Stack camps when possible. Use TP to farm dangerous lanes safely. Pattern: Lane (15s) → Jungle (45s) → repeat. Adapt based on enemy movements and safety."
        },
        {
            "instruction": "How do I maximize GPM as a support without taking core farm?",
            "output": "1) Stack camps for cores to clear. 2) Pull creep waves. 3) Clear unwarded areas safely. 4) Kill participation bounties. 5) Observer ward gold. 6) Tome of Knowledge efficiency. 7) Efficient movement between tasks. Support GPM comes from enabling cores, not competing for farm."
        },
        {
            "instruction": "When should I stack camps and which camps to prioritize?",
            "output": "Stack timing: :53-:55 seconds. Priority: Ancient camps (highest value), large camps (good efficiency), medium camps (easy to clear). Stack when: Moving between lanes, waiting for abilities, supports rotating. Benefits: Accelerates core farm, provides safe gold for supports later."
        },
        {
            "instruction": "How do I farm efficiently while avoiding ganks?",
            "output": "Ward common gank paths, farm near escape routes (towers, trees), watch minimap constantly, carry TP scroll, vary farming patterns. Don't: Farm same spot repeatedly, push without vision, ignore missing enemies. Efficiency means surviving - dead carry farms nothing."
        },
        {
            "instruction": "What's the optimal CS targets for different roles and timings?",
            "output": "By 10 minutes - Carry: 80+ CS, Mid: 70+ CS, Offlane: 40+ CS, Supports: 15+ CS. By 20 minutes - Carry: 180+ CS, Mid: 150+ CS. These are targets - prioritize quality over quantity. Perfect CS without deaths > higher CS with deaths. Adapt to game pace."
        },
        {
            "instruction": "How do I balance farming with team participation?",
            "output": "Join team when: You have key items/levels, objectives available, team needs you urgently. Farm when: Waiting for item timings, team can manage without you, safe opportunities available. Communicate your timing to team. Balance efficiency with impact."
        }
    ]

def get_advanced_warding():
    """Strategic ward placement and vision control"""
    return [
        {
            "instruction": "What are the most important ward spots for different game phases?",
            "output": "Early game: Rune wards (both sides), river wards, lane wards for safety. Mid game: Jungle entrances, Roshan area, high ground wards around objectives. Late game: Enemy high ground, Roshan pit, buyback spots. Adapt to game flow and team strategy."
        },
        {
            "instruction": "How do I deward effectively? Finding and removing enemy vision?",
            "output": "Common spots: Rune areas, jungle entrances, high ground, near objectives. Use: Sentry wards, gem carrier, true sight abilities. Timing: Before important objectives, when rotating, during map control phases. Dewarding = information advantage = better decisions."
        },
        {
            "instruction": "What's aggressive vs defensive warding? When to use each?",
            "output": "Aggressive: Enemy jungle, their high ground, around their objectives. Use when ahead or pressuring. Defensive: Your jungle, approaches to your base, around your objectives. Use when behind or farming. Adapt ward placement to game state and strategy."
        },
        {
            "instruction": "How do I ward for different team strategies?",
            "output": "Split push: Deep wards in enemy territory, escape route vision. Teamfight: Vision around objectives, high ground wards. Early aggression: Gank path wards, enemy movement vision. Late game: Roshan area, high ground approaches. Match wards to strategy."
        },
        {
            "instruction": "What's the psychology of ward placement? Predicting enemy movement?",
            "output": "Think like enemy: Where would they gank from? What routes do they take? Where do they farm? Place wards based on enemy habits and common patterns. Use fog of war to place unseen wards. Vision = prediction = safety = advantage."
        },
        {
            "instruction": "How do I manage ward economy and timing?",
            "output": "Buy wards on cooldown early game, coordinate with team for important timings, use Observer ward charges efficiently, prioritize key areas over complete coverage. Ward economy: Support burden early, team responsibility late. Don't over-ward low priority areas."
        }
    ]

def get_all_advanced_strategy():
    """Combine all advanced strategy knowledge"""
    strategy = []
    strategy.extend(get_decision_making_scenarios())
    strategy.extend(get_laning_mastery())
    strategy.extend(get_farm_optimization())
    strategy.extend(get_advanced_warding())
    return strategy