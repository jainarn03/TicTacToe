import this
import PySimpleGUI as gui
from ast import Return
from cProfile import run
from http.client import REQUEST_TIMEOUT
from operator import truediv
from re import X
from tkinter import Y

def convertBoard(backBoard):
    #changes back bone board from numbers to readable Os and Xs
    symbBoard = backBoard

    for x in range(3):
        for i in range(3):
            if (symbBoard[x][i] == 0):
                symbBoard[x][i] = " "
            elif (symbBoard[x][i] == 1):
                symbBoard[x][i] = "X"
            elif (symbBoard[x][i] == 4):
                symbBoard[x][i] = "O"
    #outputs the current board 
    printBoard(symbBoard)

def printBoard(board):
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print(f"--*---*---")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print(f"--*---*---")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]} ")
# nothing  = " "
# player 1 = "O" 
# player 2 = "4"

def checkWinner(boardList):
    winList = []
    print("0------------------------------------0")
    # check collems
    if (boardList[0][0] + boardList[1][1] + boardList[2][2] == 3 or boardList[0][2] + boardList[1][1] + boardList[2][0] == 3 ):
        return(1)
    if (boardList[0][0] + boardList[1][1] + boardList[2][2] == 12 or boardList[0][2] + boardList[1][1] + boardList[2][0] == 12 ):
        return(2)
    if (boardList[0][0] + boardList[0][1] + boardList[0][2] + boardList[1][0] + boardList[1][1] + boardList[1][2] + boardList[2][0] + boardList[2][1] + boardList[2][2] == 21):
        return(3)

    for y in range(3):
        tempC = 0
        for x in range(3):
            tempC += int(boardList[y][x])
        if(tempC == 3):
            return(1)
        if(tempC == 12):
            return(2)

    # check rows
    for x in range(3):
        tempC = 0
        for y in range(3):
            tempC += int(boardList[y][x])
        if(tempC == 3):
            return(1)
        if(tempC == 12):
            return(2)
        
    
    else:
        pass
    convertBoard(boardList)     #print board
 
def dataTrasfer(alpha):
    finishedArray =[[0,0,0],
                    [0,0,0],
                    [0,0,0]
                ]
    for x in range(3):
        for i in range(3):
            finishedArray[x][i] = alpha[x][i]
    return finishedArray

#updates the Back board of the game
def update(BB, AA):
    global a
    AA = dataTrasfer(BB)
    a = checkWinner(AA)
    convertBoard(AA)

btnSize = (8,4)
player1Score = 0
player2Score = 0
tie = 0
counter = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
x = 'X'
o = 'O'

BB = [[0,0,0],
      [0,0,0],
      [0,0,0,]
    ]

AA = []


#gui.theme_previewer()
gui.theme('LightGrey2')
#gui.theme('Black')
#gui.theme('DarkTeal')
#gui.theme('LightBlue5')
#button_color=sg.TRANSPARENT_BUTTON

#Top of the GUI text
layoutG = [[gui.Push(), gui.Text("CLICK ON A BOX TO START THE GAME",  key = ('-TEXT-')), gui.Push()],
#Buttons 1 to 3
[gui.Push(), gui.Button(key = ('-B1-'), size = (btnSize), enable_events = True, border_width=0),
gui.Button(key = ('-B2-'), size = (btnSize), enable_events = True, border_width=0), 
gui.Button(key = ('-B3-'), size = (btnSize), enable_events = True, border_width=0), gui.Push()],
#Buttons 4 to 6
[gui.Push(), gui.Button(key = ('-B4-'), size = (btnSize), enable_events = True, border_width=0),
gui.Button(key = ('-B5-'), size = (btnSize), enable_events = True, border_width=0),
gui.Button(key = ('-B6-'), size = (btnSize), enable_events = True, border_width=0), gui.Push()],
#Buttons 7 to 9
[gui.Push(), gui.Button(key = ('-B7-'), size = (btnSize), enable_events = True, border_width=0),
gui.Button(key = ('-B8-'), size = (btnSize), enable_events = True, border_width=0),
gui.Button(key = ('-B9-'), size = (btnSize), enable_events = True, border_width=0), gui.Push()]
]

