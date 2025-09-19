import datetime
from datetime import datetime


def save_log(prompt_path, user_input, response, elapsed_time, status_msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = f"logs/log_{datetime.now().strftime('%Y-%m-%d')}.txt"  # oder z. B. f"logs/{promptname}_log.txt"

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"📝 Status: {status_msg}\n")
        f.write(f"⏰ {timestamp}\n")
        f.write(f"🕓 Dauer: {elapsed_time:.2f} Sekunden\n")
        f.write(f"📤 Prompt-Datei: {prompt_path}\n")
        f.write(f"🧠 Antwort: {response}\n")
        f.write("-" * 40 + "\n")
    print(f"✅ Log gespeichert in: {log_path}")


def save_conversation_log(user_input, response, elapsed_time):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = f"logs/log_{datetime.now().strftime('%Y-%m-%d')}.txt"


    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n👤 User: {user_input}\n")
        f.write(f"🕓 Antwortzeit: {elapsed_time:.2f} Sekunden\n")
        f.write(f"🤖 KI: {response}\n")
        f.write("-" * 40 + "\n")
    print(f"✅ Log gespeichert in: {log_path}")
