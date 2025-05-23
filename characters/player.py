from characters.character import Character
from items.items import ITEMS


class Player(Character):
    def __init__(self, name: str, max_hp: int, rolls_per_turn: int):
        super().__init__(name, max_hp, rolls_per_turn)
        self.inventory: list[str] = []

    def add_item(self, item_name: str) -> None:
        if item_name in ITEMS:
            self.inventory.append(item_name)
        else:
            print(f"{item_name} não encontrado na lista de itens")

    def has_item(self, item_name: str) -> bool:
        return item_name in self.inventory

    def remove_item(self, item_name: str) -> None:
        if item_name in self.inventory:
            self.inventory.remove(item_name)

    def get_current_rolls_per_turn(self) -> int:
        base_rolls = self.rolls_per_turn

        if self.has_item("Espada ZG"):
            return ITEMS["Espada ZG"]["rolls_bonus"]

        if self.has_item("Azah Transmissão"):
            base_rolls = max(
                base_rolls, ITEMS["Azah Transmissão"]["rolls_bonus"])

        if self.has_item("Faturamentus"):
            base_rolls = max(base_rolls, ITEMS["Faturamentus"]["rolls_bonus"])

        return base_rolls
