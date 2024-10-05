import pandas as pd

from games.us_state_game.find_state_name import find_state_game
from games.find_the_capital.find_the_capital import capital_game


def game_starter():
    while True:

        print("\nWelcome to game center!")
        print("\nSelect mode:")
        print("1. Find US State Names")
        print("5. Coming more soon")

        choice = input("Enter your choice (or type 'exit' to quit): ").strip()

        match choice:
            case "1":
                df = pd.read_csv("./games/us_state_game/50_states.csv")
                image = "./games/us_state_game/blank_states_img.gif"
                find_state_game(df, image)
            case "2":
                capital_game()
            case "exit":
                break

            case _:
                print("Invalid choice. Please try again.")
