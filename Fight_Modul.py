#----------------#
# Kampf-Funktion #
#----------------#

import random
from save_manager import save_character
from Item_Modul import Items
from Ability_Modul import ABILITIES


#--------------------------------#
# Fähigkeit einsetzen
#--------------------------------#
def use_ability(player, enemy):
    """Lässt den Spieler eine Fähigkeit wählen und anwenden."""
    if not getattr(player, "abilities", []):
        print("Keine Fähigkeiten verfügbar!")
        return

    print("Fähigkeiten:")
    for i, ab_name in enumerate(player.abilities, 1):
        data = ABILITIES.get(ab_name, {})
        dmg = data.get("damage", 0)
        cost = data.get("mana_cost", 0)
        print(f"{i}) {ab_name} (Schaden: {dmg}, Mana: {cost})")

    try:
        idx = int(input("Wähle Fähigkeit: ")) - 1
    except ValueError:
        print("Ungültige Auswahl!")
        return
    if idx < 0 or idx >= len(player.abilities):
        print("Ungültige Auswahl!")
        return

    name = player.abilities[idx]
    data = ABILITIES.get(name, {})
    cost = data.get("mana_cost", 0)
    damage = data.get("damage", 0)
    if player.mana < cost:
        print("Nicht genug Mana!")
        return

    player.mana -= cost
    if damage >= 0:
        print(f"{player.name} setzt {name} ein und verursacht {damage} Schaden!")
        enemy.take_damage(damage)
    else:
        heal_amount = -damage
        player.heal(heal_amount)
        print(f"{player.name} setzt {name} ein und heilt {heal_amount} HP!")
    print(f"{player.name} hat noch {player.mana} Mana.")


#------------------------#
# Runden Basierter Kampf #
#------------------------#
def fight(player, enemy):
    while player.health > 0 and enemy.is_alive():
        print("\n--- Deine Runde ---")
        print("1) Angreifen")
        print("2) Fähigkeit einsetzen")
        print("3) Heilen (10 HP)")
        print("4) Fliehen")

        choice = input("Wähle deine Aktion: ")

        #-------------------#
        # Spieler greift an #
        #-------------------#
        if choice == "1":
            crit_roll = random.randint(1, 100)
            damage = player.attack + player.strength + random.randint(0, 5)
            if crit_roll <= player.crit_chance:
                damage *= 2
                print("💥 Kritischer Treffer!")
            print(f"{player.name} greift {enemy.type_name} an und verursacht {damage} Schaden!")
            enemy.take_damage(damage)

        elif choice == "2":
            use_ability(player, enemy)

        elif choice == "3":
            player.heal(10)
            print(f"{player.name} heilt 10 HP.")

        elif choice == "4":
            print(f"{player.name} flieht vor {enemy.type_name}!")
            return

        else:
            print("Ungültige Auswahl! Du verlierst deinen Zug.")

        #---------------------------#
        # Prüfen, ob Gegner tot ist #
        #---------------------------#
        if not enemy.is_alive():
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
            print(f"{enemy.type_name} greift {player.name} an und verursacht {enemy_damage} Schaden!")
            player.take_damage(enemy_damage)

        #----------------------------#
        # Prüfen, ob Spieler tot ist #
        #----------------------------#
        if player.health <= 0:
            print(f"💀 {player.name} wurde besiegt!")
            break

        #---------------------------------------#
        # Spielstand speichern nach jeder Runde #
        #---------------------------------------#
        save_character(player)
        print("\n✅ Spielstand gespeichert!\n")