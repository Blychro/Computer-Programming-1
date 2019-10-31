# Thomas Marshall
# vigenere.py
# This program will take the message and keyword inputed by the user and uses a
# vigenere encryption to encode the message, all inside a graphics window.
# Inputs - message and keyword
# Output - encrypted message
# I certify that this lab is entirely my own work.

# Import graphics
from graphics import *

# Function name and strings for the initial message and keyword
def code(message, keyword):

    # Create alphabet string
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Create window
    width = 500
    height = 350
    win = GraphWin("Vigenere", width, height)
    instructions1 = Text(Point(75, 75), "Message to code")
    instructions1.draw(win)
    instructions2 = Text(Point(83, 150), "Enter Keyword")
    instructions2.draw(win)

    # draw message and keyword entry boxes.
    message.draw(win)
    keyword.draw(win)

    # Encryption "button"
    bP1 = Point(width/2 - 40, 220)
    bP2 = Point(width/2 + 40, 270)
    box = Rectangle(bP1, bP2)
    button = Text(Point(width/2, 245), "Encode")
    box.draw(win)
    button.draw(win)

    # Pause to type entry
    win.getMouse()

    # Transfer entry text to strings
    messageEntry = message.getText()
    keywordEntry = keyword.getText()

    # Uppercase and remove spaces in the strings
    messageEntry = messageEntry.replace(" ", "")
    messageEntry = messageEntry.upper()
    keywordEntry = keywordEntry.replace(" ", "")
    keywordEntry = keywordEntry.upper()

    # Create empty string for final encryption
    encoded = ""

    # Use loop to change the letter of the keyword in use
    for i in range(len(messageEntry)):
        # Create the key for the letter change
        key = keywordEntry[len(messageEntry[:i])%len(keywordEntry)]
        # Change the unencrypted letter to encrypted letter
        letter = alphabet[((ord(messageEntry[i])-ord("A")) + (ord(key)-ord("A")))%26]
        # Add each new letter to the final encryption
        encoded += letter

    # Remove "button"
    box.undraw()
    button.undraw()

    # Draw final encryption
    encrypted = Text(Point(width/2, 250), "Resulting Message\n" + str(encoded))
    encrypted.draw(win)

    # Instructions to close window
    end = Text(Point(width/2, height - 30), "Click to close")
    end.draw(win)

    # Close window
    win.getMouse()
    win.close()

def main():
    # Create inputs for the code function and activate function
    code(Entry(Point(250, 75), 20), Entry(Point(205, 150), 10))
    
    

# Activate main function
main()
