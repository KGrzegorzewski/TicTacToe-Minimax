from game_functions import *
import random
from time import process_time

playerX = "X"
playerO = "O"
winner = None
currentPlayer = playerX

X_wins = 0
O_wins = 0
tied_games = 0
games = 0
games_to_be_played = 1

minimax_player = "X"

board = ["O", "X", "X",
        "-", "X", "O",
        "X", "O", "X"]

max_X_moves = 5
max_O_moves = 4

#Puste tablice przechowujace czasy
time_minmax = [[] for i in range(games_to_be_played)]
time_random = [[] for i in range(games_to_be_played)]


while (games < games_to_be_played):
    winner = None
    isGameFinished = False
    currentPlayer = playerX
    board = clear_board(board)
    print("Rozpoczyna sie gra numer ", games)
    no_move = 0
    
    while True:
        
        winner = getWinner(board)
        if (winner != None or is_draw(board)):
            break
    
        #First' player move
        if (currentPlayer == playerX):
            start = process_time()
            new_minimax_move(board, playerX)
            stop = process_time()
            
            time_minmax[games].append( stop - start )
            
            printBoard(board)
        
        
        #Second's player move
        else:
            winner = getWinner(board)
            if (winner != None or is_draw(board)):
                break
                
            else:
                start = process_time()
                AImove = randomMove(checkAvailable(board))
                insertMove(board, AImove, currentPlayer)
                stop = process_time()
                
                time_random[games].append ( stop - start )
                
                printBoard(board)

        
        #Change the player, if game is on going
        currentPlayer = changePlayer(currentPlayer)


    if winner == "X":
        X_wins += 1
    elif winner == "O":
        O_wins += 1
    else:
        tied_games += 1
        
    games += 1


print("X won ", X_wins/games_to_be_played * 100, "% games")
print("O won ", O_wins/games_to_be_played * 100, "% games")
print("Games tied :", tied_games/games_to_be_played * 100, "% games")


#Zapis danych czasowych do pliku
f=open('time_minmax.txt','w')
for time_4_move in time_minmax:
    f.writelines(str(time_4_move))
    f.write('\n')
f.close()

g=open('time_random.txt','w')
for time_4_move in time_random:
    g.writelines(str(time_4_move))
    g.write('\n')
g.close()


    








