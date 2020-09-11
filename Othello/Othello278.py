import random


def display(state):
    count = 1
    for a in state:
        if count % 10 == 0:
            print(a + " ")
        else:
            print(a + " ", end="", flush=True)
        count += 1


def opposite(tkn):
    if tkn == "o":
        return "@"
    else:
        return "o"


def possible(board, tkn):
    moves = []
    op = opposite(tkn)
    for index in range(11, 90):
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


def move(board, tkn, position):
    temp = board[:position] + tkn + board[position + 1:]
    op = opposite(tkn)
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


def count_tkn(board):
    return board.count("@"), board.count("o")


def score_board(board):
    black_score = 0
    white_score = 0
    for a in range(11, 90):
        if board[a] == "." or board[a] == "?":
            continue
        elif a in [11, 18, 81, 88]:
            if a == "@":
                black_score += 3
            else:
                white_score += 3
        else:
            is_safe = True
            op = {"o": "@", "@": "o"}[board[a]]
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
                if board[a] == "@":
                    black_score += 1
                else:
                    white_score += 1
    return black_score - white_score


def random_game(board):
    sequence = []
    tkn = "@"
    while "." in board:
        moves = possible(board, tkn)
        display(board)
        (black, white) = count_tkn(board)
        print("Black:" + str(black) + " White:" + str(white))
        print(moves)
        if len(moves) == 0:
            tkn = opposite(tkn)
            moves = possible(board, tkn)
            if len(moves) == 0:
                break
            else:
                print("pass")
                sequence.append(-1)
                continue
        ran = random.choice(moves)
        print(ran)
        print(score_board(board))
        sequence.append(ran)
        board = move(board, tkn, ran)
        tkn = opposite(tkn)
    display(board)
    (black, white) = count_tkn(board)
    print("Black:" + str(black) + " White:" + str(white))
    print("Black:" + str(black / (black + white) * 100) + "% White:" + str(white / (black + white) * 100) + "%")
    print(sequence)


board = "???????????........??........??........??...o@...??...@o...??........??........??........???????????"
board = move(board, "@", 34)
board = move(board, "o", 53)
board = move(board, "@", 66)
board = move(board, "o", 56)
print('"' + board + '"')
display(board)
# random_game(board)
# display(board)
# print()
# tkn = "@"
# while True:
#     print(possible(board, tkn))
#     m = int(input())
#     board = move(board, tkn, m)
#     display(board)
#     tkn = opposite(tkn)
