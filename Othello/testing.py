import time
weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
     0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
     0, 20, -5, 15, 3, 3, 15, -5 , 20, 0,
     0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
     0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
     0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
     0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
     0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def display(state):
    count = 1
    for a in state:
        if count % 10 == 0:
            print(a + " ")
        else:
            print(a + " ", end="", flush=True)
        count += 1


corners = [11, 18, 81, 88]
x_squares = [22, 27, 72, 77]
c_squares = [12, 17, 21, 28, 71, 82, 87, 78]
a_squares = [13, 16, 31, 38, 61, 68, 83, 86]
b_squares = [14, 15, 41, 51, 48, 58, 84, 85]


def legal_moves(board, tkn):
    moves = []
    op = {"o": "@", "@": "o"}[tkn]
    for index in range(11, 89):
        if board[index] != ".":
            continue
        if board[index - 1] == op:
            count = 1
            while board[index - 1 * count] == op:
                count += 1
            if board[index - 1 * count] == tkn and index not in moves:
                moves.append(index)
        if board[index + 1] == op:
            count = 1
            while board[index + 1 * count] == op:
                count += 1
            if board[index + 1 * count] == tkn and index not in moves:
                moves.append(index)
        if board[index - 10] == op:
            count = 1
            while board[index - 10 * count] == op:
                count += 1
            if board[index - 10 * count] == tkn and index not in moves:
                moves.append(index)
        if board[index + 10] == op:
            count = 1
            while board[index + 10 * count] == op:
                count += 1
            if board[index + 10 * count] == tkn and index not in moves:
                moves.append(index)
        if board[index - 11] == op:
            count = 1
            while board[index - 11 * count] == op:
                count += 1
            if board[index - 11 * count] == tkn and index not in moves:
                moves.append(index)
        if board[index + 11] == op:
            count = 1
            while board[index + 11 * count] == op:
                count += 1
            if board[index + 11 * count] == tkn and index not in moves:
                moves.append(index)
        if board[index - 9] == op:
            count = 1
            while board[index - 9 * count] == op:
                count += 1
            if board[index - 9 * count] == tkn and index not in moves:
                moves.append(index)
        if board[index + 9] == op:
            count = 1
            while board[index + 9 * count] == op:
                count += 1
            if board[index + 9 * count] == tkn and index not in moves:
                moves.append(index)
    return moves


def play_move(board, tkn, position):
    temp = board[:position] + tkn + board[position + 1:]
    op = {"o": "@", "@": "o"}[tkn]
    if temp[position - 1] == op:
        count = 1
        while temp[position - 1 * count] == op:
            count += 1
        if temp[position - 1 * count] == tkn:
            for change in range(position - 1, position - 1 * count, -1):
                temp = temp[:change] + tkn + temp[change + 1:]
    if temp[position + 1] == op:
        count = 1
        while temp[position + 1 * count] == op:
            count += 1
        if temp[position + 1 * count] == tkn:
            for change in range(position + 1, position + 1 * count):
                temp = temp[:change] + tkn + temp[change + 1:]
    if temp[position + 10] == op:
        count = 1
        while temp[position + 10 * count] == op:
            count += 1
        if temp[position + 10 * count] == tkn:
            for change in range(position + 10, position + 10 * count, 10):
                temp = temp[:change] + tkn + temp[change + 1:]
    if temp[position - 10] == op:
        count = 1
        while temp[position - 10 * count] == op:
            count += 1
        if temp[position - 10 * count] == tkn:
            for change in range(position - 10, position - 10 * count, -10):
                temp = temp[:change] + tkn + temp[change + 1:]
    if temp[position + 11] == op:
        count = 1
        while temp[position + 11 * count] == op:
            count += 1
        if temp[position + 11 * count] == tkn:
            for change in range(position + 11, position + 11 * count, 11):
                temp = temp[:change] + tkn + temp[change + 1:]
    if temp[position - 11] == op:
        count = 1
        while temp[position - 11 * count] == op:
            count += 1
        if temp[position - 11 * count] == tkn:
            for change in range(position - 11, position - 11 * count, -11):
                temp = temp[:change] + tkn + temp[change + 1:]
    if temp[position + 9] == op:
        count = 1
        while temp[position + 9 * count] == op:
            count += 1
        if temp[position + 9 * count] == tkn:
            for change in range(position + 9, position + 9 * count, 9):
                temp = temp[:change] + tkn + temp[change + 1:]
    if temp[position - 9] == op:
        count = 1
        while temp[position - 9 * count] == op:
            count += 1
        if temp[position - 9 * count] == tkn:
            for change in range(position - 9, position - 9 * count, -9):
                temp = temp[:change] + tkn + temp[change + 1:]
    return temp


