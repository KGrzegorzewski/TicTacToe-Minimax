import random

def isAvailable(board, place):
    return board[place] == "-"

def isBoardFull(board):
    if "-" not in board:
        return True
    else:
        return False

def printBoard(board):
    for i in range(3):
        print(board[ i * 3 : (i + 1) * 3 ] )
    print("")

def insertMove(board, place, currentPlayer):
    if isAvailable(board, place):
        board[place] = currentPlayer
        
def undoMove(board, place):
    board[place] = "-"


#Win conditions
def checkWinRows(board):
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def checkWinColumns(board):
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def checkWinDiagonal(board):
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    else:
        return None


def getWinner(board):
    row_winner = checkWinRows(board)
    col_winner = checkWinColumns(board)
    diag_winner = checkWinDiagonal(board)

    if row_winner:
        return row_winner
    elif col_winner:
        return col_winner
    elif diag_winner:
        return diag_winner


def is_draw(board):
    if isBoardFull(board):
        if (getWinner != "X" and getWinner != "O"):
            return True

def is_terminate_state(board):
    if (is_draw(board) or getWinner(board) != None):
        return True
    else:
        return False


def changePlayer(currentPlayer):
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    return currentPlayer


def opposite_Player(currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return "X"

# Return a list of available moves
def checkAvailable(board):
    free_places = []
    for index in range(len(board)):
        if isAvailable(board, index):
            free_places.append(index)
    return free_places

# Return a randomed chosen move from a list of available moves
def randomMove(free_places):
    random_ind = random.randint(0, len(free_places) - 1)
    random_move = free_places[random_ind]
    return random_move
    
    
def new_minimax(board, player):
    #Stany terminalne i ich obsługa
    if is_terminate_state(board):
    
        #okej, mamy stan terminalny, teraz jaki?
        
        #Win ktoregos playera
        if (getWinner(board) != None):
            if getWinner(board) == "X":
                return 1
            else:
                return -1
        #Remis gracza player
        elif is_draw:
            return 0
   
   #Jesli nie ma stanu terminalnego, sprawdzamy kolejne ruchy
    scores = []
    for move in checkAvailable(board):
        insertMove(board, move, player)
        #printBoard(board)
        scores.append( new_minimax( board, opposite_Player(player) ) )
        #print(scores)
        undoMove(board, move)
    
    
    if player == "X":  #jesli gracz to X (czyli ten ktory zaczyna i chce maksymalizacji)
        return max(scores)  #czy istnieje szansa win/remis/loss
    else:
        return min(scores)
        
    
    
def new_minimax_move(board, player):
    best_score = -10
    best_move = None
    for move in checkAvailable(board):
        insertMove(board, move, player)
        score = new_minimax(board, opposite_Player(player))
        #print(score)
        undoMove(board, move)
    
        if (score > best_score):
            best_score = score
            best_move = move
    insertMove(board, best_move, player)
    
    
    
    
def heuristic(board, player, depth):
    #Stany terminalne i ich obsługa
    if is_terminate_state(board) or depth == 0:
    
        #okej, mamy stan terminalny, teraz jaki?
        
        #Win ktoregos playera
        if (getWinner(board) != None):
            if getWinner(board) == "X":
                return 1*(10-depth)
            else:
                return -1*(10-depth)
        #Remis gracza player
        elif is_draw:
            return 0
   
   #Jesli nie ma stanu terminalnego, sprawdzamy kolejne ruchy
    scores = []
    for move in checkAvailable(board):
        insertMove(board, move, player)
        #printBoard(board)
        scores.append( heuristic( board, opposite_Player(player), depth - 1 ) )
        #print(scores)
        undoMove(board, move)
    
    
    if player == "X":  #jesli gracz to X (czyli ten ktory zaczyna i chce maksymalizacji)
        return max(scores)  #czy istnieje szansa win/remis/loss
    else:
        return min(scores)
        
    
    
def heuristic_move(board, player, depth):
    best_score = -100
    best_move = None
    for move in checkAvailable(board):
        insertMove(board, move, player)
        score = heuristic(board, opposite_Player(player), depth)
        print(score)
        undoMove(board, move)
    
        if (score > best_score):
            best_score = score
            best_move = move
    insertMove(board, best_move, player)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def minimax(isMaximizing, currentPlayer, board):
    #Sprawdzenie stanu gry (draw, lose, win)
    if getWinner(board) == currentPlayer:
        return -1
    elif is_draw(board):
        return 0
    elif (getWinner(board) == opposite_Player(currentPlayer)):
        return 1
    
    scores = []
    for move in checkAvailable(board):
        #zagrywa O
        insertMove(board, move, currentPlayer)
        currentPlayer = changePlayer(currentPlayer)

        scores.append(minimax(not isMaximizing, currentPlayer, board))
        
        undoMove(board, move)
        currentPlayer = changePlayer(currentPlayer)
        
    if isMaximizing:

        return max(scores) 
    else:

        return min(scores)
        

def minimax_move(board, currentPlayer):
    best_score = -10
    best_move = None
    for move in checkAvailable(board):
    
        #X zagrywa pierwszy ruch
        insertMove(board, move, currentPlayer)
        #Zmiana na O
        currentPlayer = changePlayer(currentPlayer)
        
        #Sprawdzenie wynikow (stanow terminalnych) w argumencie podany gracz O, ktory minimalizuje - False
        score = minimax(False, currentPlayer, board)

        
        undoMove(board, move)
        currentPlayer = changePlayer(currentPlayer)
        
        if (score > best_score):
            best_score = score
            best_move = move
    insertMove(board, best_move, currentPlayer)





def clear_board(board):
    for i in range(9):
        board[i] = "-"
    return board








#Zwraca sciezke dazenia do stanow terminalnych
def stany_terminalne(board, player):
    #Stany terminalne i ich obsługa
    if is_terminate_state(board):
    
        #okej, mamy stan terminalny, teraz jaki?
        
        #Win ktoregos playera
        if (getWinner(board) != None):
            if getWinner(board) == player:
                return 1
            else:
                return -1
        #Remis gracza player
        elif is_draw:
            return 0
   
   #Jesli nie ma stanu terminalnego, sprawdzamy kolejne ruchy
    scores = []
    for move in checkAvailable(board):
        insertMove(board, move, player)
        printBoard(board)
        scores.append( new_minimax( board, opposite_Player(player) ) )
        undoMove(board, move)








    


