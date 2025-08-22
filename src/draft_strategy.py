"""
Comprehensive draft strategy and team composition guides for Dota 2
Covers picking phases, team synergy, and strategic compositions
"""

def get_draft_fundamentals():
    """Basic draft concepts and picking order"""
    return [
        {
            "instruction": "What are the basic principles of drafting in Dota 2?",
            "output": "1. Ban meta/comfort picks early. 2. Pick versatile heroes early (pos 4/5). 3. Save cores for later picks to avoid counters. 4. Ensure team has: initiation, save/sustain, damage, push potential. 5. Consider laning matchups and power spikes. 6. Adapt to enemy picks - don't tunnel vision on one strategy."
        },
        {
            "instruction": "What should I pick in the first picking phase?",
            "output": "Pick supports and versatile heroes: Pudge, Invoker, Queen of Pain, Crystal Maiden, Lion. Avoid: Hard carries, very specific counterpicks, heroes with clear counters. First picks should be flexible and not easily countered. Save your win conditions for later picks."
        },
        {
            "instruction": "How do I adapt my draft based on enemy picks?",
            "output": "Against magic damage: Pick spell resistance/immunity heroes (Anti-Mage, Lifestealer). Against physical: Pick armor/evasion heroes (Invoker, Dazzle). Against split push: Pick gap closers (Storm, QoP). Against teamfight: Pick split pushers (AM, Nature's Prophet). Counter their strategy, don't force yours."
        },
        {
            "instruction": "What makes a good team composition in Dota 2?",
            "output": "Essential elements: 1. Initiation (Pudge, Axe, Mars). 2. Save potential (Dazzle, Oracle, Force Staff carriers). 3. Damage scaling (cores with good items). 4. Push/antipush capability. 5. Vision control. 6. Synergistic abilities (combos that work together). Balance is key - no single strategy wins every game."
        },
        {
            "instruction": "When should I ban certain heroes in draft?",
            "output": "Ban: Enemy comfort picks (check profiles), overpowered meta heroes, perfect counters to your strategy, heroes that ruin your game plan. Examples: Ban Pudge vs squishy lineup, ban Anti-Mage if you want long games, ban Invoker vs no gap close. Bans should have specific purpose."
        }
    ]

def get_team_composition_strategies():
    """Different team composition archetypes"""
    return [
        {
            "instruction": "How do I draft a teamfight composition? What heroes work together?",
            "output": "Core: AoE ultimates (Invoker, Queen of Pain, Crystal Maiden). Support: Setup and follow-up (Pudge, Lion, Dazzle). Synergy: Invoker Tornado → CM Freezing Field, Pudge Hook → QoP Scream. Items: Pipe, Assault Cuirass, team auras. Strategy: Group as 5, control objectives, win decisive teamfights."
        },
        {
            "instruction": "How do I draft a split push composition? Key heroes and strategy?",
            "output": "Split pusher: Anti-Mage, Queen of Pain, Nature's Prophet (heroes with escape). Team: Defensive heroes who can hold 4v5 (Invoker, Dazzle, defensive supports). Items: Boots of Travel, Manta Style. Strategy: One hero pressures side lanes while team defends or takes other objectives. Force enemy rotations."
        },
        {
            "instruction": "How do I draft an early game composition? Fast pace strategy?",
            "output": "Heroes: Storm Spirit, Queen of Pain, Pudge, Lion, Crystal Maiden (strong early spells). Strategy: Aggressive laning, early ganks, pressure towers by 15-20 minutes. Items: Early fighting items, smokes. Win condition: End before enemy cores come online. High tempo, constant action."
        },
        {
            "instruction": "How do I draft a late game composition? Scaling strategy?",
            "output": "Cores: Anti-Mage, Spectre, Invoker (scale with items/levels). Supports: Defensive and enabling (Dazzle, Oracle, defensive items). Strategy: Survive early game, farm efficiently, win through superior scaling. Items: Core items for carries, team fighting items. Patience and farming focus."
        },
        {
            "instruction": "How do I draft against invisible heroes? Detection and counters?",
            "output": "Heroes: Zeus (True Sight), Bounty Hunter (Track), Bloodseeker (Thirst), Invoker (EMP reveals). Items: Sentry Wards, Dust, Gem. Strategy: Constant detection, group movement, AoE abilities. Don't pick squishy isolated heroes vs invis. Vision control becomes critical."
        },
        {
            "instruction": "How do I draft a push composition? Taking towers and objectives?",
            "output": "Heroes: Nature's Prophet (treants), Invoker (Forge Spirits), Dazzle (heals), Crystal Maiden (wave clear). Items: Assault Cuirass, drums, team auras. Strategy: Group early, take towers, control map. End mid-game before enemies scale. Constant pressure on objectives."
        }
    ]

