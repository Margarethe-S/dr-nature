// Beispiel-Datenbank 
const datenbank = {
  kopfschmerzen: {
    hausmittel: "Viel Wasser trinken, Pfefferminzöl auf die Schläfen, Ruhe & frische Luft.",
    spirituell: "Lass mentale Überforderung los. Gönne dir Stille und verbinde dich mit deinem inneren Frieden."
  },
  husten: {
    hausmittel: "Zwiebelsaft mit Honig, Inhalieren mit Kamille, warme Brustwickel.",
    spirituell: "Drücke dich aus. Was möchtest du loswerden, das dir auf der Brust liegt?"
  },
  bauchweh: {
    hausmittel: "Fencheltee, Wärmeflasche, leicht verdauliche Nahrung.",
    spirituell: "Höre auf dein Bauchgefühl – was schlägt dir auf den Magen?"
  }
};

function suchen() {
  const symptom = document.getElementById("symptomInput").value.trim().toLowerCase();
  const chatContainer = document.querySelector(".chat-container");

  if (symptom === "") {
    alert("Bitte ein Symptom eingeben.");
    return;
  }

  const timestamp = new Date().toLocaleTimeString();

  // Baue eine neue "Nachricht" für den Chatverlauf
  const messageBlock = document.createElement("div");
  messageBlock.className = "chat-message";

  const userInput = document.createElement("p");
  userInput.className = "user-input";
  userInput.textContent = `🧑 Du: ${symptom}`;

  const kiAntwort = document.createElement("p");
  kiAntwort.className = "ki-output";

  if (datenbank[symptom]) {
    kiAntwort.textContent = `🌿 Dr. Nature: ${datenbank[symptom].hausmittel} | ${datenbank[symptom].spirituell}`;
  } else {
    kiAntwort.textContent = "🌿 Dr. Nature: Leider kenne ich dafür keine Hausmittel. Aber vielleicht möchte dein Körper dir etwas sagen?";
  }

  messageBlock.appendChild(userInput);
  messageBlock.appendChild(kiAntwort);
  chatContainer.appendChild(messageBlock);

  // Chat-Eingabefeld einblenden
  document.querySelector(".chat-input-container").hidden = false;

  // Automatisch nach unten scrollen
  requestAnimationFrame(() => {
    chatContainer.scrollTop = chatContainer.scrollHeight;
  });

}

function chatSenden() {
  const userMsg = document.getElementById("chatInput").value.trim();
  const chatContainer = document.querySelector(".chat-container");

  if (userMsg === "") return;

  // Nutzer-Nachricht anzeigen
  const userBlock = document.createElement("p");
  userBlock.className = "user-input";
  userBlock.textContent = `🧑 Du: ${userMsg}`;
  chatContainer.appendChild(userBlock);

  // Anfrage an KI stellen (Platzhalter: später LM Studio/Server.py)
  fetch("http://127.0.0.1:1234/v1/chat/completions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "mistral-7b",
      messages: [
        { role: "system", content: "Du bist Dr. Nature, eine empathische Gesundheits-KI." },
        { role: "user", content: userMsg }
      ]
    })
  })
    .then(res => res.json())
    .then(data => {
      const reply = document.createElement("p");
      reply.className = "ki-output";
      reply.textContent = `🌿 Dr. Nature: ${data.choices[0].message.content}`;
      chatContainer.appendChild(reply);

      // Auto-Scroll nach unten
  requestAnimationFrame(() => {
    chatContainer.scrollTop = chatContainer.scrollHeight;
  });
})
.catch(err => {
  const errorReply = document.createElement("p");
  errorReply.textContent = "⚠️ Fehler: keine Antwort von der KI.";
  chatContainer.appendChild(errorReply);
  console.error(err);
});

  // Eingabe zurücksetzen
  document.getElementById("chatInput").value = "";
}


