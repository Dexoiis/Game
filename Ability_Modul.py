#------------------#
# Ability Modul    #
#------------------#
"""Enthält die Definition von Fähigkeiten/Zaubern und eine
Hilfsfunktion, um diese anzuwenden."""

from typing import Optional

# Alle verfügbaren Fähigkeiten mit Basiswerten
ABILITIES = {
    # Krieger
    "Schwerthieb": {"damage": 15, "mana": 5, "cooldown": 1, "scale": "strength"},
    "Schildblock": {"defense": 10, "mana": 4, "cooldown": 2, "scale": "strength"},
    # Magier
    "Feuerball": {"damage": 25, "mana": 10, "cooldown": 2, "scale": "intelligence"},
    "Heilen": {"heal": 20, "mana": 8, "cooldown": 3, "scale": "intelligence"},
    # Dieb
    "Meucheln": {"damage": 20, "mana": 6, "cooldown": 2, "scale": "dexterity"},
    "Ausweichen": {"defense": 15, "mana": 6, "cooldown": 3, "scale": "dexterity"},
    # Paladin
    "Göttlicher Schlag": {"damage": 30, "mana": 12, "cooldown": 3, "scale": "strength"},
    "Heilige Aura": {"heal": 25, "defense": 5, "mana": 10, "cooldown": 4, "scale": "intelligence"},
    # Hexenmeister
    "Arkaner Strahl": {"damage": 28, "mana": 10, "cooldown": 2, "scale": "intelligence"},
    "Dunkles Opfer": {"damage": 15, "heal": 10, "mana": 12, "cooldown": 4, "scale": "intelligence"},
    # Druide
    "Wurzelbann": {"damage": 18, "mana": 8, "cooldown": 2, "scale": "intelligence"},
    "Tiergestalt": {"defense": 12, "mana": 9, "cooldown": 3, "scale": "strength"},
    # Nekromant
    "Skelettdiener": {"damage": 22, "mana": 12, "cooldown": 3, "scale": "intelligence"},
    "Lebensraub": {"damage": 12, "heal": 12, "mana": 10, "cooldown": 3, "scale": "intelligence"},
    # Assassine
    "Todesstoß": {"damage": 35, "mana": 15, "cooldown": 4, "scale": "dexterity"},
    "Rauchbombe": {"defense": 20, "mana": 10, "cooldown": 3, "scale": "dexterity"},
    # Alchemist
    "Sprengflasche": {"damage": 18, "mana": 8, "cooldown": 2, "scale": "intelligence"},
    "Heiltrank": {"heal": 20, "mana": 5, "cooldown": 2, "scale": "intelligence"},
}


def register_ability(name: str, attributs: dict) -> None:
    """Registriert eine neue Fähigkeit.

    Parameters
    ----------
    name : str
        Bezeichnung der Fähigkeit.
    attributs : dict
        Werte der Fähigkeit (z.B. Schaden, Mana-Kosten, Cooldown).
    """

    ABILITIES[name] = attributs


def use_ability(user, ability_name: str, target: Optional[object] = None) -> int:
    """Wendet eine Fähigkeit an.

    Parameters
    ----------
    user : object
        Anwender der Fähigkeit (benötigt Attribute `mana`, `defense`,
        `intelligence` sowie Methoden `heal` und `take_damage`).
    ability_name : str
        Name der Fähigkeit.
    target : object, optional
        Ziel für Schadenszauber.

    Returns
    -------
    int
        Ein eventueller temporärer Verteidigungsbonus, der vom Aufrufer
        wieder entfernt werden muss. Gibt 0 zurück, wenn kein Bonus
        angewendet wurde oder der Zauber fehlschlägt.
    """

    spell = ABILITIES.get(ability_name)
    if not spell:
        print("Unbekannte Fähigkeit!")
        return 0

    cooldowns = getattr(user, "ability_cooldowns", {})
    if cooldowns.get(ability_name, 0) > 0:
        print(f"{ability_name} ist noch {cooldowns[ability_name]} Runde(n) auf Cooldown!")
        return 0

    cost = spell.get("mana", 0)
    if user.mana < cost:
        print(f"{user.name} hat nicht genug Mana!")
        return 0

    user.mana -= cost

    damage = spell.get("damage", 0)
    heal = spell.get("heal", 0)
    defense = spell.get("defense", 0)

    scale_attr = spell.get("scale")
    scale_value = getattr(user, scale_attr, 0) // 2 if scale_attr else 0

    if damage:
        damage += scale_value
    if heal:
        heal += scale_value
    if defense:
        defense += scale_value

    if damage and target is not None:
        total_damage = max(0, damage - getattr(target, "magic_defense", 0))
        print(f"{user.name} nutzt {ability_name} und verursacht {total_damage} Schaden!")
        target.take_damage(total_damage)

    if heal:
        print(f"{user.name} nutzt {ability_name} und heilt {heal} HP!")
        user.heal(heal)

    bonus = 0
    if defense:
        user.defense += defense
        print(f"{user.name}s Verteidigung erhöht sich um {defense}!")
        bonus = defense

    cooldowns[ability_name] = spell.get("cooldown", 0)


    return bonus
