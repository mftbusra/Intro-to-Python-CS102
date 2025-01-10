#!/usr/bin/env python3
# Chatbot App v 7.0
# Author: Mst. Fariha Tasnim Busra
# Date: 09/01/2025

import random

# Function to display a random greeting
def greeting():
    greetings_list = [
        "Hello there, explorer!",
        "Hey hey! Welcome aboard!",
        "Hiya! Ready for some fun?",
        "Howdy, space traveler!",
        "Greetings, earthling!",
        "Ahoy, matey!",
        "Hola! What's new?",
        "Hey there! Glad to see you!",
        "What's up, champ?",
        "Hi! Let's get started!"
    ]
    print(random.choice(greetings_list))  # Randomly selecting and displaying a greeting

# Function to display a random goodbye
def goodbye():
    goodbyes_list = [
        "See you later, alligator!",
        "Bye for now, space adventurer!",
        "Peace out, friend!",
        "Take care, moonwalker!",
        "Catch you on the flip side!",
        "Adios, amigo!",
        "So long, traveler!",
        "Farewell, superstar!",
        "Later, tater!",
        "Stay awesome, earthling!"
    ]
    print(random.choice(goodbyes_list))  # Randomly selecting and displaying a goodbye

# Defining the main function
def main():
    greeting()  # Displaying a random greeting
    name, hometown = questions()  # Getting user's name and hometown
    calcMartianAge(name)  # Calculating Martian age
    if goAgain():  # Asking if user wants to chat again
        main()  # Recursively calling main to restart chatbot
    else:
        goodbye()  # Displaying a random goodbye

# Function to gather user's name and hometown
def questions():
    print("I’m Busra, your super-friendly (and maybe a little sassy) chatbot around. What’s your name?")
    name = input()
    print(f"Nice to meet you, {name}! Let’s make this chat fun and a little nerdy, shall we?")
    print("So, where are you from? I’m from Bangladesh, the land of breathtaking sunsets and biryani, or you might say a lot of B's!")
    hometown = input()
    print(f"{hometown}, huh? Never heard of it. Just kidding! I’m sure it’s a lovely place. Though I must say, Bangladesh sets the bar pretty high.")
    return name, hometown

# Function to calculate user's Martian age with input validation
def calcMartianAge(name):
    while True:
        try:
            print("How old are you? Don’t worry, I promise not to convert your age to binary... yet.")
            age = int(input())
        except ValueError:
            print("\033[91mNot a valid number. Please enter your age as a number.\033[0m")  # Error message in red text
        else:
            break

    MARTIAN_YEAR = 1.88
    martian_age = round(age / MARTIAN_YEAR)
    print(f"Whoa, {name}, did you know that on Mars, you’d only be {martian_age} years old? You’d practically be in your prime! \n"
          f"Lucky Martians—they don't have to deal with wrinkles yet.")

# Function to ask if user wants to chat again
def goAgain():
    print("Would you like to chat again? (y/n):")
    response = input().lower()
    return response == 'y'

# Starting the chatbot
if __name__ == "__main__":
    main()

# End of program