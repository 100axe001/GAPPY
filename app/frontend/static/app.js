// Global State
let token = localStorage.getItem("lifeos_token");
let currentUser = null;
let currentTab = "today";
let allItems = [];
let allConnections = [];
let lastParsedCommitment = null;

// Toast helper
function showToast(message, type = "info") {
  const container = document.getElementById("toast-container");
  if (!container) return;
  
  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;
  
  let icon = "info";
  if (type === "success") icon = "check-circle";
  if (type === "error") icon = "alert-circle";
  
  toast.innerHTML = `
    <i data-lucide="${icon}" style="width:16.8px; height:16.8px; flex-shrink:0;"></i>
    <span>${message}</span>
  `;
  
  container.appendChild(toast);
  lucide.createIcons();
  
  setTimeout(() => {
    toast.style.animation = "fadeOut 300ms ease forwards";
    setTimeout(() => {
      toast.remove();
    }, 300);
  }, 4000);
}

// Global OAuth callback handler
window.onOAuthSuccess = function(integrationName) {
  showToast(`${integrationName} connected successfully!`, "success");
  if (currentTab === "integrations") {
    renderIntegrationsView();
  }
  fetchDashboardData();
};

// Spacing colors for subjects/notes
const pastelColors = ["#8FAF8F", "#C47A72", "#C8A98A", "#D4A96A", "#9BB8CD", "#B197FC"];

// Note Editor State
let activeNoteId = null;
let saveTimeout = null;

// Practice Quiz State
let currentPracticeQuestions = [];
let currentPracticeQuestionIdx = 0;
let practiceAnswers = [];
let currentPracticeMaterialId = null;
let currentSelectedPracticeOpt = null;

// Spaced Repetition Quiz State
let currentActiveReview = null;
let currentReviewQuestions = [];

// Pomodoro Timer State
let pomodoroSeconds = 25 * 60;
let pomodoroInterval = null;
let pomodoroIsRunning = false;
let pomodoroSessionActive = false;

// Initialize Page
document.addEventListener("DOMContentLoaded", () => {
  checkAuth();
  setupEventListeners();
  setupFloatingToolbar();
});

// Auth Checks
function checkAuth() {
  token = localStorage.getItem("lifeos_token");
  if (!token) {
    document.getElementById("auth-panel").style.display = "block";
    document.getElementById("app-panel").style.display = "none";
  } else {
    document.getElementById("auth-panel").style.display = "none";
    document.getElementById("app-panel").style.display = "flex"; // Flex layout for sidebar
    try {
      const payload = JSON.parse(atob(token.split(".")[1]));
      document.getElementById("user-email-display").innerText = payload.sub;
      // Setup avatar letters
      const initials = payload.sub.substring(0, 2).toUpperCase();
      document.getElementById("avatar-letters").innerText = initials;
    } catch (e) {
      document.getElementById("user-email-display").innerText = "Logged In";
    }
    fetchDashboardData();
  }
}

// Global Event Listeners
function setupEventListeners() {
  // Auth Forms
  document.getElementById("auth-form").addEventListener("submit", handleLogin);
  document.getElementById("btn-signup").addEventListener("click", handleSignup);
  document.getElementById("btn-logout").addEventListener("click", handleLogout);
  
  // Create Forms
  document.getElementById("create-task-form").addEventListener("submit", handleCreateTask);
  document.getElementById("create-note-form").addEventListener("submit", handleCreateNote);
  document.getElementById("upload-pdf-form").addEventListener("submit", handleUploadMaterial);
  document.getElementById("study-session-form").addEventListener("submit", handleStartStudySession);

  // Commitment Inbox textarea Enter-key submit
  const commInput = document.getElementById("commitment-input");
  commInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleCommitSubmit();
    }
  });

  document.getElementById("btn-commitment-confirm").addEventListener("click", confirmCommitment);
  document.getElementById("btn-commitment-cancel").addEventListener("click", cancelCommitment);

  // Note editor inputs key triggers
  document.getElementById("note-editor-title").addEventListener("input", triggerNoteAutoSave);
  document.getElementById("note-editor-textarea").addEventListener("input", triggerNoteAutoSave);

  // Draft Generator
  document.getElementById("btn-generate-draft").addEventListener("click", handleGenerateDraft);
  document.getElementById("btn-save-draft").addEventListener("click", handleSaveDraft);

  // Pomodoro timer Start/Reset text links
  document.getElementById("btn-pomodoro-start").addEventListener("click", startPomodoro);
  document.getElementById("btn-pomodoro-reset").addEventListener("click", resetPomodoro);
  document.getElementById("pomodoro-debrief-form").addEventListener("submit", handlePomodoroDebriefSubmit);

  // Spaced repetition quiz submission
  document.getElementById("btn-submit-spaced-quiz").addEventListener("click", submitSpacedQuiz);

  // Global search input
  const searchInput = document.getElementById("global-search-input");
  if (searchInput) {
    searchInput.addEventListener("input", debounce(handleGlobalSearch, 300));
  }

  // Assistant Query Form
  const assistantForm = document.getElementById("assistant-query-form");
  if (assistantForm) {
    assistantForm.addEventListener("submit", handleAssistantQuerySubmit);
  }

  // Modal Closures
  document.getElementById("modal-close-btn").addEventListener("click", closeModal);
  document.getElementById("details-modal").addEventListener("click", (e) => {
    if (e.target.id === "details-modal") closeModal();
  });
}

// Auth Actions
async function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById("auth-email").value;
  const password = document.getElementById("auth-password").value;
  
  try {
    const res = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });
    
    if (!res.ok) {
      const err = await res.json();
      alert(err.detail || "Incorrect credentials");
      return;
    }
    
    const data = await res.json();
    localStorage.setItem("lifeos_token", data.access_token);
    checkAuth();
  } catch (err) {
    alert("Connection error: " + err);
  }
}

async function handleSignup() {
  const email = document.getElementById("auth-email").value;
  const password = document.getElementById("auth-password").value;
  if (!email || !password) {
    alert("Please enter both email and password");
    return;
  }
  
  try {
    const res = await fetch("/api/auth/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });
    
    if (!res.ok) {
      const err = await res.json();
      alert(err.detail || "Registration failed");
      return;
    }
    
    alert("Signup complete! Please click Log In.");
  } catch (err) {
    alert("Connection error: " + err);
  }
}

function handleLogout() {
  localStorage.removeItem("lifeos_token");
  checkAuth();
}

// API Fetch Wrapper
async function apiFetch(endpoint, method = "GET", body = null) {
  const headers = {
    "Authorization": `Bearer ${token}`
  };
  
  if (body && !(body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
  }
  
  const options = { method, headers };
  if (body) {
    options.body = body instanceof FormData ? body : JSON.stringify(body);
  }
  
  const res = await fetch(endpoint, options);
  if (res.status === 401) {
    handleLogout();
    throw new Error("Session expired. Please log in again.");
  }
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "API error occurred");
  }
  return res.json();
}

async function fetchDashboardData() {
  try {
    allItems = await apiFetch("/api/items");
    allConnections = await apiFetch("/api/connections");
    renderDashboard();
    lucide.createIcons();
  } catch (err) {
    console.error("Fetch error:", err);
  }
}

function switchTab(tabId) {
  currentTab = tabId;
  
  // Highlight active sidebar links and mobile tab buttons
  document.querySelectorAll(".nav-link").forEach(btn => btn.classList.remove("active"));
  document.querySelectorAll(".mobile-tab-btn").forEach(btn => btn.classList.remove("active"));
  document.querySelectorAll(".panel").forEach(panel => panel.classList.remove("active"));
  
  document.querySelectorAll(`.nav-link[onclick="switchTab('${tabId}')"]`).forEach(btn => btn.classList.add("active"));
  document.querySelectorAll(`.mobile-tab-btn[onclick="switchTab('${tabId}')"]`).forEach(btn => btn.classList.add("active"));
  
  const panel = document.getElementById(`panel-${tabId}`);
  if (panel) panel.classList.add("active");
  
  renderDashboard();
  lucide.createIcons();
}

function renderDashboard() {
  if (currentTab === "today") {
    renderTodayView();
  } else if (currentTab === "life-ops") {
    renderTaskBoard();
  } else if (currentTab === "second-brain") {
    renderSecondBrain();
  } else if (currentTab === "learning") {
    renderLearningSuite();
  } else if (currentTab === "search") {
    handleGlobalSearch();
  } else if (currentTab === "integrations") {
    renderIntegrationsView();
  }
}

