class Item:
    def __init__(self, name, item_type, bonuses=None, price=0, effect=None):
        self.name = name
        self.item_type = item_type  # weapon, armor, consumable
        self.bonuses = bonuses or {}
        self.price = price
        self.effect = effect  # e.g., ('heal', 20)

    def __str__(self):
        return self.name


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def list_items(self):
        if not self.items:
            print('(leer)')
            return
        for i, item in enumerate(self.items, 1):
            print(f"{i}) {item.name}")


class Player:
    def __init__(self, name, strength=10, defense=5, max_health=100, max_mana=50):
        self.name = name
        self.base_strength = strength
        self.base_defense = defense
        self.base_max_health = max_health
        self.base_max_mana = max_mana
        self.strength = strength
        self.defense = defense
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        self.gold = 0
        self.inventory = Inventory()
        self.equipped = {'weapon': None, 'armor': None}

    def show_stats(self):
        print('=== Spieler ===')
        print(f'Name: {self.name}')
        print(f'Gold: {self.gold}')
        print(f'Stärke: {self.strength}')
        print(f'Verteidigung: {self.defense}')
        print(f'Leben: {self.health}/{self.max_health}')
        print(f'Mana: {self.mana}/{self.max_mana}')
        wpn = self.equipped['weapon'].name if self.equipped['weapon'] else '-'
        arm = self.equipped['armor'].name if self.equipped['armor'] else '-'
        print(f'Waffe: {wpn}')
        print(f'Rüstung: {arm}')
        print('================\n')

    def _apply_item_bonuses(self, item, remove=False):
        factor = -1 if remove else 1
        for stat, bonus in item.bonuses.items():
            if stat == 'strength':
                self.strength += factor * bonus
            elif stat == 'defense':
                self.defense += factor * bonus
            elif stat == 'max_health':
                self.max_health += factor * bonus
                self.health = min(self.health, self.max_health)
            elif stat == 'max_mana':
                self.max_mana += factor * bonus
                self.mana = min(self.mana, self.max_mana)

    def equip(self, item):
        slot = item.item_type
        if slot not in ('weapon', 'armor'):
            print('Nicht ausrüstbar.')
            return
        old = self.equipped.get(slot)
        if old:
            self._apply_item_bonuses(old, remove=True)
            self.inventory.add_item(old)
        self._apply_item_bonuses(item)
        self.equipped[slot] = item
        print(f'{item.name} ausgerüstet.')

    def use(self, item):
        if item.item_type != 'consumable':
            print('Nicht benutzbar.')
            return False
        if not item.effect:
            return False
        kind, amount = item.effect
        if kind == 'heal':
            before = self.health
            self.health = min(self.max_health, self.health + amount)
            print(f'{self.name} heilt {self.health - before} HP.')
        elif kind == 'mana':
            before = self.mana
            self.mana = min(self.max_mana, self.mana + amount)
            print(f'{self.name} stellt {self.mana - before} Mana wieder her.')
        return True

    def sell(self, item):
        self.gold += item.price
        print(f'{item.name} verkauft für {item.price} Gold.')


def inventory_menu(player):
    inv = player.inventory
    while True:
        print('\n=== Inventar ===')
        inv.list_items()
        print("Wähle eine Nummer oder 'z' zum Schließen.")
        choice = input('> ').strip().lower()
        if choice == 'z':
            break
        if not choice.isdigit():
            continue
        idx = int(choice) - 1
        if idx < 0 or idx >= len(inv.items):
            continue
        item = inv.items[idx]
        print(f'Ausgewählt: {item.name}')
        options = []
        if item.item_type in ('weapon', 'armor'):
            options.append('a) Ausrüsten')
        if item.item_type == 'consumable':
            options.append('b) Benutzen')
        options.append('v) Verkaufen')
        options.append('z) Zurück')
        print(' | '.join(options))
        action = input('> ').strip().lower()
        if action == 'a' and item.item_type in ('weapon', 'armor'):
            inv.remove_item(item)
            player.equip(item)
        elif action == 'b' and item.item_type == 'consumable':
            if player.use(item):
                inv.remove_item(item)
        elif action == 'v':
            inv.remove_item(item)
            player.sell(item)
        # 'z' oder andere Eingaben: zurück zur Item-Liste


def main():
    player = Player('Held')
    inv = player.inventory
    inv.add_item(Item('Schwert', 'weapon', {'strength': 5}, price=10))
    inv.add_item(Item('Rüstung', 'armor', {'defense': 3}, price=8))
    inv.add_item(Item('Heiltrank', 'consumable', price=5, effect=('heal', 30)))
    inv.add_item(Item('Manatrank', 'consumable', price=5, effect=('mana', 20)))

    print('Steuerung: [i] Inventar, [s] Stats, [q] Beenden')
    while True:
        cmd = input('> ').strip().lower()
        if cmd == 'i':
            inventory_menu(player)
        elif cmd == 's':
            player.show_stats()
        elif cmd == 'q':
            break


if __name__ == '__main__':
    main()