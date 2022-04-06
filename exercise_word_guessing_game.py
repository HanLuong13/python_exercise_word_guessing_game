import random
total_losses = 0
total_wins = 0
num_plays = 1

# def loss_count():
#     global total_losses
#     total_losses += 1
#     return total_losses

def display_word(input):
    global word_display
    word_display = ''
    for l in input:
        if l in already_guessed_right:
            word_display += l
        else:
            word_display += '_'
    print('Word: ')
    print(word_display)
    return word_display

def pick_word():
    global all_picked_words 
    global word
    all_picked_words = []
    file_path = (r'H:\words_alpha.csv')
    file = open(file_path)
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

def play_game():
    global total_losses, total_wins
    global already_guessed_right
    global guessed_right
    global guess_count
    already_guessed_right = []
    already_guessed_wrong = {}
    word_guess_list_wrong = set()
    word = pick_word()
    display_word(word)
    total_guess = 2
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
                if guess in word and guess in already_guessed_right: 
                    print('You have already tried this letter. Do better!')
                elif guess in word and guess not in already_guessed_right:
                    already_guessed_right.append(guess)
                    print(guess) 
                    display_word(word)
                    if '_' not in word_display:   
                        guessed_right = True 
                        break
                elif guess in already_guessed_wrong.values():
                    print('You have already tried this. It wasn\'t in the word. Do better!')
                else: 
                    print('Letter not in word. Try again.')
                    guess_count += 1
                    already_guessed_wrong[guess_count] = guess                    
        else: #not valid input
            print('Try again. Enter a word or letter this time')
    if guessed_right:
        print('You won! The word is {}!'.format(word))
        total_wins += 1
    else:
        print('You\'ve tried {} times. You lost. The word is {}. Game over!'.format(guess_count, word))
        total_losses += 1
    play_again()

    # return num_plays
    # return total_wins, total_losses

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
            print('That is fine. You have played {} times.'.format(num_plays))
            break
        else:
            print('Not valid input. Try again.')

# def win_count():
#     global total_wins
#     total_wins = 0
#     total_wins += 1
#     return total_wins

# def loss_count():
#     global total_losses
#     total_losses = 0 
#     total_losses += 1
#     return total_losses

# print('Total wins: {}'.format(total_wins))



play_game()
print('Total losses: {}'.format(total_losses))
print('Number of times played: ', num_plays)

# def validate_guess(guess):
#     if guess.isalpha():
#         print('valid')
#     else:
#         print('Try again. Enter a word or letter this time')

