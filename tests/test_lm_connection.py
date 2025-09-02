import os
import requests
import json

# .env manuell einlesen
def load_env(filepath=".env"):
    if not os.path.exists(filepath):
        print(f"⚠️  .env file not found at: {filepath}")
        return
    with open(filepath, "r") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

load_env()

# Jetzt kannst du auf die Variable zugreifen
api_url = os.getenv("LMSTUDIO_API_URL")

# Systemprompt laden aus lokaler .txt Datei (eigene Datei anlegen und hier referenzieren)
with open("system_prompt//drnature_prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

print("System Prompt geladen:", prompt[:300], "...")

# Testeingabe
user_input = "Was kann ich gegen Kopfschmerzen auf natürliche Weise tun?"

# Anfrage senden
response = requests.post(
    api_url,
    headers={"Content-Type": "application/json"},
    json={
        "model": "em_german_mistral_v01",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3
    }
)

# Ausgabe
antwort = response.json()["choices"][0]["message"]["content"]
print("Antwort von LM Studio:\n")
print(antwort)
