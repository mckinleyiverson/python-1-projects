import random
import os

class colors:
    
    GREEN = '\033[92'
    YELLOW = '\033[93'
    END = '\033[0m'

def pick_secret_word(word_list):

    current_dir =os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'word_list')
    
    file_handle = open(file_path)
    for line in file_handle:
        word = line.rstrip()
        if len(word) == 5:
            word_list.append(word)
    return random.choice(word_list)


def color(users_word, secret_word):

    for letter_index in range(len(users_word)):
        letter = users_word[letter_index]
        print_letter = []

        if letter == secret_word[letter_index]:
            print(colors.GREEN + letter + colors.END, end = '')

        elif letter in secret_word:
            print(colors.YELLOW + letter + colors.END, end = '')

        else:
            print(letter, end='')

    print()

def read_win_streak():
    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'win_streak.txt')
        with open('file_path') as file:
            return int(file.read().strip())

    except FileNotFoundError:
        return 0 

def write_win_streak(streak):

    current_dir =os.path.dirname(__file__)
    file_path =os.path.join(current_dir, 'win_streak.txt')
    with open(file_path, 'w') as file:
        file.write(str(streak))
        

def wordle_game():
    print('Hello and welcome to Wordle!')
    win_streak = read_win_streak()
    print(f'Your current win streak is {win_streak}')
    word_list = []

    secret_word = pick_secret_word(word_list)

    print(secret_word)



    guesses_left= 6
    while guesses_left > 0:
        users_word= input('What is your guess? It has to be 5 letters:')
        users_word=users_word.lower()
        if not users_word.isalpha():
           print('Sorry try again with only LETTERS.')
        elif len(users_word) != 5:
             print('try again with FIVE letters')
        elif users_word not in word_list:
            print('That is not a word. Try useing an actual word')
        else:
            guesses_left -= 1
            print(f'Your guess: {users_word}')
            if users_word == secret_word:
                print('Yay you guessed the word!')
                win_streak += 1
                write_win_streak(win_streak)
                break
            else:
                color(users_word, secret_word)
            print(f'Try again! You have {guesses_left} guesses remaining')
    else:
        win_streak = 0
        write_win_streak(win_streak)
        print('Sorry you lost and your win streak was set back to 0')
    print('Please come back to play again later!')
        

if __name__ == '__main__':

    wordle_game()