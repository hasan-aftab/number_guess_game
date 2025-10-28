import random

# Generate a random integer number between 1 and 100 
jackpot = random.randint(1, 100)

# Print guess number for ease of guess
print("Random jackpot number is ", jackpot)

# Ask user to enter his guess
def askUserGuess():
    return int(input("Enter ur guess: "))

# Store user's guess in a variable
guess = askUserGuess()
counter = 1

# Keep asking user for guess until not succeeded
while guess != jackpot:
    if guess < jackpot:
        print("Guess higher number")
    else:
        print("Guess lower number")
        
    guess = askUserGuess() 
    counter += 1
    
print(f"🎉 You guessed it in {counter} tries!")