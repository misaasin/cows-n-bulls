# cows-n-bulls
Cows and Bulls is an old code-breaking mind or paper and pencil game for two or more players, predating the commercially marketed board game Mastermind.

## The Numerical Version

The numerical version of the game is usually played with 4 digits, but can also be played with 3 or any other number of digits.

On a sheet or paper, the players each write a 4-digit secret number. The digits must be all different. Then, in turn, the players try to guess their opponent’s number who gives the number of matches. If the matching digits are in their right positions, they are “bulls”, if in different positions, they are “cows”. Example:

Secret number: 4271
Opponent’s try: 1234
Answer: 1 bull and 2 cows. (The bull is “2”, the cows are “4” and “1”.)

## The Program

The program coded isn’t the full game. Instead it’s more like a player, where it holds the secret number and gives out the clues while the user of the program tries to guess the number.

In the beginning of the program the rules of the game is explained.  As seen in figure 1.

```python
******************************************************************************
Hello! Welcome to the Cows & Bulls game!
Try to guess the number I'm thinking of with n digits.
When one of your digit is in the same place as mine I will count it as a 'Bull'.
If the digit is right but it's in the wrong place, I will count it as a 'Cow'.
Good Luck!
If you don't want to play you can always enter the word 'exit'.
******************************************************************************
To make it easy for you, you can choose the digit number, just type in below :)
```

*Figure 1. The rules*

In the game there are many controls that have to be done, like:
- What happens if the user wants to quit the game?
- What if the user doesn't type in an integer or number?
- What if the user wants to quit in the middle of the game?
- What happens if the user types in something longer/shorter then expected?

All of them are taken care off and are explained through the readme.

Now if we look back at the beginning, the game requires a “digit number”.  This is basically how many digits we want the secret number to have. For a short game we can type 1 or 2 or for a challenging game we can type in 6 or more. Like said above our first problem here is the user input and the problem is solved with the code  in code snippet 1.
```python
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
```
*Code snippet 1. Checking user input*

While there is a user input the program checks what it is. If the input is “exit” or in case it is “EXIT” or 0maybe “ExiT” the input is lower cased, so how ever is typed if it is exit it is exit and the program exits with sys.exit(). If the input isn’t exit that means probably the user tried to start the game so the input is checked if it is a digit or not. If it’s not the program politely asks for a number of digits again, and the controls star over for the new input. If the input was a digit then it is checked if it is 0 which is an invalid input since there isn’t such a thing as 0 digit number. Else is that if it is a number and it isn’t 0 means that a number is given to continue so the loop is broken and the game continues.

We gave a number of digits which is assigned to n. Now the program has to generate a random secret number for the user to guess. This is done with the generateRandomNumber() funcction in code snippet 2.
```python
def generateRandomNumber(digit):
      range_start = 10 ** (digit - 1)
      range_end = (10 ** digit) - 1
      return randint(range_start, range_end)

RandomNumber = generateRandomNumber(n)
```
*Code snippet 2. Generating a random number*

The function is called with the assignment of RandomNumber. The number of digits which was the user input that has passed the check, n, is passed on to the function. In the function first a range is specified. For the start of the range we minus 1 out of the digit number, n,  the result is written as the exponent of ten  and for the range end the exponent is again taken with 10 as the base and n as the exponent.. For an example:
```
for n = 1:
	range start = = = = 1
	range end = = = 10
	range is (1,10)
for n = 2:
	range start = = = = 10
	range end = = = 100 = 100
	range is (10,100)
```
The Python function range get all the numbers between the start and end including the start number but not the end number, it gets the numbers from range start to (range end – 1).

Last the generateRandomNumber() function returns a random number using the python function implemented at the beginning of the program, randint()  with the ranges found. 

Now that there is a secret number the game can begin. The guesses the user has made is counted. This isn’t necessary, just for fun. But still for this the guesses value is assigned to 0 at the beginning. Then comes the loop of the game where the loop runs until the user exits or guesses the secret number correctly.

First a guess from the user is asked and again with same control above we check if the user wants to quit or not if not then the input is checked if it is not a digit or is it longer/shorter then the number of digits, n, it asks for a number and reminds the amount of digits. This is show in code snippet 3. Else if the digit number is as same as required and the input is a number we compare it to the secret number. If the number isn’t guessed yet the user takes another turn on a guess and the loop starts all over. All invalid inputs are not counted as guesses.
```python
 PlayerNumber = raw_input("\nPlease enter your guess below.\n")
        # Input control
        if str(PlayerNumber).lower() == "exit":
            print("\nWe we're having fun :( Goodbye :( ")
            sys.exit()
        if PlayerNumber.isdigit() == False or len(str(RandomNumber)) != len(str(PlayerNumber)):
            print("\nenter a number with " + str(n) + " digits")
        else:
	…
  ```
*Code snippet 3. The guesses*

At the beginning cows numbers and bulls numbers are 0. First the Random number is separated into a list then the same is done to the users guess. First it is checked if there are any bulls. To do this we check the same indexes in both lists till the last index. Any time they are the same +1 is added to the bulls counter. And the items that were found as bulls are assigned to a new value with a negative value so they don’t appear again on the cows count. A furthermore explanation is given in the example below.<br>
The cows count is much more easier we just check if any numbers in the user list we just updated contains any items that are same with the random number list that was also updated. If there are any the same, for each +1 is added to the cows counter. <br>
Then we show the user how many cows and bulls were found in their guess. And since this was an acceptable guess, we add 1 to the guess count.<br>
Before giving the user another guess there is one more check, did the user win? This is very simple, just have to check if the bull count is equal to the number of digits, *n*.

If the game ends the program asks to run again but this time with a simple answer ‘y’ for ‘yes’ and ‘n’ for ‘no’. Anything beside them are considered as invalid input. If the answer is yes the game restarts by asking for a digit number without printing out the rules again. 