// 1. TODAY VIEW
async function renderTodayView() {
  // Dynamic greeting
  const greetingEl = document.getElementById("today-greeting");
  if (greetingEl) {
    const hour = new Date().getHours();
    let salutation = "Good evening";
    if (hour < 12) salutation = "Good morning";
    else if (hour < 17) salutation = "Good afternoon";
    greetingEl.innerText = `${salutation}.`;
  }

  const overdueList = document.getElementById("today-overdue-list");
  const dueList = document.getElementById("today-due-list");
  const reviewsList = document.getElementById("today-reviews-list");
  const staleList = document.getElementById("today-stale-list");
  const insightCard = document.getElementById("today-insight-card");
  
  overdueList.innerHTML = "";
  dueList.innerHTML = "";
  reviewsList.innerHTML = "";
  staleList.innerHTML = "";
  insightCard.innerHTML = `<p class="loading-indicator">Thinking...</p>`;
  
  try {
    const data = await apiFetch("/api/today");
    
    // Overdue tasks
    if (data.overdue_tasks.length === 0) {
      overdueList.innerHTML = `<p class="empty-state-text">Nothing overdue.</p>`;
    } else {
      data.overdue_tasks.forEach(t => {
        overdueList.appendChild(createTodayTaskRow(t));
      });
    }
    
    // Due Today tasks
    if (data.due_today_tasks.length === 0) {
      dueList.innerHTML = `<p class="empty-state-text">Nothing due today. Enjoy the quiet.</p>`;
    } else {
      data.due_today_tasks.forEach(t => {
        dueList.appendChild(createTodayTaskRow(t));
      });
    }
    
    // Spaced Reviews Pending
    if (data.due_reviews.count === 0) {
      reviewsList.innerHTML = `<p class="empty-state-text">All caught up on reviews.</p>`;
    } else {
      data.due_reviews.items.forEach(r => {
        const row = document.createElement("div");
        row.className = "paper-row";
        row.onclick = () => {
          switchTab("learning");
          startSpacedRepQuiz(r.id, r.concept_id, r.concept_title, r.concept_content);
        };
        row.innerHTML = `
          <span style="font-weight: 500;">Review: ${r.concept_title}</span>
          <span style="font-size: 0.8rem; font-family: var(--font-mono); color: var(--accent);">Due Today</span>
        `;
        reviewsList.appendChild(row);
      });
    }
    
    // Stale Follow-ups
    if (data.stale_followups.count === 0) {
      staleList.innerHTML = `<p class="empty-state-text">No stale follow-ups.</p>`;
    } else {
      data.stale_followups.items.forEach(f => {
        const row = document.createElement("div");
        row.className = "paper-row";
        row.onclick = () => showItemDetails(f.id);
        const name = f.metadata_json.waiting_on || "someone";
        row.innerHTML = `
          <span>Waiting on <strong>${name}</strong>: ${f.title}</span>
          <span style="font-size: 0.8rem; color: var(--danger); font-family: var(--font-mono);">stale</span>
        `;
        staleList.appendChild(row);
      });
    }
    
    // Insight Card
    const ic = data.insight_card;
    insightCard.innerHTML = `
      <div class="today-insight-box">
        <h3>${ic.title}</h3>
        <p>${ic.description}</p>
        ${ic.action === 'task' ? `
          <button onclick="convertInsightToTask('${ic.title.replace(/'/g, "\\'")}', '${ic.description.replace(/'/g, "\\'")}')" class="btn btn-primary">
            Convert to Task
          </button>
        ` : ''}
      </div>
    `;
    
    lucide.createIcons();
  } catch (err) {
    console.error("Error loading today view:", err);
  }
}

function createTodayTaskRow(t) {
  const row = document.createElement("div");
  const isChecked = t.status === "done";
  row.className = `today-task-row ${isChecked ? 'checked' : ''}`;
  
  let dueTimeStr = "";
  if (t.due_date) {
    const d = new Date(t.due_date);
    dueTimeStr = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }
  
  const checkId = `check-today-${t.id}`;
  
  row.innerHTML = `
    <label class="custom-checkbox-wrapper" onclick="event.stopPropagation();">
      <input type="checkbox" id="${checkId}" ${isChecked ? 'checked' : ''} onchange="toggleTodayTask(${t.id}, this)">
      <span class="checkmark"></span>
      <span class="today-task-title" onclick="showItemDetails(${t.id})">${t.title}</span>
    </label>
    <span class="today-task-time">${dueTimeStr}</span>
  `;
  return row;
}

async function toggleTodayTask(itemId, checkbox) {
  const newStatus = checkbox.checked ? "done" : "todo";
  try {
    await apiFetch(`/api/items/${itemId}`, "PUT", { status: newStatus });
    const row = checkbox.closest(".today-task-row");
    if (checkbox.checked) {
      row.classList.add("checked");
    } else {
      row.classList.remove("checked");
    }
    fetchDashboardData();
  } catch (err) {
    checkbox.checked = !checkbox.checked;
    alert("Failed to update task: " + err.message);
  }
}

async function convertInsightToTask(title, description) {
  try {
    await apiFetch("/api/items", "POST", {
      type: "task",
      title: `Insight: ${title}`,
      content: description,
      priority: "medium",
      status: "todo"
    });
    alert("Task created from insight!");
    renderTodayView();
  } catch (err) {
    alert("Error creating task: " + err.message);
  }
}

// 2. LIFE OPS (PAPER TO-DO LISTS)
function renderTaskBoard() {
  const listContainer = document.getElementById("ops-tasks-list");
  listContainer.innerHTML = "";
  
  const tasks = allItems.filter(item => item.type === "task" || item.type === "deadline");
  
  const todoTasks = tasks.filter(t => t.status === "todo");
  const progressTasks = tasks.filter(t => t.status === "in_progress");
  const doneTasks = tasks.filter(t => t.status === "done" || t.status === "waiting");
  
  const groups = [
    { name: "To Do", items: todoTasks },
    { name: "In Progress", items: progressTasks },
    { name: "Completed / On Hold", items: doneTasks }
  ];
  
  groups.forEach(group => {
    if (group.items.length === 0) return;
    
    const header = document.createElement("div");
    header.className = "ops-group-header";
    header.innerText = group.name;
    listContainer.appendChild(header);
    
    group.items.forEach(task => {
      const row = document.createElement("div");
      row.className = `ops-task-row prio-${task.priority || 'medium'}`;
      
      const isCompleted = task.status === "done";
      const textDecorationStyle = isCompleted ? 'style="text-decoration: line-through; opacity: 0.5;"' : '';
      
      const relativeTime = getRelativeTime(task.due_date);
      
      const metaHtml = `
        <div class="ops-task-meta">
          ${relativeTime ? `<span style="font-family: var(--font-mono); font-size: 0.75rem;">${relativeTime}</span>` : ''}
          <span style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em;">${task.status.replace('_', ' ')}</span>
        </div>
      `;
      
      row.innerHTML = `
        <div style="display:flex; align-items:center; gap:0.5rem; flex:1;">
          <span class="ops-task-title" onclick="showItemDetails(${task.id})" ${textDecorationStyle}>${task.title}</span>
        </div>
        ${metaHtml}
      `;
      listContainer.appendChild(row);
    });
  });
  
  if (tasks.length === 0) {
    listContainer.innerHTML = `<p class="empty-state-text">No loops recorded. Type above to commit.</p>`;
  }
}

function getRelativeTime(dueDateStr) {
  if (!dueDateStr) return "";
  const due = new Date(dueDateStr);
  const now = new Date();
  
  const dueDate = new Date(due.getFullYear(), due.getMonth(), due.getDate());
  const nowDate = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  
  const diffTime = dueDate.getTime() - nowDate.getTime();
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
  if (diffDays === 0) return "due today";
  if (diffDays === 1) return "due tomorrow";
  if (diffDays === -1) return "overdue by 1 day";
  if (diffDays < -1) return `overdue by ${Math.abs(diffDays)} days`;
  return `in ${diffDays} days`;
}

async function handleCreateTask(e) {
  e.preventDefault();
  const title = document.getElementById("task-title").value;
  const content = document.getElementById("task-desc").value;
  const priority = document.getElementById("task-priority").value;
  const due_date = document.getElementById("task-due").value || null;
  
  const recurrence = document.getElementById("task-recurrence").value;
  const recurrence_days = document.getElementById("task-recurrence-days").value || null;
  
  const metadata_json = {
    is_recurring: recurrence !== "none",
    recurrence_interval: recurrence,
    recurrence_custom_days: recurrence_days
  };
  
  try {
    await apiFetch("/api/items", "POST", {
      type: "task",
      title,
      content,
      priority,
      due_date: due_date ? new Date(due_date).toISOString() : null,
      status: "todo",
      metadata_json: metadata_json
    });
    
    document.getElementById("create-task-form").reset();
    if (document.getElementById("custom-recurrence-days-group")) {
      document.getElementById("custom-recurrence-days-group").style.display = "none";
    }
    fetchDashboardData();
  } catch (err) {
    alert("Error creating task: " + err.message);
  }
}

async function handleCommitSubmit() {
  const input = document.getElementById("commitment-input");
  const text = input.value.trim();
  if (!text) return;
  
  const previewBox = document.getElementById("commitment-preview");
  const previewDetails = document.getElementById("commitment-preview-details");
  
  previewBox.style.display = "block";
  previewDetails.innerHTML = `<p class="loading-indicator">Thinking...</p>`;
  
  try {
    const res = await apiFetch("/api/lifeops/commit-parse", "POST", { text });
    lastParsedCommitment = res;
    
    const dateStr = res.due_date ? new Date(res.due_date).toLocaleDateString() : "None";
    previewDetails.innerHTML = `
      <div><strong>Title:</strong> ${res.title}</div>
      <div><strong>Due Date:</strong> ${dateStr}</div>
      <div><strong>Priority:</strong> <span class="priority-tag priority-${res.priority}">${res.priority}</span></div>
      <div><strong>Category:</strong> ${res.category || "None"}</div>
    `;
  } catch (err) {
    previewDetails.innerHTML = `<p style="color:var(--danger);">Parsing failed: ${err.message}</p>`;
  }
  
  lucide.createIcons();
}

