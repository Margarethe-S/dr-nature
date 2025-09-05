from backend.memory_manager import init_new_user, load_global_memory, save_user_data

def test_init_new_user_structure():
    user_id, user_data = init_new_user()
    assert user_id.startswith("user")
    assert "name" in user_data  # oder "messages", je nachdem, was deine Struktur enthält

def test_load_global_memory_structure():
    global_data = load_global_memory()
    assert isinstance(global_data, dict)
    assert "users" in global_data
    assert isinstance(global_data["users"], list)

def test_save_user_data_structure():
    user_id = "user_123"
    user_data = {"name": "Test User", "messages": []}
    save_user_data(user_id, user_data)
    # Hier könntest du überprüfen, ob die Daten korrekt gespeichert wurden