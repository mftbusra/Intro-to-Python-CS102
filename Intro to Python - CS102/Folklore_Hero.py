#!/usr/bin/env python3
# Folkore Hero
# Author: Mst. Fariha Tasnim Busra
# Date: 12/01/2025
# Description: A text-based adventure game where the player must save their village from a mythical threat. The game includes structured functions, input validation, lists, and win/lose scenarios.

import time
import datetime  # Importing the datetime module

# Function to display the current date in the specified format
def display_current_date():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%A, %B %d %Y")
    print(f"Today's date is: {formatted_date}\n")

# Function to display the introduction storyline
def display_storyline():
    display_current_date()  # Displaying the current date at the start of the storyline
    print("Welcome to 'The Folklore Hero of Rajshahi'!")
    print("Rajshahi is known as the Silk City of Bangladesh, is a serene city on the bank of the Padma River. Famous for its mangoes and rich cultural heritage, it is also a hub for education and history.")
    print("You are a brave civillian chosen to save your hometown Rajshahi from a mythical threat.")
    print("Your journey will test your wit, bravery, and decision-making.")
    print("Can you survive and save Rajshahi? Let the journey begin!\n")
    print("Before we start, for safety you will always have fish with you in this journey. Bangalis love to eat fish and rice, so you can consider fish is infinite charm or power or coin in this game. And with your every decision you get or lose a morale point for your action. ")
    time.sleep(2)

# Function to get and validate input from the user
def get_choice(options):
    while True:
        try:
            print("\nChoose one of the following options:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a number from the list.\n")
        except ValueError:
            print("Not an integer. Please enter a valid number.\n")

# Function for the Shakchunni encounter
def shakchunni_encounter(inventory):
    print("\nYou encounter a Shakchunni, a female ghost with long hair blocking your path.")
    print("\n A little insider information about Shakchunni : Shankchunni is a ghost of Hindu widow who wears the shankha(a white bangle, a symbol of hindu married woman). She died either due to abuse or has some unfulfilled desires. Hindu widows in their lifetime, were deprived of eating fish due to dietary restrictions. They often haunts the husband's family and possesses other young married woman. If I remember correctly Shankchunni loves fish specially Hilsha and would often haunt the kitchen when cooking fish.")
    print("She offers to let you pass if you answer her riddle correctly.")
    time.sleep(2)

    print("\nRiddle: 'I have cities, but no houses. I have forests and mountains, but no trees. I also have water, but no fish (´•╭╮•`). What am I?'")
    options = ["Offer her some Hilsha fish", "Answer: 'A map'", "Run away"]
    choice = get_choice(options)

    if choice == 1:
        print("\nThe Shakchunni takes the Hilsha fish and lets you pass.")
        inventory.append("Shakchunni")
        morale += 1
        print(f"Your morale increases to {morale}!")
        return True, morale
    elif choice == 2:
        print("\nCorrect! The Shakchunni smiles and vanishes. You may pass.")
        inventory.append("Shakchunni")
        morale += 2
        print(f"Your morale increases to {morale}!")
        return True, morale
    elif choice == 3:
        print("\nYou run away, but she curses you. You lose morale.")
        morale -= 1
        print(f"Your morale decreases to {morale}.")
        if morale < 0:
            print("\nYou have no morale left. The journey ends here.")
            return False, morale
        return True, morale
        

