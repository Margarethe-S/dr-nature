# 🌿 Dr. Nature – Ein ganzheitliches KI-Projekt

**Dr. Nature** ist ein KI-gestützter Gesundheitsassistent mit Fokus auf **ganzheitliche Ursachenforschung**, **emotionale Begleitung** und **naturbasierte Empfehlungen**.

Ziel des Projekts ist es, eine digitale Unterstützung zu schaffen, die auf **körperlicher, seelischer, geistiger und energetischer Ebene** arbeitet – respektvoll, ehrlich, mitfühlend und verständnisvoll.

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

---

## 🧠 Systemprompt

Dr. Nature basiert auf einem speziell entwickelten **Systemprompt**, der die KI-Verhaltensweise präzise definiert:  
Er ist **liebevoll, ganzheitlich, klar und empathisch** – mit einem Fokus auf Respekt, Tiefgang und Verantwortung.

> **Hinweis:**  
> Der vollständige Prompt ist **nicht öffentlich einsehbar**.  
> Er liegt lokal vor und ist durch `.gitignore` sowie das interne **Memory-System** vom GitHub-Upload ausgeschlossen.

---

## 📁 Strukturübersicht (Stand: 28.08.2025)

- `/frontend` – React-basiertes Interface
- `/backend` – Flask/Python-API
- `/memory` – JSON-basierte Nutzerdatenstruktur
- `/progress_logs` – Tägliche Entwicklungsfortschritte als Markdown-Dateien
- `/system_prompt` – Prompt-Dateien, Modellkonfigurationen, ethische Regeln
- `README.md` – Projektübersicht

---

## 🛠️ Installation

Stelle sicher, dass du eine virtuelle Umgebung verwendest:

```bash
python -m venv .venv
source .venv/bin/activate

Installiere anschließend alle benötigten Pakete:
```bash
pip install -r requirements.txt

---

## 🛡️ Lizenz

Dieses Projekt befindet sich in Entwicklung und unterliegt aktuell **keiner öffentlichen Lizenz**.  
Jegliche kommerzielle Nutzung oder Weiterverwendung bedarf der **ausdrücklichen Genehmigung der Entwickler:in**.

---

*Dr. Nature ist ein Herzensprojekt ❤️, das kontinuierlich wächst. Es steht für einen respektvollen Umgang mit Mensch, Tier und Natur – getragen von Wissen, Mitgefühl und Verantwortung.*


