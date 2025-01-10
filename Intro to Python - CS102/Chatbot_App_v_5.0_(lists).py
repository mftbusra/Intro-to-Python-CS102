#!/usr/bin/env python3
# Chatbot App v 5.0
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
    age = getAge()  # Getting user's age
    calcMartianAge(age, name)  # Calculating Martian age
    calcFare(age)  # Calculating fare to Mars
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

# Function to get user's age
def getAge():
    print("How old are you? Don’t worry, I promise not to convert your age to binary... yet.")
    age = float(input())
    return age

# Function to calculate user's Martian age
def calcMartianAge(age, name):
    MARTIAN_YEAR = 1.88
    martian_age = round(age / MARTIAN_YEAR)
    print(f"Whoa, {name}, did you know that on Mars, you’d only be {martian_age} years old? You’d practically be in your prime! \n"
          f"Lucky Martians—they don't have to deal with wrinkles yet.")

# Function to calculate fare to Mars
def calcFare(age):
    if age < 12:
        print("Since you're under 12, your fare to Mars is only $5000. Youth discounts are the best!")
    elif 19 < age < 65:
        print("As an adult, your fare to Mars is $10000. Time to start saving!")
    else:
        print("Senior or student? Cool. That’ll still be $7000. Mars doesn’t do free rides.")

# Function to ask if user wants to chat again
def goAgain():
    print("Would you like to chat again? (y/n):")
    response = input().lower()
    return response == 'y'

# Starting the chatbot
if __name__ == "__main__":
    main()

# End of program