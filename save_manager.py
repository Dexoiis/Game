#---------------------#
# Save Manager Module #
#---------------------#

import json
import os
from Character_Modul import Character
from Quest_Modul import QuestManager

SAVE_FOLDER = "saves"

# Stelle sicher, dass es den Ordner gibt
os.makedirs(SAVE_FOLDER, exist_ok=True)

def save_character(character):
    """Speichert den aktuellen Spielstand des Charakters."""
    filename = f"save_{character.name}.json"
    path = os.path.join(SAVE_FOLDER, filename)
    data = character.to_dict()
    if hasattr(character, "quest_manager") and character.quest_manager:
        data["quest_manager"] = character.quest_manager.to_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Spielstand gespeichert unter {filename}!")


def list_saves():
    """Gibt eine Liste aller gespeicherten Spielstände zurück."""
    files = [f for f in os.listdir(SAVE_FOLDER) if f.startswith("save_") and f.endswith(".json")]
    return files


def load_character(filename):
    """Lädt einen Spielstand aus der Datei."""
    path = os.path.join(SAVE_FOLDER, filename)

    if not os.path.isfile(path):
        print("⚠️ Kein Spielstand gefunden. Starte einen neuen Charakter.")
        return Character("Held", "Mensch", "Krieger")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        character = Character.from_dict(data)
        return character
    except FileNotFoundError:
        print("⚠️ Datei nicht gefunden.")
        return None

        print("⚠️ Kein Spielstand gefunden. Starte ein neues Spiel.")
        return None


