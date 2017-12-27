from random import randint
import sys

print ('\n'' \n'
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
    n = raw_input("\nTo make it easy for you, you can choose the digit number, just type in below :)\n")
    if str(n).lower() == "exit":
        print("\nYou could've at least try it..")
        sys.exit()
    if n.isdigit() == False:
        print("Please enter a digit\n")
    else:
        n = int(n)
        break

def generateRandomNumber(digit):
    range_start = 10**(digit-1)
    range_end = 10**digit
    return randint(range_start, range_end)
    
RandomNumber = generateRandomNumber(n)

guesses = 0
a = 0
while  0 < n:
    PlayerNumber = raw_input("\nPlease enter your guess below.\n")
    if str(PlayerNumber).lower() == "exit":
        print("\nWe we're having fun :( Goodbye :( ")
        sys.exit()
    if PlayerNumber.isdigit() == False or len(str(RandomNumber)) != len(str(PlayerNumber)):
        print("\nenter a number with " +str(n) +" digits")
    else:
        cows = 0
        bulls = 0
        
        RandomNumber_digits = list(str(RandomNumber))
        PlayerNumber_digits = list(str(PlayerNumber))

        for i in range(n):    
            if PlayerNumber_digits[i] == RandomNumber_digits[i]:
                bulls += 1
                RandomNumber_digits[i] = -1
                PlayerNumber_digits[i] = -2
        for i in range(n):
            if PlayerNumber_digits[i] in RandomNumber_digits:
                cows += 1  
        print("\nYou have " + str(bulls) + " Bulls and " + str(cows) + " Cows\n")
    
        guesses += 1
        
        if bulls == n:
            if guesses > n:
                print ("\nCongratilations!\nYou have found the number after " +str(guesses) + " guesses.\nBetter luck next time :P")
            else:
		        print ('\n'"Congratilations!\nYou have found the number after " + str(guesses) + " guess" + ("." if guesses == 1 else "es.") +
		       "\nYou were better then I expected...")
            sys.exit()
            
