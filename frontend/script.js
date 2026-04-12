function suchen() {
  const symptom = document.getElementById("messageInput").value.trim();
  const chatContainer = document.getElementById("chatMessages");

  if (!symptom) return;

  // USER MESSAGE
  const userRow = document.createElement("div");
  userRow.className = "message-row user-row";

  userRow.innerHTML = `
    <div class="avatar user-avatar">
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <circle cx="12" cy="8" r="3.5" stroke="currentColor" stroke-width="1.8" />
        <path
          d="M5.5 18C6.4 14.9 8.8 13.5 12 13.5C15.2 13.5 17.6 14.9 18.5 18"
          stroke="currentColor"
          stroke-width="1.8"
          stroke-linecap="round"
        />
      </svg>
    </div>

    <div class="message-card user-card">
      <div class="message-author">User</div>
      <div class="message-text">${symptom}</div>
      <div class="message-time">${new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</div>
    </div>
  `;

  chatContainer.appendChild(userRow);
  chatContainer.scrollTop = chatContainer.scrollHeight;

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: symptom })
  })
    .then(res => {
      if (!res.ok) throw new Error("Serverfehler");
      return res.json();
    })
    .then(data => {

      // ASSISTANT MESSAGE
      const botRow = document.createElement("div");
      botRow.className = "message-row assistant-row";

      botRow.innerHTML = `
        <div class="avatar assistant-avatar">🌿</div>

        <div class="message-card assistant-card latest-message">
          <div class="message-author">Dr. Nature</div>
          <div class="message-text">
            <p>${data.reply}</p>
          </div>
          <div class="message-footer">
            <span class="message-time">${new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</span>
          </div>
        </div>
      `;

      chatContainer.appendChild(botRow);

      requestAnimationFrame(() => {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      });
    })
    .catch(() => {
      const errorRow = document.createElement("div");
      errorRow.className = "message-row assistant-row";

      errorRow.innerHTML = `
        <div class="avatar assistant-avatar">🌿</div>
        <div class="message-card assistant-card">
          <div class="message-author">Dr. Nature</div>
          <div class="message-text">
            <p>⚠️ Fehler bei der Verbindung zum Server.</p>
          </div>
        </div>
      `;

      chatContainer.appendChild(errorRow);
    });

  document.getElementById("messageInput").value = "";
}


// BUTTON + ENTER
document.getElementById("sendButton").addEventListener("click", suchen);

document.getElementById("messageInput").addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    suchen();
  }
});


// BUTTON FLASH (DEIN CODE)
function triggerButtonFlash(button) {
  if (!button) return;

  button.classList.remove('button-flash');
  void button.offsetWidth;
  button.classList.add('button-flash');

  setTimeout(() => {
    button.classList.remove('button-flash');
  }, 380);
}

document.querySelectorAll(
  '.theme-toggle, .input-icon-button, .send-button, .message-actions button, .dots-box'
).forEach((button) => {
  button.addEventListener('click', () => {
    triggerButtonFlash(button);
  });
});
