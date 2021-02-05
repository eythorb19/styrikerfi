import constants.priority
from lib.Manager import Manager

def main():

    #   Initialize the Manager
    manager = Manager()

    while True:
        userInput = input() #   cmd <i>

        words = userInput.split()
        cmd = words[0]

        manager.execute(words[0], words[1])


if __name__ == "__main__":
    main()
