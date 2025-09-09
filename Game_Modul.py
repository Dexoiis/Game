#-------------#
# Game_Modul  #
#-------------#
# Enthält Spiellogik, Menüs, Hilfsfunktionen.

import os
import time

from Character_Modul import Character
from Enemy_Modul import Enemy
from save_manager import save_character, load_character
from Fight_Modul import fight

#------------------------#
# Mehrere Speicherstände #
#------------------------#
try:
    from save_manager import list_saves
except ImportError:
    list_saves = None

# ---------------------- #
# Rassen & Klassen-Setup #
# ---------------------- #

RACES = {
    "Mensch":        {"health": +10, "mana": +0,  "strength": +1, "dexterity": +0, "intelligence": +0},
    "Elf":           {"health": +0,  "mana": +30, "strength": -1, "dexterity": +4, "intelligence": +4},
    "Ork":           {"health": +40, "mana": -10, "strength": +5, "dexterity": -1, "intelligence": -1},
    "Echsenmensch":  {"health": +20, "mana": +0,  "strength": +2, "dexterity": +1, "intelligence": +0},
    "Untoter":       {"health": +20, "mana": +0,  "strength": +1, "dexterity": -1, "intelligence": +2},
    "Troll":         {"health": +40, "mana": -10, "strength": +4, "dexterity": -1, "intelligence": -1},
    "Goblin":        {"health": +0,  "mana": +0,  "strength": -1, "dexterity": +3, "intelligence": +1},
    "Fee":           {"health": +10, "mana": +30, "strength": -1, "dexterity": +3, "intelligence": +1},
    "Zwerg":         {"health": +30, "mana": +0,  "strength": +2, "dexterity": -1, "intelligence": +1},
}

CLASSES = {
    "Krieger": {
        "bonuses": {"health": +20, "strength": +3},
        "abilities": ["Schwerthieb", "Schildblock"]
    },
    "Magier": {
        "bonuses": {"mana": +30, "intelligence": +3},
        "abilities": ["Feuerball", "Heilen"]
    },
    "Dieb": {
        "bonuses": {"dexterity": +2},
        "abilities": ["Meucheln", "Ausweichen"]
    },
    "Paladin": {
        "bonuses": {"health": +30, "mana": +10, "strength": +2},
        "abilities": ["Göttlicher Schlag", "Heilige Aura"]
    },
    "Hexenmeister": {
        "bonuses": {"mana": +25, "intelligence": +2},
        "abilities": ["Arkaner Strahl", "Dunkles Opfer"]
    },
    "Druide": {
        "bonuses": {"mana": +20, "intelligence": +2, "health": +5},
        "abilities": ["Wurzelbann", "Tiergestalt"]
    },
    "Nekromant": {
        "bonuses": {"mana": +25, "intelligence": +3},
        "abilities": ["Skelettdiener", "Lebensraub"]
    },
    "Assassine": {
        "bonuses": {"dexterity": +3},
        "abilities": ["Todesstoß", "Rauchbombe"]
    },
    "Alchemist": {
        "bonuses": {"intelligence": +2, "mana": +10},
        "abilities": ["Sprengflasche", "Heiltrank"]
    },
}

SAVES_FOLDER = "saves"  # Fallback, falls save_manager.list_saves nicht existiert


# ---------- #
# Utilities  #
# ---------- #

def clear():
    """Einfache Bildschirm-„Bereinigung“."""
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass


def prompt_menu(title, options):
    """Zeigt ein nummeriertes Menü und gibt den gewählten Key zurück."""
    print(title)
    keys = list(options.keys())
    for i, key in enumerate(keys, start=1):
        print(f"{i}) {key}")
    while True:
        w = input("Deine Wahl: ").strip()
        if w.isdigit():
            idx = int(w)
            if 1 <= idx <= len(keys):
                return keys[idx - 1]
        print("Ungültige Auswahl – bitte erneut.")


#-------------#
# Rassen Boni #
#-------------#
def apply_bonuses(char, race_name, class_name):
    """Wendet Rassen- und Klassen-Boni dauerhaft an (bonus_*) und passt aktuelle Werte an."""
    # Safety: Bonus-Felder absichern (alte Spielstände)
    for field in ("bonus_health", "bonus_mana", "bonus_strength", "bonus_dexterity", "bonus_intelligence"):
        if not hasattr(char, field):
            setattr(char, field, 0)

    # Rassen-Boni
    for attr, delta in RACES[race_name].items():
        bonus_attr = f"bonus_{attr}"
        if hasattr(char, bonus_attr):
            setattr(char, bonus_attr, getattr(char, bonus_attr) + int(delta))

    # Klassen-Boni
    for attr, delta in CLASSES[class_name]["bonuses"].items():
        bonus_attr = f"bonus_{attr}"
        if hasattr(char, bonus_attr):
            setattr(char, bonus_attr, getattr(char, bonus_attr) + int(delta))

    # Fähigkeiten
    if not hasattr(char, "abilities") or char.abilities is None:
        char.abilities = []
    for ab in CLASSES[class_name].get("abilities", []):
        if ab not in char.abilities:
            char.abilities.append(ab)

    # Aktuelle Werte auf Max-Werte
    char.health = char.max_health()
    char.mana = char.max_mana()
    char.strength = char.max_strength()
    char.dexterity = char.max_dexterity()
    char.intelligence = char.max_intelligence()


