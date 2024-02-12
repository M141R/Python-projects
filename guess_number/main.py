import random

def guess(x) :
    randomno = random.randint(1,x)
    guess = 0
    while guess != randomno:
        guess = int(input(f'Guess a no. between 1 and {x}: '))
        if guess < randomno:
            print("Guess again, guess too low")
        elif guess > randomno:
            print("Guess again, guess too high")

    print(f'You guessed it!!!!, the no. was {randomno}')

guess(1000)
