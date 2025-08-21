import random

options = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def pick_random_move() -> str:
    """Randomly chooses output from rock, paper & scissors"""
    return random.choice(list(options.keys()))


def user_choice() -> str:
    """Takes user input"""
    action = input("Select from rock, paper or scissors: ").lower()
    return action if action in options else None


def user_choice2() -> str:
    """Takes user input"""
    action = input("Select from rock, paper or scissors: ").lower()
    if action in options:
        return action
    else:
        print("Invalid")
        return None


def take_choice() -> str:
    pass


def check_valid(string: str) -> bool:
    pass


def victor(player: str, bot: str) -> str:
    """Determines the victor based on the two inputs"""
    if player == bot:
        return "It's a tie!"
    elif options[player] == bot:
        return "You win!"
    else:
        return "You lose!"


def main():
    bot = pick_random_move()
    player = None
    while player is None:
        player = user_choice()
    print(f"You chose {player} and bot chose {bot}")
    print(victor(player, bot))


if __name__ == "__main__":
    main()
