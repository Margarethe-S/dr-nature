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
  const symptom = document.getElementById("symptomInput").value.trim();
  const chatContainer = document.querySelector(".chat-container");
  if (!symptom) return;


  document.querySelector(".chat-input-container").hidden = false;


  const userMsg = document.createElement("p");
  userMsg.className = "user-input";
  userMsg.textContent = `🧑 Du: ${symptom}`;
  chatContainer.appendChild(userMsg);


  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: symptom })
  })
    .then(res => res.json())
    .then(data => {
      const reply = document.createElement("p");
      reply.className = "ki-output";
      reply.textContent = `🌿 Dr. Nature: ${data.reply}`;
      chatContainer.appendChild(reply);
      requestAnimationFrame(() => {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      });
    })
    .catch(() => {
      const errorMsg = document.createElement("p");
      errorMsg.className = "ki-output";
      errorMsg.textContent = "⚠️ Fehler bei der Verbindung zum Server.";
      chatContainer.appendChild(errorMsg);
    });
}


function chatSenden() {
  const userMsg = document.getElementById("chatInput").value.trim();
  const chatContainer = document.querySelector(".chat-container");
  if (userMsg === "") return;


  const userBlock = document.createElement("p");
  userBlock.className = "user-input";
  userBlock.textContent = `🧑 Du: ${userMsg}`;
  chatContainer.appendChild(userBlock);


  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMsg })
  })
    .then(res => res.json())
    .then(data => {
      const reply = document.createElement("p");
      reply.className = "ki-output";
      reply.textContent = `🌿 Dr. Nature: ${data.reply}`;
      chatContainer.appendChild(reply);


      requestAnimationFrame(() => {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      });
    })
    .catch(err => {
      const errorMsg = document.createElement("p");
      errorMsg.className = "ki-output";
      errorMsg.textContent = "⚠️ Fehler bei der Verbindung zum Server.";
      chatContainer.appendChild(errorMsg);
    });


  document.getElementById("chatInput").value = "";
  }
