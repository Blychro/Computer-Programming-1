# Thomas Marshall
# hangman.py
# This program will allow the user to play hangman as many times as they want.
# Inputs - Guessing a letter and answering whether or not they want to play again
#   Outputs - The letters used, building the hangman, filling the correct letters
#   in the word at the time of the input, and the win/lose message
# I certify that this is entirely my own work

# Imports
import random
from graphics import *

# Imports a list of words
def secretList():
    # Opens file
    words = open("wordlistgames.txt", "r")

    # Returns list of words
    return words

# Randomly picks a word from the list
def secretWord(words):
    # Empty list for later
    wordList = []
    # Create a list out of the words given in the file
    for word in words:
        # Gets rid of the enter signs at the end
        word = word.replace("\n", "")
        wordList.append(word)
    # Randomizer to find a word
    randWord = random.randrange(0, len(wordList)-1)
    # Defines said word
    word = wordList[randWord]
    
    # Returns the word
    return word

# Breaks the word into a list of letters (This was mostly for prep, but it wound up
# deeply integrated into the code so I kept it).
def wordFind(word):
    # Empty list for the letters
    letters = []
    for letter in word:
        letters += letter

    # Returns letter list
    return letters

# Creates the underscores needed for the game
def gameWord(word):
    # Empty list for the underscores
    show = []
    
    # Makes however many underscores are necessary, depending on the word
    for i in range(len(word)):
        show += "_"

    # Returns the string of underscores
    return show

# Changes the underscore to the appropriate letter
def replace(word, newWord, guess):
    # Counts for setup
    count = 0
    count2 = 0
    # In case of a wrong answer
    turn = False

    # Cycle through each letter in the answer
    for letter in word:
        # Checks to see if the letters match
        if letter == guess:
            # Replaces the underscores with the correct letters (even duplicates).
            newWord[count] = letter
        else:
            # Counts up how many missed letters there were
            count2 += 1
        # Counts up how many interations there were
        count += 1
    # Checks to see if there were the same amount of misses as letters
    if count != count2:
        turn = True

    # Returns if it was a correct answer
    return turn

# Counter measure in case of a missclick, multiplee letters, things that are not letters,
# or repeated letters
def check(letterGuess, tries):
    # In case of no errors
    attempt = True
    # Alphabet string for later
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Set up a counter
    counter = 0

    # Checks for repeats
    for letter in tries:
        if letter == letterGuess:
            attempt = False

    # Checks to see if the letter is a single letter that exists in the alphabet
    for count in alphabet:
        if letterGuess != count:
            counter += 1
    if counter == 26:
        attempt = False

    # Returns if it was a vallid move
    return attempt
    
# Builds a list of the hangman
def parts():
    # Empty prep list
    pieces = []

    # Defines each piece of the hangman added after each miss and
    # appends the to the empty string
    head = Circle(Point(174, 160), 10)
    pieces.append(head)
    neck = Line(Point(174, 170), Point(174, 175))
    pieces.append(neck)
    armL = Line(Point(174, 175), Point(160, 190))
    pieces.append(armL)
    armR = Line(Point(174, 175), Point(190, 190))
    pieces.append(armR)
    body = Line(Point(174, 175), Point(174, 210))
    pieces.append(body)
    legL = Line(Point(174, 210), Point(168, 240))
    pieces.append(legL)
    legR = Line(Point(174, 210), Point(180, 240))
    pieces.append(legR)

    # Returns the list of body parts
    return pieces

# Decides if the player wins
def winner(word, newWord):
    # Returns the answer
    return word == newWord

# Checks to see if the clicks given were inside the buttons
def button(click):
    # In case they missed
    press = False
    
    # Grabs x and y values
    clickX = click.getX()
    clickY = click.getY()

    # Checks Yes
    if (clickX < 230 and clickY < 455) and (clickX > 170 and clickY > 405):
        press = True

    # Checks No
    if (clickX < 330 and clickY < 455) and (clickX > 270 and clickY > 405):
        press = True

    # Returns if a button was hit
    return press


# Sees what button was pressed
def play(click):
    # Yay, x and y values!
    clickX = click.getX()
    clickY = click.getY()

    # I'm hungry, can you tell? Gives parameters for Yes
    if (clickX < 230 and clickY < 455) and (clickX > 170 and clickY > 405):
        return True

# Creates a string of the word to use in the loss message
def fullWord(word):
    # Empty string
    wordString = ""
    # Adds to the string
    for letter in word:
        wordString += letter

    # Returns the word
    return wordString