def get_next_player(board, tkn):
    if len(legal_moves(board, tkn)) > 0:
        return tkn
    elif len(legal_moves(board, {"o": "@", "@": "o"}[tkn])) > 0:
        return {"o": "@", "@": "o"}[tkn]
    else:
        return "?"


def maxmin(board, player, depth):
    opponent = {"o": "@", "@": "o"}[player]
    best = {"o": min, "@": max}
    if depth == 0:
        score = score_board(board)
        return None, score
    possibles = []
    for move in legal_moves(board, player):
        new_board = play_move(board, player, move)
        next_player = get_next_player(new_board, opponent)
        if next_player == "?":
            score = (new_board.count("@") - new_board.count("o")) * 10000
            possibles.append((move, score))
        else:
            possibles.append((move, maxmin(new_board, next_player, depth - 1)[1]))
    return best[player](possibles, key=lambda x: x[1])


def maxmin2(board, player, depth, alpha, beta):
    opponent = {"o": "@", "@": "o"}[player]
    best = {"o": min, "@": max}
    if depth == 0:
        score = score_board(board)
        return None, score
    possibles = []
    for move in legal_moves(board, player):
        new_board = play_move(board, player, move)
        next_player = get_next_player(new_board, opponent)
        if next_player == "?":
            score = (new_board.count("@") - new_board.count("o")) * 10000
            possibles.append((move, score))
        else:
            possibles.append((move, maxmin2(new_board, next_player, depth - 1, alpha, beta)[1]))
            if player == "@":
                alpha = max(alpha, score_board(new_board))
            elif player == "o":
                beta = min(beta, score_board(new_board))
            if alpha >= beta:
                break
    return best[player](possibles, key=lambda x: x[1])


