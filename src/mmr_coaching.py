"""
MMR-specific coaching advice for different skill levels in Dota 2
Tailored guidance for Herald to Immortal players
"""

def get_low_mmr_coaching():
    """Herald to Crusader (0-2000 MMR) coaching"""
    return [
        {
            "instruction": "How do I climb from Herald to Guardian? What should I focus on?",
            "output": "Focus on basics: Last hitting (aim for 50+ CS by 10 min), buying regen, using TP scrolls defensively. Pick simple heroes: Wraith King, Dragon Knight, Ogre Magi, Crystal Maiden. Master ONE role first. Don't chase kills across the map - farm and objectives win games."
        },
        {
            "instruction": "What are the most important fundamentals for new Dota 2 players?",
            "output": "1. Last hitting - practice in demo mode daily. 2. Map awareness - check minimap every 3-5 seconds. 3. Item builds - follow guides initially. 4. Positioning - stay alive over dealing damage. 5. TP usage - carry TP always, use defensively. These basics will carry you to Crusader easily."
        },
        {
            "instruction": "Which heroes should I pick as a beginner to climb MMR?",
            "output": "Carry: Wraith King (hard to kill), Dragon Knight (tanky, simple). Support: Ogre Magi (tanky, easy spells), Crystal Maiden (high impact). Mid: Dragon Knight, Pudge (hooks are satisfying). Offlane: Axe (simple initiation). Avoid: Invoker, Meepo, Chen, Visage - too complex for learning."
        },
        {
            "instruction": "How do I improve my last hitting as a Herald player?",
            "output": "Practice in demo mode 10 minutes daily - no items, no abilities, just last hits. Learn your hero's attack animation. Use Quelling Blade on melee heroes. Don't auto-attack - only hit when creep is low. Aim for 50 CS by 10 minutes as minimum goal. Last hits = gold = items = wins."
        },
        {
            "instruction": "What mistakes do Herald players make the most?",
            "output": "1. Chasing kills instead of farming. 2. Not carrying TP scrolls. 3. Fighting without items. 4. Not buying regen. 5. Auto-attacking creeps. 6. Not checking minimap. 7. Picking complex heroes. Focus on fixing ONE mistake at a time - don't try to fix everything immediately."
        },
        {
            "instruction": "How do I use TP scrolls effectively in low MMR?",
            "output": "Always carry TP scroll (hotkey it). Use defensively: TP to towers when allies are getting dived. Don't TP to fights you can't win. TP to farm empty lanes safely. Double-click TP to go to fountain. TP cooldown is 70 seconds - track it mentally. Good TP usage can save your life and help teammates."
        }
    ]

def get_mid_mmr_coaching():
    """Archon to Legend (2000-4000 MMR) coaching"""
    return [
        {
            "instruction": "How do I climb from Archon to Legend? What's the next level?",
            "output": "Focus on: Creep pulling/stacking, ward placement, power spike timings, team coordination. Learn 2-3 heroes per role deeply. Start shotcalling objectives. Improve farming patterns - use jungle efficiently. Watch replays of your losses. Communication becomes more important at this level."
        },
        {
            "instruction": "What advanced mechanics should Archon players learn?",
            "output": "1. Creep aggro manipulation. 2. Stack pulling and camp stacking. 3. Animation canceling. 4. Smoke ganking coordination. 5. Power spike recognition. 6. Efficient farming patterns. 7. Ward timing and placement. Practice these in demo mode and unranked games first."
        },
        {
            "instruction": "How do I improve my farming efficiency in mid MMR?",
            "output": "Learn farming patterns: lane → jungle → lane rotation. Stack camps while moving between lanes. Use TP scrolls to farm dangerous lanes safely. Clear waves fast then jungle. Aim for 70+ CS by 10 minutes on cores. Time your movements with objective timings. Efficiency beats fighting for farm speed."
        },
        {
            "instruction": "What's the biggest difference between Archon and Legend players?",
            "output": "Consistency and game sense. Legend players make fewer game-losing mistakes, understand power spikes better, and coordinate objectives. They farm more efficiently and position better in teamfights. Focus on reducing deaths, improving CS consistency, and better decision making about when to fight vs farm."
        },
        {
            "instruction": "How do I improve my team fighting in mid MMR?",
            "output": "1. Focus target priority - supports first, then cores. 2. Use high ground and chokepoints. 3. Don't chase kills - take objectives after wins. 4. Coordinate initiation with team. 5. Save buyback for crucial fights. 6. Position based on your role. Practice these concepts consistently."
        },
        {
            "instruction": "When should I start learning complex heroes in mid MMR?",
            "output": "Once you're comfortable with fundamentals and have 2-3 simple heroes mastered per role. Good stepping stones: Invoker (QE only), Storm Spirit, Pudge, Mars. Avoid: Meepo, Chen, Visage until Ancient+. Master the game first, then master complex heroes. Mechanics follow understanding."
        }
    ]

