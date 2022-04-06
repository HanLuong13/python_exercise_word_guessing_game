word = 'random'

total_guess = 2
guess_count = 0 

guess_list = []
guess_list_wrong = []

def display_word():
    word_display = ''
    for l in word:
        if l in guess_list:
            word_display += l
        else:
            word_display += '_'
    print(word_display)

# print('Word: ', display_word())

while guess_count < total_guess:
    guess = input('Enter your guess: ').lower()
    # validate_guess(guess)
    if guess.isalpha():
        if guess == word:
            print('You won! Word is ' + word + '!')
            guess_count += 1
            break
        elif guess in word: 
            guess_list.append(guess)
            print(guess)
            display_word()
        else:
            if guess in guess_list_wrong:
                print('You have already tried this. Do better!')
            else:
                print('Letter not in word')
                guess_count += 1
                guess_list_wrong.append(guess)
    else:
        print('Try again. Enter a word or letter this time')

print('You\'ve tried', guess_count, 'times. You lost. Game over!')

# def validate_guess(guess):
#     if guess.isalpha():
#         print('valid')
#     else:
#         print('Try again. Enter a word or letter this time')