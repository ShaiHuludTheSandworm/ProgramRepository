



def game_loop():
    #function that runs the game loop, allowing the chess bot to play itself
    print("huge success")
    game_condition = "Game Started"
    game_state = []
    while game_condition != "Game over":
        game_condition = "Game over"
    return game_state


def rule_book():
    #function that knows chess rules
    print("making a note here")
    chess_board = 
    # K is king, Q is queen, R is rook, B is bishop, N is knight, P is pawn
    # M is movement pattern, T is take pattern, MT is for when movement and take are identical
    # L is a limitation or special rule, Z is a special ability or one time occurrence that a piece can do
    # F is forward, B is back, L is left, R is right, D is all four diagonals, S is skew or F/B2 + L/R1 | L/R2 + F/B1
    # 1 is only being able to move a single space in a direction / pattern, U is unlimited movement in a direction / pattern
    # When two directional / pattern characters are side by side the first is the limitation on the second FD is forward only diagonals
    # When + is used between two directional / pattern characters they share the final 1/2/U limit on movement or take but are disconnected otherwise
    # X is exposure, having the X limitation prevents a piece from entering or staying in a space that is threatened by an enemy piece
    # E is end, having the end limitation means that when a piece reaches the opposite side of the board it can transform into any other piece except the king (it should only ever transform into the queen or knight, except for mind game purposes)
    # C is color, it means that the piece cannot move to a different color from its starting color, G is ghost, it means it can move over other units
    # W is "swap" or more accurately castling
    chess_pieces = {
        "K": ["MT=F+B+L+R+D1", "L=X", "Z=W"],
        "Q": ["MT=F+B+L+R+DU"],
        "R": ["MT=F+B+L+RU", "Z=W"],
        "B": ["MT=DU", "L=C"],
        "N": ["MT=S1", "L=G"],
        "P": ["M=F1", "T=FD1", "Z=E"]
        "FBRLDS1UMT+="
    }


def main():
    #functions needed, main game loop here
    #main function will read from a config / text / csv file
    #will grant each game a game id
    #will call each game loop once and get the finished game as a result, which will be written to a text file


    #function that runs the game loop, allowing the chess bot to play itself
    #function that knows chess rules, can provide possible moves for each piece
    #function that knows chess rules, can provide all possible moves for the current game state
    #function that knows what is a good move
    #function that collects good moves into possible choices
    #function that creates a plan
    #function that creates and or explores a decision tree to find out good future chess board states
    #function that remembers the board state, whose turn it is, dead pieces, remembers what moves have been made
    #function that assigns a score to each chess board state
    #function that decides how the game is going
    #function that "thinks", will attempt to learn based on games played, will add weights to moves and change weights based on games
    #function that displays chess game
    #function that displays what chess bot is thinking
    #function that displays most likely future gamestates based on a move assuming enemy player is as good as the bot
    #function that handles looking up the file that holds previous games, weights, and learnings
    #function that handles outputting to the file with the game played, must compare the file as it is now, to change it, not as it was when read originally
    #function that converts between the file input/output and the data that is wanted from it
    #function that converts entire game into a score and then it is stored so if a similar or same scenario is encountered again it knows what to do
    #function that allows for outside chess games to be loaded in as training data
    #function that determines the relative value of a chess game, with chess games between more competent players being more valuable and chess games between lower elo players being less valuable
    #function that sorts / stores chess game states by how likely a player is to win in that gamestate and then moves both to get to such gamestates and moves to do after that game state
    #function to convert to and from my way of encoding chess games to the industry standard / standards for encoding chess games
    #function that predicts both most likely next move of enemy player and most optimal move of enemy player, and based on previous moves predict which is most likely


    print("this was a triumph")
    rule_book()
    game_loop()




main()
