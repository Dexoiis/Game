#------------------#
# Ability Modul    #
#------------------#
"""Enthält die Definition von Fähigkeiten/Zaubern und eine
Hilfsfunktion, um diese anzuwenden."""

from typing import Optional

# Alle verfügbaren Fähigkeiten mit Basiswerten
ABILITIES = {
    # Krieger
    "Schwerthieb": {"damage": 15, "mana": 5},
    "Schildblock": {"defense": 10, "mana": 4},
    # Magier
    "Feuerball": {"damage": 25, "mana": 10},
    "Heilen": {"heal": 20, "mana": 8},
    # Dieb
    "Meucheln": {"damage": 20, "mana": 6},
    "Ausweichen": {"defense": 15, "mana": 6},
    # Paladin
    "G\u00f6ttlicher Schlag": {"damage": 30, "mana": 12},
    "Heilige Aura": {"heal": 25, "defense": 5, "mana": 10},
    # Hexenmeister
    "Arkaner Strahl": {"damage": 28, "mana": 10},
    "Dunkles Opfer": {"damage": 15, "heal": 10, "mana": 12},
    # Druide
    "Wurzelbann": {"damage": 18, "mana": 8},
    "Tiergestalt": {"defense": 12, "mana": 9},
    # Nekromant
    "Skelettdiener": {"damage": 22, "mana": 12},
    "Lebensraub": {"damage": 12, "heal": 12, "mana": 10},
    # Assassine
    "Todessto\u00df": {"damage": 35, "mana": 15},
    "Rauchbombe": {"defense": 20, "mana": 10},
    # Alchemist
    "Sprengflasche": {"damage": 18, "mana": 8},
    "Heiltrank": {"heal": 20, "mana": 5},
}


def use_ability(user, ability_name: str, target: Optional[object] = None) -> int:
    """Wendet eine F\u00e4higkeit an.

    Parameters
    ----------
    user : object
        Anwender der F\u00e4higkeit (ben\u00f6tigt Attribute `mana`, `defense`,
        `intelligence` sowie Methoden `heal` und `take_damage`).
    ability_name : str
        Name der F\u00e4higkeit.
    target : object, optional
        Ziel f\u00fcr Schadenszauber.

    Returns
    -------
    int
        Ein eventueller tempor\u00e4rer Verteidigungsbonus, der vom Aufrufer
        wieder entfernt werden muss. Gibt 0 zur\u00fcck, wenn kein Bonus
        angewendet wurde oder der Zauber fehlschl\u00e4gt.
    """

    spell = ABILITIES.get(ability_name)
    if not spell:
        print("Unbekannte F\u00e4higkeit!")
        return 0

    cost = spell.get("mana", 0)
    if user.mana < cost:
        print(f"{user.name} hat nicht genug Mana!")
        return 0

    user.mana -= cost
    damage = spell.get("damage", 0)
    heal = spell.get("heal", 0)
    defense = spell.get("defense", 0)

    if damage and target is not None:
        total_damage = max(0, damage + getattr(user, "intelligence", 0) - getattr(target, "magic_defense", 0))
        print(f"{user.name} nutzt {ability_name} und verursacht {total_damage} Schaden!")
        target.take_damage(total_damage)

    if heal:
        print(f"{user.name} nutzt {ability_name} und heilt {heal} HP!")
        user.heal(heal)

    if defense:
        user.defense += defense
        print(f"{user.name}s Verteidigung erh\u00f6ht sich um {defense}!")
        return defense

    return 0