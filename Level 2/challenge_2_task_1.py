import random
answer = random.randint(1, 100)
guesses = set() # Doesn't store repeats
while answer not in guesses: # Loop until guess is same as answer
    try:
        guess = int(input("Guess a number between 1 & 100: "))
        guesses.add(guess) # Add guess to guesses set if it is valid (try & except)
        if guess > answer:
            print("Too high")
        elif guess == answer:
            print("You won!")
        else:
            print("Too low")
    except: # Error exception
        print("Not a valid number")
        continue
print("Answer is: {}\nNumber of valid guesses: {}".format(answer, len(guesses))) # Number of valid guesses is equal to the length of the set
print(guesses) # Display guesses
