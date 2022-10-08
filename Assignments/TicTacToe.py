#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Name-Somya Gautam
#Roll Number- 2020BTechCSE076
#Batch-A

# Tictactoe

class TicTacToe:
    
    def __init__(self):
        self.theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
                        '4': ' ' , '5': ' ' , '6': ' ' ,
                        '7': ' ' , '8': ' ' , '9': ' ' }
    def printBoard(self,board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])


    def game(self):
        turn = 'X'
        count = 0
        for i in range(10):
            self.printBoard(self.theBoard)
            print("It's your turn," + turn + "Move to which place?")
            move = input()        
            if self.theBoard[move] == ' ':
                self.theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue
            if count >= 5:
                if self.theBoard['7'] == self.theBoard['8'] == self.theBoard['9'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")                
                    break
                elif self.theBoard['4'] == self.theBoard['5'] == self.theBoard['6'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif self.theBoard['1'] == self.theBoard['2'] == self.theBoard['3'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif self.theBoard['1'] == self.theBoard['4'] == self.theBoard['7'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif self.theBoard['2'] == self.theBoard['5'] == self.theBoard['8'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif self.theBoard['3'] == self.theBoard['6'] == self.theBoard['9'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break 
                elif self.theBoard['7'] == self.theBoard['5'] == self.theBoard['3'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif self.theBoard['1'] == self.theBoard['5'] == self.theBoard['9'] != ' ': 
                    self.printBoard(self.theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break 
            if count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X' 

executer=TicTacToe()
executer.game()


# In[ ]:




