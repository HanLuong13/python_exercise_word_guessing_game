import random
from re import A




letter_guess_list = []
letter_guess_list_wrong = {}
word_guess_list_wrong = set()

def display_word(word):
    word_display = ''
    for l in word:
        if l in letter_guess_list:
            word_display += l
        else:
            word_display += '_'
    print('Word: ')
    print(word_display)

def pick_word():
    file_path = (r'H:\words_alpha.csv')
    file = open(file_path)
    word_list = file.readlines()
    word = random.choice(word_list).strip()
    return word

def play_game():
    word = pick_word()
    display_word(word)
    total_guess = 7
    guess_count = 0
    guessed_right = False
    while guess_count < total_guess:
        guess = input('Enter your guess: ').lower()
        # validate_guess(guess)
        if guess.isalpha():
            if len(guess) > 1:
                if guess == word:
                    guess_count += 1
                    guessed_right = True
                    break
                elif guess in word_guess_list_wrong:
                    print('You have already tried this word. Do better!')
                elif guess != word: 
                    print('Not the word. Try again.')  
                    word_guess_list_wrong.add(guess) 
                    guess_count += 1
            elif len(guess) == 1:
                if guess in word: 
                    if guess in letter_guess_list:
                        print('You have already tried this letter. Do better!')
                    else: 
                        letter_guess_list.append(guess)
                        print(guess)
                        display_word(word)
                else: 
                    if guess in letter_guess_list_wrong:
                        print('You have already tried this. It wasn\'t in the word. Do better!')
                    else:
                        print('Letter not in word. Try again.')
                        guess_count += 1
                        letter_guess_list_wrong[guess_count] = guess
        else:
            print('Try again. Enter a word or letter this time')
    if guessed_right:
        print('You won! The word is {}!'.format(word))
    else:
        print('You\'ve tried {} times. You lost. The word is {}. Game over!'.format(guess_count, word))

def play_again():
    replay = input('Would you like to play again? Y or N.').lower()
    play_again = False
    while not play_again:
        if replay == 'y':
            play_game()
            play_again = True
        elif replay == 'n':
            break
        else:
            print('Not valid input. Try again.')



play_game()
play_again()

print(letter_guess_list_wrong)
print(letter_guess_list)
print(word_guess_list_wrong)


# def validate_guess(guess):
#     if guess.isalpha():
#         print('valid')
#     else:
#         print('Try again. Enter a word or letter this time')

