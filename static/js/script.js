/**
 * Clash Royale Counter Guide
 * Main JavaScript file to handle user interactions and data recording
 */

// Store user data locally for this session
const sessionData = {
  startTime: null,
  lessonViews: {},
  quizAnswers: {},
  quizStartTime: null,
  results: null,
};

// Initialize when DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
  console.log(
    "Clash Royale Counter Guide loaded at:",
    new Date().toISOString()
  );

  // Track navigation for analytics
  trackPageView();

  // Add Bootstrap classes to tables if they exist
  styleTablesWithBootstrap();

  // Enable tooltips if any exist
  enableBootstrapTooltips();
});

/**
 * Record current page view for analytics
 */
function trackPageView() {
  const pagePath = window.location.pathname;
  const pageTitle = document.title;

  console.log("Page viewed:", {
    path: pagePath,
    title: pageTitle,
    timestamp: new Date().toISOString(),
  });

  // Store specific data based on page type
  if (pagePath === "/") {
    // Home page view
    sessionData.startTime = null;
  } else if (pagePath.startsWith("/learn/")) {
    // Lesson page view - extract lesson ID from URL
    const lessonId = pagePath.split("/").pop();
    sessionData.lessonViews[lessonId] = {
      viewTime: new Date().toISOString(),
      timeSpent: 0, // Will be updated on navigation away
    };
  } else if (pagePath.startsWith("/quiz/")) {
    // Quiz page view
    if (!sessionData.quizStartTime) {
      sessionData.quizStartTime = new Date().toISOString();
    }
  } else if (pagePath === "/results") {
    // Results page view
    calculateTimeSpent();
  }
}

/**
 * Calculate time spent on lessons for analytics
 */
function calculateTimeSpent() {
  console.log("Session data collected:", sessionData);
}

/**
 * Add Bootstrap styling to any tables in the content
 */
function styleTablesWithBootstrap() {
  const tables = document.querySelectorAll("table");
  tables.forEach((table) => {
    table.classList.add("table", "table-striped", "table-bordered");
  });
}

/**
 * Enable Bootstrap tooltips
 */
function enableBootstrapTooltips() {
  if (
    typeof bootstrap !== "undefined" &&
    typeof bootstrap.Tooltip !== "undefined"
  ) {
    const tooltipTriggerList = [].slice.call(
      document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
    });
  }
}

/**
 * Record quiz answer selection
 * @param {number} questionId - The ID of the current question
 * @param {number} answerId - The ID of the selected answer
 */
function recordQuizAnswer(questionId, answerId) {
  sessionData.quizAnswers[questionId] = {
    selectedOption: answerId,
    timestamp: new Date().toISOString(),
  };

  console.log("Answer recorded:", {
    question: questionId,
    answer: answerId,
    timestamp: new Date().toISOString(),
  });
}

/**
 * Format time duration in a human-readable format
 * @param {Date} start - Start time
 * @param {Date} end - End time
 * @returns {string} Formatted duration
 */
function formatTimeDuration(start, end) {
  const durationMs = end - start;
  const seconds = Math.floor(durationMs / 1000);
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;

  return `${minutes}m ${remainingSeconds}s`;
}
