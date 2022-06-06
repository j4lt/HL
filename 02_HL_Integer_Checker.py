# HL component 1 - Get (and dcheck) user input

# To Do
# Check that lowest is an integer (any integer)
# Check that highest is more than lopwest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guess is between lowest and highest (lower and upper bound)


# Number checking function goes here
def int_check(question, low=None, high=None):
    situation = ""
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # Checks input is not too high or too low if 
            # both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more" 
                    " than (or equal to) {}".format(low))
                    continue

            return response
        
        # Checks input is a integer
        except ValueError: 
            print("Please enter an integer")
            continue





































# Main routine

lowest = int_check("Low Number: ")
highest = int_check("Higher Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)