import requests
import random


def fetch_countries_and_capitals():
    """
    Fetches a list of countries and their capitals from an API.

    Returns:
        list of tuples: A list where each tuple contains the name of a country and its capital.
    """
    res = requests.get("https://freetestapi.com/api/v1/countries")
    data = res.json()
    return [(country["name"], country["capital"]) for country in data]


def capital_game():
    """
    Starts a game where the user guesses the capitals of randomly selected countries.

    The game continues until the user types 'exit' or chooses not to play again after a wrong guess.
    The user's score (number of correct guesses) is displayed at the end.
    """
    countries_and_capitals = fetch_countries_and_capitals()
    point = 0
    while True:
        country, capital = random.choice(countries_and_capitals)

        print(f"What is the capital of {country}? (Type 'exit' to stop the game))")
        user_guess = input("Your guess: ").strip()
        if user_guess.lower() == capital.lower():
            print("Correct!")
            point += 1
        elif user_guess.lower() == "exit":
            print(f"You found {point} capitals of countries.")
            break
        else:
            print(f"Wrong! The capital of {country} is {capital}.")
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()

            if play_again != "yes":
                print(f"You found {point} capitals of countries.")
                break
