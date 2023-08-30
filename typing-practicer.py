import random
import sys
import tty
import termios
import time

class TypingPractice:
    def __init__(self, quotes_file):
        self.quotes = self.load_quotes(quotes_file)
    
    def load_quotes(self, file_path):
        with open(file_path, 'r') as file:
            quotes = [line.strip() for line in file]
        return quotes
    
    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
    def display_quote(self, quote, index, wpm, errors):
        formatted_quote = quote[:index] + f"\033[1;32m{quote[index]}\033[0m" + quote[index+1:] if index < len(quote) else quote
        print(f"Type the following quote:\n{formatted_quote}\nAverage WPM: {wpm:.2f} | Errors: {errors}")
    
    def run(self):
        while True:
            chosen_quote = random.choice(self.quotes)
            self.display_quote(chosen_quote, 0, 0, 0)
            
            index, errors = 0, 0
            user_input = ''
            start_time = time.time()
            while index <= len(chosen_quote):
                if index == len(chosen_quote):
                    end_time = time.time()
                    time_taken = end_time - start_time
                    char_count = index
                    wpm = (char_count / 5) / (time_taken / 60)
                    self.display_quote(chosen_quote, index, wpm, errors)
                    break
                
                char = chosen_quote[index]
                user_input = self.getch()
                
                if user_input == char:
                    index += 1
                    self.display_quote(chosen_quote, index, 0, errors)
                else:
                    print("\rIncorrect! Try again.", end='', flush=True)
                    self.display_quote(chosen_quote, index, 0, errors)
                    errors += 1
            
            print("\nCongratulations! You typed the entire quote correctly.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    quotes_file = 'quotes.txt'
    typing_practice = TypingPractice(quotes_file)
    typing_practice.run()
