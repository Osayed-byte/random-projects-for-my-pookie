import random
number = random.randint(1, 10)

player_name = input("Hello, what is your name? ")
number_of_guesses = 0
print('nice to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 10 then you will guess, alright? '.format(player_name))

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('wrong, try again')
    if guess > number:
        print('Wrong, try again')
    if guess == number:
        break
if guess == number:
    print( 'Congrats {}, you guessed the number in {} tries!'.format(player_name, number_of_guesses))
else:
    print('Close but no quite right, . \n the correct number was {}.'.format(number))