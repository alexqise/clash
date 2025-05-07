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
        'image_url': '/static/images/hog_rider.jpg',
        'media_placeholders': {
            'gif': '/static/placeholder.gif',
            'audio': '/static/placeholder.mp3',
        },
        'counters': ['Cannon', 'Tornado', 'Skeleton Army'],
        'tips': ['Place buildings in the center.', 'Save your best counter for Hog pushes.'],
    }
] 