async function confirmCommitment() {
  if (!lastParsedCommitment) return;
  try {
    const due_date = lastParsedCommitment.due_date ? new Date(lastParsedCommitment.due_date).toISOString() : null;
    await apiFetch("/api/items", "POST", {
      type: "task",
      title: lastParsedCommitment.title,
      content: `Category: ${lastParsedCommitment.category || 'general'}`,
      priority: lastParsedCommitment.priority || 'medium',
      due_date: due_date,
      status: "todo",
      metadata_json: { category: lastParsedCommitment.category, commitment_text: document.getElementById("commitment-input").value }
    });
    
    document.getElementById("commitment-input").value = "";
    document.getElementById("commitment-preview").style.display = "none";
    lastParsedCommitment = null;
    fetchDashboardData();
  } catch (err) {
    alert("Error saving commitment: " + err.message);
  }
}

function cancelCommitment() {
  document.getElementById("commitment-preview").style.display = "none";
  lastParsedCommitment = null;
}

// 3. SECOND BRAIN (SPLIT VIEW + DETAILED WORKSPACE)
function renderSecondBrain() {
  const notesList = document.getElementById("notes-list");
  notesList.innerHTML = "";
  
  const notes = allItems.filter(item => item.type === "note");
  
  if (notes.length === 0) {
    notesList.innerHTML = `<p class="empty-state-text" style="font-size: 0.85rem;">Nothing captured.</p>`;
    return;
  }
  
  notes.forEach((note, idx) => {
    const item = document.createElement("div");
    item.className = `notes-list-item ${activeNoteId === note.id ? 'selected' : ''}`;
    item.setAttribute("data-id", note.id);
    
    item.onclick = (e) => {
      if (e.target.classList.contains("note-checkbox")) return;
      selectNote(note.id);
    };
    
    const snippet = note.content ? note.content.substring(0, 45) + (note.content.length > 45 ? "..." : "") : "No thoughts";
    
    item.innerHTML = `
      <div class="note-checkbox-container">
        <input type="checkbox" class="note-checkbox" data-id="${note.id}" onclick="event.stopPropagation();">
        <div style="flex:1; overflow:hidden;">
          <div class="notes-list-item-title">${note.title}</div>
          <div class="notes-list-item-snippet">${snippet}</div>
        </div>
      </div>
    `;
    notesList.appendChild(item);
  });
  
  // Select first note automatically if none is active
  if (!activeNoteId && notes.length > 0) {
    selectNote(notes[0].id);
  }
}

function selectNote(noteId) {
  activeNoteId = noteId;
  
  document.querySelectorAll(".notes-list-item").forEach(item => {
    item.classList.remove("selected");
  });
  const itemEl = document.querySelector(`.notes-list-item[data-id="${noteId}"]`);
  if (itemEl) itemEl.classList.add("selected");
  
  const note = allItems.find(n => n.id === noteId);
  if (!note) return;
  
  document.getElementById("note-editor-title").value = note.title;
  document.getElementById("note-editor-textarea").value = note.content || "";
  
  renderRelatedConnections(noteId);
}

function renderRelatedConnections(noteId) {
  const linksBox = document.getElementById("note-related-links");
  linksBox.innerHTML = "";
  
  const conns = allConnections.filter(c => c.source_id === noteId || c.target_id === noteId);
  if (conns.length > 0) {
    linksBox.style.display = "block";
    linksBox.innerHTML = `<strong>Related:</strong> `;
    
    conns.forEach((c, idx) => {
      const otherTitle = c.source_id === noteId ? c.target_title : c.source_title;
      const otherId = c.source_id === noteId ? c.target_id : c.source_id;
      
      const a = document.createElement("span");
      a.className = "text-link";
      a.style.marginRight = "0.75rem";
      a.onclick = () => selectNote(otherId);
      a.innerText = otherTitle;
      
      linksBox.appendChild(a);
    });
  } else {
    linksBox.style.display = "none";
  }
}

function triggerNoteAutoSave() {
  if (!activeNoteId) return;
  clearTimeout(saveTimeout);
  
  saveTimeout = setTimeout(async () => {
    const title = document.getElementById("note-editor-title").value;
    const content = document.getElementById("note-editor-textarea").value;
    
    try {
      await apiFetch(`/api/items/${activeNoteId}`, "PUT", { title, content });
      // Quietly update state copy
      const idx = allItems.findIndex(i => i.id === activeNoteId);
      if (idx !== -1) {
        allItems[idx].title = title;
        allItems[idx].content = content;
      }
      
      // Update sidebar title and snippet without reloading list
      const row = document.querySelector(`.notes-list-item[data-id="${activeNoteId}"]`);
      if (row) {
        row.querySelector(".notes-list-item-title").innerText = title;
        row.querySelector(".notes-list-item-snippet").innerText = content.substring(0, 45) + "...";
      }
    } catch (err) {
      console.error("Auto-save failed:", err);
    }
  }, 1000);
}

// Floating Selection Formatting Bar
function setupFloatingToolbar() {
  const editor = document.getElementById("note-editor-textarea");
  const toolbar = document.getElementById("floating-toolbar");
  
  editor.addEventListener("select", () => {
    const start = editor.selectionStart;
    const end = editor.selectionEnd;
    
    if (start !== end) {
      const rect = editor.getBoundingClientRect();
      toolbar.style.display = "flex";
      toolbar.style.position = "absolute";
      // Render floating above selected area roughly
      toolbar.style.top = `${editor.offsetTop + 10}px`;
      toolbar.style.left = `${editor.offsetLeft + 10}px`;
    } else {
      toolbar.style.display = "none";
    }
  });
  
  document.getElementById("toolbar-btn-bold").onclick = () => applyFormat("**", "**");
  document.getElementById("toolbar-btn-italic").onclick = () => applyFormat("*", "*");
  document.getElementById("toolbar-btn-link").onclick = () => {
    const url = prompt("Enter URL:");
    if (url) applyFormat("[", `](${url})`);
  };
}

function applyFormat(prefix, suffix) {
  const editor = document.getElementById("note-editor-textarea");
  const start = editor.selectionStart;
  const end = editor.selectionEnd;
  const text = editor.value;
  
  const formatted = prefix + text.substring(start, end) + suffix;
  editor.value = text.substring(0, start) + formatted + text.substring(end);
  
  triggerNoteAutoSave();
  document.getElementById("floating-toolbar").style.display = "none";
}

async function handleCreateNote(e) {
  e.preventDefault();
  const title = document.getElementById("note-title").value;
  const content = document.getElementById("note-body").value;
  
  const submitBtn = e.target.querySelector("button[type='submit']");
  const originalText = submitBtn.innerText;
  submitBtn.disabled = true;
  submitBtn.innerText = "Thinking...";
  
  try {
    const savedNote = await apiFetch("/api/items", "POST", {
      type: "note",
      title,
      content,
      status: "todo"
    });
    
    document.getElementById("create-note-form").reset();
    activeNoteId = savedNote.id;
    await fetchDashboardData();
  } catch (err) {
    alert("Error saving note: " + err.message);
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerText = originalText;
  }
}

async function handleGenerateDraft() {
  const checkboxes = document.querySelectorAll(".note-checkbox:checked");
  const selectedIds = Array.from(checkboxes).map(cb => parseInt(cb.getAttribute("data-id")));
  
  if (selectedIds.length === 0) {
    alert("Please select at least one note to compile.");
    return;
  }
  
  const format = document.getElementById("draft-format").value;
  const outputBox = document.getElementById("draft-output-box");
  const outputText = document.getElementById("draft-result-text");
  const btn = document.getElementById("btn-generate-draft");
  
  const origText = btn.innerText;
  btn.disabled = true;
  btn.innerText = "Thinking...";
  
  try {
    const res = await apiFetch("/api/brain/draft", "POST", {
      note_ids: selectedIds,
      format: format
    });
    
    outputBox.style.display = "block";
    outputText.value = res.draft;
  } catch (err) {
    alert("Draft generation failed: " + err.message);
  } finally {
    btn.disabled = false;
    btn.innerText = origText;
  }
}

async function handleSaveDraft() {
  const text = document.getElementById("draft-result-text").value;
  if (!text) return;
  const format = document.getElementById("draft-format").value;
  
  try {
    const saved = await apiFetch("/api/items", "POST", {
      type: "note",
      title: `Draft (${format.toUpperCase()})`,
      content: text,
      status: "todo"
    });
    alert("Draft saved!");
    document.getElementById("draft-output-box").style.display = "none";
    document.querySelectorAll(".note-checkbox:checked").forEach(cb => cb.checked = false);
    activeNoteId = saved.id;
    fetchDashboardData();
  } catch (err) {
    alert("Failed to save draft: " + err.message);
  }
}

