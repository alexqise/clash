from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime
import json

app = Flask(__name__)

# Data for learning and quiz content - in a real app, this might come from a database
# Clash Royale win conditions and their counters
clash_data = {
    "lessons": [
        {
            "id": 1,
            "title": "Hog Rider",
            "description": "The Hog Rider is a fast-moving troop that targets buildings. It's a popular win condition in many decks.",
            "image_url": "https://cdn.royaleapi.com/static/img/cards-75/hog-rider.png",
            "counters": [
                "Buildings like Cannon or Tesla",
                "Tornado to activate King Tower",
                "PEKKA for positive elixir trade",
                "Mini PEKKA for quick defense"
            ],
            "tips": "Always try to place buildings in the optimal position to pull the Hog Rider. Time your counters well to minimize the damage."
        },
        {
            "id": 2,
            "title": "Balloon",
            "description": "The Balloon is a flying troop that does massive damage to buildings. It's deadly if it reaches the tower.",
            "image_url": "https://cdn.royaleapi.com/static/img/cards-75/balloon.png",
            "counters": [
                "Air targeting troops like Musketeer",
                "Buildings to distract",
                "Rocket for direct damage",
                "Tesla or Inferno Tower"
            ],
            "tips": "Position your anti-air units carefully and be ready with spells to counter Balloon support troops."
        },
        {
            "id": 3,
            "title": "Golem",
            "description": "The Golem is a high-health troop that targets buildings and deals death damage. It's a heavy tank used in beatdown decks.",
            "image_url": "https://cdn.royaleapi.com/static/img/cards-75/golem.png",
            "counters": [
                "Inferno Tower/Dragon for high damage",
                "PEKKA as a tank killer",
                "Pressure opposite lane to reduce elixir for support",
                "Buildings to distract"
            ],
            "tips": "When facing Golem, consider pressuring the opposite lane to force your opponent to spend elixir defensively rather than supporting their Golem push."
        }
    ],
    "quiz": [
        {
            "id": 1,
            "question": "What is the best counter to Hog Rider?",
            "options": [
                "Skeleton Army",
                "Cannon or Tesla",
                "Fireball",
                "Goblin Gang"
            ],
            "answer": 1  # Index of correct answer (0-based)
        },
        {
            "id": 2,
            "question": "How should you counter Balloon?",
            "options": [
                "Use ground troops like Knight",
                "Use Goblin Barrel on King Tower",
                "Use air-targeting troops or buildings",
                "Use Earthquake"
            ],
            "answer": 2
        },
        {
            "id": 3,
            "question": "What's a good strategy against Golem decks?",
            "options": [
                "Wait until they place Golem, then push same lane",
                "Pressure opposite lane when they place Golem",
                "Save all elixir for defense",
                "Use Earthquake on their King Tower"
            ],
            "answer": 1
        },
        {
            "id": 4,
            "question": "Which card is NOT effective against Hog Rider?",
            "options": [
                "Cannon",
                "Tornado",
                "Poison",
                "Mini PEKKA"
            ],
            "answer": 2
        },
        {
            "id": 5,
            "question": "What's the best way to defend against a Balloon + Lumberjack combo?",
            "options": [
                "Use only buildings",
                "Fireball the Balloon only",
                "Use Rocket on both",
                "Combine air-targeting troops with buildings or spells"
            ],
            "answer": 3
        }
    ]
}

# User data storage - in a real app with multiple users, 
# this would be stored in a database with user sessions
user_data = {
    'started': False,
    'current_lesson': 0,
    'lesson_times': {},
    'quiz_answers': {},
    'quiz_start_time': None,
    'results': None,
    'button_interactions': []  # Store button interaction timestamps
}

@app.route('/')
def home():
    # Reset user data when returning to home
    user_data['started'] = False
    user_data['current_lesson'] = 0
    user_data['lesson_times'] = {}
    user_data['quiz_answers'] = {}
    user_data['quiz_start_time'] = None
    user_data['results'] = None
    return render_template('home.html')

