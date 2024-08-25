#Inicio do estudo de orientação a objetos, classes e métodos

from random import randint
import os

class TicTacToe:

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.o = 'O'
        self.x = 'X'
        self.done = " "


    def player_move(self):
        while True:
            try:
                print('Input index line of board:')
                x = int(input())
                print('Input index column of board:')
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Invalid value.')
                if self.board[x][y] != " ":
                    print('Satisfied position, choice another position.')
                    continue
            except Exception as e:
                print(e)
                continue

            self.board[x][y] = self.x
            break


    def machine_move(self):
        while True:
            self.num1 = randint(0,2) 
            self.num2 = randint(0,2)

            try:
                if self.board[self.num1][self.num2] == " ":
                    self.board[self.num1][self.num2] = self.o
                    break
            except Exception as e:
                print(e)
                continue
            
                
    def show_board(self):
        print("\n")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " " )
        print("----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " " )
        print("----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " " )


    def check_win_draw(self):
        conditions = {}

        for i in ['X', 'O']:

            conditions[i] = self.board[0][0] == self.board[0][1] == self.board[0][2] == i
            conditions[i] = self.board[0][0] == self.board[1][0] == self.board[2][0] == i or conditions[i]
            conditions[i] = self.board[0][0] == self.board[1][1] == self.board[2][2] == i or conditions[i]
            conditions[i] = self.board[0][2] == self.board[1][2] == self.board[2][2] == i or conditions[i]
            conditions[i] = self.board[2][0] == self.board[2][1] == self.board[2][2] == i or conditions[i]
            conditions[i] = self.board[0][2] == self.board[1][1] == self.board[2][0] == i or conditions[i]
            conditions[i] = self.board[1][0] == self.board[1][1] == self.board[1][2] == i or conditions[i]
            conditions[i] = self.board[0][1] == self.board[1][1] == self.board[2][1] == i or conditions[i]
            
        if conditions['X']:
            print('Player win!')
            self.done = 'x'
            return

        if conditions['O']:
            print('Machine win!')
            self.done = 'o'
            return

        draw = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    draw += 1
                    break

        if draw == 0:
            print('Draw!')
            self.done = 'd' 
            return
        

    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]            
            

#Code
test = TicTacToe()

next = 0
while next==0:
    os.system('cls')
    while test.done == " ":
        test.show_board()
        test.machine_move()
        test.check_win_draw()
        test.show_board()
        test.player_move()
        os.system('cls')
        test.check_win_draw()
        if test.done != " ":
            test.show_board()


    print('Enter 1 to exit or 0 to continue:')
    next = int(input())
    if next == 1:
        print("Good game!")
        break

    else:
        test.reset()
        next = 0
        test.done = " "
