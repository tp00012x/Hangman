import random
with open("wordlist.txt", "r") as mywordlist:
    wordlist = [i.strip() for i in mywordlist.readlines() if not ("-" in i or "(" in i)]

def play_hangman():
    computerword = random.choice(wordlist)
    correct_letter = []
    incorrect_letter = []
    foundation =["_"]*len(computerword)
    game_over = False
    tries = 0
    while not game_over:
        print("Incorrect letters:")
        print(",".join(incorrect_letter))
        print("Current word:")
        print("".join(foundation))
        while(1):
            tryletter = str(input("Enter a letter "))
            if tryletter in (correct_letter+incorrect_letter):
                print("You already guessed that letter, guess again")
            elif len(tryletter) != 1:
                print("Only enter one letter")
            elif tryletter in [str(x) for x in range(10)]:
                print("No numbers, guess again")
            else:
                break
        if tryletter in computerword:
            correct_letter.append(tryletter)
            print("You got a letter right")
            for i in range(len(computerword)):
                if tryletter == computerword[i]:
                    foundation[i] = tryletter
            if "".join(foundation) == computerword:
                print("You guessed " + computerword)
                print("YOU WIN!!!!!!!!")
                game_over = True
        else:
            print("You guessed wrong!")
            incorrect_letter.append(tryletter)
            tries += 1
            if tries == 7:
                game_over = True
                print("Game over! You lose!")
                print("The correct word was: " + computerword)
