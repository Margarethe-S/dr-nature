# 🌿 Dr. Nature – KI-Assistent Webanwendung für LLM-Experimente mit lokalem Deployment

![Python](https://img.shields.io/badge/Python-Backend-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![Tested](https://img.shields.io/badge/Tested-LM%20Studio-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-AGPL%20v3-blue)

**Tech Stack:**  
Python · Flask · HTML/CSS/JS · JSON · Local LLM APIs (LM Studio)

---

## Projektkontext

Dr. Nature ist ein Langzeitprojekt und wird aktiv weiterentwickelt.

Das Projekt entstand während meiner Weiterbildung und wurde dort als Abschlussprojekt präsentiert.  
Die Weiterbildung ist inzwischen abgeschlossen und das Projekt wird seitdem weiter ausgebaut.

Während der Entwicklung entstand zusätzlich das Tool LLM Response Timer Action.

Dieses Tool wurde entwickelt, um Antwortzeiten von Sprachmodellen zu messen, Modellantworten zu protokollieren und API-Anfragen zu testen.

**Repository:**  
LLM Response Timer Action  
https://github.com/Margarethe-S/llm-response-timer-action

---

## 🧠 Projektübersicht

Dr. Nature ist eine Webanwendung für einen KI-Assistenten, der über ein Chat-Interface genutzt werden kann.

Der aktuelle Fokus liegt auf einem gesundheitsorientierten KI-Assistenten, der über ein Web-Frontend mit Sprachmodellen kommuniziert.

Die Anwendung kombiniert:
- Web-Frontend mit Chat-Interface
- Flask-Backend für API-Kommunikation
- Modellanbindung über lokale oder API-basierte LLM-Endpunkte
- modulares Prompt-System
- lokale Test- und Logging-Umgebung
- vorbereitete JSON-basierte Memory-Struktur

Die Modellanbindung erfolgt aktuell über konfigurierbare API-Endpunkte, zum Beispiel über LM Studio.

Dadurch können verschiedene lokale oder externe Modellserver getestet werden.

Das Projekt dient sowohl als Anwendungsprototyp als auch als Experimentierplattform für lokale LLM-Systeme.

---

## 🧱 Architekturüberblick

Die Anwendung besteht aus drei zentralen Komponenten:

User Interface  
↓  
Flask Backend API  
↓  
LLM Runtime / Modellserver

>Ablauf einer Anfrage:
>1. Nutzer sendet eine Anfrage über das Web-Interface
>2. Das Frontend übermittelt die Anfrage an das Flask Backend
>3. Das Backend lädt den entsprechenden Systemprompt
>4. Die Anfrage wird an das konfigurierte Sprachmodell weitergeleitet
>5. Die Modellantwort wird verarbeitet und an das Frontend zurückgegeben
>6. Optional wird die Anfrage im lokalen Logging-System protokolliert

Diese modulare Architektur ermöglicht es, verschiedene Modellserver auszutauschen.

---

## 🚧 Aktuelle Weiterentwicklung

Dr. Nature wird aktiv weiterentwickelt.

Der Fokus liegt aktuell auf:
- Ausbau einer stabilen lokalen Runtime
- Integration lokal laufender Sprachmodelle
- Vorbereitung eines Developer-Modes für Tests und Debugging
- Erweiterung für Online- und Offline-Betrieb
- langfristige Memory-Strategie für Konversationsdaten
- mögliche Integration lokaler Karten- und Notfallinformationen

Langfristiges Ziel ist eine lokal installierbare Desktop-Version.

---

## 🎓 Abschlussprojekt (Stand der Weiterbildung)

Der während der Weiterbildung präsentierte Projektstand enthielt bereits:
- Web-Frontend mit Chat-Interface
- Backend-Kommunikation über Flask
- API-Anbindung an LM Studio
- Modell-API-Konfiguration über Umgebungsvariablen
- lokale Prompt-Verwaltung
- Logging- und Timing-Tests
- Testumgebung für Modellantworten
- vorbereitete JSON-Memory-Struktur

Getestete Modelle:
- Mistral 7B (optional: ausgewählt)
- LLaMA3
- OpenHermes

Zuletzt getestet:
- EM German Mistral v01

---

## 💻 Web-Interface

![Web-Interface](./images/drnature_web.png)

---

## 📊 Projektpräsentation

### Slide 1
![Slide 1](images/slide1.png)

### Slide 2
![Slide 2](images/slide2.png)

### Slide 3
![Slide 3](images/slide3.png)

### Slide 4
![Slide 4](images/slide4.png)

### Slide 5
![Slide 5](images/slide5.png)

### Slide 6
![Slide 6](images/slide6.png)

>📄 Vollständige Präsentation als PDF  
[Präsentationsfolien öffnen](./docs/Präsentation.pdf)

---

## 🔎 Logging & Testsystem

Dr. Nature erstellt lokale Log-Dateien für Modelltests.

Ordner:

>logs/

Beispiel:

>logs/log_2025-09-28.txt

Logs enthalten:
- Status der Anfrage
- Zeitstempel
- Antwortdauer
- verwendete Prompt-Datei
- Modellantwort

Logging erfolgt über das Testinterface (logger.py).

---

## 🧩 Systemprompts & Modi

Systemprompts befinden sich im Ordner:

>system_prompt/

Beispiel:

>system_prompt/core_mode.txt

Mögliche Modi:
- Core Mode
- Root Mode
- Talk Mode

---

## 📁 Projektstruktur

.github/workflows/ – GitHub Actions & Tests  
app/ – Anwendungskomponenten  
backend/ – Flask API & Modellkommunikation  
frontend/ – Web-Interface  
dev/ – Entwicklungswerkzeuge  
logs/ – Laufzeitlogs  
models/ – Modellbezogene Dateien  
private/ – lokale Entwicklungsdaten  
progress_logs/ – Entwicklungsdokumentation  
runtime/ – Laufzeitkomponenten  
system_prompt/ – Prompt-Dateien  
test_interface/ – Modelltests & Logging  

---

## ⚡ Quick Start

1. Repository klonen

>git clone https://github.com/Margarethe-S/dr-nature

2. Projektordner öffnen

>cd dr-nature

3. Virtuelle Umgebung erstellen

>python -m venv .venv

4. Umgebung aktivieren

>Windows  
>.venv\Scripts\Activate.ps1

>Linux/macOS  
>source .venv/bin/activate

5. Pakete installieren

>pip install -r requirements.txt

6. Backend starten

>python backend/server.py

---

## 🛠 Installation

Linux/macOS

>python -m venv .venv  
source .venv/bin/activate

Windows

>python -m venv .venv  
.venv\Scripts\Activate.ps1

pip install -r requirements.txt

---

## 📈 Development Status

Das Projekt befindet sich in aktiver Entwicklung.

Aktuelle Schwerpunkte:
- lokale Modellintegration
- Ausbau des Testsystems
- Weiterentwicklung der Promptstruktur
- Vorbereitung einer lokalen Runtime

---

## ⚠️ Hinweis

Dr. Nature ist ein experimentelles Entwicklungsprojekt.

Die Anwendung stellt keine medizinische Beratung dar und ersetzt keinen Arztbesuch.

---

## 🛡 Lizenz

Dieses Repository wird im Sinne von Lernen und Weiterentwicklung bereitgestellt.

Du darfst es forken oder anpassen.

Bei öffentlicher Nutzung müssen Änderungen offengelegt werden.

Lizenz: GNU Affero General Public License v3.0 (AGPL-3.0)

Details siehe Datei LICENSE.
