import os
import json
import uuid

# 🔁 Globale Konfig: Speicherpfade
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MEMORY_PATH = os.path.join(BASE_PATH, "memory")
USERS_PATH = os.path.join(MEMORY_PATH, "users")
GLOBAL_MEMORY_FILE = os.path.join(MEMORY_PATH, "global_memory.json")
DEFAULT_MODE = "core_mode"

# 🧱 Grundstruktur, wenn Datei neu erstellt wird
DEFAULT_GLOBAL_STRUCTURE = {
    "users": {},
    "default_user_structure": {
        "name": "",
        "messages": []
    }
}


# 🧠 Initialisiere Speicherstruktur (einmalig beim Start)
def init_memory():
    os.makedirs(USERS_PATH, exist_ok=True)
    if not os.path.exists(GLOBAL_MEMORY_FILE):
        with open(GLOBAL_MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_GLOBAL_STRUCTURE, f, indent=2, ensure_ascii=False)

# 🆔 Neuen User registrieren
def create_new_user():
    os.makedirs(USERS_PATH, exist_ok=True)

    # Bestehende User zählen
    existing_files = os.listdir(USERS_PATH)
    user_numbers = []

    for filename in existing_files:
        try:
            with open(os.path.join(USERS_PATH, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                name = data.get("name", "")
                if name.startswith("user") and name[4:].isdigit():
                    user_numbers.append(int(name[4:]))
        except:
            continue

    next_user_number = max(user_numbers, default=0) + 1
    new_name = f"user{next_user_number}"
    new_uuid = str(uuid.uuid4())

    user_data = {
        "name": new_name,
        "messages": [],
        "mode": DEFAULT_MODE
    }

    user_file = os.path.join(USERS_PATH, f"{new_name}.json")
    with open(user_file, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=2, ensure_ascii=False)

    return new_name

def set_user_mode(user_id, mode_name):
    user_data = load_user_data(user_id)
    user_data["mode"] = mode_name
    save_user_data(user_id, user_data)



# 🧭 Nutzer-ID anhand des Namens holen
def get_user_id_by_name(name):
    for filename in os.listdir(USERS_PATH):
        file_path = os.path.join(USERS_PATH, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("name") == name:
                    return filename.replace(".json", "")
        except:
            continue
    return None


# 📥 Lade kompletten User-Datensatz
def load_user_data(user_id):
    user_file = os.path.join(USERS_PATH, f"{user_id}.json")
    if not os.path.exists(user_file):
        raise FileNotFoundError(f"Datei für {user_id} nicht gefunden!")
    with open(user_file, "r", encoding="utf-8") as f:
        return json.load(f)

# 💾 Speichere User-Datensatz
def save_user_data(user_id, user_data):
    user_file = os.path.join(USERS_PATH, f"{user_id}.json")
    with open(user_file, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=2, ensure_ascii=False)

# ➕ Füge neue Nachricht zur Message-History hinzu
def add_message_to_user(user_id, role, content, mode=None):
    user_data = load_user_data(user_id)
    active_mode = user_data.get("mode", DEFAULT_MODE)

    user_data.setdefault("messages", []).append({
        "role": role,
        "content": content,
        "mode": mode or active_mode
    })
    save_user_data(user_id, user_data)


# 📤 Hole gesamten bisherigen Nachrichtenverlauf
def get_user_messages(user_id):
    user_data = load_user_data(user_id)
    return user_data.get("messages", [])
