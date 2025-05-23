import os
import time

from constants.constants import DIALOGUE_DELAY


def clear_screen():
    os.system("clear")


def dialogue(speaker: str, text: str, delay: float = DIALOGUE_DELAY):
    print(f"\n{speaker}: ", end="")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    input("\nPressione Enter para continuar...")
