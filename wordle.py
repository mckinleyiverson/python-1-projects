import random

class colors:
    
    GREEN = '\033[92'
    YELLOW = '\033[93'
    END = '\033[0m'

def pick_secret_word():
    words = ['carry','filth','dress','drink','elite','globe','fifty','drive','dying','grant','grade','grand','great','green','empty','level','power','press','mayor','match','phase','photo','place','piece','pitch','pilot','proof','refer','ready','reach','raise','round','march','music','mouse','party','other','prime','print','proud','right','spend','speed','shift','shock','taken','touch','tough','tired','stick','union','water','three','trudy','upset','valid','visit','voice','worry','would','white','tight','upper','brain','booth','bread','break','breed','chose','claim','cream','craft','blind','black','class','chair','chart','clear','event','brown','dealt','frank','error','exact','entry','child','extra','dozen','dramma','fresh','happy','grown','dream','drill','earth','after','angry','angle','about', 'adult','above', 'alert','beach','began','alone','alive','among']
    return random.choice(words)

def color(users_word, secret_word):
    for letter_index in range(len(users_word)):
        letter = users_word[letter_index]
        if users_word[letter_index] == secret_word[letter_index]:
        
            print(colors.green + 'Green' + colors.END, end = '')

        elif users_word[letter_index] in secret_word:
            print(colors.YELLOW + letter + colors.END, end = '')

        else:
            print(letter, ends='')

    print(users_word)
    

def wordle_game():
    print('Hello and welcome to Wordle! Are you ready to have some fun?!? Ok good luck!')
    secret_word=pick_secret_word()
    print(secret_word)

    guesses_left= 6
    while guesses_left > 0:
        users_word= input('What is your guess? It has to be 5 letters.')
        users_word=users_word.lower()
        if not users_word.isalpha():
            print('Sorry try again with only LETTERS.')
        elif len(users_word) != 5:
            print('try again with FIVE letters')
        else:
            guesses_left -= 1
            print(f'Your guess: {users_word}')
        if users_word == secret_word:
            print('Yay you guessed the word!')
            break
        else:
            color(users_word, secret_word)
        print(f'Try again! You have {guesses_left} guesses remaining')

wordle_game()