# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
BLACK = "\033[30m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BG_BLACK = "\033[40m"
RESET = "\033[0m"

def start():
    print(f"You are in the woods. Do you go {BOLD}left{RESET} or {BOLD}right?{RESET}")
    start_choice = input("Type 'left' or 'right': ").strip().lower()

    if start_choice == "right":
        print("You continue down the path to the right.")
        river()
    elif start_choice == "left":
        print("You continue down the path to the left.")
        fort()
    else:
        print("That's not a valid direction.")
        start()


def river():
    print("You reach a river. Do you swim across or walk along the bank?")
    river_choice = input("Type 'swim' or 'walk': ").strip().lower()

    if river_choice == "swim":
        print("You swim across the river and find a treasure chest!")
    elif river_choice == "walk":
        print("You walk along the bank and find a fishing spot.")
    else:
        print("That's not a valid choice.")
        river()


def fort():
    print("You arrive at a small fort. Do you enter or walk around?")
    fort_choice = input("Type 'enter' or 'walk': ").strip().lower()

    if fort_choice == "enter":
        print("You enter the fort and find a hidden passage.")
    elif fort_choice == "walk":
        print("You walk around the fort and find some supplies.")
    else:
        print("That's not a valid choice.")
        fort()

if __name__ == "__main__":
    start()
