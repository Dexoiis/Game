#----------------#
# Kampf-Funktion #
#----------------#

import random
from save_manager import save_character
from Item_Modul import Items

#------------------------#
# Runden Basierter Kampf #
#------------------------#
def fight(player, enemy):
    while player.health > 0 and enemy.is_alive():
        print("\n--- Deine Runde ---")
        print("1) Angreifen")
        print("2) Heilen (10 HP)")
        print("3) Fliehen")
        
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
            player.heal(10)
            print(f"{player.name} heilt 10 HP.")

        elif choice == "3":
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