# Clash Royale Learning App

## Overview

An interactive web app to teach Clash Royale win conditions and counters using short lessons and quizzes with media. Built with Flask, Bootstrap 5, and Jinja2. All user progress and logs are stored in session (no database).

## Features

- Interactive lessons with images and media placeholders
- Multiple-choice quizzes with instant feedback
- Progress and answers persist on refresh
- All user actions logged and viewable
- Responsive, accessible UI (desktop/mobile)

## Setup

1. Clone the repo:
   ```sh
   git clone <repo-url>
   cd clash
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   python app.py
   ```
4. Open the link in the your terminal (ip_address:5000)

## Testing

- Navigate through lessons and quizzes.
- Refresh the page to verify progress persists.
- View your interaction log from the menu.

## Project Structure

- `app.py` — Main Flask app and routes
- `lessons.py` — Lesson data
- `quizzes.py` — Quiz data
- `templates/` — HTML templates
- `static/` — Images, GIFs, audio placeholders

---

For more details, see the project spec in `Clash Royale App Specs.md`.
