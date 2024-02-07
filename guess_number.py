number = 10

print("I'm thinking of a number...")
guess = True
while guess:
    guess = input("What number am I thinking of? ")
    
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"That's not correct. Try again.")
        if int(guess) < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
