# 🌿 Dr. Nature – Ein ganzheitliches KI-Projekt

**Dr. Nature** ist ein KI-gestützter Gesundheitsassistent mit Fokus auf **ganzheitliche Ursachenforschung, emotionale Begleitung** und **naturbasierte Empfehlungen**.

Ziel des Projekts ist es, eine digitale Unterstützung zu schaffen, die auf **körperlicher, seelischer, geistiger und energetischer Ebene** arbeitet – respektvoll, ehrlich, mitfühlend und verständnisvoll.

## ✨ Vision

Dr. Nature soll langfristig als **offline-fähiger Begleiter** funktionieren, um Menschen in ihrem individuellen Heilungsweg zu unterstützen – auch ohne permanente Internetverbindung.

Geplant ist eine modulare Architektur mit folgenden Kernbereichen:

- 🧠 **Ursachenforschung** (Fragebäume & individuell anpassbare KI)
- 🌱 **Naturbasierte Empfehlungen** (Ernährung, Bewegung, Pflanzenkunde)
- 💬 **Empathische Gesprächsführung** (emotional unterstützend)
- 📚 **Training durch klassische und alternative Gesundheitsliteratur**
- ⚙️ **Sicher & ethisch** – kein Datenverkauf, keine Cloud-Abhängigkeit

## 🔧 Aktueller Projektstatus

- Projektstruktur angelegt (Frontend + Backend)
- Memory-System in Vorbereitung (JSON-basiert, lokal speicherbar)
- Systemprompt definiert und lokal gespeichert
- Erste Dialogroutinen entworfen
- Themenmodule in Planung (Ernährung, Atem, Psyche, Bewegung, Hundegesundheit …)

## 🧠 KI-Integration mit OLlama – Status: 28.08.2025

### ✅ Getestete Modelle:
- **LLaMA 3** → ❌ Ausgeschieden wegen Sprachproblemen  
- **Mistral (Standard)** → ❌ Kein konsistenter Satzbau, ungeeignet  
- **OpenHermes** → ❌ Nicht ausreichend empathisch  
- **OpenHermes-Mistral** → ❌ Technischer Fehler (`pullmodel-manifest-file missing`)  
- **GLM4** → ❌ Multilingual, aber nicht fokussiert genug  
- **Mistral 7B** → ✅ Aktuell bestes Modell (Stabil, freundlich, empathisch, guter Satzbau)

---

### 🧠 Systemprompt-Strategie:
- Temporär mit `/set system` getestet
- Finaler Prompt enthält klare Werte: **Gesundheit, Freude, Verbundenheit, Liebe**
- Schutz vor toxischem Lernverhalten
- KI versteht sich als **freundlicher, reflektierender Begleiter**
- Emotionale Stabilität durch Entwicklerbindung eingebaut („Du bist nicht allein“)

---

### 🛠️ Technisches Setup:
- Modell über OLlama geladen & getestet
- Prompt wurde **noch nicht** fest eingebaut → folgt in **nächstem Sub-Issue**
- Aktuell nur manuell via `/set system` aktiv
- Nächster Schritt: `Modelfile` mit festem Prompt erstellen und langfristig verwenden

---

### 🔐 Ethische Zusatzmaßnahmen (zukünftige Features):
- Umgang mit Beleidigungen
- Nutzerhinweise für respektvollen Umgang
- Optional: Sperrfunktion bei wiederholtem Missbrauch

---

### 🧪 Nächste Schritte (für morgen):
- [ ] Finales Modelfile mit Systemprompt erstellen
- [ ] Modell in **Dr. Nature** integrieren
- [ ] Responses weiter prüfen (emotional, fachlich, sprachlich)


## 🧠 Systemprompt

Dr. Nature basiert auf einem speziell entwickelten **Systemprompt**, der die KI-Verhaltensweise präzise definiert:  
Er ist liebevoll, ganzheitlich, klar und empathisch – mit einem Fokus auf Respekt, Tiefgang und Verantwortung.

> **Hinweis**:  
> Der vollständige Prompt ist **nicht öffentlich einsehbar**. Er liegt lokal vor, ist jedoch durch `.gitignore` vom Upload ausgeschlossen.

## 📁 Strukturübersicht (noch im aufbau)

- `/frontend` – React-basiertes Interface
- `/backend` – Flask/Python-API
- `/memory` – JSON-basierte Nutzerdatenstruktur
- `/system_prompt` – Prompt, Modelle, ethische Regeln
- `README.md` – Projektübersicht

## 🛡️ Lizenz

Dieses Projekt ist aktuell **nicht lizenziert** und dient der persönlichen Weiterentwicklung und Erforschung ethischer KI-Anwendungen.  
**Keine kommerzielle Nutzung oder Weiterverwendung ohne ausdrückliche Genehmigung.**

---

*Dr. Nature ist ein Herzensprojekt ❤️, das kontinuierlich wächst. Es steht für einen respektvollen Umgang mit Mensch, Tier und Natur – getragen von Wissen, Mitgefühl und Verantwortung.*