#-------------#
# Neues Spiel #
#-------------#
def neues_spiel():
    clear()
    print("## Charakter erstellen ##")
    name = input("Name: ").strip() or "Held"
    race = prompt_menu("\nWähle eine Rasse:", RACES)
    char_class = prompt_menu("\nWähle eine Klasse:", CLASSES)

    # Basis-Charakter
    char = Character(name, race, char_class)

    # Boni anwenden
    apply_bonuses(char, race, char_class)

    print("\nCharakter erstellt!\n")
    char.show_info()

    # Speichern (save_manager kümmert sich um Pfad/Dateinamen)
    save_character(char)
    print("✅ Spielstand gespeichert.\n")
    return char


def _fallback_list_saves_from_folder():
    """Falls save_manager.list_saves nicht existiert: suche Dateien im Ordner 'saves'."""
    if not os.path.isdir(SAVES_FOLDER):
        return []
    return [f for f in os.listdir(SAVES_FOLDER) if f.startswith("save_") and f.endswith(".json")]


def lade_spiel():
    """Spielstand auswählen und laden."""
    # benutze list_saves() wenn vorhanden, sonst Fallback in den Ordner
    saves = list_saves() if callable(list_saves) else _fallback_list_saves_from_folder()
    if not saves:
        print("Keine Spielstände gefunden.")
        return None

    print("Verfügbare Spielstände:")
    for i, fname in enumerate(saves, 1):
        print(f"{i}) {fname}")

    try:
        idx = int(input("Wählen: ").strip() or "1") - 1
    except ValueError:
        idx = 0
    idx = max(0, min(idx, len(saves) - 1))

    char = load_character(saves[idx])
    if char:
        print("\n✅ Spielstand geladen.\n")
        char.show_info()
        return char
    else:
        print("❌ Laden fehlgeschlagen.")
        return None


def hauptmenue_loop():
    """Titelmenü: Neues Spiel / Laden / Beenden. Gibt Character oder None zurück."""
    while True:
        print("\n====== Willkommen ======")
        print("1) Neues Spiel erstellen")
        print("2) Spielstand laden")
        print("0) Beenden")
        auswahl = input("Wähle eine Option: ").strip()

        if auswahl == "1":
            return neues_spiel()  # Neues Spiel erstellen
        elif auswahl == "2":
            char = lade_spiel()   # Vorhandenes Spiel laden
            if char is not None:
                return char
            print("\nZurück zum Hauptmenü.\n")
        elif auswahl == "0":      # Spiel wird beendet
            print("Spiel wird beendet.")
            return None           # wichtig: kein sys.exit()
        else:
            print("Ungültige Eingabe.\n")


def naechster_kampf(player):
    enemy = Enemy(player.level)
    enemy.show_info()
    result = fight(player, enemy)
    if result:
        print("Sieg! Zurück ins Lager.")
    else:
        print("Kampf beendet.")


def ausruhen(player):
    print("\n=== Ausruhen ===")
    try:
        secs = int(input("Wie viele Sekunden möchtest du ausruhen? ").strip() or "1")
    except ValueError:
        print("Abgebrochen.")
        return
    for _ in range(secs):
        if player.health >= player.max_health():
            print("Du bist voll geheilt.")
            break
        time.sleep(1)
        player.heal(5)
        print(f"+5 HP ({player.health}/{player.max_health()})")
    print("Ausruhe-Phase beendet.\n")


def hub(player):
    """Spiel-Hub. Rückkehr (0) bringt dich zurück zum Titelmenü."""
    while True:
        print("\n=== Hauptmenü ===")
        print("1) Kampf starten")
        print("2) Ausruhen (+5 HP/Sek.)")
        print("3) Charakter anzeigen")
        print("4) Spielstand speichern")
        print("0) Zurück zum Titel")
        choice = input("→ ").strip()

        if choice == "1":
            naechster_kampf(player)
        elif choice == "2":
            ausruhen(player)
        elif choice == "3":
            player.show_info()
            if hasattr(player, "show_equipment"):
                player.show_equipment()
        elif choice == "4":
            save_character(player)
        elif choice == "0":
            print("Zurück zum Titel …")
            return             # zurück zum Titelmenü
        else:
            print("Ungültig.")


def run():
    """Kompletter Spielablauf: Titelmenü ↔ Hub."""
    while True:
        clear()
        char = hauptmenue_loop()   # Character oder None
        if char is None:
            print("Spiel beendet.")
            return
        hub(char)                  # nach Rückkehr erneut ins Titelmenü
