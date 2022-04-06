word = 'random'
def display_word():
    word_display = ''
    for l in word:
        if l in guess_list:
            word_display += l
        else:
            word_display += '_'
    print(word_display)
    
display_word()
total_guess = 7
guess_count = 0 

guess_list = []


while guess_count < total_guess:
    guess = input('Enter your guess: ').lower()
    # validate_guess(guess)
    if guess.isalpha():
        if guess == word:
            print('You won. Word is ' + word)
            break
        elif guess in word: 
            guess_list.append(guess)
            print(guess)
            display_word()
    else:
        print('Try again. Enter a word or letter this time')

# def validate_guess(guess):
#     if guess.isalpha():
#         print('valid')
#     else:
#         print('Try again. Enter a word or letter this time')