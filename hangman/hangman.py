import pyinputplus as pyip
import collections

"""
Making guesses on a hangman game. Tried guessing by frequency but the word list is too small. Guessing from a larger database seems to be the best.

Finding some problems where words have too many consonants. By occurance, first guess will almost always be a vowel. 
Have to implement a rule that, if a vowel is found on a small word, it will probably be best to start guessing some consonants.
"""

def print_game(game):
    board = game[1]
    return print(' '.join([letter if letter!=False else '_ ' for letter in board]))


def board_info(game):
    """
    From the game board, gets each letter placement in the for of [[letter, position], [letter, position], ...]
    """
    info = []
    for index, letter in enumerate(game[1]):
        if letter:
            info.append([index,letter])
    return info


def calculated_guess(game, word_list):
    """
    Guesses based on frequency of a letter in a word of a certain size and on letter positioning.
    """
    if 0 not in game[1]:
        yield None
    # first guess if board is all blank
    if game[1] == [0]*len(game[1]):
        possibilities = [word for word in word_list if len(word) == len(game[0])]
        letters = [l for word in possibilities for l in word]
        letters_count = collections.Counter(letters)
        frequency = letters_count.most_common()
        for index in range(len(frequency)):
            if frequency[index][0] not in game[1]:
                yield frequency[index][0]
    else:
        possibilities = [word for word in word_list if len(word) == len(game[0])]
        word_info = board_info(game)
        for info in word_info:
            possibilities = [word for word in possibilities if word[info[0]]==info[1]]
        letters = [l for word in possibilities for l in word]
        letters_count = collections.Counter(letters)
        frequency = letters_count.most_common()
        for index in range(len(frequency)):
            if frequency[index][0] not in game[1]:
                yield frequency[index][0]


def take_a_guess(game, guess):
    "Analyze a guess for three otipns: Already guessed, wrong guess, correct guess."
    check = False
    if guess in game[1]:
        print("You've already guessed that")
        return False, game
    for index, letter in enumerate(game[0]):
        if letter == guess:
            hang_board[index] = letter
            check = True
    if not check:
        game[2] = game[2] - 1
        print("Wrong Guess!")
    else:
        print("Correct Guess!")
    print_game(game)
    print(f'You have {hangman[2]} lives.')
    return check, game


def complete(game):
    if 0 not in game[1]:
        print("Got it!")
        return True
    if game[2] <= 0:
        print("Failed :(")
        return True
    else:
        return False


with open('words_db.txt', newline='') as file:
     words = [word.rstrip('\r\n') for word in file]

	 
# Starting the game
lives = 8
print("Type the chosen word: ")
hang_word = pyip.inputStr()
hang_board = [0]*len(hang_word)
hangman = [hang_word, hang_board, lives]
print_game(hangman)

# # Playing the game as user input
# while not complete(hangman):
#     print("Guess a letter:" )
#     guess = pyip.inputStr()
#     result, hangman = take_a_guess(hangman, guess)


# Computer guesses
guess_track = set()
while not complete(hangman):
    result = False
    gen_guess = calculated_guess(hangman, words)
    while not result:
        guess = next(gen_guess)
        if guess not in guess_track:
            guess_track.add(guess)
            result, hangman = take_a_guess(hangman, guess)
