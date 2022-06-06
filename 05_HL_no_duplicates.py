# HL components 5 - no duplicates

# To Do
# Set up empty list called already_guessed
# When user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL component 5 - Prevent duplicate guesses

secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))  # Replace this with function

    # Checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again, "
        "You *still* have {} guesses left".format(guesses_left))
        continue
    
    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < secret:
            print("Too low, try a higher number. Guesses left: {} ".format(guesses_left))

        elif guess > secret:
            print("Too high, try a lower number. Guesses left: {} ".format(guesses_left))

    else:
        if guess < secret:
            print("Too low! ")
        elif guess > secret:
            print("Too high! ")

if guess == secret:
    if guesses_left == guesses_allowed -1:
        print("Amazing! You got it first try!!!")
    else:
        print("Well done you got it in {} trys ".format(guesses_allowed - guesses_left))
        

