# The game itself, took long enough to get here
def hangman(word, newWord, pieces):
    # Window build (smae old, same old)
    width = 500
    height = 500
    win = GraphWin("Hangman", width, height)

    # Magnificent game title
    title = Text(Point(width/2, 20), "HANGMAN!")
    title.draw(win)

    # Horizontal pole
    pole = Line(Point(100, 100), Point(100, 250))
    pole.setWidth(5)
    pole.draw(win)

    # Vertical pole
    pole2 = Line(Point(100, 102), Point(175, 102))
    pole2.setWidth(5)
    pole2.draw(win)

    # Rope to hang the thieving liar with
    rope = Line(Point(174, 150), Point(174, 102))
    rope.setWidth(2)
    rope.setFill("brown")
    rope.setOutline("brown")
    rope.draw(win)

    # Text to explain the letter listings
    guesses = Text(Point(width/2, 280), "Guesses")
    guesses.draw(win)

    # Lives count (ended up backwards to my original code so I improvised the life count)
    miss = 1
    # Lives inverse to chances
    lives = str(8 - miss)
    # Display, would not be fair otherwise
    showLives = Text(Point(width/2, 60), "Lives = " + lives)
    showLives.draw(win)

    # Text set up for the used letters
    shown = Text(Point(width/2, 300), "")
    shown.draw(win)

    # Text set up for the answer, starts as a bunch of underscores and slowly works its way
    # to being a star. Depending on if the word was star at least
    showWord = Text(Point(350, 230), newWord)
    showWord.draw(win)

    # Text setup for an illegal move. Hey, a message is better than prison
    invalid = Text(Point(width/2, height - 160), "")
    invalid.draw(win)

    # Empty list (wow I made a lot of these) for the used letters
    tries = []

    # Game "timer." Win without missing 7.
    while miss <= 7 and newWord != word:
        # Gotta love me another setup, except this one is a reset switch
        invalid.setText("")

        # Builds input message and input bar
        letterGuessHelp = Text(Point(width/2 - 30, height - 20), "Enter a letter: ")
        letterGuessHelp.draw(win)
        
        letterGuess = Entry(Point(width/2 + 30, height - 20), 2)
        letterGuess.draw(win)

        # Stalls window to allow entry
        win.getMouse()

        # Turns the box input into a string for checking
        letterGuess = letterGuess.getText()

        # Checks to see if the move was legal (and it is only possible thanks
        # to the last line).
        while check(letterGuess, tries) == False:
            # Tells the user they done goofed
            invalid.setText("Invalid input. Try again.")
            
            # Redoes all the fun stuff from above to allow a do over
            letterGuess = Entry(Point(width/2 + 30, height - 20), 2)
            letterGuess.draw(win)
            
            win.getMouse()
            
            letterGuess = letterGuess.getText()

        # Adds the newest used letter into the list of used
        # letters (see these lists all got used for something).
        tries.append(letterGuess)

        # Speaking of lists, this won shows off all your past guesses. Isn't that great?
        shown.setText(tries)

        # Changes those nasty underscores into beautiful letters
        replace(word, newWord, letterGuess)

        # Draws the next part of that lying thief (if you didn't notice I
        # switched the description from last time) and takes a life (that monster,
        # no regard for other people's extra lives).
        if replace(word, newWord, letterGuess) != True:
            
            pieces[miss - 1].draw(win)
            # Increases miss count
            miss += 1
            # Same life hack as before to keep the lives going down as misses go up
            lives = str(8 - miss)

        # Changes the life count so it doesn't lie to people
        showLives.setText("Lives = " + lives)

        # Changes the window to show the newly found letters
        showWord.setText(newWord)

    # Gives the word string a name
    wordString = fullWord(word)

    # Finally out of that loop (took long enough), this decides if you win or not.
    if winner(word, newWord) == True:
        end = Text(Point(width/2, height - 160), "You Win!")
    else:
        end = Text(Point(width/2, height - 160), "Sorry, you lose.\nThe word was "
                + str(wordString))
        
    # And this shows which message was picked
    end.draw(win)

    # Asks the user if they want to risk another person's life-I mean play again.
    again = Text(Point(width/2, 380), "Play again?")
    again.draw(win)

    # Builds up the wonderful Yes button
    yes = Rectangle(Point(170, 405), Point(230, 455))
    yes.setFill("blue")
    yes.draw(win)
    yesWord = Text(Point(200, 430), "Yes")
    yesWord.draw(win)

    # Creates an interstingly red No button
    no = Rectangle(Point(330, 405), Point(270, 455))
    no.setFill("red")
    no.draw(win)
    noWord = Text(Point(300, 430), "No")
    noWord.draw(win)

    # Pause for suspense... oh and also input
    click = win.getMouse()

    # Keeps recycling the same thing until a button gets pressed
    while button(click) == False:
        click = win.getMouse()

    # Closes the window
    win.close()

    # Returns which button was pressed
    return click

# The last function, the one that runs the full game
def main():
    # As to not crash the whole loop before it starts
    count = 0
    # Runs it all over again in case the user wants to play again
    while  count == 0 or play(game) == True:
        # Count is nno longer needed, or useful
        count = 1

        # A bunch of functions being defined as to be used again and all pretty
        # like and to keep the same randomly selected word. Also all this runs the full game
        words = secretList()
        word = secretWord(words)
        pieces = parts()
        wordSelect = wordFind(word)
        newWord = gameWord(word)
        game = hangman(wordSelect, newWord, pieces)
        game

# Auto-run is everyone's friend. I'm sorry if these comments got weird.
# I wanted to finish them before going to eat, and I've been, slowly, going crazy.
main()
