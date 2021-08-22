"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 2PM
*Title  : Tic Tac Toe Game

"""
import random

square = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def mainMethod():

    playerChoose = int(input("Choose Player 1 or 2::"))
    if playerChoose==1:
        player = 1
    else:
        player = 2
    status = -1
    playerName = input("Enter Player name:: ")

    while status == -1:
        board()
        if player % 2 == 1:
            player = 1
        else:
            player = 2

        print('\nPlayer', player, 'is', playerName)

        if player == 1:
            choice = int(input('Enter a number:'))
            mark = 'X'
        else:
            choice=random.randrange(1,9)
            print("Value Choose by Computer : ",choice)
            mark = 'O'

        if choice == 1 and square[1] == 1:
            square[1] = mark
        elif choice == 2 and square[2] == 2:
            square[2] = mark
        elif choice == 3 and square[3] == 3:
            square[3] = mark
        elif choice == 4 and square[4] == 4:
            square[4] = mark
        elif choice == 5 and square[5] == 5:
            square[5] = mark
        elif choice == 6 and square[6] == 6:
            square[6] = mark
        elif choice == 7 and square[7] == 7:
            square[7] = mark
        elif choice == 8 and square[8] == 8:
            square[8] = mark
        elif choice == 9 and square[9] == 9:
            square[9] = mark
        else:
            print('Already Occupied Please Try Another Choice')
            player -= 1

        status = game_status()
        player += 1

    print('RESULT')
    if status == 1:
        print(playerName,'win')
    else:
        print('Game draw')


def game_status():

    if square[1] == square[2] and square[2] == square[3]:
        return 1
    elif square[4] == square[5] and square[5] == square[6]:
        return 1
    elif square[7] == square[8] and square[8] == square[9]:
        return 1
    elif square[1] == square[4] and square[4] == square[7]:
        return 1
    elif square[2] == square[5] and square[5] == square[8]:
        return 1
    elif square[3] == square[6] and square[6] == square[9]:
        return 1
    elif square[1] == square[5] and square[5] == square[9]:
        return 1
    elif square[3] == square[5] and square[5] == square[7]:
        return 1
    elif square[1] != 1 and square[2] != 2 and square[3] != 3 and square[4] != 4 and square[5] != 5 and square[
        6] != 6 and square[7] != 7 and square[8] != 8 and square[9] != 9:
        return 0
    else:
        return -1

def board():
    print(' ', square[1], ' | ', square[2], ' |  ', square[3])

    print('_____|_____|_____')
    print('-----------------')
    print('     |     |     ')

    print(' ', square[4], ' | ', square[5], ' |  ', square[6])

    print('_____|_____|_____')
    print('-----------------')
    print('     |     |     ')

    print(' ', square[7], ' | ', square[8], ' |  ', square[9])

mainMethod()