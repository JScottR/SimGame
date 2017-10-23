#!/usr/bin/python
import random

##GlobalVars
avaliableMoves = [['a','b'],['a','c'],['a','d'],['a','e'],['a','f'],['a','g'],['a','h'],['b','c'],['b','d'],['b','e'],['b','f'],['b','g'],['b','h'],['c','d'],['c','e'],['c','f'],['c','g'],['c','h'],['d','e'],['d','f'],['d','g'],['d','h'],['e','f'],['e','g'],['e','h'],['f','g'],['f','h'],['g','h']]
redMoves = []
blueMoves = []
human = ''


## PsudeoMiniMaxAlgorithm


def pseudoMiniMax(color, avaliableMoves, redMoves, blueMoves,human):
    if(color == 'red'):
        if findLoop(redMoves):
            if(color == human):
                return(10,[])
            else:
                return(-10,[])
    else:
        if findLoop(blueMoves):
            if(color == human):
                return(10,[])
            else:
                return(-10,[])
    if(color == human):
        currentBest = 100
    else:
        currentBest = -100
    bestMove = random.choice(avaliableMoves)
    for possibleMoves in avaliableMoves:
        newAvaliable = list(avaliableMoves)
        newAvaliable.remove(possibleMoves)
        if(color == 'red'):
            newColor = list(redMoves)
            newColor.append(possibleMoves)
            retVal, retMove = pseudoMiniMax("blue",newAvaliable,newColor,blueMoves,human)
        else:
            newColor = list(blueMoves)
            newColor.append(possibleMoves)
            retVal, retMove = pseudoMiniMax("red",newAvaliable,redMoves,newColor,human)
        if(color==human):
            if(retVal < currentBest):
                currentBest = retVal
                bestMove = list(possibleMoves)
        else:
            if(retVal == 10):
                return(10,possibleMoves)
            elif(retVal > currentBest):
                currentBest = retVal
                bestMove = list(possibleMoves)
    return(currentBest,bestMove)




## Play Games

def play(color, avaliableMoves, redMoves, blueMoves,human,moves):
    ##Ask for move
    print(color)
    print(avaliableMoves)
    if(color == human):
        vertice = input("Choose the first vertice: ")
        vertice2 = input("Choose the secound vertice: ")
        playerMove = [vertice,vertice2]
        playerMove.sort()
    else:
        if moves <= 15:
            while True:
                playerMove = random.choice(avaliableMoves)
                if(color == 'red'):
                    tmpColor = list(redMoves)
                else:
                    tmpColor = list(blueMoves)
                tmpColor.append(playerMove)
                if not findLoop(tmpColor):
                    break
        else:
            print("entering AI")
            bestValue, bestMove = pseudoMiniMax(color,avaliableMoves,redMoves,blueMoves,human)
            print("Best Val")
            print(bestValue)
            print(bestMove)
            playerMove = bestMove
            if (bestMove == []):
                playerMove = random.choice(avaliableMoves)

    ## Remove move from avaliable
    avaliableMoves.remove(playerMove)
    printOut = repr(color) +' Moves: ' + repr(playerMove)
    moves += 1
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
            if not findLoop(redMoves):
                play('blue',avaliableMoves,redMoves,blueMoves,human,moves)
            else:
                print("Blue Wins!")
        else:
            if not findLoop(blueMoves):
                play("red",avaliableMoves,redMoves,blueMoves,human,moves)
            else:
                print("Red Wins")



def findLoop(moves):
    for edge in moves:
        list1 = []
        list2 = []
        firstVert = edge[0]
        secondVert = edge[1]
        for items in moves:
            if firstVert in items and secondVert not in items:
                list1.append(items)
        ## print("Made List 1")
        ## print(list1)
        if(len(list1) != 0):
            for sublist in list1:
                if sublist[0] != firstVert:
                    list2.append(sublist[0])
                else:
                    list2.append(sublist[1])
            ## print(list2)
            for newVerts in list2:
                newList = [secondVert, newVerts]
                newList.sort()
                ## print("New list")
                ## print(newList)
                if newList in moves:
                    ## print("returningTrue")
                    return True
    ## print("returningFalse")
    return False
## Initlize Game

def initializeGame():
    var = input("Play Red or Blue: ")
    if(var == "Red" or var == "r" or var == "red"):
        human = "red"
        play("red",avaliableMoves,redMoves,blueMoves,human,0)
    else:
        human = "blue"
        move = random.choice(avaliableMoves)
        print(move)
        avaliableMoves.remove(move)
        redMoves.append(move)
        printOut = 'Red Moves: ' + repr(move)
        print(printOut)
        play("blue",avaliableMoves,redMoves,blueMoves,human,1)

initializeGame()



