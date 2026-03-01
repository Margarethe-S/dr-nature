# 🌿 Dr. Nature – Lokaler KI-Assistent & LLM-Experimentierprojekt


[![License: AGPL v3](https://img.shields.io/badge/license-AGPL--3.0-green.svg)](https://www.gnu.org/licenses/agpl-3.0)
![Tested on LM Studio](https://img.shields.io/badge/tested-LM%20Studio-blue)
![Status](https://img.shields.io/badge/status-active%20development-brightgreen)

>**Tech Stack:** Python · Flask · HTML/CSS/JS · JSON · Local LLM APIs (LM Studio)

## 🧠 Projektübersicht

**Dr. Nature** ist ein KI-gestütztes Entwicklungsprojekt mit Fokus auf:

- lokale LLM-Integration  
- modulare AI-Architektur  
- Memory-basierte Interaktion  
- Offline- und Online-Testing  
- experimentelle AI-Workflows  


Der aktuelle Haupt-Use-Case ist ein gesundheitsorientierter KI-Assistent, der über ein Web-Frontend genutzt wird und lokal oder API-basiert mit Sprachmodellen kommunizieren kann.

Das Projekt dient gleichzeitig als:

- praktische AI-Engineering-Umgebung  
- Experimentierplattform für lokale Modelle  
- Entwicklungsbasis für zukünftige Offline-AI-Assistenten  

Das Projekt verbindet einen health-orientierten Use Case mit einer technischen Experimentierumgebung für lokale und API-basierte LLM-Integrationen.

---

## 🎯 Zielsetzung

Das Projekt verfolgt zwei technische Richtungen.

### 👤 End-User Perspektive

- lokaler KI-Assistent mit Chat-Interface  
- langfristig offline und online nutzbar  
- Fokus auf unterstützende Gesundheitskommunikation  
- optionale Erweiterungen wie Arztsuche oder lokale Hilfsinformationen  

### 🧑‍💻 Developer Perspektive

- austauschbare Modell-APIs  
- Testen unterschiedlicher LLMs  
- Logging und Response-Analyse  
- Prompt-Testing und Evaluation des Systemverhaltens  
- Vorbereitung für Online-Offline-Switching  

---

## ⚙️ Technische Architektur (vereinfacht)

Dr. Nature basiert auf einer modularen Struktur:

- Frontend mit Chat-Interface  
- Flask Backend API  
- LLM Connector (API-basiert oder lokal)  
- Prompt-System  
- Logging und Testinterface  
- JSON-basiertes Memory-System  

Die API-Verbindung wird über Umgebungsvariablen gesteuert, wodurch unterschiedliche Modell-Endpunkte flexibel genutzt werden können.

---

## 🚧 Aktueller Entwicklungsstand

**Bereits umgesetzt:**

- Web-Frontend mit Chat-Interface  
- Backend-Kommunikation über Flask  
- API-Anbindung an LM Studio  
- API-Konfiguration über Umgebungsvariablen für flexible Modell-Endpunkte  
- lokale Prompt-Verwaltung  
- Logging und Timing-Tests  
- Testumgebung für Modellantworten  
- vorbereitete Memory-Struktur (JSON-basiert)  
- GitHub Action zur Antwortzeitmessung (LLM Response Timer Action)

**Getestete Modelle:**

- Mistral 7B  
- LLaMA3  
- OpenHermes  

**Aktuelle Entwicklungsrichtung:**

- Ausbau der lokalen Runtime  
- Vorbereitung eines Developer-Modes  
- Online-Offline-Testing erweitern  
- langfristige Memory-Strategie  

---

## 🧩 Systemprompts & Modi

Dr. Nature nutzt ein modulares Prompt-System.

Die Systemprompts sind im Repository sichtbar und können angepasst werden, um unterschiedliche Test- oder Gesprächsmodi zu evaluieren (z. B. Core, Root oder Talk Mode).

Damit kann das Verhalten der KI flexibel getestet und weiterentwickelt werden.

---

## 📁 Projektstruktur (vereinfacht)

- `backend/` – Flask API & Modellkommunikation  
- `frontend/` – Web-Interface  
- `memory/` – JSON-basiertes Memory-System  
- `system_prompt/` – Prompt-Dateien & Konfiguration  
- `tests_interface/` – Logging & Modelltests  
- `progress_logs/` – Entwicklungsdokumentation  
- `.env.example` – lokale Umgebungsvariablen  

Geplante Richtung: Ausbau einer lokalen Runtime sowie optionaler Online-/Offline-Testmodi für verschiedene LLM-Setups.

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

Dieses Repository wird im Sinne von Lernen und Weiterentwicklung bereitgestellt.
Du darfst es forken oder anpassen – beachte dabei jedoch die Bedingungen der Lizenz.

🔒 Bei einer Weitergabe oder öffentlichen Nutzung (z. B. Web-Anwendung, Hosting) bist du verpflichtet, auch deine Änderungen offenzulegen.

📜 Lizenz: Dieses Projekt steht unter der GNU Affero General Public License v3.0 (AGPL-3.0).
Details findest du in der Datei LICENSE.