import random
import sys
import tty
import termios
import time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def display_quote(quote, index, wpm, errors):
    if index < len(quote):
        formatted_quote = quote[:index] + f"\033[1;32m{quote[index]}\033[0m" + quote[index+1:]
    else:
        formatted_quote = quote
    print(f"Type the following quote:\n{formatted_quote}\nAverage WPM: {wpm:.2f} | Errors: {errors}")

with open('quotes.txt', 'r') as file:
    quotes = [line.strip() for line in file.readlines()]

while True:
    chosen_quote = random.choice(quotes)
    display_quote(chosen_quote, 0, 0, 0)
    
    index, errors = 0, 0
    user_input = ''
    start_time = time.time()
    while index < len(chosen_quote):
        char = chosen_quote[index]
        
        if char == user_input:
            index += 1
            user_input = ''
            display_quote(chosen_quote, index, 0, errors)
            continue
        
        user_input = getch()
        if user_input != char:
            print("\rIncorrect! Try again.", end='', flush=True)
            display_quote(chosen_quote, index, 0, errors)
            errors += 1
        else:
            index += 1
            if index == len(chosen_quote):
                end_time = time.time()
                time_taken = end_time - start_time
                char_count = len(chosen_quote)
                wpm = (char_count / 5) / (time_taken / 60)
            else:
                wpm = 0
            display_quote(chosen_quote, index, wpm, errors)
    
    print("\nCongratulations! You typed the entire quote correctly.")
    input("\nPress Enter to continue...")
