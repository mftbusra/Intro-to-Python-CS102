#!/usr/bin/env python3
# Folkore Hero
# Author: Mst. Fariha Tasnim Busra
# Date: 11/01/2025
# Description: A text-based adventure game where the player must save their village from a mythical threat. The game includes structured functions, input validation, lists, and win/lose scenarios.

import time
import datetime  # Importing the datetime module

# Function to display the current date in the specified format
def display_current_date():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%A, %B %d %Y")
    print(f"Today's date is: {formatted_date}\n")

    