@app.route('/start')
def start():
    # Record when the user starts the learning process
    user_data['started'] = True
    user_data['start_time'] = datetime.datetime.now().isoformat()
    return redirect(url_for('learn', lesson_id=1))

@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    # Check if user has started the app
    if not user_data['started']:
        return redirect(url_for('home'))
    
    # Record time spent on this lesson
    user_data['current_lesson'] = lesson_id
    user_data['lesson_times'][str(lesson_id)] = datetime.datetime.now().isoformat()
    
    # Get lesson data
    lesson = next((l for l in clash_data['lessons'] if l['id'] == lesson_id), None)
    if not lesson:
        return redirect(url_for('quiz', question_id=1))
    
    # Check if there's a next lesson
    next_lesson = next((l for l in clash_data['lessons'] if l['id'] == lesson_id + 1), None)
    next_url = url_for('learn', lesson_id=lesson_id + 1) if next_lesson else url_for('quiz', question_id=1)
    
    return render_template('learn.html', lesson=lesson, next_url=next_url)

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    # Check if user has started the app
    if not user_data['started']:
        return redirect(url_for('home'))
    
    # Handle form submission
    if request.method == 'POST':
        selected_option = int(request.form.get('answer', -1))
        user_data['quiz_answers'][str(question_id)] = selected_option
        
        # Redirect to next question or results
        next_question = next((q for q in clash_data['quiz'] if q['id'] == question_id + 1), None)
        if next_question:
            return redirect(url_for('quiz', question_id=question_id + 1))
        else:
            return redirect(url_for('results'))
    
    # GET request handling
    question = next((q for q in clash_data['quiz'] if q['id'] == question_id), None)
    if not question:
        return redirect(url_for('results'))
    
    # Record start time for the quiz if this is the first question
    if question_id == 1 and not user_data['quiz_start_time']:
        user_data['quiz_start_time'] = datetime.datetime.now().isoformat()
    
    total_questions = len(clash_data['quiz'])
    return render_template('quiz.html', question=question, question_id=question_id, total_questions=total_questions)

@app.route('/results')
def results():
    # Check if user has started the app
    if not user_data['started']:
        return redirect(url_for('home'))
    
    # Calculate score
    correct_answers = 0
    quiz_data = clash_data['quiz']
    
    for question in quiz_data:
        question_id = str(question['id'])
        if question_id in user_data['quiz_answers']:
            user_answer = user_data['quiz_answers'][question_id]
            if user_answer == question['answer']:
                correct_answers += 1
    
    score = {
        'correct': correct_answers,
        'total': len(quiz_data),
        'percentage': int((correct_answers / len(quiz_data)) * 100) if quiz_data else 0
    }
    
    user_data['results'] = score
    
    return render_template('results.html', score=score)

@app.route('/track_interaction', methods=['POST'])
def track_interaction():
    """
    Endpoint to track user button interactions with timestamps.
    Receives:
    - button_id: ID of the button that was clicked
    - page: Page where the interaction occurred (learn, quiz)
    - context: Additional context (e.g., lesson_id, question_id)
    """
    if request.method == 'POST':
        try:
            data = request.json
            button_id = data.get('button_id')
            page = data.get('page')
            context = data.get('context')
            
            # Create interaction record with timestamp
            interaction = {
                'timestamp': datetime.datetime.now().isoformat(),
                'button_id': button_id,
                'page': page,
                'context': context
            }
            
            # Store the interaction
            user_data['button_interactions'].append(interaction)
            
            return jsonify({'status': 'success', 'interaction': interaction}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 400
    
    return jsonify({'status': 'error', 'message': 'Method not allowed'}), 405

@app.route('/interaction_data')
def interaction_data():
    """
    Display all button interaction timestamps for debugging/analysis
    """
    return render_template('interaction_data.html', interactions=user_data['button_interactions'])

if __name__ == '__main__':
    app.run(debug=True, port=5000) 