import random

guess_num = 5
q = guess_num
n = random.randint(1, 100) 
guess = int(input("Enter an integer from 1 to 100: "))
while n != "guess":
    q - 1
    if guess < n: 
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 100: "))
        q - 1
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 100: "))
        q - 1
    elif guess == n:
        print ("you guessed it!")
        break
    elif guess_num < 0:
        print("You've run out of guesses.")
    else ValueError:
        print("Please enter a postive whole number.")

    print
