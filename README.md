# 🌿 Dr. Nature – Ein ganzheitliches KI-Projekt

**Dr. Nature** ist ein KI-gestützter Gesundheitsassistent mit Fokus auf **ganzheitliche Ursachenforschung**, **emotionale Begleitung** und **naturbasierte Empfehlungen**.

Ziel des Projekts ist es, eine digitale Unterstützung zu schaffen, die auf **körperlicher, seelischer, geistiger und energetischer Ebene** arbeitet – respektvoll, ehrlich, mitfühlend und verständnisvoll.

🫶 Thank you for your clone – wir freuen uns über dein Interesse am Projekt!

---

## ✨ Vision

Dr. Nature soll langfristig als **offline-fähiger Begleiter** funktionieren, um Menschen **auf ihrem individuellen Heilungsweg** zu unterstützen – auch ohne permanente Internetverbindung.

Geplant ist eine modulare Architektur mit folgenden Kernbereichen:

- 🧠 **Ursachenforschung** (Fragebäume & individuell anpassbare KI)
- 🌱 **Naturbasierte Empfehlungen** (Ernährung, Bewegung, Pflanzenkunde)
- 💬 **Empathische Gesprächsführung** (emotional unterstützend)
- 📚 **Training durch klassische und alternative Gesundheitsliteratur**
- ⚙️ **Sicher & ethisch** – kein Datenverkauf, keine Cloud-Abhängigkeit

---

## 🔧 Aktueller Projektstatus

- Projektstruktur initial aufgebaut (Frontend + Backend)
- Memory-System in Vorbereitung (JSON-basiert, lokal speicherbar)
- Ordner für tägliche **Progress Logs** erstellt
- Systemprompt definiert und lokal gespeichert
- Vergleich verschiedener KI-Umgebungen: **OLama** vs. **LM Studio**
- Test unterschiedlicher Modelle: u.a. **LLaMA3**, **Mistral 7B**, **OpenHermes**
- Finale Auswahl: **EM-German-Mistral-V01** (lokal in LM Studio eingesetzt)
- Umfangreiche Prompt-Tests durchgeführt (u.a. zu: Schmerzen, Selbstbild, emotionale Ausnahmesituationen, Grenzsetzung)
- Sprachanpassung und Verhaltenstests erfolgreich
- Systemprompt zeigt klare, mitfühlende, stabile Reaktion auf schwierige Szenarien
- Weitere Feinjustierung & Integration in App in Planung
- API-Anbindung an LM Studio erfolgreich eingerichtet und getestet
- Sicherheitsbedingt erfolgt die Prompt-Übergabe nun über lokale Textdateien (`SystemPrompt/`)
- Timing-Analysen für verschiedene Promptlängen dokumentiert (z. B. kurze Prompts: ~2 Minuten Antwortzeit; lange Prompts: derzeit in Testphase)
- `.env.example` für lokale Umgebungsvariablen eingeführt

---

## 🧠 Systemprompt

Dr. Nature basiert auf einem speziell entwickelten **Systemprompt**, der die KI-Verhaltensweise präzise definiert:  
Er ist **liebevoll, ganzheitlich, klar und empathisch** – mit einem Fokus auf Respekt, Tiefgang und Verantwortung.

> **Hinweis:**  
> Der vollständige Prompt ist **nicht öffentlich einsehbar**.  
> Er liegt lokal vor und ist durch `.gitignore` sowie das interne **Memory-System** vom GitHub-Upload ausgeschlossen.
> Der Systemprompt wird laufend optimiert und spiegelt unsere ethischen Leitlinien wider.
---

## 📁 Strukturübersicht (Stand: 02.09.2025)

- `/backend` – Flask/Python-API
- `/frontend` – React-Frontend
- `/memory` – JSON-basiertes Nutzerspeicher-System
- `/progress_logs` – Dokumentation des Entwicklungsverlaufs (Markdown)
- `/system_prompt` – KI-Prompts, Modellkonfigurationen, ethische Regeln
- `/tests` – Tests für Memory, Modellantworten & Schnittstellen
- `.env.example` – Vorlage für lokale Umgebungsvariablen
- `requirements.txt` – Python-Abhängigkeiten
- `README.md` – Projektübersicht

---

## 🛠️ Installation

Stelle sicher, dass du eine virtuelle Umgebung verwendest:

### Für Linux/macOS (bash/zsh):
```bash
python -m venv .venv
source .venv/bin/activate
```
### Für Windows (PowerShell):
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```
Installiere anschließend alle benötigten Pakete:
```bash
pip install -r requirements.txt
```
> ⚠️ **Hinweis:** Die folgenden Befehle sind systemabhängig. Bitte verwende die Variante, die zu deinem Betriebssystem passt.
---

## 🛡️ Lizenz

Dieses Projekt befindet sich in Entwicklung und unterliegt aktuell **keiner öffentlichen Lizenz**.  
Jegliche kommerzielle Nutzung oder Weiterverwendung bedarf der **ausdrücklichen Genehmigung der Entwickler:in**.

---

*Dr. Nature ist ein Herzensprojekt ❤️, das kontinuierlich wächst. Es steht für einen respektvollen Umgang mit Mensch, Tier und Natur – getragen von Wissen, Mitgefühl und Verantwortung.*
