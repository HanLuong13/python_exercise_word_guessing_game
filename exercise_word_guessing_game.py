import random


num_plays = 1

def display_word(input):
    global word_display
    word_display = ''
    for l in input:
        if l in letter_guess_list:
            word_display += l
        else:
            word_display += '_'
    print('Word: ')
    print(word_display)
    return word_display


# def pick_word():
#     file_path = (r'H:\words_alpha.csv')
#     file = open(file_path)
#     word_list = file.readlines()
#     global word
#     word = random.choice(word_list).strip()
#     return word

def play_game():
    global letter_guess_list
    global guessed_right
    letter_guess_list = []
    letter_guess_list_wrong = {}
    word_guess_list_wrong = set()
    word = 'random'
    # word = pick_word()
    display_word(word)
    total_guess = 7
    guess_count = 0
    guessed_right = False
    while guess_count < total_guess and not guessed_right:
        guess = input('Enter your guess: ').lower()
        # validate_guess(guess)
        if guess.isalpha():
            if len(guess) > 1: #if it's a word
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
            elif len(guess) == 1:  #if it's a letter 
                if guess in word and guess in letter_guess_list: 
                    print('You have already tried this letter. Do better!')
                elif guess in word and guess not in letter_guess_list:
                    letter_guess_list.append(guess)
                    print(guess) 
                    display_word(word)
                    guess_count += 1
                    if '_' not in word_display:   
                        guessed_right = True 
                        break
                elif guess in letter_guess_list_wrong:
                    print('You have already tried this. It wasn\'t in the word. Do better!')
                else: 
                    print('Letter not in word. Try again.')
                    guess_count += 1
                    letter_guess_list_wrong[guess_count] = guess                    
                    # else: 
                    # elif guess in word and '_' not in word_display: 
                    #     letter_guess_list.append(guess)
                    #     print(guess)
                    #     display_word(word)
                    # else: 
                    #     guess_count += 1
                    #     guessed_right = True
                    #     break
                # else: 
                #     if guess in letter_guess_list_wrong:
                #         print('You have already tried this. It wasn\'t in the word. Do better!')
                #     else:
                #         print('Letter not in word. Try again.')
                #         guess_count += 1
                #         letter_guess_list_wrong[guess_count] = guess
        else: #not valid input
            print('Try again. Enter a word or letter this time')
    if guessed_right:
        print('You won! The word is {}!'.format(word))
    else:
        print('You\'ve tried {} times. You lost. The word is {}. Game over!'.format(guess_count, word))


play_game()


replay = input('Would you like to play again? Y or N.').lower()
play_again = False
while not play_again:
    if replay == 'y':
        play_game()
        play_again = True
        num_plays += 1
    elif replay == 'n':
        break
    else:
        print('Not valid input. Try again.')

print('Number of tries: ', num_plays)


# def validate_guess(guess):
#     if guess.isalpha():
#         print('valid')
#     else:
#         print('Try again. Enter a word or letter this time')