def get_high_mmr_coaching():
    """Ancient to Divine (4000-6000 MMR) coaching"""
    return [
        {
            "instruction": "How do I climb from Ancient to Divine? High-level concepts?",
            "output": "Master: Advanced laning (aggro, denies, trading), efficient movement, draft understanding, detailed matchup knowledge, precise timing windows. Learn every hero's abilities and cooldowns. Improve communication and shotcalling. Watch professional games for strategy. Consistency at this level requires deep game knowledge."
        },
        {
            "instruction": "What separates Ancient from Divine players?",
            "output": "Divine players have superior: 1. Laning mechanics (aggro, last hit under pressure). 2. Map awareness and rotation timing. 3. Itemization adaptation. 4. Communication and coordination. 5. Mental resilience and tilt control. The skill gap is significant - focus on perfecting fundamentals rather than flashy plays."
        },
        {
            "instruction": "How important is draft knowledge at Ancient+ level?",
            "output": "Extremely important. Learn: Power spikes, team composition synergy, counter-picking, lane matchups, timing windows. Understand what your team needs: initiation, save, damage, push. Communicate picks and strategy. Bad drafts are much harder to overcome at high skill. Study professional drafts and adapt to meta changes."
        },
        {
            "instruction": "What advanced mechanics should Ancient players master?",
            "output": "1. Perfect creep aggro control. 2. Advanced animation canceling. 3. Precise spell combos and timings. 4. Efficient camera movement. 5. Quick itemization decisions. 6. Advanced ward spots and dewarding. 7. Buyback timing optimization. These separate good players from great players."
        },
        {
            "instruction": "How do I improve my decision making at high MMR?",
            "output": "Study: Power spike timings, map state analysis, risk/reward calculation, objective prioritization. Watch your replays critically - analyze every death and missed opportunity. Learn from professional players and high MMR streamers. Develop game sense through experience and study. Decision making trumps mechanical skill at this level."
        },
        {
            "instruction": "What mental aspects become important at Ancient+ level?",
            "output": "Tilt control, communication skills, leadership, adaptability, and learning from mistakes. Games are more competitive and teammates more skilled. Positive attitude and good communication can win close games. Learn to play from behind and make comeback calls. Mental game becomes as important as mechanical skill."
        }
    ]

def get_immortal_coaching():
    """Divine to Immortal (6000+ MMR) coaching"""
    return [
        {
            "instruction": "How do I reach Immortal rank? What's required at the highest level?",
            "output": "Perfection in: Laning efficiency, teamfight execution, draft understanding, communication, mental resilience. Study professional games extensively. Specialize in 1-2 roles with deep hero pools. Understand meta shifts quickly. Maintain consistent performance over hundreds of games. The margin for error is extremely small."
        },
        {
            "instruction": "What's the difference between Divine and Immortal players?",
            "output": "Immortal players have: 1. Near-perfect laning fundamentals. 2. Exceptional map awareness and timing. 3. Perfect itemization for situations. 4. Superior teamfight positioning and execution. 5. Advanced game sense and prediction. 6. Consistent performance under pressure. Every aspect must be refined to the highest level."
        },
        {
            "instruction": "How important is meta knowledge for reaching Immortal?",
            "output": "Critical. Immortal players: Adapt to patches immediately, understand hero strength timings, know optimal item builds for situations, recognize power spikes precisely, play around team compositions expertly. Follow professional scene, analyze patch changes deeply, experiment with new strategies. Meta knowledge gives competitive edges."
        },
        {
            "instruction": "What mindset is required for Immortal rank?",
            "output": "Growth mindset, extreme patience, emotional control, willingness to grind, constant self-improvement focus. Accept that games are very difficult and losses happen. Focus on incremental improvements rather than rank. Study replays religiously. Learn from every mistake. The mental game is as important as mechanical skill."
        },
        {
            "instruction": "How do I maintain Immortal rank once I reach it?",
            "output": "Continue improving - Immortal is the beginning, not the end. Stay updated with meta changes, maintain hero pools, practice consistently, study professional games, work on weaknesses identified in replays. The skill level continues rising, so continuous improvement is mandatory. Never stop learning."
        }
    ]

def get_role_specific_mmr_advice():
    """MMR advice specific to each role"""
    return [
        {
            "instruction": "How do I climb MMR as a support player? Low to high MMR progression?",
            "output": "Low MMR: Ward key spots, stack camps, buy detection, save cores with items. Mid MMR: Learn rotation timing, smoke coordination, advanced ward spots. High MMR: Perfect positioning, game sense, shotcalling, detailed matchup knowledge. Support impact increases with game knowledge - study extensively."
        },
        {
            "instruction": "How do I climb MMR as a carry player? Farming vs fighting balance?",
            "output": "Low MMR: Focus purely on farming and last hitting. Mid MMR: Learn farming patterns and power spike timings. High MMR: Perfect efficiency, join fights at optimal times, understand space creation. Carry progression is about maximizing farm while contributing at the right moments."
        },
        {
            "instruction": "How do I climb MMR as a mid player? Impact and roaming?",
            "output": "Low MMR: Win your lane, get levels and farm. Mid MMR: Learn roaming timing, coordinate with supports. High MMR: Control game tempo, perfect matchup knowledge, efficient movement. Mid players must balance personal farm with team impact - timing is everything."
        },
        {
            "instruction": "How do I climb MMR as an offlaner? Space creation and initiation?",
            "output": "Low MMR: Don't feed, get what farm you can, buy utility items. Mid MMR: Learn initiation timing, space creation concepts. High MMR: Perfect engagement timing, advanced positioning, team coordination. Offlane success depends on game sense and team fighting more than mechanics."
        }
    ]

def get_all_mmr_coaching():
    """Combine all MMR-specific coaching"""
    coaching = []
    coaching.extend(get_low_mmr_coaching())
    coaching.extend(get_mid_mmr_coaching())
    coaching.extend(get_high_mmr_coaching())
    coaching.extend(get_immortal_coaching())
    coaching.extend(get_role_specific_mmr_advice())
    return coaching