# -------------#
# Enemy Module #
# -------------#

import random
from Item_Modul import Items, DROP_RAT

#---------------#
# Monster Typen #
#---------------#

class Enemy:
    MONSTER_TYPES = {
#------------------#
# Einfache Monster #
#------------------#
        "Goblin": {
            "base_health": 40, "base_attack": 5, "base_defense": 5, "base_speed": 3,
            "base_exp": 8,
            "drops": ["Altes Messer", "Zerfetzte Stoffhose", "Kleiner Heiltrank"]
            },
        "Kobold": {
            "base_health": 50, "base_attack": 6, "base_defense": 6, "base_speed": 4,
            "base_exp": 12,
            "drops": ["Kupfermünze", "Lederkappe", "Kleiner Manatrank"]
        },
        "Rattenkönig": {
            "base_health": 30, "base_attack": 5, "base_defense": 2, "base_speed": 4,
            "base_exp": 10,
            "drops": ["Zerkaute Lederrüstung", "Stinkender Fellfetzen", "Kleiner Heiltrank"]
        },
        "Höhlenkrabbler": {
            "base_health": 40, "base_attack": 6, "base_defense": 3, "base_speed": 5,
            "base_exp": 15,
            "drops": ["Spinnengift", "Zerbrochene Krallen", "Gifttrank (klein)"]
        },
        "Bandit": {
            "base_health": 50, "base_attack": 8, "base_defense": 4, "base_speed": 6,
            "base_exp": 20,
            "drops": ["Rostiges Schwert", "Lederweste", "Kupfermünzen"]
        },
        "Glühwürmenschwarm": {
            "base_health": 25, "base_attack": 4, "base_defense": 1, "base_speed": 10,
            "base_exp": 12,
            "drops": ["Leuchtstaub", "Käferflügel", "Mini-Heiltrank"]
        },
        "Verfluchter Vogel": {
            "base_health": 30, "base_attack": 6, "base_defense": 3, "base_speed": 10,
            "base_exp": 15,
            "drops": ["Rabenklaue", "Schwarze Feder", "Amulett des Flüsterns"]
        },
#------------------#
# Mittlere Monster #
#------------------#      
        "Schattenwolf": {
            "base_health": 60, "base_attack": 10, "base_defense": 5, "base_speed": 9,
            "base_exp": 30,
            "drops": ["Wolfspelz", "Schattenzahn", "Mittlerer Heiltrank"]
            },
        "Morastgeist": {
            "base_health": 55, "base_attack": 9, "base_defense": 4, "base_speed": 7,
            "base_exp": 28,
            "drops": ["Geisteressenz", "Schleimtrank", "Magischer Splitter"]
        },
        "Steinwurm": {
            "base_health": 35, "base_attack": 7, "base_defense": 6, "base_speed": 2,
            "base_exp": 18,
            "drops": ["Splitterstein", "Wurmzahn", "Steinhaut-Salbe"]
        },
        "Blutegelriese": {
            "base_health": 80, "base_attack": 12, "base_defense": 6, "base_speed": 4,
            "base_exp": 40,
            "drops": ["Blutegelzahn", "Schleimhaut", "Gifttrank (mittel)"]
        },
        "Eiswyrmling": {
            "base_health": 90, "base_attack": 14, "base_defense": 8, "base_speed": 6,
            "base_exp": 50,
            "drops": ["Eisschuppe", "Frostzahn", "Kälteschutz-Trank"]
        },
        "Sandläufer": {
            "base_health": 100, "base_attack": 16, "base_defense": 10, "base_speed": 5,
            "base_exp": 55,
            "drops": ["Giftstachel", "Chitinpanzer", "Sandjuwel"]
        },
        "Knochenkrieger": {
            "base_health": 70, "base_attack": 12, "base_defense": 8, "base_speed": 5,
            "base_exp": 35,
            "drops": ["Knochenschwert", "Zerbeulte Eisrüstung", "Schädelamulet"]
        },
#----------------#    
# Schere Monster #
#----------------#
        "Schattendämon": {
            "base_health": 120, "base_attack": 18, "base_defense": 10, "base_speed": 8,
            "base_exp": 90,
            "drops": ["Dämonenherz", "Seelenfragment", "Großer Trank der Dunkelsicht"]
        },
        "Flammen-Golem": {
            "base_health": 150, "base_attack": 20, "base_defense": 15, "base_speed": 3,
            "base_exp": 100,
            "drops": ["Feuerkern", "Glutklinge", "Hitzeschutz-Ring"]
        },
         "Schattenritter": {
            "base_health": 160, "base_attack": 22, "base_defense": 14, "base_speed": 7,
            "base_exp": 120,
            "drops": ["Verfluchtes Schwert", "Rüstung der Schatten", "Seelenstein"]
        },
         "Kristallgolem": {
            "base_health": 180, "base_attack": 24, "base_defense": 18, "base_speed": 3,
            "base_exp": 140,
            "drops": ["Kristallfragment", "Leuchtender Kern", "Kristallrüstung"]
        },
        "Schrecken der Tiefen": {
            "base_health": 220, "base_attack": 28, "base_defense": 16, "base_speed": 5,
            "base_exp": 180,
            "drops": ["Tiefseeperle", "Tentakelpeitsche", "Essenz des Ozeans"]
        },
        "Drache": {
            "base_health": 120, "base_attack": 15, "base_defense": 10, "base_speed": 10,
            "base_exp": 80, "drops": ["Drachenzahn", "Drachenschuppe", "Großer Feuertrank"]
        },
#--------------#
# Boss Monster #
#--------------#
        "Uralter Drache": {
            "base_health": 250, "base_attack": 30, "base_defense": 20, "base_speed": 6,
            "base_exp": 200,
            "drops": ["Drachenzahnklinge", "Drachenschuppenrüstung", "Großer Heiltrank"]
        },
        
    }

