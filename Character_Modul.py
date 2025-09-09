#--------------------#
# Character_Modul.py #
#--------------------#

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from Inventory_Modul import Inventory

@dataclass
class Character:
    name: str
    race: str
    char_class: str

    # Basiswerte
    level: int = 1
    xp: int = 0
    xp_to_next: int = 10

    health: int = 120
    mana: int = 60
    strength: int = 10
    dexterity: int = 10
    intelligence: int = 10

    attack: int = 5
    defense: int = 3
    magic_defense: int = 2
    speed: int = 5

    crit_chance: int = 5
    evasion: int = 3
    accuracy: int = 90
    luck: int = 1
    resistance: int = 0

    # ökonomisch
    draken: int = 0

    # Fortschritt/Skills
    abilities: List[str] = field(default_factory=list)

    # Ausrüstung
    equipped: Dict[str, Optional[Dict]] = field(default_factory=lambda: {
        "waffe": None, "helm": None, "brust": None, "hose": None,
        "schuhe": None, "amulett": None, "ring1": None, "ring2": None
    })
    equip_bonus_totals: Dict[str, int] = field(default_factory=lambda: {
        "attack": 0, "defense": 0, "strength": 0, "max_health": 0
    })
    active_set_bonuses: Dict[str, int] = field(default_factory=lambda: {
        "attack": 0, "defense": 0, "strength": 0, "max_health": 0
    })

    # Bonus-Pools (z. B. durch Rasse/Klasse)
    bonus_health: int = 0
    bonus_strength: int = 0
    bonus_mana: int = 0
    bonus_dexterity: int = 0
    bonus_intelligence: int = 0

    # Inventar
    inventory: Inventory = field(default_factory=Inventory)

    # ---------- abgeleitete Max-Werte ----------
    def max_health(self) -> int:
        hp_bonus = self.equip_bonus_totals.get("max_health", 0) + self.active_set_bonuses.get("max_health", 0)
        return 120 + (self.level - 1) * 15 + self.bonus_health + hp_bonus

    def max_strength(self) -> int:
        return 10 + (self.level - 1) * 2 + self.bonus_strength

    def max_mana(self) -> int:
        return 60 + int((self.level - 1) * 5) + self.bonus_mana

    def max_dexterity(self) -> int:
        return 10 + (self.level - 1) * 2 + self.bonus_dexterity

    def max_intelligence(self) -> int:
        return 10 + (self.level - 1) * 2 + self.bonus_intelligence

    # ---------- Anzeige ----------
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
        print("=========================================================")
        print()

    def show_equipment(self):
        def fmt(x):
            return f"{x['name']} ({x.get('rarity','?')})" if x else "—"
        print("=== Ausrüstung ===")
        print(f"Waffe : {fmt(self.equipped.get('waffe'))}")
        print(f"Helm  : {fmt(self.equipped.get('helm'))}")
        print(f"Brust : {fmt(self.equipped.get('brust'))}")
        print(f"Hose  : {fmt(self.equipped.get('hose'))}")
        print(f"Schuhe: {fmt(self.equipped.get('schuhe'))}")
        print(f"Amulett: {fmt(self.equipped.get('amulett'))}")
        print(f"Ring1 : {fmt(self.equipped.get('ring1'))}")
        print(f"Ring2 : {fmt(self.equipped.get('ring2'))}")
        print("==================")
        print()

    # ---------- Fortschritt ----------
    def level_up(self):
        self.level += 1
        self.xp_to_next *= 2
        self.health = self.max_health()
        self.mana = self.max_mana()
        self.strength = self.max_strength()
        self.dexterity = self.max_dexterity()
        self.intelligence = self.max_intelligence()
        self._reapply_equip_and_set_bonuses_after_base_reset()

    def gain_xp(self, amount: int):
        self.xp += amount
        print(f"{self.name} erhält {amount} Erfahrungspunkte. ({self.xp}/{self.xp_to_next})")
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()

    # ---------- Kampf ----------
    def take_damage(self, amount: int):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} hat {amount} Schaden genommen. Gesundheit: {self.health}/{self.max_health()}")

    def heal(self, amount: int):
        self.health += amount
        if self.health > self.max_health():
            self.health = self.max_health()
        print(f"{self.name} wurde um {amount} geheilt. Gesundheit: {self.health}/{self.max_health()}")

    # ---------- Equip-Boni anwenden ----------
    def _reapply_equip_and_set_bonuses_after_base_reset(self):
        eq = getattr(self, "equip_bonus_totals", {})
        for stat in ("attack", "defense", "strength"):
            self.__dict__[stat] = int(self.__dict__.get(stat, 0)) + int(eq.get(stat, 0))

        sb = getattr(self, "active_set_bonuses", {})
        for stat in ("attack", "defense", "strength"):
            self.__dict__[stat] = int(self.__dict__.get(stat, 0)) + int(sb.get(stat, 0))

        if self.health > self.max_health():
            self.health = self.max_health()

    # Alias für Draken
    @property
    def gold(self) -> int:
        return self.draken

    @gold.setter
    def gold(self, value: int):
        self.draken = int(value)
