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

def display_progress(text, index):
    progress = text[:index] + '_' + text[index+1:]
    print("\r" + progress, end='', flush=True)

def main():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    
    while True:
        chosen_word = random.choice(words)
        print("Type the following word:")
        print(chosen_word)
        
        index = 0
        previous_correct = False
        while index < len(chosen_word):
            char = chosen_word[index]
            display_progress(chosen_word, index)
            user_input = getch()
            
            while user_input != char:
                print("\rIncorrect! Try again.", end='', flush=True)
                display_progress(chosen_word, index)
                user_input = getch()
                previous_correct = False
            
            if not previous_correct and index < len(chosen_word) - 1:
                print("\rCorrect! Proceed to the next letter:", char)
            previous_correct = True
            index += 1
        
        print("\nCongratulations! You typed the entire word correctly.")

if __name__ == "__main__":
    main()
