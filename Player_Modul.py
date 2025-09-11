#------------------#
# Player_Modul.py  #
#------------------#
# NEU: In-Game-Menü-Helfer, Inventar/Equip, Ausruhen
# <<< NEU >>>

import threading  # <<< NEU
import time       # <<< NEU
from typing import Dict

# Minimaler Item-Katalog mit Slot/Stats/Wert/Use (kannst du später mit Item_Modul mappen)
# <<< NEU >>>
ITEM_REGISTRY: Dict[str, Dict] = {
    "Rostiges Schwert":      {"slot": "waffe",   "rarity": "gewöhnlich", "bonuses": {"attack": 2},  "value": 5},
    "Lederweste":            {"slot": "brust",   "rarity": "gewöhnlich", "bonuses": {"defense": 1}, "value": 5},
    "Lederkappe":            {"slot": "helm",    "rarity": "gewöhnlich", "bonuses": {"defense": 1}, "value": 4},
    "Knochenschwert":        {"slot": "waffe",   "rarity": "selten",     "bonuses": {"attack": 4},  "value": 20},
    "Amulett des Flüsterns": {"slot": "amulett", "rarity": "episch",     "bonuses": {"intelligence": 2}, "value": 60},
    "Kupfermünze":           {"slot": None,      "rarity": "gewöhnlich", "bonuses": {}, "value": 1},
    "Kupfermünzen":          {"slot": None,      "rarity": "gewöhnlich", "bonuses": {}, "value": 5},

    # Tränke (Verbrauch)
    "Mini-Heiltrank":        {"slot": None, "rarity": "gewöhnlich", "bonuses": {}, "value": 3,  "use": ("heal", 10)},
    "Kleiner Heiltrank":     {"slot": None, "rarity": "gewöhnlich", "bonuses": {}, "value": 6,  "use": ("heal", 20)},
    "Mittlerer Heiltrank":   {"slot": None, "rarity": "selten",     "bonuses": {}, "value": 12, "use": ("heal", 50)},
    "Großer Heiltrank":      {"slot": None, "rarity": "episch",     "bonuses": {}, "value": 30, "use": ("heal", 120)},
}

EQUIP_SLOTS = ["waffe", "helm", "brust", "hose", "schuhe", "amulett", "ring1", "ring2"]  # <<< NEU

# --- Hilfen ----------------------------------------------------------------

def _ensure_player_fields(player):  # <<< NEU
    if not hasattr(player, "inventory"):
        player.inventory = []
    if not hasattr(player, "equipped"):
        player.equipped = {s: None for s in EQUIP_SLOTS}
    if not hasattr(player, "draken"):
        player.draken = 0
    if not hasattr(player, "equip_bonus_totals"):
        player.equip_bonus_totals = {}

def add_loot_to_inventory(player, item_name: str):  # <<< NEU
    """Loot als einfacher String ins Inventar legen."""
    _ensure_player_fields(player)
    player.inventory.append(item_name)
    print(f"📦 {item_name} ins Inventar gelegt.")
    if hasattr(player, "quest_manager"):
        player.quest_manager.update_progress("collect", item_name)

def _apply_all_equip_bonuses(player):  # <<< NEU
    """Equip-Boni zusammenfassen und anwenden."""
    totals = {"attack": 0, "defense": 0, "strength": 0, "max_health": 0, "intelligence": 0}
    for slot, equipped in player.equipped.items():
        if not equipped:
            continue
        reg = ITEM_REGISTRY.get(equipped["name"], {})
        for k, v in reg.get("bonuses", {}).items():
            totals[k] = totals.get(k, 0) + int(v)

    player.equip_bonus_totals.update({k: totals.get(k, 0) for k in totals})

    # Additive Anwendung (einfach, robust)
    player.attack       = max(0, player.attack)       + totals.get("attack", 0)
    player.defense      = max(0, player.defense)      + totals.get("defense", 0)
    player.strength     = max(0, player.strength)     + totals.get("strength", 0)
    player.intelligence = max(0, player.intelligence) + totals.get("intelligence", 0)

    # HP clampen, falls max_health durch Equip steigt
    if hasattr(player, "max_health"):
        player.health = min(player.health, player.max_health())

# --- Equip/Unequip/Use/Sell ------------------------------------------------

