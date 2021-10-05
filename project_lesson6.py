

WORDS = ["rabbit", "computer", "mask"]


word = 'rabbit'
lives = 7
guessed_letters = []

while True:
    for c in word:
        if c in guessed_letters:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()
    print(f'Lives {lives}')
    print(f'Guessed Letters{guessed_letters}')

    guess = input("Enter the letter: ")
    guessed_letters.append(guess)
    if guess in word:
        print('You guessed')
    else:
        lives -=1
        print('You are wrong')
    if len(set(guessed_letters) & set(word)) == len(set(word)):
        print(f'You won. World {word} is correct!')
        break
    elif lives == 0:
        print(f'Game Over! You out of lives. The word was {word}')