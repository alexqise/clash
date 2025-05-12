# app.py
# Main Flask app for Clash Royale Learning App
# Follows project spec: modular, simple, session-based, well-commented

from flask import Flask, render_template, session, redirect, url_for, request
from lessons import lessons
from quizzes import quiz_questions
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'dev-key'  # For session management (replace in production)

# --- Helper Functions ---


def log_interaction(button_id, context_id):
    """Log a button interaction with timestamp and context."""
    if 'button_logs' not in session:
        session['button_logs'] = []
    session['button_logs'].append({
        'timestamp': datetime.now().isoformat(timespec='seconds'),
        'button': button_id,
        'context': context_id,
    })
    session.modified = True

# --- Routes ---


@app.route('/')
def home():
    """Home page with Start Learning button."""
    # Initialize progress if not already set
    if 'lesson_progress' not in session:
        session['lesson_progress'] = 0
    if 'quiz_idx' not in session:
        session['quiz_idx'] = 0
    if 'quiz_answers' not in session:
        session['quiz_answers'] = [None] * len(quiz_questions)

    # Only reset if explicitly requested
    if request.args.get('reset'):
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
    # Initialize lesson progress if not already set
    if 'lesson_progress' not in session:
        session['lesson_progress'] = 0

    # Only reset progress if explicitly requested
    if request.args.get('reset'):
        session['lesson_progress'] = 0

    # Check if a specific lesson ID is requested
    specific_lesson = request.args.get('id')
    if specific_lesson and specific_lesson.isdigit():
        # Find the lesson with this ID
        lesson_id = int(specific_lesson)
        for i, l in enumerate(lessons):
            if l['id'] == lesson_id:
                session['lesson_progress'] = i
                break

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
        # Redirect to the lesson with ID to maintain state on refresh
        return redirect(url_for('lesson', id=lessons[idx]['id']))

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

    # Get the lesson ID the user came from, if available
    from_lesson = session.get('from_lesson')

    return render_template('certificate.html', quiz_score=quiz_score, from_lesson=from_lesson)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Quiz navigation and answering."""
    # Initialize quiz progress if not already set
    if 'quiz_idx' not in session:
        session['quiz_idx'] = 0

    # Track which lesson the user came from if provided
    from_lesson = request.args.get('from_lesson')
    if from_lesson:
        session['from_lesson'] = from_lesson

    # Only reset progress if explicitly requested
    if request.args.get('reset'):
        session['quiz_idx'] = 0
        session['quiz_answers'] = [None] * len(quiz_questions)

    # Check if a specific question ID is requested
    specific_question = request.args.get('id')
    if specific_question and specific_question.isdigit():
        # Find the question with this ID
        question_id = int(specific_question)
        for i, q in enumerate(quiz_questions):
            if q['id'] == question_id:
                session['quiz_idx'] = i
                break

    # Ensure quiz_answers always matches the number of quiz questions
    if 'quiz_answers' not in session or len(session['quiz_answers']) != len(quiz_questions):
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
            # Redirect to maintain state on refresh
            return redirect(url_for('quiz', id=quiz_questions[idx]['id']))
        elif action == 'answer':
            selected = request.form.get('option')
            if selected is not None:
                # Store the answer in session
                session['quiz_answers'][idx] = int(selected)
                session.modified = True  # Ensure session is saved
                log_interaction('answer', quiz_questions[idx]['id'])
                # Redirect to maintain state and show feedback
                return redirect(url_for('quiz', id=quiz_questions[idx]['id']))

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
