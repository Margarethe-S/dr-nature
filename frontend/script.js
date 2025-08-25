// Beispiel-Datenbank (diese kannst du später durch echte Daten ersetzen oder dynamisch erweitern)
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
  const resultContainer = document.getElementById("result");
  const hausmittel = document.getElementById("hausmittel");
  const spirituell = document.getElementById("spirituell");

  if (symptom === "") {
    alert("Bitte ein Symptom eingeben.");
    return;
  }

  if (datenbank[symptom]) {
    hausmittel.textContent = datenbank[symptom].hausmittel;
    spirituell.textContent = datenbank[symptom].spirituell;
    resultContainer.style.display = "block";
  } else {
    hausmittel.textContent = "Leider keine Hausmittel gefunden.";
    spirituell.textContent = "Bitte spüre in dich hinein – was möchte dir dein Körper sagen?";
    resultContainer.style.display = "block";
  }
}