// 4. LEARNING SUITE
function renderLearningSuite() {
  const materialsList = document.getElementById("study-resources-list");
  const topicsList = document.getElementById("weak-topics-list");
  
  materialsList.innerHTML = "";
  topicsList.innerHTML = "";
  
  const materials = allItems.filter(item => item.type === "study_material");
  const weakTopics = allItems.filter(item => item.type === "study_topic");
  
  // Render Materials as subject list rows with pastel borders
  if (materials.length === 0) {
    materialsList.innerHTML = `<p class="empty-state-text" style="font-size:0.85rem;">No study resources.</p>`;
  } else {
    materials.forEach((mat, idx) => {
      const item = document.createElement("div");
      item.className = "subject-row";
      item.style.borderLeftColor = pastelColors[idx % pastelColors.length];
      
      item.innerHTML = `
        <div class="material-title" style="font-weight: 500;">${mat.title}</div>
        <button class="btn" style="padding:0.3rem 0.6rem; font-size:0.8rem;" onclick="selectMaterialForStudy(${mat.id})">
          Study
        </button>
      `;
      materialsList.appendChild(item);
    });
  }
  
  // Render Weak Topic Radar as simple text percentages
  if (weakTopics.length === 0) {
    topicsList.innerHTML = `<p class="empty-state-text" style="font-size:0.85rem;">No topics identified.</p>`;
  } else {
    weakTopics.forEach((topic, idx) => {
      const item = document.createElement("div");
      item.className = "subject-row";
      item.style.borderLeftColor = pastelColors[idx % pastelColors.length];
      
      // Extract score or status
      const score = topic.metadata_json.score || "0%";
      item.innerHTML = `
        <div>
          <h4 style="font-size:0.9rem; font-weight:600; margin-bottom: 0.15rem;">${topic.title}</h4>
          <p style="font-size:0.8rem; color:var(--text-secondary);">${topic.content}</p>
        </div>
        <span class="topic-strength-percentage">${score} strength</span>
      `;
      topicsList.appendChild(item);
    });
  }

  fetchAndRenderDueReviews();
}

async function handleUploadMaterial(e) {
  e.preventDefault();
  const fileInput = document.getElementById("study-file");
  if (!fileInput.files.length) return;
  
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  
  const btn = e.target.querySelector("button[type='submit']");
  const origText = btn.innerText;
  btn.disabled = true;
  btn.innerText = "Thinking...";
  
  try {
    await apiFetch("/api/learning/upload", "POST", formData);
    fileInput.value = "";
    fetchDashboardData();
  } catch (err) {
    alert("Upload failed: " + err.message);
  } finally {
    btn.disabled = false;
    btn.innerText = origText;
  }
}

function selectMaterialForStudy(materialId) {
  const mat = allItems.find(item => item.id === materialId);
  if (!mat) return;
  
  document.getElementById("study-material-id").value = materialId;
  document.getElementById("study-session-form").style.display = "block";
  document.getElementById("study-session-output").style.display = "none";
  
  document.getElementById("quiz-room-card").querySelector("h2").innerHTML = `<i data-lucide="book-open"></i> Study: ${mat.title}`;
  lucide.createIcons();
}

async function handleStartStudySession(e) {
  e.preventDefault();
  const materialId = document.getElementById("study-material-id").value;
  const confusion = document.getElementById("study-confusion").value;
  
  const btn = document.getElementById("btn-start-study");
  const origText = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = `Thinking...`;
  
  try {
    const formData = new FormData();
    formData.append("material_id", materialId);
    formData.append("self_reported_confusion", confusion);
    
    const data = await apiFetch("/api/learning/study", "POST", formData);
    
    // Set Practice Quiz state variables
    currentPracticeQuestions = data.practice_questions || [];
    currentPracticeQuestionIdx = 0;
    practiceAnswers = [];
    currentPracticeMaterialId = parseInt(materialId);
    
    renderPracticeQuestion();
    fetchDashboardData();
  } catch (err) {
    alert("Study session failed: " + err.message);
  } finally {
    btn.disabled = false;
    btn.innerHTML = origText;
  }
}

// Single-Question Practice Quiz system with Custom Square Radios
function renderPracticeQuestion() {
  const output = document.getElementById("study-session-output");
  output.innerHTML = "";
  output.style.display = "block";
  
  if (currentPracticeQuestionIdx >= currentPracticeQuestions.length) {
    renderPracticeQuizSummary();
    return;
  }
  
  const q = currentPracticeQuestions[currentPracticeQuestionIdx];
  
  const box = document.createElement("div");
  box.className = "quiz-single-question";
  
  const optionsHtml = q.options.map((opt, oIdx) => {
    const optId = `practice-opt-${currentPracticeQuestionIdx}-${oIdx}`;
    return `
      <label class="custom-radio-wrapper" style="margin-bottom:0.75rem; display:flex; align-items:center;">
        <input type="radio" name="practice-radio" id="${optId}" value="${opt}" onchange="selectPracticeOption('${opt.replace(/'/g, "\\'")}')">
        <span class="radiomark"></span>
        <span style="font-size:0.95rem;">${opt}</span>
      </label>
    `;
  }).join("");
  
  box.innerHTML = `
    <span class="category-label">Question ${currentPracticeQuestionIdx + 1} of ${currentPracticeQuestions.length}</span>
    <div class="quiz-question-text" style="font-size: 1.2rem; line-height: 1.5; margin-bottom: 1.5rem;">${q.question}</div>
    <div class="quiz-options-list">${optionsHtml}</div>
    
    <div style="display:flex; justify-content:flex-end; margin-top:2rem;">
      <button class="btn btn-primary" id="btn-next-practice-question" disabled onclick="nextPracticeQuestion()">Next</button>
    </div>
  `;
  
  output.appendChild(box);
}

function selectPracticeOption(opt) {
  currentSelectedPracticeOpt = opt;
  document.getElementById("btn-next-practice-question").disabled = false;
}

function nextPracticeQuestion() {
  const q = currentPracticeQuestions[currentPracticeQuestionIdx];
  practiceAnswers.push({
    question: q.question,
    selected: currentSelectedPracticeOpt,
    correct: q.correct_answer,
    topic: q.topic || "general"
  });
  
  currentSelectedPracticeOpt = null;
  currentPracticeQuestionIdx++;
  renderPracticeQuestion();
}

function renderPracticeQuizSummary() {
  const output = document.getElementById("study-session-output");
  output.innerHTML = "";
  
  let correctCount = 0;
  practiceAnswers.forEach(ans => {
    if (ans.selected.trim() === ans.correct.trim()) correctCount++;
  });
  
  const container = document.createElement("div");
  container.className = "quiz-single-question";
  container.innerHTML = `
    <span class="category-label">Practice Quiz Completed</span>
    <div class="quiz-question-text" style="font-size: 1.4rem; margin-bottom: 1rem;">
      Score: <strong>${correctCount} / ${practiceAnswers.length}</strong>
    </div>
    <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:1.5rem;">Clicking submit maps topics to your strength radar.</p>
    <button id="btn-submit-practice-quiz" class="btn btn-primary" style="width:100%;">Submit Results & Map Weak Topics</button>
  `;
  output.appendChild(container);
  
  document.getElementById("btn-submit-practice-quiz").onclick = async () => {
    const btn = document.getElementById("btn-submit-practice-quiz");
    btn.disabled = true;
    btn.innerText = "Thinking...";
    
    try {
      await apiFetch("/api/learning/test-submit", "POST", {
        material_id: currentPracticeMaterialId,
        answers: practiceAnswers
      });
      alert("Practice results mapped to Weak Topic Radar!");
      output.style.display = "none";
      fetchDashboardData();
    } catch (err) {
      alert("Failed to submit practice test: " + err.message);
      btn.disabled = false;
      btn.innerText = "Submit Results & Map Weak Topics";
    }
  };
}

// 5. SPACED REPETITION QUIZZING (Single Question / Custom Radio wrapper)
async function fetchAndRenderDueReviews() {
  const queueList = document.getElementById("spaced-rep-list");
  if (!queueList) return;
  queueList.innerHTML = `<p class="loading-indicator">Thinking...</p>`;
  
  try {
    const reviews = await apiFetch("/api/learning/reviews/due");
    queueList.innerHTML = "";
    
    if (reviews.length === 0) {
      queueList.innerHTML = `<p class="empty-state-text" style="font-size: 0.85rem;">No reviews due today.</p>`;
    } else {
      reviews.forEach(r => {
        const item = document.createElement("div");
        item.className = "subject-row";
        item.innerHTML = `
          <div>
            <div style="font-weight:600; font-size:0.95rem;">${r.concept_title}</div>
            <div style="font-size:0.75rem; color:var(--text-secondary);">Interval: ${r.interval_days}d</div>
          </div>
          <button class="btn" onclick="startSpacedRepQuiz(${r.id}, ${r.concept_id}, '${r.concept_title.replace(/'/g, "\\'")}', '${r.concept_content.replace(/'/g, "\\'")}')">
            Review
          </button>
        `;
        queueList.appendChild(item);
      });
    }
  } catch (err) {
    queueList.innerHTML = `<p style="color:var(--danger); font-size:0.85rem;">Failed to load reviews: ${err.message}</p>`;
  }
}

