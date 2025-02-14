import random

def choose_word():
    words = ['python', 'hangman', 'developer', 'programming', 'challenge']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum incorrect guesses allowed
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()
