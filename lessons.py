# lessons.py
# Contains lesson data for the Clash Royale Learning App
# Each lesson is a dict with required fields as per the project spec

lessons = [
    {
        'id': 1,
        'title': 'What is a Win Condition?',
        'description': 'A win condition is a card or strategy that can deal significant damage to enemy towers. Learning to use and counter them is key to victory.',
        'image_url': '/static/images/elite_barbarians.png',
        'media_placeholders': {
            'gif': '/static/placeholder.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['Cannon', 'Zap', 'Skeleton Army', 'Fireball', 'Inferno Tower'],
        'counter_descriptions': {
            'Cannon': 'Building, pulls troops',
            'Zap': 'Quick spell, stuns',
            'Skeleton Army': 'Swarm troop',
            'Fireball': 'Medium splash spell',
            'Inferno Tower': 'High damage building'
        },
        'tips': ['Always have a counter in hand.', "Don't overcommit elixir.", "Go for positive elixir trades."],
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
        'counter_descriptions': {
            'Cannon': 'Building, pulls troops',
            'Tornado': 'Pull spell, repositions',
            'Skeleton Army': 'Swarm troop'
        },
        'tips': ['Place buildings in the center.', 'Save your best counter for Hog pushes.'],
    },
    {
        'id': 3,
        'title': 'Mega Knight',
        'description': 'The Mega Knight is a high-cost, high-health troop that deals area damage and has a unique spawn jump. Best deployed defensively to counter swarms and then used in a counterpush.',
        'image_url': '/static/images/mega_knight.png',
        'media_placeholders': {
            'gif': '/static/mega_knight.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['P.E.K.K.A', 'Mini P.E.K.K.A', 'Inferno Tower', 'Skeleton Army', 'Valkyrie'],
        'counter_descriptions': {
            'P.E.K.K.A': 'Heavy tank, high damage',
            'Mini P.E.K.K.A': 'Medium tank, high damage',
            'Inferno Tower': 'High damage building',
            'Skeleton Army': 'Swarm troop',
            'Valkyrie': 'Medium splash troop'
        },
        'tips': ['Deploy Mega Knight defensively and counterpush.'],
    },
    {
        'id': 4,
        'title': 'Golem',
        'description': 'The Golem is a slow, ground-based tank with massive health. Upon death, it splits into two Golemites. Best used behind your towers to build a strong push.',
        'image_url': '/static/images/golem.png',
        'media_placeholders': {
            'gif': '/static/golem.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['Inferno Tower', 'Mini P.E.K.K.A', 'Lumberjack', 'Night Witch', 'P.E.K.K.A'],
        'counter_descriptions': {
            'Inferno Tower': 'High damage building',
            'Mini P.E.K.K.A': 'Medium tank, high damage',
            'Lumberjack': 'Fast melee, rage on death',
            'Night Witch': 'Spawns bats, melee',
            'P.E.K.K.A': 'Heavy tank, high damage'
        },
        'tips': ['Start Golem pushes from the back for maximum support.'],
    },
    {
        'id': 5,
        'title': 'Lava Hound',
        'description': 'The Lava Hound is a flying tank that targets buildings. Upon death, it bursts into several Lava Pups that deal chip damage.',
        'image_url': '/static/images/lava_hound.png',
        'media_placeholders': {
            'gif': '/static/lava_hound.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['Minions', 'Mega Minion', 'Inferno Dragon', 'Electro Dragon', 'Musketeer'],
        'counter_descriptions': {
            'Minions': 'Air swarm troop',
            'Mega Minion': 'Flying high damage',
            'Inferno Dragon': 'Flying, increasing damage',
            'Electro Dragon': 'Flying splash, stuns',
            'Musketeer': 'Ranged high damage'
        },
        'tips': ['Use air-targeting troops to counter Lava Hound.'],
    },
    {
        'id': 6,
        'title': 'Elite Barbarians',
        'description': 'Elite Barbarians are a fast, high-damage pair of melee units. They can shred through low-health troops and towers if left unchecked.',
        'image_url': '/static/images/elite_barbarians.png',
        'media_placeholders': {
            'gif': '/static/elite_barbarians.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['P.E.K.K.A', 'Mini P.E.K.K.A', 'Fireball', 'Valkyrie', 'Skeleton Army'],
        'counter_descriptions': {
            'P.E.K.K.A': 'Heavy tank, high damage',
            'Mini P.E.K.K.A': 'Medium tank, high damage',
            'Fireball': 'Medium splash spell',
            'Valkyrie': 'Medium splash troop',
            'Skeleton Army': 'Swarm troop'
        },
        'tips': ['Use high-damage or splash units to stop Elite Barbarians.'],
    },
] 