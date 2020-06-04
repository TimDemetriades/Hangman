from random import choice

print('H A N G M A N')
while True:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == "exit":
        break
    elif play != "play":
        continue
    print()

    word_list = ['python', 'java', 'kotlin', 'javascript']
    answer = choice(word_list)      # random word from list

    word_so_far = list("-" * len(answer))       # word is a list of dashes to start

    lives = 8
    guessed_letters = []

    while True:  

        # print word so far
        for i in word_so_far:
            print(i, end='')

        print()

        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
            print()
            continue        # Repeat while loop

        if guess.isupper() or not guess.isalpha():     # isalpha checks for letters a-z
            print("It is not an ASCII lowercase letter")
            print()
            continue

        # check if guess matches any letters of answer
        # if it does add location to a list
        locations = [i for i in range(len(answer)) if answer.startswith(guess, i)]      

        if guess in guessed_letters:      # check if letter already guessed
            print("You already typed this letter")
        elif not locations:       # check if locations list is empty
            print("No such letter in the word")
            guessed_letters.append(guess)               # add guessed letters to a list
            lives -= 1
        else:
            for i in range(len(locations)):
                word_so_far[locations[i]] = guess       # adjust word so far based on locations of letter guessed
            guessed_letters.append(guess)               # add guessed letters to a list

        if lives == 0:      # out of lives
            print("You are hanged!")
            break

        if "-" not in word_so_far:      # guessed all the letters
            print()
            for i in word_so_far:
                print(i, end='')        # print word
            print()
            print("You guessed the word!")
            print("You survived!")
            break

        print()