#Formatting for the whole right side. Player scores, Restart game, and RAGE QUIT!!!
layoutS = [[gui.Push(), gui.Text("PLAYER 1 [X]:", size = (12,3)), gui.Push(), gui.Text(player1Score, size = (2,3), key = '-P1-')],
[gui.Push(), gui.Text("PLAYER 2 [O]:", size = (12,3)), gui.Push(), gui.Text(player2Score, size = (2,3), key = '-P2-')],
[gui.Push(), gui.Text("TIE: ", size = (12,3)), gui.Push(), gui.Text(tie, size = (2,3), key = '-TIE-')],
[gui.Push(), gui.Button("CLEAR BOARD", key = ('-RESTART-'), enable_events = True, size = (12,2)), gui.Push()],
[gui.Push(), gui.Button("RAGE QUIT!!!", key = ('-EXIT-'), enable_events = True, size = (12,2)), gui.Push()]
]

#Sets the layout of the game
layout = [  
    [
        gui.Column(layoutG),
        gui.VSeperator(),
        gui.Column(layoutS)
    ]
]

#displays the actual GUI window
window = gui.Window("TIC TAC TOE", layout)

#Event loop
while True:
    event, values = window.read()
    if event in (gui.WIN_CLOSED, '-EXIT-'):
        break
    if event == '-B1-':
        c1 += 1
        if c1 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B1-'].update(o)
                BB[0][0]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B1-'].update(x)
                BB[0][0]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B2-':
        c2 += 1
        if c2 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B2-'].update(o)
                BB[0][1]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B2-'].update(x)
                BB[0][1]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B3-':
        c3 += 1
        if c3 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B3-'].update(o)
                BB[0][2]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B3-'].update(x)
                BB[0][2]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B4-':
        c4 += 1
        if c4 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B4-'].update(o)
                BB[1][0]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B4-'].update(x)
                BB[1][0]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B5-':
        c5 += 1
        if c5 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B5-'].update(o)
                BB[1][1]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B5-'].update(x)
                BB[1][1]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B6-':
        c6 += 1
        if c6 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B6-'].update(o)
                BB[1][2]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B6-'].update(x)
                BB[1][2]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B7-':
        c7 += 1
        if c7 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B7-'].update(o)
                BB[2][0]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B7-'].update(x)
                BB[2][0]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B8-':
        c8 += 1
        if c8 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B8-'].update(o)
                BB[2][1]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B8-'].update(x)
                BB[2][1]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-B9-':
        c9 += 1
        if c9 == 1:
            counter +=1
            if counter % 2 == 0:
                window['-B9-'].update(o)
                BB[2][2]= 4
                update(BB, AA)
                if (a == 2):
                    player2Score += 1
                    window['-P2-'].update(player2Score)
                    gui.popup("PLAYER 2 WINS")
                    event = '-RESTART-'
            elif counter % 2 == 1:
                window['-B9-'].update(x)
                BB[2][2]= 1
                update(BB, AA)
                if (a == 1):
                    player1Score += 1
                    window['-P1-'].update(player1Score)
                    gui.popup("PLAYER 1 WINS")
                    event = '-RESTART-'
                if (a==3):
                    tie += 1
                    window['-TIE-'].update(tie)
                    gui.popup("ITS A TIE")
                    event = '-RESTART-'
    if event == '-RESTART-':
        window['-B1-'].update("")
        window['-B2-'].update("")
        window['-B3-'].update("")
        window['-B4-'].update("")
        window['-B5-'].update("")
        window['-B6-'].update("")
        window['-B7-'].update("")
        window['-B8-'].update("")
        window['-B9-'].update("")
        counter = 0
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        BB = [[0,0,0],
            [0,0,0],
            [0,0,0,]
            ]
        AA = []

        
window.close()