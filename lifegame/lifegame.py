# -*- coding:utf-8 -*-
import os
import time
import sys

class LifeGame:
    def __init__(self, mode=sys.argv[1]):
        self.gen = 0
        self.pause = 0.1
        self.field = []
        self.around_list = []
        self.vecs = [
            [1, 1],
            [1, 0],
            [1, -1],
            [0, 1],
            [0, -1],
            [-1, 1],
            [-1, 0],
            [-1, -1]
            ]
        try:
            self.mode = mode
        except:
            self.mode = 'game'
        
        self.initialize()

    def initialize(self):
        for i in range(0, 12):
            self.field.append([])

            for j in range(0, 12):
                self.field[i].append(False)

        cell_position = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

        for i in range(0, 10):
            for j in range(0, 10):
                if(cell_position[i][j] == 1):
                    self.field[i][j] = True
                else:
                    self.field[i][j] = False

        for i in range(0, 10):
            self.around_list.append([])

            for j in range(0, 10):
                self.around_list[i].append(0)

    def board(self, mode='display'):
        os.system('cls')    #UNIX系で動かすときはここをclearに変更
        if(mode == 'display'):
            self.gen += 1
            print('GENERATION: ' + str(self.gen))
        elif(mode == 'edit'):
            print('EDIT MODE\nstartと書いてライフゲームを開始\nclearと書いてセルをすべて死亡させる\n座標(例: "9.8")を書いてそこにあるセルのステータスを変更')
        
        for i in range(1, 11):
            for j in range(1, 11):
                if(self.field[i][j]):
                    print('■', end='')
                else:
                    print('□', end='')

            print('')

    def around(self, line, column):
        value = 0

        for vec in self.vecs:
            if(self.field[line + vec[0]][column + vec[1]]):
                value += 1
            else:
                pass

        return(value)

    def set_list(self):
        for i in range(0, 10):
            for j in range(0, 10):
                self.around_list[i][j] = self.around(i + 1, j + 1)

    def edit(self):
        self.board(mode='edit')
        com = input('>>>')
        if(com == 'start'):
            self.mode = 'game'
        elif(com == 'clear'):
            for i in range(0, 12):
                for j in range(0, 12):
                    self.field[i][j] = False
        else:
            i = int(com.split('.')[0])
            j = int(com.split('.')[1])
            if(self.field[i][j]):
                self.field[i][j] = False
            else:
                self.field[i][j] = True
    
    def game(self):
        self.board()
        self.set_list()

        for i in range(1, 11):
            for j in range(1, 11):
                if(self.around_list[i-1][j-1] == 3):
                    self.field[i][j] = True
                elif((self.field[i][j]) & (self.around_list[i-1][j-1] == 2)):
                    self.field[i][j] = True
                else:
                    self.field[i][j] = False

        time.sleep(self.pause)

    def user(self):
        if(self.mode == 'game'):
            self.game()
        elif(self.mode == 'edit'):
            self.edit()
        else:
            print('ERROR!')

spam = LifeGame()
while(True):
    spam.user()
