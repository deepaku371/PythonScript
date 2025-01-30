import colorama
from termcolor import colored
import time
import random

# Initialize colorama for Windows compatibility
colorama.init()

def print_rainbow_text(text):
    """Print text in rainbow colors"""
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(colored(char, color), end='')
    print()

def create_color_pattern(width, height):
    """Create a colorful pattern using ASCII characters"""
    chars = ['*', '#', '@', '$', '%']
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    
    for _ in range(height):
        line = ''
        for _ in range(width):
            char = random.choice(chars)
            color = random.choice(colors)
            line += colored(char, color) + ' '
        print(line)

def animated_loading_bar():
    """Create an animated loading bar with colors"""
    colors = ['red', 'yellow', 'green', 'blue']
    width = 40
    
    for i in range(width + 1):
        bar = '[' + '=' * i + ' ' * (width - i) + ']'
        percentage = i * 100 // width
        color = colors[(i // 10) % len(colors)]
        print(colored(f'\r{bar} {percentage}%', color), end='')
        time.sleep(0.1)
    print()

def main():
    # Example usage of all color functions
    print("\nRainbow Text Example:")
    print_rainbow_text("Hello, Colorful World!")
    
    print("\nRandom Color Pattern:")
    create_color_pattern(20, 5)
    
    print("\nAnimated Loading Bar:")
    animated_loading_bar()
    
    # Demonstrate basic colored text
    print("\nBasic Color Examples:")
    print(colored("This is red text", 'red'))
    print(colored("This is green text on white background", 'green', 'on_white'))
    print(colored("This is bold blue text", 'blue', attrs=['bold']))

if __name__ == "__main__":
    main()