#----------------#
# Kampf-Funktion #
#----------------#

import random
from save_manager import save_character
from Item_Modul import Items
from Ability_Modul import ABILITIES, use_ability

#------------------------#
# Runden Basierter Kampf #
#------------------------#
def fight(player, enemy):
    active_def_buff = 0
    while player.health > 0 and enemy.is_alive():
        print("\n--- Deine Runde ---")
        print("1) Angreifen")
        print("2) Heilen (10 HP)")
        print("3) Fliehen")
        if getattr(player, "abilities", []):
            print("4) Fähigkeit wirken")

        choice = input("Wähle deine Aktion: ")

#-------------------#
# Spieler greift an #
#-------------------#
        if choice == "1":
            crit_roll = random.randint(1, 100)
            base = player.attack + player.strength + random.randint(0, 5)
            if crit_roll <= player.crit_chance:
                base *= 2
                print("💥 Kritischer Treffer!")
            damage = max(0, base - enemy.defense)
            print(f"{player.name} greift {enemy.type_name} an und verursacht {damage} Schaden!")
            enemy.take_damage(damage)

        elif choice == "2":
            player.heal(10)
            print(f"{player.name} heilt 20 HP.")

        elif choice == "3":
            print(f"{player.name} flieht vor {enemy.type_name}!")
            return

        elif choice == "4" and getattr(player, "abilities", []):
            print("Verfügbare Fähigkeiten:")
            for i, ab in enumerate(player.abilities, 1):
                info = ABILITIES.get(ab, {})
                cost = info.get("mana", 0)
                parts = []
                if info.get("damage"):
                    parts.append(f"DMG:{info['damage']}")
                if info.get("heal"):
                    parts.append(f"HEAL:{info['heal']}")
                if info.get("defense"):
                    parts.append(f"DEF:{info['defense']}")
                stats = ", ".join(parts)
                print(f"{i}) {ab} (Mana:{cost}{', ' + stats if stats else ''})")
            try:
                idx = int(input("Fähigkeit wählen: ")) - 1
            except ValueError:
                idx = -1
            if 0 <= idx < len(player.abilities):
                ability_name = player.abilities[idx]
                buff = use_ability(player, ability_name, enemy)
                if buff:
                    active_def_buff = buff
            else:
                print("Ungültige Auswahl!")
        else:
            print("Ungültige Auswahl! Du verlierst deinen Zug.")

#---------------------------#
# Prüfen, ob Gegner tot ist #
#---------------------------#
        if not enemy.is_alive():
            if active_def_buff:
                player.defense -= active_def_buff
                active_def_buff = 0
            print(f"🏆 {enemy.type_name} besiegt!")
            print(f"{player.name} erhält {enemy.exp_reward} XP!")
            player.gain_xp(enemy.exp_reward)
            dropped = enemy.drop_item()
            if dropped:
                print(f"{player.name} erhält: {dropped}")
            save_character(player)
            print("\n✅ Spielstand gespeichert!\n")

            break
#------------------#
# Gegner greift an #
#------------------#
        print(f"\n--- Gegner-Runde ---")
        if enemy.is_alive():
            enemy_damage = enemy.attack + random.randint(0, 3)
            enemy_damage = max(0, enemy_damage - player.defense)
            print(f"{enemy.type_name} greift {player.name} an und verursacht {enemy_damage} Schaden!")
            player.take_damage(enemy_damage)
        if active_def_buff:
            player.defense -= active_def_buff
            active_def_buff = 0
#----------------------------#
# Prüfen, ob Spieler tot ist #
#----------------------------#
        if player.health <= 0:
            print(f"💀 {player.name} wurde besiegt!")
            break
        
#---------------------------------------#
# Spielstand speichern nach jeder Runde #
#---------------------------------------#
