from characters.character import Character


class Monster(Character):
    def __init__(self, name, max_hp, rolls_per_turn):
        super().__init__(name, max_hp, rolls_per_turn)