async function startSpacedRepQuiz(reviewId, conceptId, conceptTitle, conceptContent) {
  const quizCard = document.getElementById("spaced-rep-quiz-card");
  const infoBox = document.getElementById("spaced-quiz-concept-info");
  const questionsList = document.getElementById("spaced-quiz-questions-list");
  const submitBtn = document.getElementById("btn-submit-spaced-quiz");
  
  quizCard.style.display = "block";
  infoBox.innerHTML = `<strong>Concept:</strong> ${conceptTitle}<br><span style="font-size:0.8rem; font-style:italic;">${conceptContent.substring(0, 80)}...</span>`;
  questionsList.innerHTML = `<p class="loading-indicator">Thinking...</p>`;
  submitBtn.style.display = "none";
  
  currentActiveReview = { reviewId, conceptId };
  
  try {
    const data = await apiFetch(`/api/learning/reviews/generate-quiz?concept_id=${conceptId}`);
    currentReviewQuestions = data.questions || [];
    questionsList.innerHTML = "";
    
    if (currentReviewQuestions.length === 0) {
      questionsList.innerHTML = `<p class="empty-state-text">No questions generated.</p>`;
      return;
    }
    
    currentReviewQuestions.forEach((q, idx) => {
      const box = document.createElement("div");
      box.className = "quiz-single-question";
      box.style.border = "none";
      box.style.padding = "0";
      box.style.boxShadow = "none";
      box.style.marginBottom = "1.5rem";
      box.setAttribute("data-q-idx", idx);
      
      const optionsHtml = q.options.map((opt, oIdx) => `
        <label class="custom-radio-wrapper" style="margin-bottom:0.5rem; display:flex; align-items:center;">
          <input type="radio" name="spaced-opt-${idx}" value="${opt}" onclick="selectSpacedOpt(this)">
          <span class="radiomark"></span>
          <span style="font-size:0.9rem;">${opt}</span>
        </label>
      `).join("");
      
      box.innerHTML = `
        <div style="font-size:0.95rem; font-weight:600; margin-bottom:0.75rem;">Q${idx+1}: ${q.question}</div>
        <div class="spaced-options-list">${optionsHtml}</div>
        <div class="explanation-box-placeholder" style="margin-top:0.5rem;"></div>
      `;
      questionsList.appendChild(box);
    });
    
    submitBtn.style.display = "block";
    quizCard.scrollIntoView({ behavior: "smooth" });
  } catch (err) {
    questionsList.innerHTML = `<p style="color:var(--danger); font-size:0.85rem;">Error loading quiz: ${err.message}</p>`;
  }
}

function selectSpacedOpt(input) {
  const list = input.closest(".spaced-options-list");
  list.querySelectorAll("label").forEach(lbl => {
    lbl.style.color = "var(--text-primary)";
  });
  const label = input.parentElement;
  label.style.color = "var(--accent)";
}

async function submitSpacedQuiz() {
  if (!currentActiveReview) return;
  
  let score = 0;
  let allAnswered = true;
  
  currentReviewQuestions.forEach((q, idx) => {
    const selectedInput = document.querySelector(`input[name="spaced-opt-${idx}"]:checked`);
    if (!selectedInput) {
      allAnswered = false;
      return;
    }
    const val = selectedInput.value;
    const isCorrect = val.trim() === q.correct_answer.trim();
    if (isCorrect) {
      score++;
    }
    
    const box = document.querySelector(`.quiz-single-question[data-q-idx="${idx}"]`);
    box.querySelectorAll("label").forEach(lbl => {
      const input = lbl.querySelector("input");
      input.disabled = true;
      if (input.value.trim() === q.correct_answer.trim()) {
        lbl.style.color = "var(--success)";
      } else if (input.checked) {
        lbl.style.color = "var(--danger)";
      }
    });
    
    const explanationBox = box.querySelector(".explanation-box-placeholder");
    explanationBox.innerHTML = `
      <div style="font-size:0.8rem; padding:0.5rem; background:var(--bg-primary); border-left:3px solid ${isCorrect ? 'var(--success)' : 'var(--danger)'}; border-radius:4px; margin-top:0.5rem;">
        <strong>Correct:</strong> ${q.correct_answer}<br>
        <strong>Explanation:</strong> ${q.explanation}
      </div>
    `;
  });
  
  if (!allAnswered) {
    alert("Please answer all questions before submitting.");
    return;
  }
  
  const submitBtn = document.getElementById("btn-submit-spaced-quiz");
  submitBtn.disabled = true;
  
  try {
    const res = await apiFetch("/api/learning/reviews/submit", "POST", {
      review_id: currentActiveReview.reviewId,
      score: score
    });
    
    alert(`Recall Quiz Completed! Score: ${score}/3.\nNew Interval: ${res.interval_days} day(s).`);
    
    setTimeout(() => {
      document.getElementById("spaced-rep-quiz-card").style.display = "none";
      submitBtn.disabled = false;
      currentActiveReview = null;
      fetchDashboardData();
    }, 3000);
  } catch (err) {
    alert("Failed to submit review score: " + err.message);
    submitBtn.disabled = false;
  }
}

// 6. POMODORO TIMER start/pause text links toggles
function startPomodoro() {
  const startBtn = document.getElementById("btn-pomodoro-start");
  if (pomodoroIsRunning) {
    // Pause
    clearInterval(pomodoroInterval);
    pomodoroIsRunning = false;
    startBtn.innerText = "Start";
  } else {
    // Start
    pomodoroIsRunning = true;
    pomodoroSessionActive = true;
    startBtn.innerText = "Pause";
    
    pomodoroInterval = setInterval(() => {
      pomodoroSeconds--;
      updatePomodoroDisplay();
      
      if (pomodoroSeconds <= 0) {
        clearInterval(pomodoroInterval);
        pomodoroIsRunning = false;
        startBtn.innerText = "Start";
        alert("Pomodoro session completed! Please submit your study debrief.");
        showPomodoroDebriefForm();
      }
    }, 1000);
  }
}

function resetPomodoro() {
  clearInterval(pomodoroInterval);
  pomodoroIsRunning = false;
  pomodoroSeconds = 25 * 60;
  updatePomodoroDisplay();
  document.getElementById("btn-pomodoro-start").innerText = "Start";
  
  if (pomodoroSessionActive) {
    showPomodoroDebriefForm();
  }
}

function updatePomodoroDisplay() {
  const min = Math.floor(pomodoroSeconds / 60);
  const sec = pomodoroSeconds % 60;
  document.getElementById("pomodoro-timer").innerText = `${min.toString().padStart(2, "0")}:${sec.toString().padStart(2, "0")}`;
}

function showPomodoroDebriefForm() {
  document.getElementById("pomodoro-debrief-form").style.display = "block";
  document.getElementById("debrief-output").style.display = "none";
}

async function handlePomodoroDebriefSubmit(e) {
  e.preventDefault();
  const summary = document.getElementById("debrief-summary").value;
  const confusion = document.getElementById("debrief-confusion").value;
  
  const debriefOutput = document.getElementById("debrief-output");
  const form = document.getElementById("pomodoro-debrief-form");
  const submitBtn = form.querySelector("button[type='submit']");
  
  const origText = submitBtn.innerText;
  submitBtn.disabled = true;
  submitBtn.innerText = "Thinking...";
  
  try {
    const res = await apiFetch("/api/learning/debrief", "POST", { summary, confusion });
    
    debriefOutput.style.display = "block";
    debriefOutput.innerHTML = `
      <div style="font-weight:600; margin-bottom:0.25rem;">AI Session Debrief Insights</div>
      <p style="margin-bottom:0.5rem;">${res.feedback}</p>
      <div><strong>Suggested next focus:</strong> ${res.suggested_next_focus}</div>
    `;
    
    form.reset();
    form.style.display = "none";
    pomodoroSessionActive = false;
    
    fetchDashboardData();
  } catch (err) {
    alert("Debrief analysis failed: " + err.message);
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerText = origText;
  }
}

// 7. SUNDAY WEEKLY REVIEW
async function startWeeklyReview() {
  const modal = document.getElementById("weekly-review-modal");
  const summaryBody = document.getElementById("weekly-review-body");
  const attentionList = document.getElementById("weekly-review-attention-list");
  
  modal.classList.add("active");
  summaryBody.innerHTML = `<p class="loading-indicator">Thinking...</p>`;
  attentionList.innerHTML = "";
  
  try {
    const data = await apiFetch("/api/lifeops/weekly-review");
    
    let formattedSummary = data.summary
      .replace(/\n/g, "<br>")
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/\*(.*?)/g, "• $1");
      
    summaryBody.innerHTML = formattedSummary;
    
    const attentionIds = data.attention_item_ids || [];
    const tasks = allItems.filter(t => attentionIds.includes(t.id));
    if (tasks.length === 0) {
      attentionList.innerHTML = `<p class="empty-state-text" style="font-size:0.85rem;">No items slipping.</p>`;
    } else {
      tasks.forEach(t => {
        const row = document.createElement("div");
        row.className = "paper-row";
        row.innerHTML = `
          <div style="flex:1;">
            <div style="font-weight:600;">${t.title}</div>
            <div style="font-size:0.75rem; color:var(--text-secondary);">Due: ${t.due_date ? new Date(t.due_date).toLocaleDateString() : 'no date'}</div>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <button onclick="snoozeWeeklyItem(${t.id})" class="btn btn-secondary" style="padding:0.25rem 0.5rem; font-size:0.75rem;">Snooze</button>
            <button onclick="rescheduleWeeklyItem(${t.id})" class="btn btn-secondary" style="padding:0.25rem 0.5rem; font-size:0.75rem;">Reschedule</button>
            <button onclick="deleteWeeklyItem(${t.id})" class="btn btn-danger" style="padding:0.25rem 0.5rem; font-size:0.75rem;">Delete</button>
          </div>
        `;
        attentionList.appendChild(row);
      });
    }
  } catch (err) {
    summaryBody.innerHTML = `<p style="color:var(--danger);">Summary failed: ${err.message}</p>`;
  }
}

