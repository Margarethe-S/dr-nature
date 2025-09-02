## 🧠 Progress Log – 02.09.2025

### 🔧 Backend & LM Studio Integration

- Lokale Verbindung zu LM Studio getestet 
- API-Endpunkt `/v1/chat/completions` erfolgreich getestet
- Code angepasst für Prompt-Loading, Output-Zertifizierung und Timing-Analyse
- `test_connection.py` verwendet zur Laufzeitüberprüfung der Promptverarbeitung

### ⏱️ Prompt Timing Analysis

- **Kurzer Prompt** (ca. 600 Tokens): Antwortzeit ~2:14 Minuten
- **Chat-Nachfrage**: Antwortzeit ~7 Sekunden – korrekt verarbeitet
- **Langer Prompt** (ca. 900 Tokens): aktuell „Generating“ – läuft seit 8h30min, RAM und CPU dauerhaft aktiv
  - Ziel: Stabilität prüfen, ggf. maximale Promptgröße ermitteln
  - Ergebnis wird später bewertet (overnight test)

### 🧠 Prompt & Memory Testing

- Systemprompt `DrNature_Prompt.txt` vorbereitet und geladen
- Weitere Tests mit dem langen Prompt laufen noch
- Entscheidung über finalen Prompt steht für morgen an
- Ziel: höchste Ausdruckskraft mit möglichst wenigen Tokens
- JSON-Output und strukturierte Ausgabe korrekt erkannt

### 🔀 Merge Requests

- ✅ Merge: `#13` → Branch `#10-documentation-structure`
- ✅ Merge: `#12` → Branch `test-09-lm-rp-and-prompt-tuning` (Margarete)

### 🧩 Nächste Schritte

- Über Nacht wird der große Prompt weiter beobachtet
- Morgen: Testphase zur Optimierung des Systemprompts beginnt
- Fokus: Genauigkeit, Tokenreduktion, Stilabgleich
- Aktualisierung der README und finaler Prompt-Vergleich folgen
- Automatische Antwortanalyse wird vorbereitet

---

## 🧾 Sprint-Log (25.08.–02.09.)

In dieser Woche haben wir den Grundstein für das gesamte KI-Projekt gelegt.  
Vom ersten Tag an stand die Struktur im Mittelpunkt: Wir haben das Repository aufgebaut und die gesamte Projektarchitektur mit Frontend, Backend, KI-Logik und Memory-System vorbereitet.

Zuerst haben wir die Ordnerstruktur festgelegt und die ersten Dateien erstellt – darunter ein funktionales `Memory-System`, das Nutzerdaten verarbeiten kann. Im Frontend wurde die Basis für HTML, CSS und JavaScript gelegt, erste Komponenten wurden skizziert und verbunden.

Parallel dazu haben wir GitHub vollständig integriert:  
Wir haben Branches eingerichtet, Issues sauber organisiert und die Projektstruktur dokumentiert. Die `README.md` wuchs täglich mit uns mit, genau wie die `Progress Logs`, die wir zur lückenlosen Nachverfolgung eingeführt haben.

Ein zentraler Meilenstein war die Entscheidung, mit **LM Studio** zu arbeiten statt OLama. Die Verbindung zur API wurde erfolgreich getestet, erste Prompts wurden geladen und in ihrer Antwortzeit gemessen. So entstand eine robuste Grundlage für den weiteren Ausbau der KI.

Besonderer Fokus lag darauf, alles **nachvollziehbar und sauber** zu dokumentieren – inklusive:
- Fortschrittslogs
- Beispielumgebungen (.env)
- Exkludierung sensibler Daten im `.gitignore`
- GitHub-Projektverknüpfung mit Pull Requests, Branches und Kommentaren

Wir sind jetzt bereit, alle gesammelten Informationen strukturiert zu testen, zu verarbeiten und in den nächsten Sprint mitzunehmen. Ziel ist, das finale Prompt-Design und die Ausgabe ins Frontend zu bringen – aufbauend auf allem, was wir diese Woche erschaffen haben.