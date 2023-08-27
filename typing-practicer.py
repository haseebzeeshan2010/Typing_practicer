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

def display_quote(quote, index, wpm, error_count):
    if index < len(quote):
        highlighted_char = quote[index]
        formatted_quote = quote[:index] + f"\033[1;33m{highlighted_char}\033[0m" + quote[index+1:]
    else:
        formatted_quote = quote
    print("Type the following quote:")
    print(formatted_quote)
    print(f"Average WPM: {wpm:.2f} | Errors: {error_count}")

def main():
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    
    while True:
        chosen_quote = random.choice(quotes).strip()
        display_quote(chosen_quote, 0, 0, 0)
        
        index = 0
        previous_correct = False
        user_input = ''
        start_time = time.time()
        error_count = 0
        while index < len(chosen_quote):
            char = chosen_quote[index]
            
            if char == user_input:
                index += 1
                user_input = ''
                display_quote(chosen_quote, index, 0, error_count)
                continue
            
            user_input = getch()
            if user_input != char:
                print("\rIncorrect! Try again.", end='', flush=True)
                display_quote(chosen_quote, index, 0, error_count)
                previous_correct = False
                error_count += 1
            else:
                previous_correct = True
                index += 1
                end_time = time.time()
                time_taken = end_time - start_time
                char_count = index  # Update character count for calculating WPM
                wpm = (char_count / 5) / (time_taken / 60)
                display_quote(chosen_quote, index, wpm, error_count)
        
        print("\nCongratulations! You typed the entire quote correctly.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
