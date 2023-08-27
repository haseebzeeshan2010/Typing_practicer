import random
import sys
import tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def display_quote(quote, index):
    if index < len(quote):
        highlighted_char = quote[index]
        formatted_quote = quote[:index] + f"\033[1;33m{highlighted_char}\033[0m" + quote[index+1:]
    else:
        formatted_quote = quote
    print("Type the following quote:")
    print(formatted_quote)

def main():
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    
    while True:
        chosen_quote = random.choice(quotes).strip()
        display_quote(chosen_quote, 0)
        
        index = 0
        previous_correct = False
        user_input = ''
        while index < len(chosen_quote):
            char = chosen_quote[index]
            
            if char == user_input:
                index += 1
                user_input = ''
                display_quote(chosen_quote, index)
                continue
            
            user_input = getch()
            if user_input != char:
                print("\rIncorrect! Try again.", end='', flush=True)
                display_quote(chosen_quote, index)
                previous_correct = False
            else:
                previous_correct = True
                index += 1
                display_quote(chosen_quote, index)
        
        print("\nCongratulations! You typed the entire quote correctly.")

if __name__ == "__main__":
    main()
