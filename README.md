# Clash Royale Learning App

A Flask-based web application for learning about Clash Royale win conditions and their counters.

## Features

- Interactive lessons about Clash Royale win conditions
- Quiz to test your knowledge
- Session-based user progress tracking

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Access the application at http://localhost:5000

## Development

### Environment Variables

- `SECRET_KEY`: Flask session encryption key (defaults to a development key if not set)

## Project Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
- `static/`: Static assets (CSS, JavaScript, images)

## Future Improvements

- Database integration for persistent user data
- More lessons and quiz questions
- User authentication system
- Improved UI/UX
