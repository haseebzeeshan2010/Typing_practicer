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

def display_quote(quote):
    print("Type the following quote:")
    print(quote)

def main():
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    
    while True:
        chosen_quote = random.choice(quotes)
        display_quote(chosen_quote)
        
        index = 0
        previous_correct = False
        user_input = ''
        while index < len(chosen_quote):
            char = chosen_quote[index]
            if char == user_input:
                display_quote(chosen_quote)
                index += 1
                user_input = ''
                continue
            
            user_input = getch()
            if user_input != char:
                print("\rIncorrect! Try again.", end='', flush=True)
                display_quote(chosen_quote)
                previous_correct = False
            else:
                previous_correct = True
        
        print("\nCongratulations! You typed the entire quote correctly.")

if __name__ == "__main__":
    main()
