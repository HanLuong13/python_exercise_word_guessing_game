import string


word = 'random'

total_guess = 7
guess_count = 0 

while guess_count < total_guess:
    guess = input('Enter your guess: ')
    print(guess)
    if guess.isalpha():
        print('valid')
    else:
        print('Try again. Enter a word or letter this time')
        