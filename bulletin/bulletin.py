# -*- coding:utf-8 -*-
import os
import time
import sys

class Characters():
    a = (' ***','*  *','****','*  *','*  *')
    b = ('*** ','* * ','****','*  *','****')
    c = ('*** ','*   ','*   ','*   ','****')
    d = ('*** ','*  *','*  *','*  *','****')
    e = ('****','*   ','*** ','*   ','****')
    f = ('****','*   ','*** ','*   ','*   ')
    g = ('****','*   ','* **','*  *','****')
    h = ('*  *','*  *','****','*  *','*  *')
    i = ('****','  * ','  * ','  * ','****')
    j = (' ***','   *','   *','   *','****')
    k = ('*  *','*  *','*** ','*  *','*  *')
    l = ('*   ','*   ','*   ','*   ','****')
    m = ('*****','* * *','* * *','*   *','*   *')
    n = ('*  *','** *','* **','* **','*  *')
    o = ('****','*  *','*  *','*  *','****')
    p = ('****','*  *','****','*   ','*   ')
    q = ('****','*  *','*  *','* * ','** *')
    r = ('****','*  *','*** ','*  *','*  *')
    s = ('****','*   ','****','   *','****')
    t = ('****','  * ','  * ','  * ','  * ')
    u = ('*  *','*  *','*  *','*  *',' ***')
    v = ('*  *','*  *','* * ','* * ','**  ')
    w = ('*   *','*   *','* * *','* * *','*****')
    x = ('*  *','*  *',' ** ','*  *','*  *')
    y = ('*  *','*  *','****','  * ','  * ')
    z = ('****','  **',' ** ','**  ','****')
    whitespace = ('    ','    ','    ','    ','    ')
    space = (' ',' ',' ',' ',' ')
    
class Make_str(Characters):
    def __init__(self, string):
        self.string = list(string)
        self.script = """
self.first = self.first + Characters.{0}[0]
self.second = self.second + Characters.{1}[1]
self.third = self.third + Characters.{2}[2]
self.fourth = self.fourth + Characters.{3}[3]
self.fifth = self.fifth + Characters.{4}[4]
        """
        self.checklist = list('abcdefghijklmnopqrstuvwxyz ')
        
        self.first = ''
        self.second = ''
        self.third = ''
        self.fourth = ''
        self.fifth = ''
            
    def make(self):
        for char in self.string:
            if(not(char in self.checklist)):
                return('boo')
            elif(char == ' '):
                exec(self.script.format('whitespace', 'whitespace', 'whitespace', 'whitespace', 'whitespace'))
            else:
                exec(self.script.format(char, char, char, char, char))
                exec(self.script.format('space', 'space', 'space', 'space', 'space'))
                
        return((self.first, self.second, self.third, self.fourth, self.fifth))

class User:
    def __init__(self, string):
        self.string = Make_str(string).make()
        self.num = 0
        self.width = 50

    def display(self):
        stat = True
        os.system('cls')

        if(self.string != 'boo'):
            for i in range(0, 5):
                for j in range(0, self.width):
                    try:
                        print(self.string[i][self.num+j], end='')
                    except:
                        print(' ', end='')
                        stat = False

                print('')
        else:
            stat = False
                
        return(stat)

    def start(self):
        if(self.display()):
            self.num += 1
            time.sleep(0.1)
            self.start()

while(True):
    command = input('Now you type a string.\nType q to quit\n>>>')
    if(command != 'q'):
        User(command).start()
    else:
        sys.exit(0)
