from characters.player import Player
from characters.monster import Monster
from items.items import ITEMS
from utils.utils import clear_screen, dialogue
from constants.constants import HP_GAIN_VICTORY


def handle_battle(player: Player, monster: Monster) -> str:
    dialogue("Narrador",
             f"Uma batalha sangreta ocorre entre{player.name} e {monster.name}")

    player.set_secret_number()
    monster.set_secret_number()

    print(f"NÚMEROS SECRETOS---------------")
    print(f"{player.name}: {player.secret_number}")
    print(f"{monster.name}: {monster.secret_number}")
    print("--------------------------------")

    monster_damage_bonus_to_player = 0
    player_damage_taken_from_azah_consequence = 0

    while player.is_alive() and monster.is_alive():
        print("\n--- Nova Rodada ---")
        print(f"{player.name}: {player.current_hp}/{player.max_hp} de vida")
        print(f"{monster.name}: {monster.current_hp}/{monster.max_hp} de vida")

        print(f"\n--- Turno de {player.name} ---")

        if player.has_item("Colar da estátua sagrada") and not player.has_item("Espada ZG"):
            player.take_damage(3)
            dialogue(
                "Narrador", f"{player.name} perdeu 3 de vida ao Colar da Estátua Sagrada! Vida atual: {player.current_hp}")
            if not player.is_alive():
                break

        player_rolls_per_turn = player.get_current_rolls_per_turn()

        print("    " + player.name + " sorteia: ", end='')
        player_rolls = player.roll_dice(
            player_rolls_per_turn, monster.max_hp)

        damage_deal_by_player = player.calculate_damage_dealt(
            monster.secret_number, player_rolls)

        if damage_deal_by_player > 0:
            monster.take_damage(damage_deal_by_player)
            dialogue(
                "Narrador", f"Houve dano! {player.name} Causa {damage_deal_by_player} de dano a {monster.name}! Vida atual de {monster.name}: {monster.current_hp}")
        else:
            dialogue("Narrador", f"Não houve dano para {monster.name}")

        # Faturamentus
        if player.has_item("Faturamentus") and monster.secret_number not in player_rolls:
            monster_damage_bonus_to_player = 2
            dialogue(
                "Narrador", f"Consequência de Faturamentus ativada! O próximo ataque de {monster.name} causará +{monster_damage_bonus_to_player} de dano em {player.name}")
        else:
            monster_damage_bonus_to_player = 0

        # Azah
        if player.has_item("Azah Transmissão") and damage_deal_by_player == 0:
            player_damage_taken_from_azah_consequence = 3
            player.take_damage(player_damage_taken_from_azah_consequence)
            dialogue(
                "Narrador", f"Consequência de Azah Transmissão ativada! {player.name} errou e perdeu {player_damage_taken_from_azah_consequence} de vida. Vida atual: {player.current_hp}")
        else:
            player_damage_taken_from_azah_consequence = 0

        if not player.is_alive():
            break

        print(f"\n--- Turno de {monster.name} ---")

        print("    " + monster.name + " sorteia: ", end='')
        monster_rolls = monster.roll_dice(
            monster.rolls_per_turn, player.current_hp)

        damage_deal_by_moster = monster.calculate_damage_dealt(
            player.secret_number, monster_rolls)

        damage_deal_by_moster += monster_damage_bonus_to_player

        if damage_deal_by_moster > 0:
            player.take_damage(damage_deal_by_moster)
            dialogue(
                "Narrador", f"Houve dano! {monster.name} Causa {damage_deal_by_moster} de dano a {player.name}! Vida de {player.name}: {player.current_hp}")
        else:
            dialogue("Narrador", f"Não houve dano para {player.name}")

        if not player.is_alive():
            break
