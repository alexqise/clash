# lessons.py
# Contains lesson data for the Clash Royale Learning App
# Each lesson is a dict with required fields as per the project spec

lessons = [
    {
        'id': 1,
        'title': 'What is a Win Condition?',
        'description': 'A win condition is a card or strategy that can deal significant damage to enemy towers. Learning to use and counter them is key to victory.',
        'image_url': '/static/images/win_condition_example.jpg',
        'media_placeholders': {
            'gif': '/static/placeholder.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['Building placement', 'Cheap cycle cards'],
        'tips': ['Always have a counter in hand.', "Don't overcommit elixir."],
    },
    {
        'id': 2,
        'title': 'Countering Hog Rider',
        'description': 'Hog Rider is a fast win condition. Use buildings or swarms to distract and minimize tower damage.',
        # Updated to use official Supercell asset
        'image_url': '/static/images/hog_rider.png',
        'media_placeholders': {
            # Now served locally for reliability
            'gif': '/static/hog_rider.mp4',
            'audio': '/static/hogrider.wav',  # Hog Rider sound effect
        },
        'counters': ['Cannon', 'Tornado', 'Skeleton Army'],
        'tips': ['Place buildings in the center.', 'Save your best counter for Hog pushes.'],
    },
    {
        'id': 3,
        'title': 'Mega Knight',
        'description': 'The Mega Knight is a high-cost, high-health troop that deals area damage and has a unique spawn jump. Best deployed defensively to counter swarms and then used in a counterpush.',
        'image_url': 'https://static.wikia.nocookie.net/clashroyale/images/e/e4/MegaKnightCard.png',
        'media_placeholders': {
            'gif': 'https://media.tenor.com/PzU0RE1aOXUAAAAC/mega-knight.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['P.E.K.K.A', 'Mini P.E.K.K.A', 'Inferno Tower', 'Skeleton Army', 'Valkyrie'],
        'tips': ['Deploy Mega Knight defensively and counterpush.'],
    },
    {
        'id': 4,
        'title': 'Golem',
        'description': 'The Golem is a slow, ground-based tank with massive health. Upon death, it splits into two Golemites. Best used behind your towers to build a strong push.',
        'image_url': 'https://static.wikia.nocookie.net/clashroyale/images/0/02/GolemCard.png',
        'media_placeholders': {
            'gif': 'https://media.tenor.com/O8zMefXUQHIAAAAC/golem-clash-royale.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['Inferno Tower', 'Mini P.E.K.K.A', 'Lumberjack', 'Night Witch', 'P.E.K.K.A'],
        'tips': ['Start Golem pushes from the back for maximum support.'],
    },
    {
        'id': 5,
        'title': 'Lava Hound',
        'description': 'The Lava Hound is a flying tank that targets buildings. Upon death, it bursts into several Lava Pups that deal chip damage.',
        'image_url': 'https://static.wikia.nocookie.net/clashroyale/images/2/29/LavaHoundCard.png',
        'media_placeholders': {
            'gif': 'https://media.tenor.com/Mbwa-EAyAakAAAAC/lava-hound.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['Minions', 'Mega Minion', 'Inferno Dragon', 'Electro Dragon', 'Musketeer'],
        'tips': ['Use air-targeting troops to counter Lava Hound.'],
    },
    {
        'id': 6,
        'title': 'Elite Barbarians',
        'description': 'Elite Barbarians are a fast, high-damage pair of melee units. They can shred through low-health troops and towers if left unchecked.',
        'image_url': 'https://static.wikia.nocookie.net/clashroyale/images/4/48/EliteBarbariansCard.png',
        'media_placeholders': {
            'gif': 'https://media.tenor.com/LnJJM1CyaQ8AAAAC/elite-barbarians-clash-royale.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['P.E.K.K.A', 'Mini P.E.K.K.A', 'Fireball', 'Valkyrie', 'Skeleton Army'],
        'tips': ['Use high-damage or splash units to stop Elite Barbarians.'],
    },
] 