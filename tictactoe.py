# Thomas Marshall
# tictactoe.py
# Input - Moves on the board for players 1 and 2 as X and O respectively
# Outputs - The player turn, the board with the moves, and the victor or
# declares ties
# I certify that this lab is entirely my own work

# Function used to create the spots on the board
def num():
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Returns spots on board
    return numList

# Creates board
def board(numbers):
    print(str(numbers[0]) + " | "  + str(numbers[1]) + " | "  + str(numbers[2]))
    print("---------")
    print(str(numbers[3]) + " | "  + str(numbers[4]) + " | "  + str(numbers[5]))
    print("---------")
    print(str(numbers[6]) + " | "  + str(numbers[7]) + " | "  + str(numbers[8]))

# Determines if a move is legal
def legal(board, spot):
    # Not before 1, after 9, or already used
    return spot <= 9 and spot >= 1 and board[spot - 1] != "O" and board[spot - 1] != "X"

# Uses legal to block illegal moves
def tester(board, space):
    while legal(board, space) == False:
        print("Illegal move.\n")
        # Allows input to be redone
        space = eval(input("Please, enter a number between 1 and 9 that hasn't been used: "))
    # Returns the input
    return space

# Decides victor
def victor(numbers, mark):
    # Horizontal win
    if numbers[0] == mark and numbers[1] == mark and numbers[2] == mark:
        return True
    else:
        # Horizontal win
        if numbers[3] == mark and numbers[4] == mark and numbers[5] == mark:
            return True
        else:
            # Horizontal win
            if numbers[6] == mark and numbers[7] == mark and numbers[8] == mark:
                return True
            else:
                # Diagonal win
                if numbers[0] == mark and numbers[4] == mark and numbers[8] == mark:
                    return True
                else:
                    # Diagonal win
                    if numbers[2] == mark and numbers[4] == mark and numbers[6] == mark:
                        return True
                    else:
                        # Vertical win
                        if numbers[0] == mark and numbers[3] == mark and numbers[6] == mark:
                            return True
                        else:
                            # Vertical win
                            if numbers[1] == mark and numbers[4] == mark and numbers[7] == mark:
                                return True
                            else:
                                # Vertical win
                                if numbers[2] == mark and numbers[5] == mark and numbers[8] == mark:
                                    return True
                                else:
                                    # For when the game is not over
                                    return False

# The game itself
def game():
    # grabs the spaces
    numbers = num()
    # variable for while loop ending
    winner = 0
    # Set X to start
    mark = "X"
    # Creates turns
    for i in range(9):
        # Decides player turn
        player = (i % 2) + 1
        # Decides to continue the game
        if victor(numbers, mark) == False:
            # Player number decision
            if player == 1:
                mark = "X"
            else:
                mark = "O"
            # Gives player turn
            print("\nPlayer " + str(player) + "'s turn.\n")
            board(numbers)
            # Allows move input
            move = eval(input("\nEnter a number between 1 and 9 that hasn't "
                              "been used: "))
            # Checks to see if the move is possible
            test = tester(numbers, move)
            # Changes move for the next loop
            move = test
            # Places X or O depending on the turn
            if player == 1:
                numbers[test - 1] = "X"
            else:
                numbers[test - 1] = "O"
            print("")
        else:
            # If a winner is decided, it declares a winner
            if winner == 0:
                player = ((i + 1) % 2) + 1
                board(numbers)
                print("\nPlayer " + str(player) + " wins!")
                winner += 1

    # Declares a tie if necessary
    if victor(numbers, mark) == False:
        board(numbers)
        print("\nIt's a tie!")
    # Declares player 1 the winner in case of all the turns being used up
    else:
        if victor(numbers, mark) == True and winner == 0:
            board(numbers)
            print("\nPlayer 1 wins!")

# Runs the game
game()