function closeWeeklyReviewModal() {
  document.getElementById("weekly-review-modal").classList.remove("active");
}

async function snoozeWeeklyItem(itemId) {
  try {
    const item = allItems.find(t => t.id === itemId);
    if (!item) return;
    const baseDate = item.due_date ? new Date(item.due_date) : new Date();
    const newDueDate = new Date(baseDate.getTime() + 24 * 60 * 60 * 1000).toISOString();
    
    await apiFetch(`/api/items/${itemId}`, "PUT", { due_date: newDueDate });
    alert("Item snoozed 24 hours.");
    closeWeeklyReviewModal();
    fetchDashboardData();
  } catch (err) {
    alert("Snooze failed: " + err.message);
  }
}

async function rescheduleWeeklyItem(itemId) {
  const newDateStr = prompt("Enter new due date (YYYY-MM-DD):");
  if (!newDateStr) return;
  
  try {
    const due_date = new Date(newDateStr).toISOString();
    await apiFetch(`/api/items/${itemId}`, "PUT", { due_date });
    alert("Item rescheduled!");
    closeWeeklyReviewModal();
    fetchDashboardData();
  } catch (err) {
    alert("Reschedule failed: " + err.message);
  }
}

async function deleteWeeklyItem(itemId) {
  if (!confirm("Delete this loop?")) return;
  try {
    await apiFetch(`/api/items/${itemId}`, "DELETE");
    alert("Item deleted.");
    closeWeeklyReviewModal();
    fetchDashboardData();
  } catch (err) {
    alert("Deletion failed: " + err.message);
  }
}

// 8. GLOBAL FULL PAGE SEARCH
async function handleGlobalSearch() {
  const query = document.getElementById("global-search-input").value.trim();
  const resultsList = document.getElementById("search-results-list");
  
  if (query.length < 2) {
    resultsList.innerHTML = `<p class="empty-state-text">Type something above to begin searching.</p>`;
    return;
  }
  
  resultsList.innerHTML = `<p class="loading-indicator">Thinking...</p>`;
  
  try {
    const results = await apiFetch(`/api/search?q=${encodeURIComponent(query)}`);
    resultsList.innerHTML = "";
    
    if (results.length === 0) {
      resultsList.innerHTML = `<p class="empty-state-text">No results found.</p>`;
    } else {
      results.forEach(item => {
        const row = document.createElement("div");
        row.className = "paper-row";
        row.onclick = () => showItemDetails(item.id);
        
        const snippet = item.content ? item.content.substring(0, 100) : "No description";
        row.innerHTML = `
          <div style="flex:1;">
            <div style="font-weight:600; font-size:0.95rem;">${item.title}</div>
            <div style="font-size:0.8rem; color:var(--text-secondary);">${snippet}</div>
          </div>
          <span style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--accent);">${item.type}</span>
        `;
        resultsList.appendChild(row);
      });
    }
  } catch (err) {
    resultsList.innerHTML = `<p style="color:var(--danger); font-size:0.85rem;">Search failed: ${err.message}</p>`;
  }
}

// 9. DETAILS MODALS AND OTHER HELPERS
async function showItemDetails(itemId) {
  const item = allItems.find(i => i.id === itemId);
  if (!item) return;
  
  const modal = document.getElementById("details-modal");
  const title = document.getElementById("modal-title");
  const body = document.getElementById("modal-body");
  const actionBtn = document.getElementById("modal-action-btn");
  
  title.innerText = `${item.type.toUpperCase()}: ${item.title}`;
  
  let html = `<p style="white-space: pre-wrap; margin-bottom: 1.5rem;">${item.content || "No description."}</p>`;
  
  const conns = allConnections.filter(c => c.source_id === item.id || c.target_id === item.id);
  if (conns.length > 0) {
    html += `<h4>Related Items (${conns.length})</h4><ul style="margin: 0.5rem 0 1.5rem 1.5rem; font-size:0.85rem;">`;
    conns.forEach(c => {
      const otherTitle = c.source_id === item.id ? c.target_title : c.source_title;
      const otherId = c.source_id === item.id ? c.target_id : c.source_id;
      const relation = c.connection_type.replace("_", " ");
      html += `<li>Mapped to <span class="text-link" onclick="closeModal(); showItemDetails(${otherId})">${otherTitle}</span> (${otherType(c, item.id)}) via <em>${relation}</em></li>`;
    });
    html += `</ul>`;
  }
  
  const isAuto = item.metadata_json.auto_generated || item.metadata_json.is_study_revision;
  if (isAuto) {
    html += `
      <div class="explainability-box">
        <strong>AI Origin Trace</strong>
        <p>This item was auto-generated by the AI when you logged the source content.</p>
      </div>
    `;
  }
  
  if (item.type === "note" && item.metadata_json.ai_analysis) {
    const analysis = item.metadata_json.ai_analysis;
    const suggestedTasks = analysis.suggested_tasks || [];
    const suggestedConns = analysis.suggested_connections || [];
    
    html += `
      <div class="explainability-box" style="margin-top: 1rem;">
        <strong>Second Brain AI Trace</strong>
        <p style="margin-bottom:0.5rem;"><strong>Analysis summary:</strong> ${analysis.trace ? analysis.trace.prompt_summary : "Note linkage complete."}</p>
    `;
    
    if (suggestedTasks.length > 0) {
      html += `<p style="margin-top:0.25rem;"><strong>Auto-created Tasks:</strong></p><ul style="margin-left: 1rem;">`;
      suggestedTasks.forEach(t => {
        html += `<li>${t.title} (${t.priority} priority)</li>`;
      });
      html += `</ul>`;
    }
    
    if (suggestedConns.length > 0) {
      html += `<p style="margin-top:0.25rem;"><strong>Suggested Links (Click to Connect):</strong></p><ul style="margin-left: 1rem; list-style: none;">`;
      suggestedConns.forEach(c => {
        const matchNote = allItems.find(n => n.id === c.target_id);
        const matchTitle = matchNote ? matchNote.title : `Note #${c.target_id}`;
        
        const exists = allConnections.some(conn => 
          (conn.source_id === item.id && conn.target_id === c.target_id) || 
          (conn.target_id === item.id && conn.source_id === c.target_id)
        );
        
        if (exists) {
          html += `<li style="margin-bottom:0.5rem; color:var(--success);"><i data-lucide="check" style="width:12px; height:12px; display:inline-block;"></i> Linked with <strong>${matchTitle}</strong></li>`;
        } else {
          html += `<li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem; justify-content:space-between;">
            <span>Link with <strong>${matchTitle}</strong> <em>(${c.reason})</em></span>
            <button onclick="acceptConnection(${item.id}, ${c.target_id}, '${c.connection_type}')" class="btn" style="padding:0.2rem 0.5rem; font-size:0.7rem; border:none; line-height:1;">Accept</button>
          </li>`;
        }
      });
      html += `</ul>`;
    }
    
    html += `</div>`;
  }

  if (item.type === "task" || item.type === "deadline") {
    let waitingHtml = `
      <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--border);">
        <h4 style="font-size:0.9rem; margin-bottom:0.5rem;">Follow-up Tracker</h4>
    `;
    if (item.status === "waiting" || (item.metadata_json && item.metadata_json.waiting_on)) {
      const name = item.metadata_json.waiting_on || "someone";
      const since = item.metadata_json.waiting_since ? new Date(item.metadata_json.waiting_since).toLocaleDateString() : 'unknown';
      waitingHtml += `
        <p style="font-size:0.85rem; margin-bottom:0.5rem;">Currently waiting on <strong>${name}</strong> (since ${since}).</p>
        <button onclick="clearWaitingStatus(${item.id})" class="btn btn-secondary" style="padding:0.3rem 0.6rem; font-size:0.8rem; border:none;">Clear Waiting Status</button>
      `;
    } else {
      waitingHtml += `
        <div style="display:flex; gap:0.5rem;">
          <input type="text" id="waiting-person-input" placeholder="Person's name..." style="flex:1; padding:0.3rem 0.5rem; font-size:0.85rem; border-radius:4px; border:1px solid var(--border); background:var(--bg-surface); color:var(--text-primary);">
          <button onclick="setWaitingStatus(${item.id})" class="btn btn-primary" style="padding:0.3rem 0.6rem; font-size:0.8rem;">Set Waiting</button>
        </div>
      `;
    }
    waitingHtml += `</div>`;
    html += waitingHtml;
  }
  
  body.innerHTML = html;
  
  if (item.type === "task" || item.type === "deadline") {
    actionBtn.style.display = "block";
    if (item.status === "todo") {
      actionBtn.innerText = "Start Task";
      actionBtn.onclick = () => updateItemStatus(item.id, "in_progress");
    } else if (item.status === "in_progress") {
      actionBtn.innerText = "Complete Task";
      actionBtn.onclick = () => updateItemStatus(item.id, "done");
    } else {
      actionBtn.innerText = "Reopen Task";
      actionBtn.onclick = () => updateItemStatus(item.id, "todo");
    }
  } else {
    actionBtn.style.display = "none";
  }
  
  modal.classList.add("active");
  lucide.createIcons();
}

