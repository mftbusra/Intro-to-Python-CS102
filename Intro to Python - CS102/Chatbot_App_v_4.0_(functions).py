#!/usr/bin/env python3
# Chatbot App v 4.0
# Author: Mst. Fariha Tasnim Busra 
# Date: 07/01/2025

# Defining the main function
def main():
    name, hometown = questions()  # Get user's name and hometown
    age = getAge()  # Get user's age
    calcMartianAge(age, name)  # Calculate Martian age
    calcFare(age)  # Calculate fare to Mars
    if goAgain():  # Ask if user wants to chat again
        main()  # Recursively call main to restart chatbot

# Defining the functions
def questions():
    print("Hi! I’m Busra, your super-friendly (and maybe a little sassy) chatbot around. What’s your name?")
    name = input()
    print(f"Nice to meet you, {name}! Let’s make this chat fun and a little nerdy, shall we?")
    print("So, where are you from? I’m from Bangladesh, the land of breathtaking sunsets and biryani, or you might say a lot of B's!")
    hometown = input()
    print(f"{hometown}, huh? Never heard of it. Just kidding! I’m sure it’s a lovely place. Though I must say, Bangladesh sets the bar pretty high.")
    return name, hometown

def getAge():
    print("How old are you? Don’t worry, I promise not to convert your age to binary... yet.")
    age = float(input())
    return age

def calcMartianAge(age, name):
    MARTIAN_YEAR = 1.88
    martian_age = round(age / MARTIAN_YEAR)
    print(f"Whoa, {name}, did you know that on Mars, you’d only be {martian_age} years old? You’d practically be in your prime! \n"
          f"Lucky Martians—they don't have to deal with wrinkles yet.")

def calcFare(age):
    if age < 12:
        fare = "$5000"
        print("Since you're under 12, your fare to Mars is only $5000. Youth discounts are the best!")
    elif 19 < age < 65:
        fare = "$10000"
        print("As an adult, your fare to Mars is $10000. Time to start saving!")
    else:
        fare = "$7000"
        print("Senior or student? Cool. That’ll still be $7000. Mars doesn’t do free rides.")

def goAgain():
    print("Would you like to chat again? (y/n):")
    response = input().lower()
    return response == 'y'

# Calling the main function
if __name__ == "__main__":
    main()