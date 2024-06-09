#Number Guessing Game

import random

#Create Game
def play_game():

    #Generate random number and start attempts count
    number = random.randint(1,100)
    attempts = 0

    #Introduction to Game
    print('Hi! Welcome to the Number Guessing Game')
    print("I'm thinking of a number between 1 and 100.")

    while True:

        #Verify guess is an valid number
        try:
            guess = int(input('Enter guess: '))
            
            #Verify guess is in range
            if (guess < 0 or guess > 100):
                print('Value outside of guessing range.')
                continue

            #Keep track of valid attempts
            attempts += 1

            #Keep checking until user guesses correctly
            if (guess > number):
                print('Too high! Try again')
            elif (guess < number):
                print('Too low! Try again')
            else:
                print('Congrats! You guessed the number in ', attempts, ' attempts.')
                
                #Ask user if they want to play again
                play_again = input('Do you want to play again? (yes/no):')
                if (play_again == 'yes' or play_again == 'Yes'):
                    play_game()
                else:
                    print('Thank you for playing the Number Guessing Game!')
                    break
        except:
            print('Not a valid input')
            continue
        
play_game()
    