function otherType(c, currentId) {
  return c.source_id === currentId ? c.target_type.toUpperCase() : c.source_type.toUpperCase();
}

async function updateItemStatus(itemId, newStatus) {
  try {
    await apiFetch(`/api/items/${itemId}`, "PUT", { status: newStatus });
    closeModal();
    fetchDashboardData();
  } catch (err) {
    alert("Status update failed: " + err.message);
  }
}

function closeModal() {
  document.getElementById("details-modal").classList.remove("active");
}

async function setWaitingStatus(itemId) {
  const name = document.getElementById("waiting-person-input").value.trim();
  if (!name) return;
  
  try {
    const item = allItems.find(t => t.id === itemId);
    const meta = { ...item.metadata_json, waiting_on: name, waiting_since: new Date().toISOString() };
    await apiFetch(`/api/items/${itemId}`, "PUT", {
      status: "waiting",
      metadata_json: meta
    });
    closeModal();
    fetchDashboardData();
  } catch (err) {
    alert("Failed to set waiting status: " + err.message);
  }
}

async function clearWaitingStatus(itemId) {
  try {
    const item = allItems.find(t => t.id === itemId);
    const meta = { ...item.metadata_json };
    delete meta.waiting_on;
    delete meta.waiting_since;
    await apiFetch(`/api/items/${itemId}`, "PUT", {
      status: "todo",
      metadata_json: meta
    });
    closeModal();
    fetchDashboardData();
  } catch (err) {
    alert("Failed to clear waiting status: " + err.message);
  }
}

async function acceptConnection(sourceId, targetId, connType) {
  try {
    await apiFetch("/api/connections", "POST", {
      source_id: parseInt(sourceId),
      target_id: parseInt(targetId),
      connection_type: connType
    });
    fetchDashboardData();
    showItemDetails(sourceId);
  } catch (err) {
    alert("Failed to accept connection: " + err.message);
  }
}

function toggleCustomRecurrence() {
  const select = document.getElementById("task-recurrence");
  const group = document.getElementById("custom-recurrence-days-group");
  if (select.value === "custom") {
    group.style.display = "block";
  } else {
    group.style.display = "none";
  }
}