def get_position_specific_drafting():
    """Drafting advice for each position"""
    return [
        {
            "instruction": "How do I draft position 1 carries? Safe vs risky picks?",
            "output": "Safe picks: Wraith King, Dragon Knight, Juggernaut (hard to counter). Risky picks: Anti-Mage, Spectre (need specific conditions). Consider: Laning matchup, team protection, item timing windows, enemy lineup. Pick carries that fit your team's strategy and timing."
        },
        {
            "instruction": "How do I draft position 2 mid heroes? Impact and scaling?",
            "output": "Tempo controllers: Queen of Pain, Storm Spirit, Pudge (early impact). Scalers: Invoker, Shadow Fiend (late game). Consider: Matchup vs enemy mid, team's need for initiation/damage, power spike timing. Mid should complement team strategy - tempo or scaling."
        },
        {
            "instruction": "How do I draft position 3 offlaners? Initiation and space creation?",
            "output": "Initiators: Axe, Mars, Tidehunter (start teamfights). Space creators: Nature's Prophet, Queen of Pain (split map). Consider: Team's need for initiation, enemy mobility, your survival in lane. Offlane should provide what team lacks - usually initiation or space."
        },
        {
            "instruction": "How do I draft position 4 supports? Roaming and utility?",
            "output": "Roamers: Pudge, Spirit Breaker (ganking potential). Utility: Lion, Crystal Maiden (teamfight impact). Consider: Team's needs for disable/damage, synergy with pos 5, laning potential. Pos 4 should complement team strategy and enable cores."
        },
        {
            "instruction": "How do I draft position 5 supports? Lane support and late game utility?",
            "output": "Lane enablers: Dazzle, Oracle (keep cores alive). Teamfight: Crystal Maiden, Lion (big impact). Consider: Laning synergy with carry, save potential, late game utility. Pos 5 should enable carry and provide team utility. Usually picked early for flexibility."
        }
    ]

def get_situational_drafting():
    """Specific drafting scenarios and adaptations"""
    return [
        {
            "instruction": "We're last pick and need a carry against Pudge, Invoker, Lion. What should I pick?",
            "output": "Pick: Lifestealer (Rage immunity), Anti-Mage (spell resistance), or Juggernaut (Blade Fury). Avoid: Squishy carries without escape. Build: BKB early, Linken's vs single target. Strategy: Farm safely, avoid face checking, group with team when fighting."
        },
        {
            "instruction": "Enemy has strong teamfight with Invoker, Crystal Maiden. How do I counter-draft?",
            "output": "Pick: Split pushers (Anti-Mage, Queen of Pain), gap closers (Storm Spirit), or spread fighting heroes. Avoid: Grouping up, squishy heroes without escape. Strategy: Don't take 5v5 fights, spread out, pressure multiple lanes. Force them to split attention."
        },
        {
            "instruction": "Enemy picked early carry like Anti-Mage. How do I punish this?",
            "output": "Pick: Early fighting cores (Queen of Pain, Storm Spirit), aggressive supports (Pudge, Lion). Strategy: Pressure his jungle, force early fights, end by 25-30 minutes. Ban/pick his support heroes. Don't let him free farm - constant pressure wins."
        },
        {
            "instruction": "We need initiation but offlaner is picked. Who can provide backup initiation?",
            "output": "Heroes: Pudge (any position), Lion (support), Storm Spirit (mid), Nature's Prophet (global). Items: Blink Dagger on cores, Force Staff positioning. Strategy: Multiple heroes can initiate - don't rely on one. Coordinate engagement timing."
        },
        {
            "instruction": "Enemy has heavy magic damage. How do I draft defensively?",
            "output": "Heroes: Anti-Mage (resistance), Lifestealer (immunity), Pudge (high HP). Items: Pipe of Insight, BKB, Hood components. Strategy: Stack magic resistance, use spell immunity timing, spread out in fights. Don't group vs AoE magic damage."
        },
        {
            "instruction": "We want to play aggressive early game. What draft enables this?",
            "output": "Heroes: Storm Spirit, Queen of Pain, Pudge, Lion, Crystal Maiden (strong early spells). Items: Early fighting items, smokes, wards. Strategy: Aggressive laning, constant ganks, tower pressure. Win before enemies scale - high tempo throughout."
        }
    ]

def get_meta_and_patch_drafting():
    """Meta-specific and patch-related drafting advice"""
    return [
        {
            "instruction": "How do I adapt my drafting to patch changes?",
            "output": "Read patch notes carefully: hero buffs/nerfs, item changes, meta shifts. Test changes in unranked first. Watch pro games and high MMR streams for new strategies. Buffed heroes become priority picks/bans. Nerfed heroes need evaluation. Meta takes 1-2 weeks to stabilize after patches."
        },
        {
            "instruction": "What heroes are typically first pick/ban material?",
            "output": "Usually: Overpowered meta heroes, versatile picks (Pudge, Invoker), comfort heroes for high skill players. Changes with patches. Current meta should determine priority. Check professional games and high MMR trends. First pick/ban priority shifts with balance changes."
        },
        {
            "instruction": "How do I identify emerging meta trends?",
            "output": "Watch: Professional tournaments, high MMR streams, patch analysis videos. Check: Hero pick/win rates on Dotabuff, recent buffs/nerfs. Test: New strategies in unranked games. Meta emerges from: Item changes, hero buffs, professional innovation. Stay informed and adaptable."
        }
    ]

def get_all_draft_strategy():
    """Combine all draft strategy knowledge"""
    strategy = []
    strategy.extend(get_draft_fundamentals())
    strategy.extend(get_team_composition_strategies())
    strategy.extend(get_position_specific_drafting())
    strategy.extend(get_situational_drafting())
    strategy.extend(get_meta_and_patch_drafting())
    return strategy