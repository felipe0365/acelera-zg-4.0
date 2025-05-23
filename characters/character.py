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

    def set_secret_number(self, max_value: int) -> None:
        self.secret_number = random.randint(1, max_value)

    def roll_dice(self, num_rolls: int, max_value: int) -> list[int]:
        rolls = [random.randint(1, max_value) for _ in range(num_rolls)]
        return rolls

    def calculate_damage_taken_from_self_rolls(self, rolls_made: list[int]) -> int:
        damage_count = rolls_made.count(self.secret_number)
        return self.secret_number * damage_count
