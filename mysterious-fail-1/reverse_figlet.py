import sys

from pyfiglet import Figlet


def main():
    f = Figlet(font='big')
    for line in sys.stdin:
        print(f.renderText(reversed(line.strip())))

if __name__ == "__main__":
    main()