#------------------------#
# Zufälliger Monster-Typ #
#------------------------#
    def __init__(self, player_level, drop_rate=0.3):
        self.type_name = random.choice(list(self.MONSTER_TYPES.keys()))
        base = self.MONSTER_TYPES[self.type_name]

#-------------------------------------#
# Level basierend auf Spielerlevel ±5 #
#-------------------------------------#
        self.level = max(1, player_level + random.choice([-3, -1, 0, 1]))

#----------------------------------------------------------------#
# Stats zufällig mit kleinen Schwankungen + Skalierung pro Level #
#----------------------------------------------------------------#
        self.health = random.randint(base["base_health"], base["base_health"] + 10) + (self.level - 1) * 10
        self.attack = random.randint(base["base_attack"], base["base_attack"] + 3) + (self.level - 1) * 2
        self.defense = random.randint(base["base_defense"], base["base_defense"] + 2) + (self.level - 1)
        self.speed = random.randint(base["base_speed"], base["base_speed"] + 2) + (self.level - 1)

#---------------------------------------------------#
# EXP-Belohnung dynamisch skalieren (10% pro Level) #
#---------------------------------------------------#
        base_exp = base.get("base_exp", 10)
        self.exp_reward = int(base_exp * (1 + 0.2 * (self.level - 1)))

#--------------#
# Drops-System #
#--------------#
        self.drop_rate = drop_rate
        self.loot_table = base.get("drops", ["Nichts"])
        self.dropped_items = []
        
# --------------#
# Status prüfen #
# --------------#
    def is_alive(self):
        return self.health > 0

#----------------#
# Schaden nehmen #
#----------------#
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.type_name} nimmt {amount} Schaden! HP: {self.health}")

#-----------#
# Angreifen #
#-----------#
    def attack_target(self, target):
        damage = self.attack + random.randint(0, 5)
        print(f"{self.type_name} greift {target.name} an und verursacht {damage} Schaden!")
        target.take_damage(damage)

#----------------------#
# Drop Items berechnen #
#----------------------#
    #----------------------#
    # Drop Items berechnen #
    #----------------------#
    def drop_item(self):
        if random.random() > self.drop_rate:
            return None

        rarities = list(DROP_RATE.keys())
        weights = [DROP_RATE[r] for r in rarities]
        rarity = random.choices(rarities, weights=weights)[0]

        candidates = []
        for category, enemy_map in Items.get(rarity, {}).items():
            candidates.extend(enemy_map.get(self.type_name, []))

        if not candidates:
            candidates = self.loot_table

        if not candidates:
            return None

        item = random.choice(candidates)
        self.dropped_items.append(item)
        print(f"{self.type_name} droppt: {item}")
        return item

#-------------------#
# Anzeige der Stats #
#-------------------#
    def show_info(self):
        print(f"--- {self.type_name} (Level {self.level}) ---")
        print(f"HP: {self.health} | ATK: {self.attack} | DEF: {self.defense} | SPD: {self.speed}")
        print(f"EXP-Belohnung: {self.exp_reward} | Drop-Rate: {self.drop_rate*100:.0f}%")
        print("---------------------------\n")
        
#-----------------------#
# TEST / SPAWN BEISPIEL #
#-----------------------#
if __name__ == "__main__":
    player_level = 1  # Beispielcharakterlevel
    
#---------------------------#
# Zufällige Gegner erzeugen #
#---------------------------#
    enemies = [Enemy(player_level, drop_rate=0.3) for _ in range(5)]

    for e in enemies:
        e.show_info()

    # Beispielkampf: Jeder Gegner droppt Items
    for e in enemies:
        e.drop_item()