// 6. INTEGRATIONS MANAGEMENT
// 6. INTEGRATIONS MANAGEMENT
function getBrandLogo(name) {
  const normalized = name.replace("-", "_").toLowerCase();
  if (normalized === "google_calendar" || normalized === "googlecalendar") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M19 4H18V2H16V4H8V2H6V4H5C3.89 4 3.01 4.9 3.01 6L3 20C3 21.1 3.89 22 5 22H19C20.1 22 21 21.1 21 20V6C21 4.9 20.1 4 19 4ZM19 20H5V9H19V20ZM7 11H12V16H7V11Z" fill="#4285F4"/>
    </svg>`;
  }
  if (normalized === "google_tasks" || normalized === "googletasks") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM9.29 16.29L5.7 12.7C5.31 12.31 5.31 11.68 5.7 11.29C6.09 10.9 6.72 10.9 7.11 11.29L10 14.17L16.89 7.29C17.28 6.9 17.91 6.9 18.3 7.29C18.69 7.68 18.69 8.31 18.3 8.7L10.71 16.29C10.32 16.68 9.68 16.68 9.29 16.29Z" fill="#1A73E8"/>
    </svg>`;
  }
  if (normalized === "gmail") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M20 4H4C2.9 4 2 4.9 2 6V18C2 19.1 2.9 20 4 20H20C21.1 20 22 19.1 22 18V6C22 4.9 21.1 4 20 4ZM20 8L12 13L4 8V6L12 11L20 6V8Z" fill="#EA4335"/>
    </svg>`;
  }
  if (normalized === "slack") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523 2.528 2.528 0 0 1-2.522-2.523 2.528 2.528 0 0 1 2.522-2.52h2.52v2.52zm1.261 0a2.528 2.528 0 0 1 2.52-2.52h5.043a2.528 2.528 0 0 1 2.522 2.52v5.042a2.528 2.528 0 0 1-2.522 2.52H8.823a2.528 2.528 0 0 1-2.52-2.52v-5.042zM8.823 5.043a2.528 2.528 0 0 1-2.52-2.52A2.528 2.528 0 0 1 8.823 0a2.528 2.528 0 0 1 2.52 2.523v2.52h-2.52zm0 1.261a2.528 2.528 0 0 1 2.52 2.52v5.043a2.528 2.528 0 0 1-2.52 2.522H3.78a2.528 2.528 0 0 1-2.522-2.522V8.824A2.528 2.528 0 0 1 3.78 6.304h5.043zm10.135 3.78a2.528 2.528 0 0 1 2.522-2.52 2.528 2.528 0 0 1 2.52 2.52 2.528 2.528 0 0 1-2.52 2.52h-2.522v-2.52zm-1.262 0a2.528 2.528 0 0 1-2.52 2.52h-5.043a2.528 2.528 0 0 1-2.522-2.52V5.043a2.528 2.528 0 0 1 2.522-2.52h5.043a2.528 2.528 0 0 1 2.52 2.52v5.042zm-3.78 10.135a2.528 2.528 0 0 1 2.52 2.522 2.528 2.528 0 0 1-2.52 2.522 2.528 2.528 0 0 1-2.522-2.522v-2.52h2.522zm0-1.262a2.528 2.528 0 0 1-2.52-2.52v-5.043a2.528 2.528 0 0 1 2.52-2.522h5.043a2.528 2.528 0 0 1 2.522 2.522v5.043a2.528 2.528 0 0 1-2.522 2.52H15.18z" fill="#E01E5A"/>
    </svg>`;
  }
  if (normalized === "notion") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M4.2 2h15.6C21 2 22 3 22 4.2v15.6c0 1.2-1 2.2-2.2 2.2H4.2C3 22 2 21 2 19.8V4.2C2 3 3 2 4.2 2zm3.1 3.5c-.3 0-.6.1-.8.4l-2 2.7c-.2.2-.3.5-.3.8V17c0 .8.7 1.5 1.5 1.5h1.2v-7.1l6.1 7.1h2.2c.3 0 .6-.1.8-.4l2-2.7c.2-.2.3-.5.3-.8V7c0-.8-.7-1.5-1.5-1.5h-1.2v7.1L10.5 5.5H7.3z" fill="#000000"/>
    </svg>`;
  }
  if (normalized === "github") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.464-1.11-1.464-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.579.688.481C19.137 20.164 22 16.418 22 12c0-5.523-4.477-10-10-10z" fill="#24292E"/>
    </svg>`;
  }
  if (normalized === "linear") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM12 20C7.58 20 4 16.42 4 12C4 7.58 7.58 4 12 4C16.42 4 20 7.58 20 12C20 16.42 16.42 20 12 20ZM14.5 9.5H9.5V14.5H14.5V9.5Z" fill="#5E6AD2"/>
    </svg>`;
  }
  if (normalized === "jira") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M11.53 2C11.53 2 11.95 5.58 8.89 8.64C5.83 11.7 2.25 11.28 2.25 11.28C2.25 11.28 5.48 12.35 7.42 14.29C9.36 16.23 10.43 19.46 10.43 19.46C10.43 19.46 10.85 15.88 13.91 12.82C16.97 9.76 20.55 10.18 20.55 10.18C20.55 10.18 17.32 9.11 15.38 7.17C13.44 5.23 12.37 2 12.37 2H11.53Z" fill="#0052CC"/>
    </svg>`;
  }
  if (normalized === "trello") {
    return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3ZM10 15C10 15.6 9.6 16 9 16H7C6.4 16 6 15.6 6 15V7C6 6.4 6.4 6 7 6H9C9.6 6 10 6.4 10 7V15ZM18 11C18 11.6 17.6 12 17 12H15C14.4 12 14 11.6 14 11V7C14 6.4 14.4 6 15 6H17C17.6 6 18 6.4 18 7V11Z" fill="#0079BF"/>
    </svg>`;
  }
  return `<i data-lucide="link-2"></i>`;
}

async function renderIntegrationsView() {
  const container = document.getElementById("integrations-list");
  if (!container) return;
  
  container.innerHTML = `<p class="loading-indicator">Fetching integrations status...</p>`;
  
  try {
    const integrations = await apiFetch("/api/integrations");
    container.innerHTML = "";
    
    if (integrations.length === 0) {
      container.innerHTML = `<p class="empty-state-text">No integrations configured in tool registry.</p>`;
      return;
    }
    
    integrations.forEach(item => {
      const card = document.createElement("div");
      card.className = "integration-card";
      card.id = `card-${item.name}`;
      
      const isConnected = item.is_connected;
      const health = item.health_status;
      const meta = item.metadata_json || {};
      const email = meta.email || "N/A";
      const errorMsg = item.error_message;
      
      // Determine badge class
      let badgeClass = "integration-status-disconnected";
      let statusLabel = "Not Connected";
      if (isConnected) {
        if (health === "broken") {
          badgeClass = "integration-status-broken";
          statusLabel = "Auth Expired";
        } else {
          badgeClass = "integration-status-connected";
          statusLabel = "Connected";
        }
      }
      
      const iconLogo = getBrandLogo(item.name);
      
      // Capitalize display name cleanly
      const displayName = item.name.split("_")
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");
        
      const descriptions = {
        google_calendar: "Sync events, schedule tasks, and track calendar deadlines seamlessly.",
        google_tasks: "Organize tasks and track priorities dynamically through your Life Board.",
        gmail: "Scan incoming messages and create second brain elements on the fly.",
        notion: "Import pages, sync databases, and reference structured notes.",
        slack: "Post status updates, fetch direct notifications, and keep team loops closed.",
        github: "Track open issues, pull requests, and code modifications in real time.",
        jira: "Manage sprint tasks, follow issues, and monitor roadmap delivery.",
        linear: "Link your cycles, track developer tasks, and close loops quickly.",
        trello: "Map project boards, lists, and visual card pipelines in LifeOS."
      };
      
      const desc = descriptions[item.name] || "Automated third-party service integration.";
        
      let detailsHtml = "";
      if (isConnected) {
        const lastSync = item.last_sync_at ? new Date(item.last_sync_at).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) : "Just now";
        detailsHtml = `
          <ul class="integration-details-list">
            <li><span>Connected Account</span> <span>${email}</span></li>
            <li><span>Active Sync</span> <span>Enabled</span></li>
            <li><span>Last Health Check</span> <span>${lastSync}</span></li>
            <li><span>Permissions</span> <span>Read/Write</span></li>
          </ul>
        `;
      }
      
      let errorHtml = "";
      if (isConnected && health === "broken" && errorMsg) {
        errorHtml = `
          <div class="integration-error-box">
            <strong>Error details:</strong> ${errorMsg}
          </div>
        `;
      }
      
      let actionsHtml = "";
      if (!isConnected) {
        actionsHtml = `
          <button class="btn btn-primary" onclick="connectIntegration('${item.name}')" style="width: 100%; display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
            <i data-lucide="plus" style="width:14px; height:14px;"></i> Connect Service
          </button>
        `;
      } else {
        actionsHtml = `
          <div style="display: flex; gap: 0.5rem; width: 100%;">
            <button class="btn btn-secondary" onclick="testIntegration('${item.name}')" style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 0.4rem;">
              <i data-lucide="activity" style="width:14px; height:14px;"></i> Test
            </button>
            <button class="btn btn-danger" onclick="disconnectIntegration('${item.name}')" style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 0.4rem;">
              <i data-lucide="trash-2" style="width:14px; height:14px;"></i> Disconnect
            </button>
          </div>
          ${health === "broken" ? `
            <button class="btn btn-primary" onclick="connectIntegration('${item.name}')" style="width: 100%; margin-top: 0.5rem; display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
              <i data-lucide="refresh-cw" style="width:14px; height:14px;"></i> Reconnect Account
            </button>
          ` : ""}
        `;
      }
      
      card.innerHTML = `
        <div class="integration-card-header">
          <div class="integration-meta">
            <div class="integration-icon-wrapper">
              ${iconLogo}
            </div>
            <div>
              <h3 class="integration-title">${displayName}</h3>
              <p style="font-size: 0.8rem; color: var(--text-secondary); margin-top: 0.15rem; line-height: 1.3;">${desc}</p>
            </div>
          </div>
          <span class="integration-status-badge ${badgeClass}">${statusLabel}</span>
        </div>
        
        ${detailsHtml}
        ${errorHtml}
        
        <div style="margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--border);">
          ${actionsHtml}
        </div>
      `;
      
      container.appendChild(card);
    });
    
    lucide.createIcons();
  } catch (err) {
    container.innerHTML = `<p style="color:var(--danger); font-size:0.95rem;">Failed to load integrations: ${err.message}</p>`;
  }
}

async function connectIntegration(name) {
  const card = document.getElementById(`card-${name}`);
  const originalHtml = card ? card.innerHTML : "";
  if (card) {
    card.innerHTML = `
      <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 180px; gap: 1rem;">
        <i data-lucide="loader-2" class="spinner" style="width: 32px; height: 32px; color: var(--accent);"></i>
        <p style="font-size: 0.9rem; color: var(--text-secondary);">Connecting to ${name}...</p>
      </div>
    `;
    lucide.createIcons();
  }
  
  try {
    const res = await apiFetch(`/api/integrations/${name}/auth-url`);
    const authUrl = res.auth_url;
    if (authUrl) {
      // Open OAuth in a separate popup tab
      const width = 600;
      const height = 700;
      const left = (screen.width - width) / 2;
      const top = (screen.height - height) / 2;
      const popup = window.open(authUrl, "LifeOS OAuth", `width=${width},height=${height},left=${left},top=${top}`);
      
      const displayName = name.split("_").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
      
      // Periodically refresh integrations panel to catch active connection state updates
      const checkInterval = setInterval(async () => {
        const integrations = await apiFetch("/api/integrations");
        const match = integrations.find(i => i.name === name);
        if (match && match.is_connected && match.health_status === "healthy") {
          clearInterval(checkInterval);
          showToast(`${displayName} connected successfully!`, "success");
          fetchDashboardData();
          renderIntegrationsView();
        }
      }, 2000);
      
      // Watch for popup close to stop check
      const popupTimer = setInterval(() => {
        if (!popup || popup.closed) {
          clearInterval(popupTimer);
          setTimeout(() => {
            clearInterval(checkInterval);
            if (card) renderIntegrationsView();
          }, 3000);
        }
      }, 1000);
    } else {
      showToast("Could not retrieve authorization URL.", "error");
      if (card) card.innerHTML = originalHtml;
    }
  } catch (err) {
    showToast(err.message, "error");
    if (card) renderIntegrationsView();
  }
}

async function disconnectIntegration(name) {
  if (!confirm(`Are you sure you want to disconnect ${name}?`)) return;
  
  const card = document.getElementById(`card-${name}`);
  if (card) {
    card.innerHTML = `
      <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 180px; gap: 1rem;">
        <i data-lucide="loader-2" class="spinner" style="width: 32px; height: 32px; color: var(--danger);"></i>
        <p style="font-size: 0.9rem; color: var(--text-secondary);">Disconnecting service...</p>
      </div>
    `;
    lucide.createIcons();
  }
  
  try {
    await apiFetch(`/api/integrations/${name}`, "DELETE");
    showToast(`Disconnected ${name} successfully.`, "success");
    renderIntegrationsView();
  } catch (err) {
    showToast("Disconnection failed: " + err.message, "error");
    renderIntegrationsView();
  }
}

async function testIntegration(name) {
  const card = document.getElementById(`card-${name}`);
  
  // Show in-place checking state
  if (card) {
    const badge = card.querySelector(".integration-status-badge");
    if (badge) {
      badge.className = "integration-status-badge";
      badge.style.backgroundColor = "rgba(212, 169, 106, 0.15)";
      badge.style.color = "var(--warning)";
      badge.innerHTML = `<i data-lucide="loader-2" class="spinner" style="width:10px; height:10px; margin-right:4px;"></i> Checking...`;
      lucide.createIcons();
    }
  }
  
  try {
    const res = await apiFetch(`/api/integrations/${name}/test`, "POST");
    if (res.status === "healthy") {
      showToast(`${name.split("_").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ")} connection is healthy!`, "success");
    } else {
      showToast(`${name.split("_").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ")} health test failed: ${res.error_message}`, "error");
    }
    renderIntegrationsView();
  } catch (err) {
    showToast("Health test failed: " + err.message, "error");
    renderIntegrationsView();
  }
}

// 7. ASSISTANT CHAT TRIGGER
async function handleAssistantQuerySubmit(e) {
  e.preventDefault();
  const input = document.getElementById("assistant-query-input");
  const responseBox = document.getElementById("assistant-query-response");
  
  const text = input.value.trim();
  if (!text) return;
  
  responseBox.style.display = "block";
  responseBox.innerHTML = `<p class="loading-indicator">Assistant thinking...</p>`;
  
  try {
    const res = await apiFetch("/api/assistant/query", "POST", { query: text });
    
    // Format response markdown/bold text simply
    const formatted = res.response_message
      .replace(/\n/g, "<br>")
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
      
    let shortcutHtml = "";
    if (res.execution_status === "need_connection" || res.response_message.includes("isn't connected") || res.response_message.includes("not connected")) {
      shortcutHtml = `
        <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px dashed var(--border);">
          <button class="btn btn-primary" onclick="connectIntegration('google_calendar')" style="font-size: 0.85rem; padding: 0.4rem 0.8rem; display: flex; align-items: center; gap: 0.4rem; cursor: pointer;">
            <i data-lucide="plus" style="width:14px; height:14px;"></i> Connect Google Calendar
          </button>
        </div>
      `;
    }
      
    responseBox.innerHTML = `
      <div style="font-weight: 600; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.4rem; color: var(--text-primary);">
        <i data-lucide="sparkles" style="width: 14px; height: 14px; color: var(--accent);"></i> Assistant
      </div>
      <div style="color: var(--text-primary); font-size: 0.95rem;">${formatted}</div>
      ${shortcutHtml}
    `;
    
    input.value = "";
    
    // If command successfully triggered updates, refresh dashboard widgets in background
    if (res.execution_status === "success") {
      fetchDashboardData();
    }
    
    lucide.createIcons();
  } catch (err) {
    responseBox.innerHTML = `<p style="color: var(--danger);">Query failed: ${err.message}</p>`;
  }
}

// Utilities
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

