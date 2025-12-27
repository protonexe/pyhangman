import random
from wordlist import word_list
session_active=True
hangman_pics = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
def save(name,score):
    players=[]
    present=False
    try:
        with open("leaderboard.txt","r") as f:
            for i in f:
                i=(i.strip()).split(",")
                players.append([i[0],int(i[1])])
    except FileNotFoundError:
        pass
    for i in players:
        if i[0]==name:
            i[1]+=score
            present=True
            break
    if not present:
        players.append([name,score])
    with open("leaderboard.txt","w") as f:
        for i in players:
            f.write(f"{i[0]},{i[1]}\n")          

while session_active:
    print("WELCOME TO HANGMAN")
    selection=input("PLAY (1)\nVIEW LEADERBOARD (2)\nEXIT (3)\nENTER SELECTION:")
    if selection=="1":
        name=input("ENTER PLAYER NAME:")
        game=True
        incorrect=[]
        word=(random.choice(word_list)).upper()
        mistakes=0
        hint=""
        score=0
        print(hangman_pics[mistakes])
        guessed=[]
        for i in word: hint=hint+("_ ")
        while game==True:
            print(hint)
            print("INCORRECT LETTERS",incorrect)
            guess=input(("ENTER GUESS:")).upper()
            if guess in guessed:
                print("ALREADY GUESSED!")
            else:    
                if guess in word and len(guess)==1:
                    print(f"{guess} is in the word!")
                    for i in range(len(word)):
                        if word[i]==guess:
                            hint=hint.split()
                            hint[i]=guess
                            hint=" ".join(hint)
                    print(hangman_pics[mistakes])
                elif guess not in word and len(guess)==1:
                    for i in word: print("_",end=" ")
                    if guess not in incorrect: incorrect.append(guess)
                    mistakes+=1
                    print(hangman_pics[mistakes])
                else:
                    print("INVALID INPUT!")
                if "".join(hint.split())==word:
                    print("YOU WIN!")
                    score+=60-(mistakes*10)
                    save(name,score)
                    replayloop=True
                    while replayloop:
                        game_continue=input("CONTINUE GAME? (y/n)")
                        if game_continue=="y":
                            word=random.choice(word_list)
                            mistakes=0
                            hint=""
                            guessed=[]
                            for i in word: hint=hint+("_ ")
                            incorrect=[]
                            print(hangman_pics[mistakes])
                            replayloop=False
                        elif game_continue=="n":
                            game=False
                            replayloop=False
                        else:
                            print("INVALID INPUT")
                elif mistakes==6:
                    print("GAME OVER! YOU LOSE!\nTHE WORD WAS",word)
                    replayloop=True
                    game_continue=input("CONTINUE GAME? (y/n)")
                    while replayloop:
                        if game_continue=="y":
                            word=random.choice(word_list)
                            mistakes=0
                            hint=""
                            guessed=[]
                            for i in word: hint=hint+("_ ")
                            incorrect=[]
                            print(hangman_pics[mistakes])
                            replayloop=False
                        elif game_continue=="n":
                            game=False
                            replayloop=False
                        else:
                            print("INVALID INPUT")
                guessed.append(guess)
    elif selection=="2":
        leaderboard=[]
        print(f"LEADERBOARD:\nRANK NAME      SCORE")
        try:
            with open("leaderboard.txt","r") as f:
                for i in f:
                    i=i.strip()
                    i=i.split(",")
                    leaderboard.append([i[0],int(i[1])])
            leaderboard.sort(key=lambda x:x[1],reverse=True)
            for i in range(len(leaderboard)):
                print(f"{i+1:<5}{leaderboard[i][0]:<10}{leaderboard[i][1]}") 
        except FileNotFoundError:
            print("No saves yet!")

    elif selection=="3":
        print("Exiting...")
        session_active=False
    
            


        
