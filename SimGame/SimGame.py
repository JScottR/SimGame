#!/usr/bin/python
import random

##GlobalVars
avaliableMoves = [['a','b'],['a','c'],['a','d'],['a','e'],['a','f'],['a','g'],['a','h'],['b','c'],['b','d'],['b','e'],['b','f'],['b','g'],['b','h'],['c','d'],['c','e'],['c','f'],['c','g'],['c','h'],['d','e'],['d','f'],['d','g'],['d','h'],['e','f'],['e','g'],['e','h'],['f','g'],['f','h'],['g','h']]
redMoves = []
blueMoves = []
human = ''


## Play Games

def play(color, avaliableMoves, redMoves, blueMoves,human):
    ##Ask for move
    print(color)
    print(avaliableMoves)
    if(color == human):
        vertice = input("Choose the first vertice: ")
        vertice2 = input("Choose the secound vertice: ")
        playerMove = [vertice,vertice2]
    else:
        playerMove = random.choice(avaliableMoves)
    ## Remove move from avaliable
    avaliableMoves.remove(playerMove)
    printOut = repr(color) +' Moves: ' + repr(move)
    print(printOut)
    ##add move to colors moves
    if(color == 'red'):
        redMoves.append(playerMove)
    else:
        blueMoves.append(playerMove)
    ## search for loop

    ## if no loop switch players

    ## if loop announce winner
    if(len(avaliableMoves) == 0):
        finish = repr(color) + 'is the winner'
    else:
        if(color == 'red'):
            play('blue',avaliableMoves,redMoves,blueMoves,human)
        else:
            play("red",avaliableMoves,redMoves,blueMoves,human)

## Initlize Game

def initializeGame():
    var = input("Play Red or Blue: ")
    if(var == "Red" or var == "r" or var == "red"):
        human = "red"
        play("red",avaliableMoves,redMoves,blueMoves,human)
    else:
        human = "blue"
        move = random.choice(avaliableMoves)
        print(move)
        avaliableMoves.remove(move)
        redMoves.append(move)
        printOut = 'Red Moves: ' + repr(move)
        print(printOut)
        play("blue",avaliableMoves,redMoves,blueMoves,human)

initializeGame()



