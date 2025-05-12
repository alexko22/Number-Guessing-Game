# Task 1: Generate Random Numbers
import random
# Initialize the random number
number_to_guess = random.randint(1, 100)

# Task 2 + 3: Promt the User for Guesses
# Get the first guess from the user
guess = int(input("Enter your number: "))
# Keep Track of Guesses
guess_count = 1
while (guess != number_to_guess):
    # guess logic
    if (guess > number_to_guess):
        print("Too high! Try again.")
    elif (guess < number_to_guess):
        print("Too low! Try again.")
    else:
        # if we reach this they got it correct so exit loop
        break
    # if we get here they need to guess again so we update accordingly
    guess_count += 1
    # bonus task... added logic outside for loop
    if (guess_count > 10):
        break
    guess = int(input("Enter your number: "))
# Return the correct message based on what caused the loop break
if (guess_count > 10):
    print("Sorry! You used all 10 guesses!")
else:
    print("Congratulations! You got it in", guess_count, "attempts!")



