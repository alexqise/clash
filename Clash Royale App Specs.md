# Clash Royale Learning App — Project Specification

## 1. Project Overview

**Name:** Clash Royale Learning App  
**Type:** Interactive Educational Web Application  
**Purpose:** To teach users about Clash Royale win conditions and their counters using interactive, media-rich content.  
**Key Principles:**  
- Interactive learning over passive consumption  
- Immediate feedback and visual engagement  
- Lightweight, session-based tracking  
- Modular, media-focused lessons and quizzes  

---

## 2. Technical Stack

| Layer             | Technology                            |
|------------------|----------------------------------------|
| Backend           | Python 3, Flask                        |
| Frontend          | HTML5, Jinja2, Bootstrap 5, jQuery     |
| Session Storage   | Flask session (in-memory, per user)    |
| Persistent Storage| Not implemented (future SQLite/PostgreSQL) |
| Media             | Static assets (images, GIFs, audio/video placeholders) |
| Deployment        | Localhost (development), portable to production |

---

## 3. Core Features

### 3.1 Interactive Learn Mode
- **Lesson Format:** Short segments (2–3 sentences) with associated media.
- **Navigation:** "Next" and "Previous" buttons required; no long scrolling.
- **Media Support:** Each lesson must include:
  - At least one image (e.g., card art or gameplay screenshot)
  - Optional: GIF or 5–10 second video clip (or placeholder)
  - Optional: Audio clip for feedback or card sound effects
- **Timestamp Logging:** Each navigation action logs a timestamp in the session.
- **Feedback:** Visual indicators (e.g., button highlights, progress bar updates).

### 3.2 Quiz Mode
- **Question Design:** Short, focused, multiple-choice questions linked to lessons.
- **Media Integration:** Questions may include images, GIFs, or short clips.
- **Navigation:** Users can move forward/backward; answers are saved.
- **Immediate Feedback:** Correctness is shown after each answer with a brief explanation.
- **Progress Persistence:** State is saved in-session and restored on refresh.

### 3.3 Interaction Tracking
- **Log Capturing:** Button interactions are logged with:
  - Timestamp
  - Button identifier
  - Associated context (lesson or quiz question ID)
- **User Access:** Users can view a table of their interactions.
- **Summary Stats:** Total clicks, unique buttons pressed, and pages visited.

### 3.4 Media & Accessibility Requirements
- **Mandatory Media:** Each lesson/quiz question must include at least one image.
- **Encouraged Media:** GIF or short video/audio clips (5–10 seconds); placeholder shown if unavailable.
- **No Long Content:** No video/audio exceeds 30 seconds; no long text blocks.
- **Accessibility:** Semantic HTML and ARIA labels for buttons and navigation.
- **Responsive Design:** Must support both desktop and mobile devices.

---

## 4. Data Model

### 4.1 Lesson Object
- `id`: Unique identifier  
- `title`: Short title of the lesson  
- `description`: Brief textual description (2–3 sentences max)  
- `image_url`: Path to image  
- `media_placeholders`: Paths or flags for GIF/video/audio  
- `counters`: List of counter strategies  
- `tips`: Supporting strategy tips  

### 4.2 Quiz Question Object
- `id`: Unique identifier  
- `question`: Text of the quiz question  
- `options`: List of answer choices  
- `correct_answer_index`: Index of the correct answer  
- `media_placeholders`: Paths or flags for associated media  

### 4.3 Session Data
- `lesson_progress`: Current lesson index  
- `quiz_answers`: Stored answers per question  
- `button_logs`: List of interaction events  
- `timestamp_history`: Navigation history with timestamps  

---

## 5. Example User Flow

1. **Home Page:** User clicks "Start Learning."
2. **Lesson 1:** User sees a short description, image, and GIF placeholder. Clicks "Next" → timestamp recorded.
3. **Lesson 2:** New content appears. User clicks "Previous," then "Next" again → timestamps recorded.
4. **Quiz Mode:** User answers a question with media. Immediate feedback shown. Progress saved.
5. **Page Refresh:** User's state is preserved (quiz answers + lesson position).
6. **Interaction View:** User accesses a table of interaction logs.
7. **Completion:** Quiz results displayed; user can review their learning journey.

---

## 6. Media Placeholder Requirements

### 6.1 Image
- **Usage:** Required in every lesson and question.
- **Fallback:** Use gameplay screenshot or card art.

### 6.2 GIF/Video
- **Preferred:** 5–10 second clips showing card action or counter strategy.
- **Placeholder:**
```html
<img src="/static/placeholder.gif" alt="GIF/Video coming soon!">
```

### 6.3 Audio
- **Optional:** 5–10 second clips for feedback or effects.
- **Placeholder:**
```html
<audio src="/static/placeholder.mp3"></audio>
```

---

## 7. User Experience Guidelines

- **Progress Indicator:** A progress bar is visible throughout.
- **Consistent UI Feedback:** Interactive feedback on all actions (correct/wrong, next/previous).
- **No Passive Learning:** Avoid long text or videos; emphasize interaction.
- **Mobile Ready:** Bootstrap layout adapts to different screens.

---

## 8. Compliance with Assignment Constraints

| Requirement                                 | Status                     |
|--------------------------------------------|----------------------------|
| No long text blocks                         | ✅ Enforced via short segments |
| No long videos                              | ✅ Max 30 seconds per clip |
| All actions interactive with feedback       | ✅ Buttons, quizzes, media |
| Media included in every learning unit       | ✅ With fallback placeholders |
| Quiz progress persists on refresh           | ✅ Stored in session       |
| All user actions tracked and timestamped    | ✅ Full interaction log    |

---

## 9. Future Roadmap

- **Persistent Database:** Add SQLite or PostgreSQL for saving data across sessions/devices.
- **Authentication:** User login system to retain history and achievements.
- **Enhanced Media:** Upload and embed high-quality GIFs, videos, and audio.
- **Gamification:** Add streaks, badges, and user leaderboards.
- **Deck Builder Module:** Interactive card/deck testing with lesson integration.