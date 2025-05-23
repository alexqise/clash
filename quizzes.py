# quizzes.py
# Contains quiz question data for the Clash Royale Learning App
# Each question is a dict with required fields as per the project spec

quiz_questions = [
    {
        'id': 1,
        'question': 'Which of these is a win condition card?',
        'options': ['Cannon', 'Hog Rider', 'Zap', 'Knight'],
        'card_descriptions': {
            'Cannon': 'Building, pulls troops',
            'Hog Rider': 'Fast building targeter',
            'Zap': 'Quick spell, stuns',
            'Knight': 'Mini tank, melee'
        },
        'correct_answer_index': 1,  # Hog Rider
        'media_placeholders': {
            # Updated to use official Supercell asset
            'image': '/static/images/hog_rider.png',
            # Now served locally for reliability
            'gif': '/static/hog_rider.mp4',
            'audio': '/static/hogrider.wav',  # Hog Rider sound effect
        },
    },
    {
        'id': 2,
        'question': 'What is the best way to counter Hog Rider?',
        'options': ['Fireball', 'Cannon', 'Arrows', 'Freeze'],
        'card_descriptions': {
            'Fireball': 'Medium splash spell',
            'Cannon': 'Building, pulls troops',
            'Arrows': 'Area damage spell',
            'Freeze': 'Stops troops temporarily'
        },
        'correct_answer_index': 1,  # Cannon
        'media_placeholders': {
            'image': '/static/images/cannon.jpg',
            'gif': '/static/placeholder.gif',
            'audio': '/static/placeholder.mp3',
        },
    },
    {
        'id': 3,
        'question': 'Which of the following is a good counter to Mega Knight?',
        'options': ['Witch', 'P.E.K.K.A', 'Bats', 'Furnace'],
        'card_descriptions': {
            'Witch': 'Spawns skeletons, splash',
            'P.E.K.K.A': 'Heavy tank, high damage',
            'Bats': 'Flying swarm, cheap',
            'Furnace': 'Spawns fire spirits'
        },
        'correct_answer_index': 1,  # P.E.K.K.A
        'media_placeholders': {
            'image': 'https://static.wikia.nocookie.net/clashroyale/images/e/e4/MegaKnightCard.png',
            'gif': 'https://media.tenor.com/PzU0RE1aOXUAAAAC/mega-knight.gif',
            'audio': '/static/placeholder.mp3',
        },
    },
    {
        'id': 4,
        'question': 'Which card is best used to counter a Golem?',
        'options': ['Princess', 'Inferno Tower', 'Heal Spirit', 'Goblin Gang'],
        'card_descriptions': {
            'Princess': 'Long range, splash',
            'Inferno Tower': 'High damage building',
            'Heal Spirit': 'Healing, one-time',
            'Goblin Gang': 'Mixed ground swarm'
        },
        'correct_answer_index': 1,  # Inferno Tower
        'media_placeholders': {
            'image': 'https://static.wikia.nocookie.net/clashroyale/images/0/02/GolemCard.png',
            'gif': 'https://media.tenor.com/O8zMefXUQHIAAAAC/golem-clash-royale.gif',
            'audio': '/static/placeholder.mp3',
        },
    },
    {
        'id': 5,
        'question': 'Which troop best counters the Lava Hound?',
        'options': ['Wizard', 'Baby Dragon', 'Inferno Dragon', 'Ice Wizard'],
        'card_descriptions': {
            'Wizard': 'Ground troop, splash',
            'Baby Dragon': 'Flying splash, tanky',
            'Inferno Dragon': 'Flying, increasing damage',
            'Ice Wizard': 'Slows, splash'
        },
        'correct_answer_index': 2,  # Inferno Dragon
        'media_placeholders': {
            'image': 'https://static.wikia.nocookie.net/clashroyale/images/2/29/LavaHoundCard.png',
            'gif': 'https://media.tenor.com/Mbwa-EAyAakAAAAC/lava-hound.gif',
            'audio': '/static/placeholder.mp3',
        },
    },
    {
        'id': 6,
        'question': 'Which of these is an effective counter to Elite Barbarians?',
        'options': ['Goblin Barrel', 'Valkyrie', 'Electro Spirit', 'Archers'],
        'card_descriptions': {
            'Goblin Barrel': 'Air troop spawner',
            'Valkyrie': 'Medium splash troop',
            'Electro Spirit': 'Quick stun, area',
            'Archers': 'Ranged, dual troop'
        },
        'correct_answer_index': 1,  # Valkyrie
        'media_placeholders': {
            'image': 'https://static.wikia.nocookie.net/clashroyale/images/4/48/EliteBarbariansCard.png',
            'gif': 'https://media.tenor.com/LnJJM1CyaQ8AAAAC/elite-barbarians-clash-royale.gif',
            'audio': '/static/placeholder.mp3',
        },
    },
] 