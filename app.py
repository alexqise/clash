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
    return render_template('home.html')

@app.route('/lesson', methods=['GET', 'POST'])
def lesson():
    """Lesson navigation and display."""
    # Initialize progress if not set
    if 'lesson_progress' not in session:
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

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Quiz navigation and answering."""
    if 'quiz_idx' not in session:
        session['quiz_idx'] = 0
    if 'quiz_answers' not in session:
        session['quiz_answers'] = [None] * len(quiz_questions)
    idx = session['quiz_idx']
    feedback = None
    # Handle answer submission
    if request.method == 'POST':
        action = request.form.get('action')
        if action in ['next', 'prev']:
            if action == 'next' and idx < len(quiz_questions) - 1:
                idx += 1
            elif action == 'prev' and idx > 0:
                idx -= 1
            session['quiz_idx'] = idx
            log_interaction(action, quiz_questions[idx]['id'])
        elif action == 'answer':
            selected = request.form.get('option')
            if selected is not None:
                session['quiz_answers'][idx] = int(selected)
                log_interaction('answer', quiz_questions[idx]['id'])
                # Provide immediate feedback
                correct = quiz_questions[idx]['correct_answer_index']
                feedback = (int(selected) == correct)
    question = quiz_questions[idx]
    answer = session['quiz_answers'][idx]
    progress = (idx + 1, len(quiz_questions))
    return render_template('quiz.html', question=question, answer=answer, feedback=feedback, progress=progress)

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