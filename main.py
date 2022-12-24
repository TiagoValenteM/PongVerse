import sys
import src.interface
from src.config import *


def main():
    if len(sys.argv) == 3:  # if received resolution as arguments
        settings = GlobalSettings((int(sys.argv[1]), int(sys.argv[2])), False)

    else:  # if not, use default resolution
        settings = GlobalSettings()

    # Initialize Interface with settings
    thePongVerseGame = src.interface.Interface(settings)
    thePongVerseGame.mainMenu()


if __name__ == '__main__':
    main()
