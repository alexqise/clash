# app.py
# Main Flask app for Clash Royale Learning App
# Follows project spec: modular, simple, session-based, well-commented

from flask import Flask, render_template, session, redirect, url_for, request
from lessons import lessons
from quizzes import quiz_questions
from datetime import datetime

app = Flask(__name__)
app.secret_key = "replace-this-with-a-very-secret-key-123"

def log_interaction(action, item_id):
    # Simple logger: store logs in session
    if 'button_logs' not in session:
        session['button_logs'] = []
    session['button_logs'].append({
        'button': action,
        'context': item_id,
        'timestamp': datetime.now().isoformat()
    })
    session.modified = True

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
    'results': None
}

@app.route('/')
def home():
    """Home page with Start Learning button."""
    # Reset both lesson and quiz progress when visiting home page
    session['lesson_progress'] = 0
    session['quiz_idx'] = 0
    session['quiz_answers'] = [None] * len(quiz_questions)
    return render_template('home.html')


@app.route('/play')
def play():
    """Interactive Clash Royale game simulation with cards from lessons."""
    # Get all unique cards from lessons
    cards = set()
    counters = set()

    for lesson in lessons:
        counters.update(lesson['counters'])

    # Add commonly used cards
    cards = list(counters)
    cards.extend(['Hog Rider', 'Mega Knight', 'Golem',
                 'Lava Hound', 'Elite Barbarians'])

    # Remove duplicates while preserving order
    unique_cards = []
    for card in cards:
        if card not in unique_cards:
            unique_cards.append(card)

    return render_template('play.html', cards=unique_cards)


@app.route('/lesson', methods=['GET', 'POST'])
def lesson():
    """Lesson navigation and display."""
    # Reset quiz progress when coming from another section
    if request.referrer and '/quiz' in request.referrer:
        session['quiz_idx'] = 0
        session['quiz_answers'] = [None] * len(quiz_questions)

    # Initialize or get current lesson progress
    if 'lesson_progress' not in session or request.args.get('reset'):
        session['lesson_progress'] = 0
    idx = session['lesson_progress']

    # Handle navigation
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'next' and idx < len(lessons) - 1:
            idx += 1
        elif action == 'prev' and idx > 0:
            idx -= 1
        session['lesson_progress'] = idx
        log_interaction(action, lessons[idx]['id'])
    lesson = lessons[idx]
    progress = (idx + 1, len(lessons))
    return render_template('lesson.html', lesson=lesson, progress=progress)


@app.route('/certificate')
def certificate():
    """Show a certificate of completion after finishing the quiz."""
    # Calculate quiz score based on correct answers
    quiz_answers = session.get('quiz_answers', [None] * len(quiz_questions))
    correct_count = 0
    for i, answer in enumerate(quiz_answers):
        if answer is not None and answer == quiz_questions[i]['correct_answer_index']:
            correct_count += 1

    # Calculate percentage score (avoid division by zero)
    total_questions = len(quiz_questions)
    quiz_score = round((correct_count / total_questions)
                       * 100) if total_questions > 0 else 0

    return render_template('certificate.html', quiz_score=quiz_score)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Quiz navigation and answering."""
    # Reset lesson progress when coming from another section
    if request.referrer and '/lesson' in request.referrer:
        session['lesson_progress'] = 0

    # Initialize or reset quiz progress
    if 'quiz_idx' not in session or request.args.get('reset'):
        session['quiz_idx'] = 0
    # Ensure quiz_answers always matches the number of quiz questions
    if 'quiz_answers' not in session or len(session['quiz_answers']) != len(quiz_questions) or request.args.get('reset'):
        session['quiz_answers'] = [None] * len(quiz_questions)
    idx = session['quiz_idx']
    feedback = None
    # Handle answer submission
    if request.method == 'POST':
        action = request.form.get('action')
        if action in ['next', 'prev']:
            if action == 'next':
                if idx < len(quiz_questions) - 1:
                    idx += 1
                elif idx == len(quiz_questions) - 1:
                    # User clicked Next on the last question, redirect to certificate
                    return redirect(url_for('certificate'))
            elif action == 'prev' and idx > 0:
                idx -= 1
            session['quiz_idx'] = idx
            log_interaction(action, quiz_questions[idx]['id'])
        elif action == 'answer':
            selected = request.form.get('option')
            if selected is not None:
                # Store the answer in session
                session['quiz_answers'][idx] = int(selected)
                session.modified = True  # Ensure session is saved
                log_interaction('answer', quiz_questions[idx]['id'])
                # Just redirect back to the same question to refresh
                return redirect(url_for('quiz'))

    progress = (idx + 1, len(quiz_questions))  # Always set before rendering
    question = quiz_questions[idx]
    answer = session['quiz_answers'][idx]

    # Check if the current answer is correct to enable the Next button
    is_correct = False
    if answer is not None:
        is_correct = (answer == question['correct_answer_index'])

    return render_template('quiz.html', question=question, answer=answer, feedback=feedback,
                           progress=progress, is_correct=is_correct)


@app.route('/interactions')
def interactions():
    """Show user interaction logs and summary stats."""
    logs = session.get('button_logs', [])
    total_clicks = len(logs)
    unique_buttons = len(set(log['button'] for log in logs))
    pages_visited = len(set(log['context'] for log in logs))
    return render_template('interactions.html', logs=logs, total_clicks=total_clicks, unique_buttons=unique_buttons, pages_visited=pages_visited)


if __name__ == '__main__':
    app.run(debug=True)
