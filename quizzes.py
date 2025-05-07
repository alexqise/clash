# quizzes.py
# Contains quiz question data for the Clash Royale Learning App
# Each question is a dict with required fields as per the project spec

quiz_questions = [
    {
        'id': 1,
        'question': 'Which of these is a win condition card?',
        'options': ['Cannon', 'Hog Rider', 'Zap', 'Knight'],
        'correct_answer_index': 1,  # Hog Rider
        'media_placeholders': {
            'image': '/static/images/hog_rider.jpg',
            'gif': '/static/placeholder.gif',
            'audio': '/static/placeholder.mp3',
        },
    },
    {
        'id': 2,
        'question': 'What is the best way to counter Hog Rider?',
        'options': ['Fireball', 'Cannon', 'Arrows', 'Freeze'],
        'correct_answer_index': 1,  # Cannon
        'media_placeholders': {
            'image': '/static/images/cannon.jpg',
            'gif': '/static/placeholder.gif',
            'audio': '/static/placeholder.mp3',
        },
    }
] 