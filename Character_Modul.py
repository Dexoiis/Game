from Quest_Modul import QuestManager

#------------------#
# Character Module #
#------------------#

class Character:
    def __init__(self, name, race, char_class):
#Hauptwerte
        self.name = name 				# Name
        self.race = race 				# Rasse
        self.char_class = char_class 	# Klasse
        self.level = 1 					# Level
        self.xp = 0 					# Erfahrungspunkte
        self.xp_to_next = 10 			# Startwert für lvl-UP

#Hauptwerte
        self.health = 120 				# HP
        self.strength = 10 				# STR
        self.mana = 60 					# MP
        self.dexterity = 10 			# Geschick.
        self.intelligence = 10 			# INT.

#Kampfwerte
        self.attack = 10				# Basis-Angriff
        self.defense = 8				# Physische Verteidigung
        self.magic_defense = 5			# Magische Verteidigung
        self.speed = 10					# Geschwindigkeit / Zugreihenfolge
        self.crit_chance = 5			# Chance auf Krit. Treffer (%)
        self.evasion = 8				# Ausweichchance (%)
        self.accuracy = 90				# Trefferchance (%)

#Sekundärwerte
        self.luck = 5					# Glück (Krit, Drops, Zufall)
        self.resistance = 5				# Widerstand gg. Status-Effekte

#--------------------------------------------------#
# Fähigkeitenliste wird durch klassen wahl befüllt #
#--------------------------------------------------#
        self.abilities = []
        self.ability_cooldowns = {}
        
        self.bonus_health = 0
        self.bonus_strength = 0
        self.bonus_mana = 0
        self.bonus_dexterity = 0
        self.bonus_intelligence = 0
        
        self.draken = getattr(self, "draken", 0)
        
        self.equipped = getattr(self, "equipped", {
            "waffe": None, "helm": None, "brust": None, "hose": None,
            "schuhe": None, "amulett": None, "ring1": None, "ring2": None
        })
        
        self.equip_bonus_totals = getattr(self, "equip_bonus_totals",
                                          {"attack": 0, "defense": 0, "strength": 0, "max_health": 0 })
        self.active_set_bonuses = getattr(self, "active_set_bonuses",
                                          {"attack": 0, "defense": 0, "strength": 0, "max_health": 0 })

        self.quest_manager = getattr(self, "quest_manager", QuestManager())
        
#------------------------------------#
# Werte die bei einem lvl-UP steigen #
#------------------------------------#

# Berechnet die max. Gesundheit anhand vom lvl.
    def max_health(self):
        hp_bonus = 0
        hp_bonus += self.equip_bonus_totals.get("max_health", 0)
        hp_bonus += self.active_set_bonuses.get("max_health", 0)
        return 120 + (self.level - 1) * 15 + self.bonus_health + hp_bonus

# Berechnet die max. Stärke anhand vom lvl.
    def max_strength(self):
        return 10 + (self.level  - 1) * 2 + self.bonus_strength
    
# Berechnet das max. Mana abhängig vom lvl.      
    def max_mana(self):
        return 60 + int((self.level - 1)   * 5) + self.bonus_mana

# Berechnet die max. Geschick. anhand vom lvl.
    def max_dexterity(self):
        return 10 + (self.level - 1) * 2 + self.bonus_dexterity
    
# Berechnet die max. Intelligenz anhand vom lvl.
    def max_intelligence(self):
        return 10 + (self.level - 1) * 2 + self.bonus_intelligence
    
#-------------------------------------#       
# Zeigt die Charakterinformationen an #
#-------------------------------------#
    def show_info(self):
        print("=== Charakter Info ===")
        print(f"Name: {self.name}")
        print(f"Rasse: {self.race}")
        print(f"Klasse: {self.char_class}")
        print(f"Level: {self.level}")
        print(f"Erfahrungspunkte: {self.xp}/{self.xp_to_next}")
        print(f"Gesundheit: {self.health}/{self.max_health()}")
        print(f"Mana: {self.mana}")
        print(f"Stärke: {self.strength}")
        print(f"Geschick: {self.dexterity}")
        print(f"Intelligenz: {self.intelligence}")
        print(f"Angriff: {self.attack} | Verteidigung: {self.defense} | Mag. Verteidigung: {self.magic_defense}")
        print(f"Speed: {self.speed} | Crit: {self.crit_chance}% | Ausweichen: {self.evasion}% | Genauigkeit: {self.accuracy}%")
        print(f"Glück: {self.luck} | Widerstand: {self.resistance}")
        print(f"Draken: {self.draken}")
        if self.abilities:
            print(f"Fähigkeiten: {', '.join(self.abilities)}")
        print("=========================================================\n")

