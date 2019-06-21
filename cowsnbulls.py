from random import randint
import sys

print('\n'' \n'
      "******************************************************************************"'\n'
      "Hello! Welcome to the Cows & Bulls game!"'\n'
      "Try to guess the number I'm thinking of with n digits."'\n'
      "When one of your digit is in the same place as mine I will count it as a 'Bull'."'\n'
      "If the digit is right but it's in the wrong place, I will count it as a 'Cow'."'\n'
      "Good Luck!\n"
      "If you don't want to play you can always enter the word 'exit'.\n"
      "******************************************************************************"
      '\n''\n')
while True:
    # First loop if for checking user input
    while True:
        n = raw_input("\nTo make it easy for you, you can choose the digit number, just type in below :)\n")
        if n.lower() == "exit":
            print("\nYou could've at least try it..")
            sys.exit()
        if not n.isdigit():
            print("Please enter the amount of digits\n")
        if n == '0':
            print("Invalid input.")
        else:
            n = int(n)
            break

    # Based on its name this function generates a random number
    def generateRandomNumber(digit):
      range_start = 10 ** (digit - 1)
      range_end = (10 ** digit) - 1
      return randint(range_start, range_end)

    RandomNumber = generateRandomNumber(n)

    guesses = 0
    # This loop runs until user exits or guesses the number
    while True:
        PlayerNumber = raw_input("\nPlease enter your guess below.\n")
        # Input control
        if str(PlayerNumber).lower() == "exit":
            print("\nWe we're having fun :( Goodbye :( ")
            sys.exit()
        if PlayerNumber.isdigit() == False or len(str(RandomNumber)) != len(str(PlayerNumber)):
            print("\nenter a number with " + str(n) + " digits")
        # This is the game :D
        else:
            cows = 0
            bulls = 0

            RandomNumber_digits = list(str(RandomNumber))
            PlayerNumber_digits = list(str(PlayerNumber))

            # First check is for any bulls
            for i in range(n):
                # If a bull is found we replace the integer so it haunt us
                if PlayerNumber_digits[i] == RandomNumber_digits[i]:
                    bulls += 1
                    RandomNumber_digits[i] = -1
                    PlayerNumber_digits[i] = -2
            # Second check is for cows
            for i in range(n):
                if PlayerNumber_digits[i] in RandomNumber_digits:
                    cows += 1
            print("\nYou have " + str(bulls) + " Bulls and " + str(cows) + " Cows\n")

            guesses += 1

            # Well if the bulls are equal to n you're a winner :)
            if bulls == n:
                if guesses > n:
                    print("\nCongratulations!\nYou have found the number after " + str(
                        guesses) + " guesses.\nBetter luck next time :P")
                    break
                else:
                    print('\n'"Congratulations!\nYou have found the number after " + str(guesses) + " guess" + (
                        "." if guesses == 1 else "es.") + "\nYou were better then I expected...")
                    break
    # Last loop is to restart the game
    while True:
        answer = raw_input('\nRun again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break

