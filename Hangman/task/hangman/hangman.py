import random

print("H A N G M A N")
wins = 0
losses = 0

while True:
    instruction = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if instruction == "results":
        print(f"You won: {wins} times")
        print(f"You lost: {losses} times")
        continue

    elif instruction == "exit":
        break;

    elif instruction == "play":
        words = ["python", "java", "swift", "javascript"]
        word_original = random.choice(words)
        word = word_original
        guessed_letters = ""

        word_progress = "-" * (len(word))
        # while "-" in word_progress:
        wrong_attempts = 0

        while wrong_attempts < 8:
            print()
            print(word_progress)

            if "-" not in word_progress:
                print(f"You guessed the word {word_progress}!")
                print("You survived!")
                wins += 1
                break

            guess = input("Input a letter:")

            if (len(guess) != 1):
                print("Please, input a single letter.")
                continue

            if not guess.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue


            if guess in guessed_letters:
                print("You've already guessed this letter.")
                continue

            if guess in word_original:
                if guess in word:
                    for letter in range(word.count(guess)):
                        word_update = word_progress[:word.find(guess)] + guess + word_progress[word.find(guess) + 1:]
                        word2 = word[:word.find(guess)] + "_" + word[word.find(guess) + 1:]
                        word = word2
                        word_progress = word_update

                else:
                    print("You've already guessed this letter.")
                    guessed_letters = guessed_letters + guess
            else:
                print("That letter doesn't appear in the word.")
                guessed_letters = guessed_letters + guess
                wrong_attempts += 1;

        print()
        if "-" in word_progress:
            print("You lost!")
            losses += 1

        continue

    else:
        continue
