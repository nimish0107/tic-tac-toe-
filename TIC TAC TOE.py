"""
Description of game
2 player should be able to play game sitting on same computer

board must be printed out everytime player makes a move

should be able to accept the input of player position and then place a symbol on board

we will be using idea of a numpad to match numbers to the grid on tic tac toe board
"""
def display_rules():
    """To Display The Rules of The Game"""
    print("All the rules are same to a basic tic tac toe game")
    print("To input your choice in board we will be using a numpad format which will be off form:")
    print("\n")
    print("7","|","8","|","9")
    print("_"*10,"\n")
    print("4","|","5","|","6")
    print("_"*10,"\n")
    print("1","|","2","|","3")
def display_board(board):
    """To Display the board"""
    print("\n"*100)
    print("\nCurrently the board looks like: \n")
    print(board[7],"|",board[8],"|",board[9])
    print("_"*10,"\n")
    print(board[4],"|",board[5],"|",board[6])
    print("_"*10,"\n")
    print(board[1],"|",board[2],"|",board[3])
def choose_p1():
    """To get player's choice what he wants to take."""
    kya_lega = input("Please enter your choice Player1 X or O : ").upper()
    while kya_lega not in ["X","O"]:
        kya_lega = input("Please enter a valid choice Player1 among X or O : ").upper()
    if kya_lega == "X":
        return ["X","O"]
    elif kya_lega == "O":
        return ["O","X"]
def input_position(board):
    """To get input from player about what position he wants to enter his mark"""
    kaha_lagau = input("Please Enter a position from 1 to 9 :")
    position_list = ["1","2","3","4","5","6","7","8","9"]
    while (kaha_lagau not in position_list) or space_check(board,int(kaha_lagau)) == False:
        kaha_lagau = input("Enter a valid position from 1 to 9 :")
    else:
        return int(kaha_lagau)
def place_marker(board, marker, position):
    """To place mark on board at required position"""
    board[position] = marker
    return board

def win_check(board, mark):
    """To check if player has won or not"""
    if board[1] == " " and board[3] == " " and board[5] == " " and board[7] == " " and  board[9] == " " :
        return False
    elif board[1] == mark and board[2] == mark and board[3] == mark :
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[9] == mark and board[5] == mark and board[1] == mark:
        return True
    else:
        return False

def choose_first():
    """To choose which player goes first"""
    player_list = ["player 1","player 2"]
    return random.choice(player_list)
def space_check(board, position):
    """To check if desired space is available on board or not"""
    return board[position] == " "
def full_board_check(board):
    """To check if board is completely filled or not"""
    return (" " not in board)

def replay():
    tell_me = input("Enter Y to play again and N to quit")
    while tell_me not in ["Y","N"]:
        print("Please Enter a valid choice . . .")
        tell_me = input("Enter Y to play again and N to quit")
    if tell_me == "Y":
        return True
    else:
        return False


import random

print("WELCOME TO TIC TAC TOE . . .")
display_rules()
while True:
    board = [None] + [" "] * 9

    how_to_start = choose_p1()
    who_starts = choose_first()
    if who_starts == "player 1":
        pass
    elif who_starts == "player 2":
        how_to_start.reverse()
    display_board(board)
    while full_board_check(board) == False:
        if win_check(board, "O") == True:
            break
        elif win_check(board, "X") == True:
            break
        for i in how_to_start:
            display_board(board)
            if win_check(board, "O") == True:
                print("O has won the game")
                break
            elif win_check(board, "X") == True:
                print("X has won the game")
                break

            if full_board_check(board) == False:
                display_board(board)
                print(f"It's {i} turn")
                position = input_position(board)
                print(position)
                board = place_marker(board, i, position)

    else:
        print("game tied")

    again = replay()
    if again == False:
        print("exiting . . . ")
        break