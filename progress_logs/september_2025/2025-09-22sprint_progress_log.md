# 📓 22.09.2025 – Progress Log

## 🔧 Technische Fortschritte

Drei Systemprompts wurden getestet:
- `core_mode1.txt`
- `core_mode.txt`
- `doctor_mode.txt`

Konversationen wurden erfolgreich aufgezeichnet – inklusive Antwortzeiten, KI-Antworten und Nutzereingaben.  
Die Prompt-Tests zeigen: Jeweils zwei Folgeantworten werden stabil verarbeitet, danach erfolgt keine Rückfrage mehr.  
Die KI erkennt einfache Gesprächsverläufe zuverlässig und schlägt bei Symptomen wie Kopfschmerzen passende Maßnahmen vor.

## 🧪 Logging & Tests

Der komplette Gesprächsverlauf wird im Ordner `logs/` dokumentiert, inklusive:
- 📤 verwendete Prompt-Dateien
- ⏰ Antwortdauer 
- 🤖 KI-Antworten
- 👤 Nutzereingaben

**Testziel:** Stabilität und Kontexttiefe der Antworten vergleichen.

**Erkenntnis:**  
Prompts funktionieren zuverlässig in den ersten ein bis zwei Interaktionen. Danach stellt die KI keine Rückfragen mehr.  
➡️ **Nächster Schritt:** Anbindung des Memory-Systems zur Sicherung des Gesprächskontexts.

## 🧾 Sprint-Log – 16.–22.09.2025

In dieser Woche wurde die lokale Gesprächsfunktion erfolgreich erweitert und getestet:
- Textausgabe erfolgt vollständig über die Konsole, inklusive Zeitmessung, Logging und Prompt-Zuordnung.
- Erste Testgespräche wurden in Markdown gespeichert und dienen als Vergleichsbasis für Folgeversionen.

Die Systemprompts (`core_mode`, `doctor_mode`) wurden weiterentwickelt und zeigen stabile Ergebnisse bei maximal zwei Rückfragen – ein zentrales Kriterium für die kommende UI-Integration.  
Zudem wurde das Logging überarbeitet: Alle Antworten der KI werden automatisiert mit Zeitstempel, Prompt-Datei und Dauer gespeichert.

## 🔜 Nächster Sprint
- Anbindung des Memory-Systems ins Frontend  
- Integration interaktiver Antwortbuttons (z. B. „Arzt finden“, „Ursachenforschung“, „nur reden“, „nein danke“)  
- Konversationsübergabe vom Backend ins Frontend vorbereiten  
- Präsentationsvorbereitung für das Abschlussprojekt (Demo: lokaler KI-Dialog mit Logging und Buttons)
