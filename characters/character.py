import random


class Character:
    def __init__(self, name: str, max_hp: int, rolls_per_turn: int):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.secret_number = 0
        self.rolls_per_turn = rolls_per_turn

    def take_damage(self, amount: int) -> None:
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def set_secret_number(self) -> None:
        self.secret_number = random.randint(1, self.max_hp)

    def roll_dice(self, num_rolls: int, max_value: int) -> list[int]:
        rolls = [random.randint(1, max_value) for _ in range(num_rolls)]
        return rolls

    def calculate_damage_dealt(self, defender_secret_number: int, rolls_made: list[int]) -> int:
        damage_count = rolls_made.count(defender_secret_number)

        if damage_count > 0:
            return defender_secret_number * damage_count
        return 0
