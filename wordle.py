import random

def pick_secret_word():
    words = ['carry','filth','dress','drink','elite','globe','fifty','drive','dying','grant','grade','grand','great','green','empty','level','power','press','mayor','match','phase','photo','place','piece','pitch','pilot','proof','refer','ready','reach','raise','round','march','music','mouse','party','other','prime','print','proud','right','spend','speed','shift','shock','taken','touch','tough','tired','stick','union','water','three','trudy','upset','valid','visit','voice','worry','would','white','tight','upper','brain','booth','bread','break','breed','chose','claim','cream','craft','blind','black','class','chair','chart','clear','event','brown','dealt','frank','error','exact','entry','child','extra','dozen','dramma','fresh','happy','grown','dream','drill','earth','after','angry','angle','about', 'adult','above', 'alert','beach','began','alone','alive','among']
    return random.choice(words)

def wordle_game():
    print('Hello and welcome to Wordle! Are you ready to have some fun?!? Ok good luck!')
    secret_word=pick_secret_word()
    print(secret_word)
    
    for guesses_left in range(5,-1,-1):
        users_word= input('What is your guess? It has to be 5 letters.')
        users_word=users_word.lower()
        if not users_word.isalpha():
            print('Sorry try again with only LETTERS.')
        elif len(users_word) != 5:
            print('try again with FIVE letters')
        else:
            print(f'Your guess: {users_word}')
        if users_word == secret_word:
            print('Yay you guessed the word!')
            break
        else:
            print(f'That was a good guess but not quite right, you have {guesses_left} guesses remaining')

wordle_game()