def equip_item(player, item_name: str) -> bool:  # <<< NEU
    _ensure_player_fields(player)
    reg = ITEM_REGISTRY.get(item_name)
    if not reg or not reg.get("slot"):
        print("❌ Dieses Item ist nicht ausrüstbar.")
        return False
    slot = reg["slot"]

    if item_name not in player.inventory:
        print("❌ Item nicht im Inventar.")
        return False

    if player.equipped.get(slot):
        player.inventory.append(player.equipped[slot]["name"])

    player.equipped[slot] = {"name": item_name, "rarity": reg.get("rarity", "gewöhnlich")}
    player.inventory.remove(item_name)

    _apply_all_equip_bonuses(player)
    print(f"✅ Ausgerüstet: {item_name} ({slot}).")
    return True

def unequip_slot(player, slot: str) -> bool:  # <<< NEU
    _ensure_player_fields(player)
    if slot not in EQUIP_SLOTS:
        print("❌ Unbekannter Slot.")
        return False
    item = player.equipped.get(slot)
    if not item:
        print("Slot ist leer.")
        return False
    player.inventory.append(item["name"])
    player.equipped[slot] = None
    _apply_all_equip_bonuses(player)
    print(f"✅ Abgelegt: {item['name']} ({slot}).")
    return True

def use_item(player, item_name: str) -> bool:  # <<< NEU
    _ensure_player_fields(player)
    if item_name not in player.inventory:
        print("❌ Nicht im Inventar.")
        return False
    reg = ITEM_REGISTRY.get(item_name, {})
    use_def = reg.get("use")
    if not use_def:
        print("❌ Nicht benutzbar.")
        return False

    kind, amount = use_def
    if kind == "heal":
        before = player.health
        player.heal(int(amount))
        print(f"✨ {item_name} benutzt (+{player.health - before} HP).")
    # (erweiterbar für mana, buff etc.)

    player.inventory.remove(item_name)
    return True

def sell_item(player, item_name: str) -> bool:  # <<< NEU
    _ensure_player_fields(player)
    if item_name not in player.inventory:
        print("❌ Nicht im Inventar.")
        return False
    value = ITEM_REGISTRY.get(item_name, {}).get("value", 0)
    player.inventory.remove(item_name)
    player.draken = getattr(player, "draken", 0) + value
    print(f"💰 {item_name} verkauft (+{value} Draken).")
    return True

# --- Ansichten/Menüs -------------------------------------------------------

def show_full_character(player):  # <<< NEU
    player.show_info()
    if hasattr(player, "show_equipment"):
        player.show_equipment()

def inventory_menu(player):  # <<< NEU
    _ensure_player_fields(player)
    while True:
        print("\n=== Inventar ===")
        if not player.inventory:
            print("Leer.")
        else:
            counts = {}
            for it in player.inventory:
                counts[it] = counts.get(it, 0) + 1
            for i, (name, qty) in enumerate(sorted(counts.items()), 1):
                print(f"{i}) {name} x{qty}")
        print("\n[A]usrüsten  [U]nablegen  [B]enutzen  [V]erkaufen  [Z]urück")
        choice = input("> ").strip().lower()
        if choice == "a":
            item = input("Itemname zum Ausrüsten: ").strip()
            equip_item(player, item)
        elif choice == "u":
            slot = input(f"Slot ({', '.join(EQUIP_SLOTS)}): ").strip().lower()
            unequip_slot(player, slot)
        elif choice == "b":
            item = input("Itemname zum Benutzen: ").strip()
            use_item(player, item)
        elif choice == "v":
            item = input("Itemname zum Verkaufen: ").strip()
            sell_item(player, item)
        elif choice == "z":
            break
        else:
            print("Ungültig.")

def rest_until_enter(player):  # <<< NEU
    """1 HP/Sekunde bis Enter gedrückt wird (plattf.-neutral)."""
    stop_flag = {"stop": False}
    def wait_for_enter():
        input("⏳ Ausruhen… (Enter = abbrechen)\n")
        stop_flag["stop"] = True

    t = threading.Thread(target=wait_for_enter, daemon=True)
    t.start()

    while not stop_flag["stop"] and player.health < player.max_health():
        player.heal(1)
        time.sleep(1)

    print(f"🏕️ Ausruhen beendet. HP: {player.health}/{player.max_health()}")

