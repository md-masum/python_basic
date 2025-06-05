from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
print('original number is: ', answer)  # For debugging purposes, you can remove this line later.

while True:
    guess = input("Guess a number between 1 and 10: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please try again.")
        continue
    
    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the right number!")
        break