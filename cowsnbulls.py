from random import randint
import sys

print ('\n'' \n'
		"******************************************************************************"'\n'
		"Hello! Welcome to the Cows & Bulls game!"'\n'
		"Try to guess the number I'm thinking of with n digits."'\n'
		"When one of your digit is in the same place as mine I will count it as a Cow."'\n'
		"If the digit is right but it is place is wrong, I will count it as a Bull."'\n'
		"Good Luck!"'\n'
		"******************************************************************************"
		'\n''\n')

n = ""

while True:
	n = raw_input("\nTo make it easy for you, you can choose the digit number, just type in below :)\n\n")
	if n.isdigit():
		n = int(n)
		break

if str(n).lower() == "exit":
	print '\n'"We were having fun, goodbye :("
	sys.exit(0)

PlayerNumber = []
RandomNumber = []
def RandomNumber (n):
	range_start = 10**(n - 1)
	range_end = (10 ** n)-1
	return randint(range_start, range_end)

RandomNumber = "123"  #str(RandomNumber(n))

cows = 0
bulls = 0
guesses = 0


while cows < n:
	PlayerNumber = raw_input("\nPlease enter your guess below. \nEnter 'exit' to quit the game.\n\n" )
	if str(PlayerNumber).lower() == "exit":
		print '\n'"We we're having fun :( Goodbye :( "
		break
	if len(PlayerNumber) == len(RandomNumber):
		if PlayerNumber.isdigit():

			cows = 0
			bulls = 0
			for i in range (0,n):
				if PlayerNumber[i] == RandomNumber[i]:
					cows += 1
				elif PlayerNumber[i] in RandomNumber[-1 * (n-i)]:
                                        bulls += 1

			#bulls = bulls - cows

			print ('\n'"You have " + str(cows) + " Cows and " + str(bulls) + " Bulls"'\n')
			guesses += 1

		else:
			print "Please enter only numbers."

	else:
		print ("\nPlese enter " + str(n) + " digits of numbers.")


if cows == n:
	if guesses > 3:
		print ('\n'"Congratilations!\nYou have found the number after " + str(guesses) + " guesses.\n"
				"Better luck next time!")
	else:
		print ('\n'"Congratilations!\nYou have found the number after " + str(guesses) + " guess" + ("." if guesses == 1 else "es.") +
		       "\nYou were better then I expected...")


