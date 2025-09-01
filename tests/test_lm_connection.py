import requests
import json

# 📁 Lies den Systemprompt aus deiner Datei ein
with open("system_prompt/drnature_prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

print("System Prompt geladen:", prompt[:300], "...")

# 💬 Testeingabe für das Modell
user_input = "Was kann ich gegen Kopfschmerzen auf natürliche Weise tun?"

# 📡 Anfrage an LM Studio senden
response = requests.post(
    "http://localhost:1234/v1/chat/completions",
    headers={"Content-Type": "application/json"},
    json={
        "model": "em_german_mistral_v01",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }
)

# 📤 Ausgabe anzeigen
antwort = response.json()["choices"][0]["message"]["content"]
print("Antwort von LM Studio:\n")
print(antwort)