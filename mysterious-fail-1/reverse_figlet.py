import sys

from pyfiglet import Figlet


f = Figlet(font='big')

def render(line):
    return f.renderText(reversed(line.strip()))


def main():
    for line in sys.stdin:
        print(render(line))

if __name__ == "__main__":
    main()
