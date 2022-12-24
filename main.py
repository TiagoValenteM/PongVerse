import sys

import src.interface
from src.config import *


def main():
    settings = GlobalSettings()

    if len(sys.argv) == 3:  # received resolution as arguments
        settings = GlobalSettings((int(sys.argv[1]), int(sys.argv[2])))

    interface = src.interface.Interface(settings)
    interface.mainMenu()


if __name__ == '__main__':
    main()
