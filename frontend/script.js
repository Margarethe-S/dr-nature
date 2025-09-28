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

function ladeStandardVideos() {
  const videoContainer = document.getElementById("video-container");
  const videos = [
    "https://www.youtube.com/embed/QH2-TGUlwu4",
    "https://www.youtube.com/embed/dQw4w9WgXcQ",
    "https://www.youtube.com/embed/Ij4p0xkWkVY",
    "https://www.youtube.com/embed/tgbNymZ7vqY"
  ];
  videoContainer.innerHTML = "";
  videos.forEach(link => {
    const iframe = document.createElement("iframe");
    iframe.src = link;
    iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
    iframe.allowFullscreen = true;
    videoContainer.appendChild(iframe);
  });
}

function modusWechsel(modus) {
    if (modus === "arzt") {
        zeigeArztsuche();
        return;
    }
    // Weitere Modi wie 'ursache', 'reden', 'feedback' kannst du auch hier behandeln
}




function zeigeArztsuche() {
    const chatContainer = document.querySelector(".chat-container");


    const arztsucheBlock = document.createElement("div");
    arztsucheBlock.className = "arztsuche-block";


    arztsucheBlock.innerHTML = `
        <h3>🔍 Arztsuche</h3>
        <label for="plz">Postleitzahl:</label>
        <input type="text" id="plz" placeholder="z. B. 86899" />
        <button onclick="arztSuche()">Suchen</button>


        <div class="arztsuche-info" id="arztsuche-ergebnisse" style="display: none;">
            <h4>📞 Notfallnummern:</h4>
            <ul>
                <li>112 – Notruf</li>
                <li>116117 – Ärztlicher Bereitschaftsdienst</li>
                <li>110 – Polizei</li>
            </ul>


            <h4>🧑‍⚕️ Ärzte in der Nähe:</h4>
            <ul>
                <li>Dr. Mustermann – Allgemeinmedizin</li>
                <li>Dr. Beispiel – Hausarzt</li>
                <li>Dr. Fiktion – Naturheilkunde</li>
            </ul>


            <h4>🗺️ Karte:</h4>
            <div class="map-placeholder">
                <p>[🗺️ Google Maps Platzhalter]</p>
            </div>
        </div>
    `;


    chatContainer.appendChild(arztsucheBlock);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}


function arztSuche() {
    const plz = document.getElementById("plz").value.trim();
    if (!plz) {
        alert("Bitte gib eine Postleitzahl ein.");
        return;
    }


    const ergebnisse = document.getElementById("arztsuche-ergebnisse");
    ergebnisse.style.display = "block";
}


function arztSuche() {
    const plz = document.getElementById("plz").value.trim();
    if (!plz) {
        alert("Bitte gib eine Postleitzahl ein.");
        return;
    }


    const ergebnisse = document.getElementById("arztsuche-ergebnisse");
    ergebnisse.style.display = "block";
}


document.addEventListener("DOMContentLoaded", ladeStandardVideos);
