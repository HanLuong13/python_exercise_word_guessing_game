import random

total_losses = 0
total_wins = 0
num_plays = 1
all_picked_words = []

#displaying word
def display_word(input):
    global word_display
    word_display = ''
    for l in input:
        if l in already_guessed_letter_right:
            word_display += l
        else:
            word_display += '_'
    print(f'Word: {word_display}')
    return word_display

#picking random words, making sure not already picked
def pick_word():
    global all_picked_words, word 
    file = open('words_alpha.txt')
    word_list = file.readlines()
    word = random.choice(word_list).strip()
    unique_word = False
    while not unique_word:
        if word in all_picked_words:
            word = random.choice(word_list).strip()
        else:
            unique_word = True
    all_picked_words.append(word)
    return word

#main game function
def play_game():
    global total_losses, total_wins, already_guessed_letter_right, guessed_right, guesses_left, total_guess, word_display
    guesses_left = 7
    already_guessed_letter_right = []
    already_guessed_letter_wrong = {}
    already_guessed_word_wrong = set()
    total_guess = 0
    word = pick_word()
    guessed_right = False
    while guesses_left > 0 and not guessed_right:
        display_word(word)
        # if word was revealed through letter choices
        if '_' not in word_display:
            guessed_right = True 
            break
        # word not revealed yet, continue with user input
        else:
            print(f'You have {guesses_left} guesses left.')
            guess = input('Enter your guess: ').lower()
        #validate word is alphabetical
        if guess.isalpha():
            # input is a word
            if len(guess) > 1: 
                # & input is THE word
                if guess == word:
                    guesses_left -= 1
                    total_guess += 1
                    guessed_right = True
                    break
                # & input is a word that has already been guessed
                elif guess in already_guessed_word_wrong:
                    print(f'You\'ve already tried this word. Do better! ')
                # & input is a word that hasn't been guessed but is wrong
                elif guess != word:   
                    already_guessed_word_wrong.add(guess) 
                    guesses_left -= 1
                    total_guess += 1
                    print(f'Not the word. Try again.')
            # input is a letter
            elif len(guess) == 1:  
                # & input is in word and already guessed
                if guess in word and guess in already_guessed_letter_right: 
                    print(f'You\'ve already tried this letter. Do better!')
                # & input is in word but not already guessed
                elif guess in word and guess not in already_guessed_letter_right:
                    already_guessed_letter_right.append(guess)
                    print('You got one.') 
                # & input is NOT in word and is already guessed                        
                elif guess in already_guessed_letter_wrong.values():
                    print(f'You\'ve already tried this letter. It wasn\'t in the word. Do better!')
                # & input is NOT in word and not previously guessed
                else: 
                    guesses_left -= 1
                    total_guess += 1
                    already_guessed_letter_wrong[total_guess] = guess  
                    print(f'Letter not in word. Try again.')                  
        # input is not valid 
        else: 
            print('Try again. Enter a word or letter this time')
    # guessed right
    if guessed_right:
        print('You won! The word is {}!'.format(word))
        total_wins += 1
    # out of guesses 
    else:
        print('You\'ve tried {} times. You lost. The word is {}. Game over!'.format(total_guess, word))
        total_losses += 1
    play_again()

# asks if player wants to play again
def play_again():
    global num_plays
    play_again = False
    while not play_again:
        replay = input('Would you like to play again? Y or N. ').lower()
        if replay == 'y':
            play_again = True
            num_plays += 1
            play_game()
        elif replay == 'n':
            print('That is fine. See you next time!')
            break
        else:
            print('Not valid input. Try again.')


play_game()
print(f'You\'ve played {num_plays} times. You\'ve won {total_wins} times. You\'ve lost {total_losses} times.')
print('The words were', all_picked_words)


