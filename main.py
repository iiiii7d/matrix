from blessed import Terminal
from random import randint, choice
term = Terminal()

while True:
    if choice([True, False]):
        print(term.green(str(randint(0,1))), end="")
    else:
        print(term.bright_green(str(randint(0,1))), end="")