
import random
import sys

def guess_my_number(name="Player_one"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins

        player_choice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number()

        computer_choice = random.choice(["1", "2", "3"])

        print(f"\n{name}, you chose {player_choice}.")
        print(f"I was thinking about the number {computer_choice}.\n")

        player = int(player_choice)
        computer = int(computer_choice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 😢"

        game_result = decide_winner(player, computer)

        print(game_result)

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            play_again = input("\nY for Yes or \nQ to Quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    play_guess_number()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    guess_my_number(args.name)
