
secret = 6
print('Guess a Number Game v1')
print('Guess the secret number!')




while True:
    while True:
        tries = 1
        guess = int(input("Guess a number between 1 and 10:"))
        tries += 1
        if not guess:
            break
        if guess < secret:
            print('Too low')
        elif guess > secret:
            print('Too high')
        elif guess == secret:
            print("You guessed it! It was", secret)
            print("It only took you", tries, "tries!")
            play = input("Play again (Y or N): ")
            if play == 'N':
                break
        
            
