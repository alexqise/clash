# Clash Royale Counter Guide

A web application that teaches users how to counter popular win conditions in Clash Royale. The application includes a learning module with lessons on countering Hog Rider, Balloon, and Golem, followed by a quiz to test knowledge.

## Features

- **Home page** with a start button to begin the learning process
- **Learning module** with detailed lessons on countering specific win conditions
- **Quiz** to test knowledge gained from the lessons
- **Results page** displaying quiz performance
- **Data tracking** for user interactions throughout the application

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5, jQuery
- **Data Storage**: In-memory Python dictionaries (for simplicity in this single-user application)

## Setup Instructions

1. **Clone the repository**:

   ```
   git clone <repository-url>
   cd clash_royale_counter_guide
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```
   python app.py
   ```

5. **Access the application**:
   Open your browser and navigate to `http://localhost:5000/`

## Application Structure

- **`app.py`**: Main Flask application with routes and data
- **`templates/`**: HTML templates using Jinja2
  - `base.html`: Base template with common structure
  - `home.html`: Home page with start button
  - `learn.html`: Template for learning pages
  - `quiz.html`: Template for quiz questions
  - `results.html`: Template for displaying quiz results
- **`static/`**: Static assets
  - `css/style.css`: Custom styling
  - `js/script.js`: Client-side JavaScript

## Data Structure

The application uses an in-memory Python dictionary to store:

- Lesson data (win conditions and their counters)
- Quiz questions and answers
- User progress and answers

## Contributor Guidelines

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## Acknowledgments

- This application is for educational purposes only
- All Clash Royale assets and references are the property of Supercell