# Function for the Padma River crossing
def padma_river_encounter(inventory):
    print("\nYou reach the Padma River. As you already know Rajshahi is located on the bank of Padma river, so in order to move forward, you need to cross the river.")
    print(" You encounter the ghost named 'Mechhobhoot'. Mechhobhoot is another lover of fish who accosts late night fishermen or lone people carrying fish.")
    print("A boatman demands fish or challenges you to a riddle.")
    time.sleep(2)

    options = ["Swim", "Offer some fish", "Play the riddle game"]
    choice = get_choice(options)

    if choice == 1:
        print("\nYou can not keep up with the flow of cold water of the Padma. You drown.")
        inventory.append("Boatman")
        if morale < 0:
            print("\nYou have no morale left. The journey ends here.")
            return False, morale
        return True, morale
    elif choice == 2:
        print("\nThe boatman takes the fish and takes you across.")
        inventory.append("Boatman")
        morale += 1
        print(f"Your morale increases to {morale}!")
        return True, morale    
    elif choice == 3:
        print("The boatman asks:")
        print("""
        I travel the rivers, where waters flow,
        In the Padma’s depths is where I glow.
        A treasure of taste, both rich and grand,
        Loved by people of this land.
        What am I?
        """)
        while True:
            answer = input("Your answer: ").strip().lower()
            if answer:
                break
            print("Answer cannot be empty. Try again.")

        if answer == "Hilsha fish":
            print("\nCorrect! The boatman takes you across.")
            inventory.append("Boatman")
            morale += 2
        print(f"Your morale increases to {morale}!")
        return True, morale
        else:
            print("\nWrong! The boatman refuses to take you. You lose morale.")
            if morale < 0:
            print("\nYou have no morale left. The journey ends here.")
            return False, morale
        return True, morale

# Function for the final battle
def final_battle(inventory):
    print("\nYou face the Skondhokata, headless ghosts whose origin stories have changed over time. They usually attack or enslave humans to help them find their lost heads. They generally dwell in low moist lands, outside a village, in bogs and fens, and go about in the dark, rolling on the ground, with their huge arms stretched out. However, some describe them as the ghosts of people beheaded on the train tracks. They haunt railway stations, but can easily be outwitted because of their lack of sight.")
    print("To defeat him, you must solve a riddle and use your collected morale points.")
    time.sleep(2)

    if "Shakchunni" in inventory and "Boatman" in inventory:
        print("\nYour morale give you an advantage in the battle!")
    else:
        print("\nYou lack the necessary morale. The battle will be harder.")
        time.sleep(2)

    print("\nRiddle: 'The more you take, the more you leave behind. What am I?'")
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer:
            break
        print("Answer cannot be empty. Try again.")

    if answer == "footsteps":
        print("\nCorrect! You defeated the Skondhokata and saved Rajshahi!")
        return True
    else:
        print("\nWrong! The Skondhokata overpowers you.")
        return False


# Asking to restart function
def ask_to_restart():
    while True:
        play_again = input("\nWould you like to try again? (yes/no): ").strip().lower()
        if play_again in ["yes", "no"]:
            return play_again == "yes"
        print("Invalid input. Please enter 'yes' or 'no'.")

# Main function to organize the game flow
def main():
    while True:
        # Initializing player state
        morale = 0  # Starting with 0 morale
        inventory = []

        # Displaying the storyline
        display_storyline()

        # Encounter 1: Shakchunni
        success, morale = shakchunni_encounter(inventory, morale)
        if not success:
            if not ask_to_restart():
                print("\nThank you for playing 'The Folklore Hero of Rajshahi'!")
                break
            continue

        if morale <= 0:
            print("\nYour morale is too low to continue. You return to the village defeated.")
            if not ask_to_restart():
                print("\nThank you for playing 'The Folklore Hero of Rajshahi'!")
                break
            continue

        # Encounter 2: Padma River
        success, morale = padma_river_encounter(inventory, morale)
        if not success:
            if not ask_to_restart():
                print("\nThank you for playing 'The Folklore Hero of Rajshahi'!")
                break
            continue

        if morale <= 0:
            print("\nYour morale is too low to continue. You return to the village defeated.")
            if not ask_to_restart():
                print("\nThank you for playing 'The Folklore Hero of Rajshahi'!")
                break
            continue

        # Final Encounter: Skondhokata
        if final_battle(inventory):
            print("\nCongratulations! You have saved Rajshahi and became a hero of folklore!")
        else:
            print("\nYou failed in your mission. You became a cautionary tale in folklore.")
            if not ask_to_restart():
                print("\nThank you for playing 'The Folklore Hero of Rajshahi'!")
                break
            continue

# Asking the player if they want to play again
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again in ["yes", "no"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == "no":
            print("\nThank you for playing 'The Folklore Hero of Rajshahi'!")
            break

# Calling the main function
if __name__ == "__main__":
    main()
    
# End of program

