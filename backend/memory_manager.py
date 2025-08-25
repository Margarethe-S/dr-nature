import json
import os

# 📁 Pfad zur globalen Speicherdatei (JSON), die alle User-IDs verwaltet
MEMORY_PATH = "./memory/global_memory.json"

# 📁 Ordner, in dem einzelne Nutzerdateien gespeichert werden (user1.json usw.)
USERS_PATH = "./memory/users/"

# 🔄 Funktion zum Laden des globalen Speicherstatus (alle registrierten User, Default-Template)
def load_global_memory():
    if not os.path.exists(MEMORY_PATH):
        raise FileNotFoundError("global_memory.json nicht gefunden!")  # Fehler, wenn Datei fehlt
    with open(MEMORY_PATH, "r", encoding="utf-8") as file:
        return json.load(file)  # JSON als Python-Dictionary laden

# 💾 Funktion zum Speichern einer Nutzerdatei (z. B. user1.json)
def save_user_data(user_id, user_data):
    user_file = os.path.join(USERS_PATH, f"{user_id}.json")  # z. B. ./memory/users/user1.json
    with open(user_file, "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4, ensure_ascii=False)  # als schön formatierte JSON speichern

# 🔢 Funktion, die automatisch eine freie User-ID erzeugt (user1, user2, user3, …)
def generate_next_user_id(existing_users):
    index = 1
    while f"user{index}" in existing_users:
        index += 1
    return f"user{index}"

# ✨ Funktion zur Initialisierung eines neuen anonymen Nutzers
def init_new_user():
    memory = load_global_memory()  # global_memory.json laden

    # Neue, nicht vergebene User-ID ermitteln
    new_user_id = generate_next_user_id(memory["users"])
    print(f"[INFO] Neuer User wird angelegt: {new_user_id}")

    # 🧬 Benutzer-Template kopieren und User-ID setzen
    user_template = memory["default_user_structure"]
    user_template["name"] = new_user_id

    # Template in globale Übersicht eintragen
    memory["users"][new_user_id] = user_template

    # Nutzerdatei separat speichern (z. B. user1.json)
    save_user_data(new_user_id, user_template)

    # global_memory.json ebenfalls aktualisieren
    with open(MEMORY_PATH, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)

    return new_user_id, user_template  # Rückgabe für weitere Verwendung

# 🧪 Testlauf, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    user_id, user_data = init_new_user()
    print(f"[OK] Neuer anonymer User gespeichert: {user_id}")
