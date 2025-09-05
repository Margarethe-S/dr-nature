import os
import requests
import json
import time

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
with open("system_prompt\\drnature_prompt_test1.4.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

print("System Prompt geladen:", prompt[:300], "...")

# Testeingabe
user_input = "Was kann ich gegen Kopfschmerzen auf natürliche Weise tun?"

# Zeit messung beginn
start_time = time.time()

try:
    # Anfrage senden mit 5min timeout
    response = requests.post(
        api_url,
        headers={"Content-Type": "application/json"},
        json={
            "model": "em_german_mistral_v01",
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.0
        },
        timeout=300 # 5 Minuten Timeout
    )

    # Zeit messung ende
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Minuten und Sekunden ausgeben
    minutes, seconds = divmod(elapsed_time, 60)
    print(f"\n  🧠 Die Antwort hat {elapsed_time:.2f} Sekunden gedauert.")
    print(f"\n  ⏱️ : {minutes:.0f} Minuten und {seconds:.0f} Sekunden.")
    os.system('powershell -c "[console]::beep(1000, 500)"')  # System-Benachrichtigungston


    # Ausgabe
    antwort = response.json()["choices"][0]["message"]["content"]
    print(f"\n  Antwort von LM Studio:\n{antwort}")
except requests.exceptions.Timeout:
    print("⚠️  Die Anfrage hat das Zeitlimit von 5 Minuten überschritten.")
    print("🛑 Das Modell konnte innerhalb des vorgegebenen Zeitraums (300 Sekunden) keine Antwort generieren.")
    os.system('powershell -c "[console]::beep(1000, 500); Start-Sleep -Milliseconds 200; [console]::beep(1000, 500)"')  # System-Benachrichtigungston


except requests.exceptions.RequestException as e:
    print(f"⚠️  Ein Fehler ist aufgetreten: {e}")
    os.system('powershell -c "[console]::beep(1000, 500); Start-Sleep -Milliseconds 200; [console]::beep(1000, 500)"')  # System-Benachrichtigungston
