# inventory_module.py

from Item_Modul import Items

class InventoryItem:
    def __init__(self, name, category, rarity="gewöhnlich", quantity=1, stackable=True, max_stack=99):
        self.name = name
        self.category = category
        self.rarity = rarity
        self.quantity = quantity
        self.stackable = stackable
        self.max_stack = max_stack

    def use(self, player):
        if self.category == "trank":
            print(f"{player.name} benutzt {self.name}!")
            if "Heil" in self.name:
                player.heal(20)
            elif "Mana" in self.name:
                print(f"{player.name} stellt 20 Mana wieder her!")
            self.quantity -= 1
            return self.quantity <= 0
        else:
            print(f"{self.name} kann nicht benutzt werden.")
            return False

    def __str__(self):
        return f"{self.name} (x{self.quantity}) - {self.category} [{self.rarity}]"


class Inventory:
    def __init__(self, max_slots=30):
        self.max_slots = max_slots
        self.items = []

    def find_category(self, name, rarity):
        """Sucht die Kategorie eines Items im Items-Dictionary."""
        if rarity not in Items:
            return "sonstiges"

        for category, monsters in Items[rarity].items():
            for monster, loot in monsters.items():
                if name in loot:
                    return category
        return "sonstiges"

    def add_item(self, name, rarity="gewöhnlich", quantity=1):
        """Item hinzufügen: Name + Rarität reichen, Kategorie wird automatisch gefunden."""
        category = self.find_category(name, rarity)

        # Stack-Regeln (z. B. Tränke und Münzen stacken)
        stackable = category in ["trank", "sonstiges"]

        for inv_item in self.items:
            if inv_item.name == name and inv_item.rarity == rarity:
                if inv_item.quantity + quantity <= inv_item.max_stack:
                    inv_item.quantity += quantity
                    return True

        if len(self.items) < self.max_slots:
            self.items.append(InventoryItem(name, category, rarity, quantity, stackable))
            return True
        else:
            print("Inventar ist voll!")
            return False

    def remove_item(self, name, quantity=1):
        for inv_item in self.items:
            if inv_item.name == name:
                inv_item.quantity -= quantity
                if inv_item.quantity <= 0:
                    self.items.remove(inv_item)
                return True
        print(f"{name} nicht im Inventar.")
        return False

    def use_item(self, name, player):
        for inv_item in self.items:
            if inv_item.name == name:
                if inv_item.use(player):
                    self.items.remove(inv_item)
                return True
        print(f"{name} nicht gefunden.")
        return False

    def show_inventory(self, filter_category=None, filter_rarity=None):
        print("\n--- Inventar ---")
        if not self.items:
            print("Leer.")
            return
        for item in sorted(self.items, key=lambda i: i.name):
            if (filter_category is None or item.category == filter_category) and \
               (filter_rarity is None or item.rarity == filter_rarity):
                print(item)
        print("----------------\n")

    def expand_slots(self, amount):
        self.max_slots += amount
        print(f"Inventar erweitert! Neue Slots: {self.max_slots}")