#-------------------------------------#
# Zeigt die Ausrüstungsgegenstände an #
#-------------------------------------#
    def show_equipment(self):
        def fmt(x):
            return f"{x['name']} ({x['rarity']})" if x else "—"
        print("=== Ausrüstung ===")
        print(f"Waffe : {fmt(self.equipped.get('waffe'))}")
        print(f"Helm  : {fmt(self.equipped.get('helm'))}")
        print(f"Brust : {fmt(self.equipped.get('brust'))}")
        print(f"Hose  : {fmt(self.equipped.get('hose'))}")
        print(f"Schuhe: {fmt(self.equipped.get('schuhe'))}")
        print(f"Amulett: {fmt(self.equipped.get('amulett'))}")
        print(f"Ring1 : {fmt(self.equipped.get('ring1'))}")
        print(f"Ring2 : {fmt(self.equipped.get('ring2'))}")
        print("==================\n")
            
#-------------------------------------------------#
# Erhöht das Level und verbessert die Werte/Level #
#-------------------------------------------------#

#Nächstes level braucht doppelt so viel xp
    def level_up(self):
        self.level += 1
        self.xp_to_next *= 2 
        
#Hauptwerte Skalieren    
        self.health = self.max_health()  
        self.mana = self.max_mana() 
        self.strength = self.max_strength() 
        self.dexterity = self.max_dexterity() 
        self.intelligence= self.max_intelligence()
        self.strength= self.max_strength()
        
        self._reapply_equip_and_set_bonuses_after_base_reset()
        
#-----------------------------------------------------#
# Fügt Erfahrungspunkte hinzu und prüft Levelaufstieg #
#-----------------------------------------------------#
    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} erhält {amount} Erfahrungspunkte. ({self.xp}/{self.xp_to_next})")
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()
            
#----------------------------------------#       
# Gesundheit verändern (Schaden/Heilung) #
#----------------------------------------#
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} hat {amount} Schaden genommen. Gesundheit: {self.health}/{self.max_health()}")

    def heal(self, amount):
        """Heilt den Charakter um einen bestimmten Wert."""
        self.health += amount
        if self.health > self.max_health():
            self.health = self.max_health()
        print(f"{self.name} wurde um {amount} geheilt. Gesundheit: {self.health}/{self.max_health()}")

    def reduce_cooldowns(self):
        """Senkt alle aktiven Fähigkeits-Cooldowns um 1."""
        for ab in list(self.ability_cooldowns.keys()):
            if self.ability_cooldowns[ab] > 0:
                self.ability_cooldowns[ab] -= 1

    def _reapply_equip_and_set_bonuses_after_base_reset(self):
        eq = getattr(self, "equip_bonus_totals", {})
        for stat in ("attack", "defense", "strength"):
            self.__dict__[stat] = self.__dict__.get(stat, 0) + int(eq.get(stat, 0))
       
        sb = getattr(self, "active_set_bonuses", {})
        for stat in ("attack", "defense", "strength"):
            self.__dict__[stat] = self.__dict__.get(stat, 0) + int(sb.get(stat, 0))

#------------------------------------------#
# Sicherheit Aktuelle HP nicht über Max HP #
#------------------------------------------#

        if self.health > self.max_health():
            self.health = self.max_health()
            
    @property
    def gold(self):
        return self.draken
    @gold.setter
    def gold(self, value):
        self.draken = int(value)

#--------------#
# Testfunktion #
#--------------#
def test_character():
    hero = Character("Arthas", "Mensch", "Krieger")

# Startwerte anzeigen
    hero.show_info()

# sollte ein Level-Up auslösen
    hero.gain_xp(10)  
    hero.show_info()

# Schaden nehmen
    hero.take_damage(15)

# Heilung testen
    hero.heal(20)

# Mehr XP für weiteres Level-Up (z. B. 35)
    hero.gain_xp(20)
    hero.show_info()


# Test ausführen
if __name__ == "__main__":
    test_character()

    
