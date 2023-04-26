import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""           # tell the computer if it's: low, high or the correct number. Besides the user can type whatever it wants.
    while feedback != "c":
        if low != high:
           guess = random.randint(low, high)
        else:
            guess = low
            print(guess)
            # might be high b/c low = high
        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)?? ").lower()
        if feedback == "h":
            high = guess - 1   # both -1 and +1 are important the program runs without any problems
        elif feedback == "l":
            low = guess + 1

    print(f"The computer guessed the number {guess} correctly. ")

computer_guess(10)
