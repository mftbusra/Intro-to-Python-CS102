#!/usr/bin/env python3
# Chatbot App v 1.0
# Author: Mst. Fariha Tasnim Busra 
# Date: 06/01/2025

# Constant for Martian year ratio
MARTIAN_YEAR = 1.88

# Greetings to the user and ask for name
print("Hi! I’m Busra, your super-friendly (and maybe a little sassy) chatbot around. What’s your name?")
name = input()

# Personalized greetings
print(f"Nice to meet you, {name}! Let’s make this chat fun and a little nerdy, shall we?")

# Asking about the user's hometown
print("So, where are you from? I’m from Bangladesh, the land of breathtaking sunsets and biryani, or you might say a lot of B's!")
hometown = input()

print(f"{hometown}, huh? Never heard of it. Is that even on Google Maps, {name}? \n"
  f"Just kidding! I’m sure it’s a lovely place. Though I must say, Bangladesh sets the bar pretty high.")

# Asking about the user's age
print(f"Alright, {name}, how old are you? And don’t worry, I promise not to convert your age to binary... yet.")
age = float(input())

# Calculating the user's age in Martian years
martian_age = round(age / MARTIAN_YEAR)
print(f"Whoa, {name}, did you know that on Mars, you’d only be {martian_age} years old? You’d practically be in your prime! \n \
  Lucky Martians—they don't have to deal with wrinkles yet.")

# Asking about the user's favorite food
print(f"What’s your favorite food, {name}? I won’t judge—unless you say something like boiled broccoli.")
favorite_food = input()

print(f"{favorite_food}? Yum! That’s a solid choice, {name}. You’d probably code better if you had a plate of {favorite_food} next to your keyboard.")

# Asking about the user's favorite programming language
print(f"Okay, {name}, final question: What’s your favorite programming language? (Hint: if it’s not Python, we might have a problem.)")
favorite_language = input()

if favorite_language.lower() == "python":
    print(f"Python? Excellent choice, {name}! It’s the kind of language that even aliens on Mars would use.")
else:
    print(f"{favorite_language}? Huh. That’s like preferring a typewriter over a MacBook, {name}. Just saying.")

# Summary of the user's answers 
print(f"Thanks for the chat, {name} from {hometown}! I'm glad to learn about your favourite food {favorite_food} which I can't wait to try, and keep coding in {favorite_language}. "
      f"I’d say you’re pretty awesome despite you are {age} years old. Catch you later, alligator!")

# End of program
