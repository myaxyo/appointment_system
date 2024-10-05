"""
This script is a U.S. States Game using the turtle module and pandas library.

The script reads a CSV file containing information about
the 50 states of the U.S. The user is prompted to guess the
names of the states one by one. If the user's guess matches
a state name in the CSV file, the state name is
displayed on the screen using the turtle module.

Functions:
    - None

Variables:
    - num_states: An integer representing the total number
    of states in the CSV file.
    - found_states: A list that stores the names of the states that
    have been correctly guessed by the user.
    - screen: A turtle.Screen object that represents the game screen.
    - image: A string representing the file path of the image
    used as the background of the game screen.
    - turtle: A turtle.Turtle object used for writing the state
    names on the screen.

Usage:
    - Run the script and follow the prompts to guess the names of
    the U.S. states.
"""

import turtle


def find_state_game(df, image):

    num_states = df["state"].count()
    found_states = []
    screen = turtle.Screen()
    screen.title("U.S. States Game")

    screen.addshape(image)
    turtle.shape(image)
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()

    while len(found_states) != num_states:
        answer_state = (
            screen.textinput(
                title=f"{len(found_states)}/{num_states} Guess the State",
                prompt="What is next state's name?",
            )
            .title()
            .strip()
        )

        if answer_state is None or "Exit":
            break

    is_real_state_name = df["state"].isin([answer_state]).any()

    if is_real_state_name and answer_state not in found_states:
        state_data = df[df.state == answer_state].iloc[0]
        x, y = state_data["x"], state_data["y"]
        writer.goto(x, y)
        writer.write(answer_state)
        found_states.append(answer_state)

    turtle.exitonclick()