def score_board(board):
    black_edge = 0
    white_edge = 0
    black_internal = 0
    white_internal = 0
    black_frontier = 0
    white_frontier = 0
    move = 61 - board.count(".")
    esac = 312 + 6.24 * move
    if move <= 25:
        cmac = 50 + 2 * move
    else:
        cmac = 75 + move
    black_moves = legal_moves(board, "@")
    white_moves = legal_moves(board, "o")
    white_only = len(white_moves)
    black_only = len(black_moves)
    common = 0
    for a in black_moves:
        if a in white_moves:
            common += 1
    white_only -= common
    black_only -= common
    b = black_only * 2 + common
    w = white_only * 2 + common
    mobility = int(1000 * (b - w) / (b + w + 2))
    black_empty = 0
    white_empty = 0
    black_weight = 0
    white_weight = 0
    for a in range(11, 90):
        if board[a] == "?":
            continue
        if board[a] == ".":
            adj_black = False
            adj_white = False
            if board[a + 1] == "@":
                adj_black = True
                black_weight += 1
            elif board[a + 1] == "o":
                adj_white = True
                white_weight += 1
            if board[a + 11] == "@":
                adj_black = True
                black_weight += 1
            elif board[a + 11] == "o":
                adj_white = True
                white_weight += 1
            if board[a + 10] == "@":
                adj_black = True
                black_weight += 1
            elif board[a + 10] == "o":
                adj_white = True
                white_weight += 1
            if board[a - 1] == "@":
                adj_black = True
                black_weight += 1
            elif board[a - 1] == "o":
                adj_white = True
                white_weight += 1
            if board[a + 9] == "@":
                adj_black = True
                black_weight += 1
            elif board[a + 9] == "o":
                adj_white = True
                white_weight += 1
            if board[a - 10] == "@":
                adj_black = True
                black_weight += 1
            elif board[a - 10] == "o":
                adj_white = True
                white_weight += 1
            if board[a - 11] == "@":
                adj_black = True
                black_weight += 1
            elif board[a - 11] == "o":
                adj_white = True
                white_weight += 1
            if board[a - 9] == "@":
                adj_black = True
                black_weight += 1
            elif board[a - 9] == "o":
                adj_white = True
                white_weight += 1
            if adj_black:
                black_empty += 1
            if adj_white:
                white_empty += 1
        else:
            is_safe = True
            stable = True
            op = {"o": "@", "@": "o"}[board[a]]
            if board[a + 1] == "." or board[a - 1] == "." or board[a + 10] == "." or board[a - 10] == '.' or board[a + 11] == "." or board[a - 11] == "." or board[a - 9] == "." or board[a + 9] == ".":
                if board[a] == "@":
                    black_frontier += 1
                else:
                    white_frontier += 1
            if board[a + 1] != ".":
                if board[a + 1] == op:
                    if board[a - 1] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a - count * 1] == board[a]:
                            count += 1
                        if board[a - count * 1] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a + count * 1] == board[a]:
                        count += 1
                    if board[a + count * 1] == op:
                        if board[a - 1] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a - count * 1] == board[a]:
                                count += 1
                            if board[a - count * 1] == ".":
                                is_safe = False
            if board[a - 1] != ".":
                if board[a - 1] == op:
                    if board[a + 1] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a + count * 1] == board[a]:
                            count += 1
                        if board[a + count * 1] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a - count * 1] == board[a]:
                        count += 1
                    if board[a - count * 1] == op:
                        if board[a + 1] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a + count * 1] == board[a]:
                                count += 1
                            if board[a - count * 1] == ".":
                                is_safe = False
            if board[a + 10] != ".":
                if board[a + 10] == op:
                    if board[a - 10] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a - count * 10] == board[a]:
                            count += 1
                        if board[a - count * 10] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a + count * 10] == board[a]:
                        count += 1
                    if board[a + count * 10] == op:
                        if board[a - 10] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a - count * 10] == board[a]:
                                count += 1
                            if board[a - count * 10] == ".":
                                is_safe = False
            if board[a - 10] != ".":
                if board[a - 10] == op:
                    if board[a + 10] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a + count * 10] == board[a]:
                            count += 1
                        if board[a + count * 10] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a - count * 10] == board[a]:
                        count += 1
                    if board[a - count * 10] == op:
                        if board[a + 10] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a + count * 10] == board[a]:
                                count += 1
                            if board[a - count * 10] == ".":
                                is_safe = False
            if board[a + 11] != ".":
                if board[a + 11] == op:
                    if board[a - 11] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a - count * 11] == board[a]:
                            count += 1
                        if board[a - count * 11] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a + count * 11] == board[a]:
                        count += 1
                    if board[a + count * 11] == op:
                        if board[a - 11] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a - count * 11] == board[a]:
                                count += 1
                            if board[a - count * 11] == ".":
                                is_safe = False
            if board[a - 11] != ".":
                if board[a - 11] == op:
                    if board[a + 11] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a + count * 11] == board[a]:
                            count += 1
                        if board[a + count * 11] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a - count * 11] == board[a]:
                        count += 1
                    if board[a - count * 11] == op:
                        if board[a + 11] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a + count * 11] == board[a]:
                                count += 1
                            if board[a - count * 11] == ".":
                                is_safe = False
            if board[a + 9] != ".":
                if board[a + 9] == op:
                    if board[a - 9] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a - count * 9] == board[a]:
                            count += 1
                        if board[a - count * 9] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a + count * 9] == board[a]:
                        count += 1
                    if board[a + count * 9] == op:
                        if board[a - 9] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a - count * 9] == board[a]:
                                count += 1
                            if board[a - count * 9] == ".":
                                is_safe = False
            if board[a - 9] != ".":
                if board[a - 9] == op:
                    if board[a + 9] == ".":
                        is_safe = False
                    else:
                        count = 1
                        while board[a + count * 9] == board[a]:
                            count += 1
                        if board[a + count * 9] == ".":
                            is_safe = False
                else:
                    count = 1
                    while board[a - count * 9] == board[a]:
                        count += 1
                    if board[a - count * 9] == op:
                        if board[a + 9] == ".":
                            is_safe = False
                        else:
                            count = 1
                            while board[a + count * 9] == board[a]:
                                count += 1
                            if board[a - count * 9] == ".":
                                is_safe = False
            if is_safe:
                if a not in corners:
                    count = 1
                    while board[a - count] != "." and board[a - count] != "?":
                        count += 1
                    if board[a - count] == ".":
                        count = 1
                        while board[a + count] != "." and board[a + count] != "?":
                            count += 1
                        if board[a + count] == ".":
                            stable = False
                    count = 1
                    while board[a - 10 * count] != "." and board[a - 10 * count] != "?":
                        count += 1
                    if board[a - 10 * count] == ".":
                        count = 1
                        while board[a + 10 * count] != "." and board[a + 10 * count] != "?":
                            count += 1
                        if board[a + 10 * count] == ".":
                            stable = False
                    count = 1
                    while board[a - 11 * count] != "." and board[a - 11 * count] != "?":
                        count += 1
                    if board[a - 11 * count] == ".":
                        count = 1
                        while board[a + 11 * count] != "." and board[a + 11 * count] != "?":
                            count += 1
                        if board[a + 11 * count] == ".":
                            stable = False
                    count = 1
                    while board[a - 9 * count] != "." and board[a - 9 * count] != "?":
                        count += 1
                    if board[a - 9 * count] == ".":
                        count = 1
                        while board[a + 9 * count] != "." and board[a + 9 * count] != "?":
                            count += 1
                        if board[a + 9 * count] == ".":
                            stable = False
            else:
                stable = False
            if board[a] == "@":
                if a in corners:
                    black_edge += 700
                elif a in c_squares:
                    if stable:
                        black_edge += 1200
                    elif is_safe:
                        black_edge += 200
                    else:
                        black_edge -= 25
                elif a in a_squares:
                    if stable:
                        black_edge += 1000
                    elif is_safe:
                        black_edge += 200
                    else:
                        black_edge += 75
                elif a in b_squares:
                    if stable:
                        black_edge += 1000
                    elif is_safe:
                        black_edge += 200
                    else:
                        black_edge += 50
                elif stable:
                    black_internal += 1000
                elif is_safe:
                    black_internal += 200
                else:
                    black_internal += 50
            else:
                if a in corners:
                    white_edge += 700
                elif a in c_squares:
                    if stable:
                        white_edge += 1200
                    elif is_safe:
                        white_edge += 200
                    else:
                        white_edge -= 25
                elif a in a_squares:
                    if stable:
                        white_edge += 1000
                    elif is_safe:
                        white_edge += 200
                    else:
                        white_edge += 75
                elif a in b_squares:
                    if stable:
                        white_edge += 1000
                    elif is_safe:
                        white_edge += 200
                    else:
                        white_edge += 50
                elif stable:
                    white_internal += 1000
                elif is_safe:
                    white_internal += 200
                else:
                    white_internal += 50
    potential = white_empty + white_frontier + white_weight - black_empty - black_frontier - black_weight
    return esac * (black_edge - white_edge) + 36 * (black_internal - white_internal) + cmac * mobility + 99 * potential


board = "???????????o@@o@@@@??o@@@@@@@??oooo@oo@??o@oooo@@??o@@oo@o@??o@oooo@@??@@@@@@o@??oooooooo???????????"
print(weights)
