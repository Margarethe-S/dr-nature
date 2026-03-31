import sys
import os
import requests
import time
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))


try:
    from .logger import save_log, save_conversation_log
except ImportError:
    from logger import save_log, save_conversation_log

from memory_manager import (
    init_memory,
    get_user_id_by_name,
    create_new_user,
    set_user_mode,
    add_message_to_user,
    get_user_messages
)

os.makedirs("logs", exist_ok=True)

prompt_path = "system_prompt/core_mode.txt" # DEIN Pfad zum Systemprompt (Textdatei)

stop_event = threading.Event() # Stopp-Event für die Stoppuhr

elapsed_time = 0  # Initialisierung der elapsed_time-Variable

status_msg = "✅ Erfolgreich!"  # Initialisierung der status_msg-Variable


# .env einlesen
def load_env(filepath=".env"):
    if not os.path.exists(filepath):
        print(f"⚠️  .env file not found at: {filepath}")
        return
    with open(filepath, "r") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value


# 🧠 Speicher initialisieren
def run_dev_mode():
    load_env()
    init_memory()
    user_name = "user1"  # später dynamisch, z. B. Login
    user_id = get_user_id_by_name(user_name) or create_new_user()

    # Modus aus Dateinamen extrahieren
    modename = os.path.basename(prompt_path).replace(".txt", "")
    set_user_mode(user_id, modename)  # Setze den Modus für user1

    print(f"👤 Nutzer: {user_name}, 🛠️  Modus: {modename}")


    # API-URL aus Umgebungsvariable holen
    api_url = os.getenv("LMSTUDIO_API_URL")

    # Systemprompt laden – DEIN Pfad:
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt = f.read()

    print("System Prompt wird geladen:", prompt[:300], "...")

    # 🕒 Gemeinsame Startzeit
    start_time = time.time()
    success = True  # Annahme: Erfolgreich, bis ein Fehler kommt
    response = None  # Initialisierung der response-Variable
    elapsed_time = 0

    # Stoppuhr in separatem Thread starten
    def live_stopwatch(start_time):
        while not stop_event.is_set():
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            millis = int((elapsed - int(elapsed)) * 1000)
            print(f"\r⏳ Laufzeit: {mins:02d}:{secs:02d}.{millis:03d}", end="")
            time.sleep(0.1)
        print("\n✅ Stoppuhr beendet.")

    # 🟢 Stoppuhr starten (mit übergebener Startzeit)
    t = threading.Thread(target=live_stopwatch, args=(start_time,))
    t.start()



    # Beispiel-Eingabe
    user_input = "Was kann ich gegen Kopfschmerzen auf natürliche Weise tun?"


    try:

        
        
        # Anfrage an LM Studio senden
        add_message_to_user(user_id, "user", user_input)

        conversation_history = get_user_messages(user_id)
        payload = {
            "model": "em_german_mistral_v01",
            "messages": [{"role": "system", "content": prompt}] + conversation_history,
            "temperature": 0.0
        }

        response = requests.post(
            api_url,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=300
        )

        response_data = response.json()
        response_text = response_data["choices"][0]["message"]["content"]
        status_msg = "✅ Erfolgreich!"
        print(f"\n📩 Antwort von LM Studio:\n{response_text}")
        add_message_to_user(user_id, "assistant", response_text)
        
        # Endzeit und Berechnung
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)

        save_log(prompt_path, user_input, response_text, elapsed_time, status_msg)

        print(f"\n✅ Die Antwort hat: {elapsed_time:.2f} Sekunden gedauert.")
        print(f"🕓 = {int(minutes)} Minuten und {int(seconds)} Sekunden.")

    except requests.exceptions.Timeout:
        error_msg = "⏱️ Die Anfrage hat das Zeitlimit von 5 Minuten überschritten."
        status_msg = f"Response: {response}"
        print(error_msg)
        print(status_msg)
        response = f"{error_msg}"
        success = False

    except requests.exceptions.RequestException as e:
        error_msg = f"❌ Ein Fehler ist aufgetreten: {e}"
        status_msg = f"Response: {response}"
        print(error_msg)
        print(status_msg)
        response = f"{error_msg}"
        success = False

    except ValueError:
        error_msg = "❌❌ Antwort konnte nicht als JSON gelesen werden."
        status_msg = f"Response: {response}"
        print(error_msg)
        print(status_msg)
        response = f"{error_msg}"
        success = False

    except KeyError as e:
        error_msg = f"❌ Die Antwort der API war unvollständig oder fehlerhaft (KeyError: '{e.args[0]}')."
        status_msg = f"Response: {response}"
        print(error_msg)
        print(status_msg)
        response = f"{error_msg}"
        success = False

    finally:

        stop_event.set()
        t.join()

        if success:
            os.system('powershell -c "[console]::beep(1000, 500)"')
            print(status_msg)
        else:
            os.system('powershell -c "[console]::beep(1000, 500); Start-Sleep -Milliseconds 200; [console]::beep(600, 500)"')

    print("\n💬 Starte interaktive Konsole. Tippe 'exit' zum Beenden.\n")

    conversation = []  # speichert den Verlauf lokal in dieser Session

    while True:
        user_input = input("👤 User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("............................🚪 Gespräch beendet.")
            break


        # ⏱️ Neue Startzeit für diese Anfrage
        start_time = time.time()
        stop_event.clear()
        t = threading.Thread(target=live_stopwatch, args=(start_time,))
        t.start()


        try:
            add_message_to_user(user_id, "user", user_input)

            conversation_history = get_user_messages(user_id)
            payload = {
                "model": "em_german_mistral_v01",
                "messages": [{"role": "system", "content": prompt}] + conversation_history,
                "temperature": 0.0
            }

            response = requests.post(
                api_url,
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=300
            )

            response_data = response.json()
            response_text = response_data["choices"][0]["message"]["content"]
            status_msg = "✅ Erfolgreich!"
            print(f"\n📩 Antwort von LM Studio:\n{response_text}")
            add_message_to_user(user_id, "assistant", response_text)
            
            # ⏱️ Antwortzeit berechnen
            end_time = time.time()
            elapsed_time = end_time - start_time
            minutes, seconds = divmod(elapsed_time, 60)


            stop_event.set()
            t.join()



            # Verlauf speichern
            conversation.append((user_input, response_text))


            print(f"🤖 KI: {response_text}\n")
            print(f"🕓 Antwortzeit: {elapsed_time:.2f} Sekunden ({int(minutes)} Min {int(seconds)} Sek)")


            
            save_conversation_log(user_input, response_text, elapsed_time)

        



        except Exception as e:
            stop_event.set()
            t.join()
            print(f"❌ Fehler im Gespräch: {e}")
            save_log(prompt_path, user_input, f"Fehler: {e}", 0, "❌ Fehler (Gespräch)")

# ===================================================
# 🔁 Funktion zum Abrufen der KI-Antwort (für server.py)
# ===================================================
def get_lm_response(user_msg, prompt_path, messages=None):
    try:
        load_env()
        if not os.path.exists(prompt_path):
            return "⚠️ Prompt-Datei nicht gefunden."


        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read()


        api_url = os.getenv("LMSTUDIO_API_URL", "http://127.0.0.1:1234/v1/chat/completions")
        
        if messages is None:
            messages = [{"role": "user", "content":user_msg}]
        
        payload = {
            "model": "em_german_mistral_v01",
            "messages": [
                {"role": "system", "content": prompt}] + messages,
            "temperature": 0.0
        }


        response = requests.post(api_url, headers={"Content-Type": "application/json"}, json=payload, timeout=300)
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]


    except Exception as e:
        return f"⚠️ Fehler bei der KI-Anfrage: {e}"




# ===================================================
# 🧪 Manuelle Testfunktion zum Schnell-Check (optional)
# ===================================================
def test_lm_model_connection():
    test_prompt_path = "system_prompt/core_mode.txt"
    test_input = "Hallo, was kannst du für meine Gesundheit tun?"


    print("🧪 Testlauf mit:", test_input)
    print("📂 Prompt-Datei:", test_prompt_path)


    antwort = get_lm_response(test_input, test_prompt_path)
    print("\n🤖 Antwort vom Modell:")
    print(antwort)




# ================================================
# ⚙️ Testmodus nur bei direktem Start (nicht beim Import)
# ================================================
if __name__ == "__main__":
    run_dev_mode()
