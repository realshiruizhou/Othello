import time


def display(state):
    count = 1
    for a in state:
        if count % 10 == 0:
            print(a + " ")
        else:
            print(a + " ", end="", flush=True)
        count += 1


class Strategy:
    corners = [11, 18, 81, 88]
    x_squares = [22, 27, 72, 77]
    c_squares = [12, 17, 21, 28, 71, 82, 87, 78]
    a_squares = [13, 16, 31, 38, 61, 68, 83, 86]
    b_squares = [14, 15, 41, 51, 48, 58, 84, 85]
    edges = [13, 14, 15, 16, 83, 84, 85, 86, 31, 41, 51, 62, 38, 48, 58, 68]
    weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
               0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
               0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
               0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
               0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
               0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
               0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
               0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    move_2 = {"???????????........??........??...@....??...@@...??...@o...??........??........??........???????????": 53,
              "???????????........??........??........??..@@@...??...@o...??........??........??........???????????": 35,
              "???????????........??........??........??...o@...??...@@...??....@...??........??........???????????": 46,
              "???????????........??........??........??...o@...??...@@@..??........??........??........???????????": 64}

    move_3 = {"???????????........??........??..o@....??...o@...??...@o...??........??........??........???????????": 43,
              "???????????........??........??...@o...??...@o...??...@o...??........??........??........???????????": 46,
              "???????????........??........??...@....??...@@...??..ooo...??........??........??........???????????": 66}

    move_4 = {"???????????........??........??...@....??...@@...??..@oo...??.@......??........??........???????????": 36,
              "???????????........??........??...@....??...@@...??..o@o...??..@.....??........??........???????????": 35,
              "???????????........??........??...@....??...@@...??..o@o...??...@....??........??........???????????": 35,
              "???????????........??........??...@....??...@@...??..oo@...??....@...??........??........???????????": 56,
              "???????????........??........??....o...??..@@o...??...@@...??.....@..??........??........???????????": 65,
              "???????????........??........??....o...??..@@o...??...@@@..??........??........??........???????????": 65,
              "???????????........??........??...@....??...@@...??..oo@...??.....@..??........??........???????????": 56,
              "???????????........??........??....o...??..@@@@..??...@o...??........??........??........???????????": 53,
              "???????????........??........??....o@..??..@@@...??...@o...??........??........??........???????????": 53,
              "???????????........??.....@..??....@...??..@@o...??...@o...??........??........??........???????????": 63,
              "???????????........??........??......@.??...oo@..??...@@...??....@...??........??........???????????": 63,
              "???????????........??........??.....@..??...o@o..??...@@...??....@...??........??........???????????": 64,
              "???????????........??........??....@...??...o@o..??...@@...??....@...??........??........???????????": 64,
              "???????????........??........??..@.....??...@oo..??...@@...??....@...??........??........???????????": 43,
              "???????????........??........??...@....??...@oo..??...@@...??....@...??........??........???????????": 43,
              "???????????........??........??..@.....??...@@...??...o@@..??...o....??........??........???????????": 34,
              "???????????........??........??........??..@@@...??...o@@..??...o....??........??........???????????": 34,
              "???????????........??........??........??...o@...??...@o...??........??........??........???????????": 46,
              "???????????........??........??........??...o@...??...@@@..??..@o....??........??........???????????": 46,
              "???????????........??........??........??...o@...??...o@@..??...@....??..@.....??........???????????": 36}

    move_5 = {"???????????........??........??..o@....??..o@@...??..ooo...??........??........??........???????????": 64,
              "???????????........??........??..ooo...??..@@o...??...@o...??........??........??........???????????": 46,
              "???????????........??........??..ooo...??...o@@..??...@o...??........??........??........???????????": 56,
              "???????????........??........??...@o...??...o@@..??..ooo...??........??........??........???????????": 36,
              "???????????........??........??...@o.o.??...@@o..??...@o...??........??........??........???????????": 47,
              "???????????........??........??...@o...??...@@o..??...@o.o.??........??........??........???????????": 47,
              "???????????........??...o....??...o....??...o@...??..oo@...??.....@..??........??........???????????": 63,
              "???????????........??........??...@o...??...o@...??..oo@...??.....@..??........??........???????????": 33,
              "???????????........??........??...@.o..??...@o...??..oo@...??.....@..??........??........???????????": 56,
              "???????????........??........??...@....??...@@...??..oooo..??.....@..??........??........???????????": 65}

    @staticmethod
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

    @staticmethod
    def move(board, tkn, position):
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

    def get_next_player(self, board, tkn):
        if len(self.legal_moves(board, tkn)) > 0:
            return tkn
        elif len(self.legal_moves(board, {"o": "@", "@": "o"}[tkn])) > 0:
            return {"o": "@", "@": "o"}[tkn]
        else:
            return "?"

    def score_board(self, board):
        black_corners = 0
        white_corners = 0
        black_stable = 0
        white_stable = 0
        black_safe = 0
        white_safe = 0
        black = 0
        white = 0
        black_x = 0
        white_x = 0
        black_c = 0
        white_c = 0
        for a in range(11, 89):
            if board[a] == "." or board[a] == "?":
                continue
            else:
                is_safe = True
                stable = True
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
                    if a not in self.corners:
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
                if a in self.corners:
                    if board[a] == "@":
                        black_corners += 1
                    else:
                        white_corners += 1
                elif is_safe and stable:
                    if board[a] == "@":
                        black_stable += 1
                    else:
                        white_stable += 1
                elif a in self.x_squares:
                    if board[a] == "@":
                        black_x += 1
                    else:
                        white_x += 1
                elif a in self.c_squares:
                    if board[a] == "@":
                        black_c += 1
                    else:
                        white_c += 1
                elif is_safe:
                    if board[a] == "@":
                        black_safe += 1
                    else:
                        white_safe += 1
                else:
                    if board[a] == "@":
                        black += 1
                    else:
                        white += 1
        if black_stable + black_corners == 0 or white_stable + white_corners == 0:
            black_score = 0
            white_score = 0
            for a in range(11, 90):
                if board[a] == "@":
                    black_score += self.weights[a]
                elif board[a] == "o":
                    white_score += self.weights[a]
            return black_score - white_score + (len(self.legal_moves(board, "@")) - len(self.legal_moves(board, "o"))) * 10
        else:
            return (black_corners - white_corners) * 20 + (black_stable - white_stable) * 10 + (black_safe - white_safe) * 5 + black - white

    # def score_board(self, board):
    #     black_edge = 0
    #     white_edge = 0
    #     black_internal = 0
    #     white_internal = 0
    #     black_frontier = 0
    #     white_frontier = 0
    #     move = 61 - board.count(".")
    #     esac = 312 + 6.24 * move
    #     if move <= 25:
    #         cmac = 50 + 2 * move
    #     else:
    #         cmac = 75 + move
    #     black_moves = self.legal_moves(board, "@")
    #     white_moves = self.legal_moves(board, "o")
    #     white_only = len(white_moves)
    #     black_only = len(black_moves)
    #     common = 0
    #     for a in black_moves:
    #         if a in white_moves:
    #             common += 1
    #     white_only -= common
    #     black_only -= common
    #     b = black_only * 2 + common
    #     w = white_only * 2 + common
    #     mobility = int(1000 * (b - w) / (b + w + 2))
    #     black_empty = 0
    #     white_empty = 0
    #     black_weight = 0
    #     white_weight = 0
    #     for a in range(11, 90):
    #         if board[a] == "?":
    #             continue
    #         if board[a] == ".":
    #             adj_black = False
    #             adj_white = False
    #             if board[a + 1] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 1] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a + 11] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 11] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a + 10] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 10] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 1] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 1] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a + 9] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 9] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 10] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 10] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 11] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 11] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 9] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 9] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if adj_black:
    #                 black_empty += 1
    #             if adj_white:
    #                 white_empty += 1
    #         else:
    #             is_safe = True
    #             stable = True
    #             op = {"o": "@", "@": "o"}[board[a]]
    #             if board[a + 1] == "." or board[a - 1] == "." or board[a + 10] == "." or board[a - 10] == '.' or board[
    #                 a + 11] == "." or board[a - 11] == "." or board[a - 9] == "." or board[a + 9] == ".":
    #                 if board[a] == "@":
    #                     black_frontier += 1
    #                 else:
    #                     white_frontier += 1
    #             if board[a + 1] != ".":
    #                 if board[a + 1] == op:
    #                     if board[a - 1] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 1] == board[a]:
    #                             count += 1
    #                         if board[a - count * 1] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 1] == board[a]:
    #                         count += 1
    #                     if board[a + count * 1] == op:
    #                         if board[a - 1] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 1] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 1] == ".":
    #                                 is_safe = False
    #             if board[a - 1] != ".":
    #                 if board[a - 1] == op:
    #                     if board[a + 1] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 1] == board[a]:
    #                             count += 1
    #                         if board[a + count * 1] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 1] == board[a]:
    #                         count += 1
    #                     if board[a - count * 1] == op:
    #                         if board[a + 1] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 1] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 1] == ".":
    #                                 is_safe = False
    #             if board[a + 10] != ".":
    #                 if board[a + 10] == op:
    #                     if board[a - 10] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 10] == board[a]:
    #                             count += 1
    #                         if board[a - count * 10] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 10] == board[a]:
    #                         count += 1
    #                     if board[a + count * 10] == op:
    #                         if board[a - 10] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 10] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 10] == ".":
    #                                 is_safe = False
    #             if board[a - 10] != ".":
    #                 if board[a - 10] == op:
    #                     if board[a + 10] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 10] == board[a]:
    #                             count += 1
    #                         if board[a + count * 10] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 10] == board[a]:
    #                         count += 1
    #                     if board[a - count * 10] == op:
    #                         if board[a + 10] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 10] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 10] == ".":
    #                                 is_safe = False
    #             if board[a + 11] != ".":
    #                 if board[a + 11] == op:
    #                     if board[a - 11] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 11] == board[a]:
    #                             count += 1
    #                         if board[a - count * 11] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 11] == board[a]:
    #                         count += 1
    #                     if board[a + count * 11] == op:
    #                         if board[a - 11] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 11] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 11] == ".":
    #                                 is_safe = False
    #             if board[a - 11] != ".":
    #                 if board[a - 11] == op:
    #                     if board[a + 11] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 11] == board[a]:
    #                             count += 1
    #                         if board[a + count * 11] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 11] == board[a]:
    #                         count += 1
    #                     if board[a - count * 11] == op:
    #                         if board[a + 11] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 11] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 11] == ".":
    #                                 is_safe = False
    #             if board[a + 9] != ".":
    #                 if board[a + 9] == op:
    #                     if board[a - 9] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 9] == board[a]:
    #                             count += 1
    #                         if board[a - count * 9] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 9] == board[a]:
    #                         count += 1
    #                     if board[a + count * 9] == op:
    #                         if board[a - 9] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 9] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 9] == ".":
    #                                 is_safe = False
    #             if board[a - 9] != ".":
    #                 if board[a - 9] == op:
    #                     if board[a + 9] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 9] == board[a]:
    #                             count += 1
    #                         if board[a + count * 9] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 9] == board[a]:
    #                         count += 1
    #                     if board[a - count * 9] == op:
    #                         if board[a + 9] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 9] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 9] == ".":
    #                                 is_safe = False
    #             if is_safe:
    #                 if a not in self.corners:
    #                     count = 1
    #                     while board[a - count] != "." and board[a - count] != "?":
    #                         count += 1
    #                     if board[a - count] == ".":
    #                         count = 1
    #                         while board[a + count] != "." and board[a + count] != "?":
    #                             count += 1
    #                         if board[a + count] == ".":
    #                             stable = False
    #                     count = 1
    #                     while board[a - 10 * count] != "." and board[a - 10 * count] != "?":
    #                         count += 1
    #                     if board[a - 10 * count] == ".":
    #                         count = 1
    #                         while board[a + 10 * count] != "." and board[a + 10 * count] != "?":
    #                             count += 1
    #                         if board[a + 10 * count] == ".":
    #                             stable = False
    #                     count = 1
    #                     while board[a - 11 * count] != "." and board[a - 11 * count] != "?":
    #                         count += 1
    #                     if board[a - 11 * count] == ".":
    #                         count = 1
    #                         while board[a + 11 * count] != "." and board[a + 11 * count] != "?":
    #                             count += 1
    #                         if board[a + 11 * count] == ".":
    #                             stable = False
    #                     count = 1
    #                     while board[a - 9 * count] != "." and board[a - 9 * count] != "?":
    #                         count += 1
    #                     if board[a - 9 * count] == ".":
    #                         count = 1
    #                         while board[a + 9 * count] != "." and board[a + 9 * count] != "?":
    #                             count += 1
    #                         if board[a + 9 * count] == ".":
    #                             stable = False
    #             else:
    #                 stable = False
    #             if board[a] == "@":
    #                 if a in self.corners:
    #                     black_edge += 1200
    #                 elif stable:
    #                     black_edge += 1000
    #                 elif a in self.x_squares:
    #                     black_edge -= 200
    #                 elif a in self.c_squares:
    #                     black_edge -= 100
    #                 elif a in self.a_squares:
    #                     black_internal += 100
    #                 if is_safe:
    #                     black_internal += 200
    #                 else:
    #                     black_internal += 50
    #             else:
    #                 if a in self.corners:
    #                     white_edge += 1200
    #                 elif stable:
    #                     white_edge += 1000
    #                 elif a in self.x_squares:
    #                     white_internal -= 200
    #                 elif a in self.c_squares:
    #                     white_internal -= 100
    #                 elif a in self.a_squares:
    #                     white_internal += 100
    #                 if is_safe:
    #                     white_internal += 200
    #                 else:
    #                     white_internal += 50
    #     potential = white_empty + white_frontier + white_weight - black_empty - black_frontier - black_weight
    #     return esac * (black_edge - white_edge) + 36 * (black_internal - white_internal) + cmac * mobility + 99 * potential
    
    # def score_board(self, board):
    #     black_edge = 0
    #     white_edge = 0
    #     black_internal = 0
    #     white_internal = 0
    #     black_frontier = 0
    #     white_frontier = 0
    #     move = 61 - board.count(".")
    #     esac = 312 + 6.24 * move
    #     if move <= 25:
    #         cmac = 50 + 2 * move
    #     else:
    #         cmac = 75 + move
    #     black_moves = self.legal_moves(board, "@")
    #     white_moves = self.legal_moves(board, "o")
    #     temp_black = black_moves.copy()
    #     temp_white = white_moves.copy()
    #     for a in temp_black:
    #         temp_moves = self.legal_moves(self.move(board, "@", a), "o")
    #         for b in temp_moves:
    #             if b in self.corners and a in black_moves:
    #                 black_moves.remove(a)
    #     for c in temp_white:
    #         temp_moves = self.legal_moves(self.move(board, "o", c), "@")
    #         for d in temp_moves:
    #             if d in self.corners and c in white_moves:
    #                 white_moves.remove(c)
    #     white_only = len(white_moves)
    #     black_only = len(black_moves)
    #     common = 0
    #     for a in black_moves:
    #         if a in white_moves:
    #             common += 1
    #     white_only -= common
    #     black_only -= common
    #     b = black_only * 2 + common
    #     w = white_only * 2 + common
    #     mobility = int(1000 * (b - w) / (b + w + 2))
    #     black_empty = 0
    #     white_empty = 0
    #     black_weight = 0
    #     white_weight = 0
    #     for a in range(11, 90):
    #         if board[a] == "?":
    #             continue
    #         if board[a] == ".":
    #             adj_black = False
    #             adj_white = False
    #             if board[a + 1] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 1] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a + 11] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 11] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a + 10] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 10] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 1] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 1] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a + 9] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a + 9] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 10] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 10] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 11] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 11] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if board[a - 9] == "@":
    #                 adj_black = True
    #                 black_weight += 1
    #             elif board[a - 9] == "o":
    #                 adj_white = True
    #                 white_weight += 1
    #             if adj_black:
    #                 black_empty += 1
    #             if adj_white:
    #                 white_empty += 1
    #         else:
    #             is_safe = True
    #             stable = True
    #             op = {"o": "@", "@": "o"}[board[a]]
    #             if board[a + 1] == "." or board[a - 1] == "." or board[a + 10] == "." or board[a - 10] == '.' or board[
    #                 a + 11] == "." or board[a - 11] == "." or board[a - 9] == "." or board[a + 9] == ".":
    #                 if board[a] == "@":
    #                     black_frontier += 1
    #                 else:
    #                     white_frontier += 1
    #             if board[a + 1] != ".":
    #                 if board[a + 1] == op:
    #                     if board[a - 1] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 1] == board[a]:
    #                             count += 1
    #                         if board[a - count * 1] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 1] == board[a]:
    #                         count += 1
    #                     if board[a + count * 1] == op:
    #                         if board[a - 1] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 1] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 1] == ".":
    #                                 is_safe = False
    #             if board[a - 1] != ".":
    #                 if board[a - 1] == op:
    #                     if board[a + 1] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 1] == board[a]:
    #                             count += 1
    #                         if board[a + count * 1] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 1] == board[a]:
    #                         count += 1
    #                     if board[a - count * 1] == op:
    #                         if board[a + 1] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 1] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 1] == ".":
    #                                 is_safe = False
    #             if board[a + 10] != ".":
    #                 if board[a + 10] == op:
    #                     if board[a - 10] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 10] == board[a]:
    #                             count += 1
    #                         if board[a - count * 10] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 10] == board[a]:
    #                         count += 1
    #                     if board[a + count * 10] == op:
    #                         if board[a - 10] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 10] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 10] == ".":
    #                                 is_safe = False
    #             if board[a - 10] != ".":
    #                 if board[a - 10] == op:
    #                     if board[a + 10] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 10] == board[a]:
    #                             count += 1
    #                         if board[a + count * 10] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 10] == board[a]:
    #                         count += 1
    #                     if board[a - count * 10] == op:
    #                         if board[a + 10] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 10] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 10] == ".":
    #                                 is_safe = False
    #             if board[a + 11] != ".":
    #                 if board[a + 11] == op:
    #                     if board[a - 11] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 11] == board[a]:
    #                             count += 1
    #                         if board[a - count * 11] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 11] == board[a]:
    #                         count += 1
    #                     if board[a + count * 11] == op:
    #                         if board[a - 11] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 11] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 11] == ".":
    #                                 is_safe = False
    #             if board[a - 11] != ".":
    #                 if board[a - 11] == op:
    #                     if board[a + 11] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 11] == board[a]:
    #                             count += 1
    #                         if board[a + count * 11] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 11] == board[a]:
    #                         count += 1
    #                     if board[a - count * 11] == op:
    #                         if board[a + 11] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 11] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 11] == ".":
    #                                 is_safe = False
    #             if board[a + 9] != ".":
    #                 if board[a + 9] == op:
    #                     if board[a - 9] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a - count * 9] == board[a]:
    #                             count += 1
    #                         if board[a - count * 9] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a + count * 9] == board[a]:
    #                         count += 1
    #                     if board[a + count * 9] == op:
    #                         if board[a - 9] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a - count * 9] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 9] == ".":
    #                                 is_safe = False
    #             if board[a - 9] != ".":
    #                 if board[a - 9] == op:
    #                     if board[a + 9] == ".":
    #                         is_safe = False
    #                     else:
    #                         count = 1
    #                         while board[a + count * 9] == board[a]:
    #                             count += 1
    #                         if board[a + count * 9] == ".":
    #                             is_safe = False
    #                 else:
    #                     count = 1
    #                     while board[a - count * 9] == board[a]:
    #                         count += 1
    #                     if board[a - count * 9] == op:
    #                         if board[a + 9] == ".":
    #                             is_safe = False
    #                         else:
    #                             count = 1
    #                             while board[a + count * 9] == board[a]:
    #                                 count += 1
    #                             if board[a - count * 9] == ".":
    #                                 is_safe = False
    #             if is_safe:
    #                 if a not in self.corners:
    #                     count = 1
    #                     while board[a - count] != "." and board[a - count] != "?":
    #                         count += 1
    #                     if board[a - count] == ".":
    #                         count = 1
    #                         while board[a + count] != "." and board[a + count] != "?":
    #                             count += 1
    #                         if board[a + count] == ".":
    #                             stable = False
    #                     count = 1
    #                     while board[a - 10 * count] != "." and board[a - 10 * count] != "?":
    #                         count += 1
    #                     if board[a - 10 * count] == ".":
    #                         count = 1
    #                         while board[a + 10 * count] != "." and board[a + 10 * count] != "?":
    #                             count += 1
    #                         if board[a + 10 * count] == ".":
    #                             stable = False
    #                     count = 1
    #                     while board[a - 11 * count] != "." and board[a - 11 * count] != "?":
    #                         count += 1
    #                     if board[a - 11 * count] == ".":
    #                         count = 1
    #                         while board[a + 11 * count] != "." and board[a + 11 * count] != "?":
    #                             count += 1
    #                         if board[a + 11 * count] == ".":
    #                             stable = False
    #                     count = 1
    #                     while board[a - 9 * count] != "." and board[a - 9 * count] != "?":
    #                         count += 1
    #                     if board[a - 9 * count] == ".":
    #                         count = 1
    #                         while board[a + 9 * count] != "." and board[a + 9 * count] != "?":
    #                             count += 1
    #                         if board[a + 9 * count] == ".":
    #                             stable = False
    #             else:
    #                 stable = False
    #             if board[a] == "@":
    #                 if a in self.corners:
    #                     black_edge += 1200
    #                 elif a in self.c_squares:
    #                     if stable:
    #                         black_edge += 1200
    #                     elif is_safe:
    #                         black_edge += 200
    #                     else:
    #                         black_edge -= 25
    #                 elif a in self.a_squares:
    #                     if stable:
    #                         black_edge += 1000
    #                     elif is_safe:
    #                         black_edge += 200
    #                     else:
    #                         black_edge += 75
    #                 elif a in self.b_squares:
    #                     if stable:
    #                         black_edge += 1000
    #                     elif is_safe:
    #                         black_edge += 200
    #                     else:
    #                         black_edge += 50
    #                 elif stable:
    #                     black_edge += 1000
    #                 elif a in self.x_squares:
    #                     black_internal -= 1000
    #                 elif is_safe:
    #                     black_internal += 200
    #                 else:
    #                     black_internal += 50
    #             else:
    #                 if a in self.corners:
    #                     white_edge += 1200
    #                 elif a in self.c_squares:
    #                     if stable:
    #                         white_edge += 1200
    #                     elif is_safe:
    #                         white_edge += 200
    #                     else:
    #                         white_edge -= 25
    #                 elif a in self.a_squares:
    #                     if stable:
    #                         white_edge += 1000
    #                     elif is_safe:
    #                         white_edge += 200
    #                     else:
    #                         white_edge += 75
    #                 elif a in self.b_squares:
    #                     if stable:
    #                         white_edge += 1000
    #                     elif is_safe:
    #                         white_edge += 200
    #                     else:
    #                         white_edge += 50
    #                 elif stable:
    #                     white_edge += 1000
    #                 elif a in self.x_squares:
    #                     white_internal -= 1000
    #                 elif is_safe:
    #                     white_internal += 200
    #                 else:
    #                     white_internal += 50
    #     potential = white_empty + white_frontier + white_weight - black_empty - black_frontier - black_weight
    #     return esac * (black_edge - white_edge) + 36 * (black_internal - white_internal) + cmac * mobility + 99 * potential

    def maxmin(self, board, player, depth):
        opponent = {"o": "@", "@": "o"}[player]
        best = {"o": min, "@": max}
        if depth == 0:
            score = self.score_board(board)
            return None, score
        possibles = []
        for move in self.legal_moves(board, player):
            new_board = self.move(board, player, move)
            next_player = self.get_next_player(new_board, opponent)
            if next_player == "?":
                score = (new_board.count("@") - new_board.count("o")) * 10000
                possibles.append((move, score))
            else:
                possibles.append((move, self.maxmin(new_board, next_player, depth - 1)[1]))
        return best[player](possibles, key=lambda x: x[1])

    def maxmin2(self, board, player, depth, alpha, beta):
        opponent = {"o": "@", "@": "o"}[player]
        best = {"o": min, "@": max}
        if depth == 0:
            score = self.score_board(board)
            return None, score
        possibles = []
        for move in self.legal_moves(board, player):
            new_board = self.move(board, player, move)
            next_player = self.get_next_player(new_board, opponent)
            if next_player == "?":
                score = (new_board.count("@") - new_board.count("o")) * 10000
                possibles.append((move, score))
            else:
                score = self.maxmin2(new_board, next_player, depth - 1, alpha, beta)[1]
                possibles.append((move, score))
            if player == "@":
                alpha = max(alpha, score)
            elif player == "o":
                beta = min(beta, score)
            if alpha >= beta:
                break
        return best[player](possibles, key=lambda x: x[1])

    def maxmin3(self, board, player, depth, alpha, beta):
        opponent = {"o": "@", "@": "o"}[player]
        best = {"o": min, "@": max}
        if depth == 0:
            score = self.score_board2(board)
            return None, score
        possibles = []
        for move in self.legal_moves(board, player):
            new_board = self.move(board, player, move)
            next_player = self.get_next_player(new_board, opponent)
            if next_player == "?":
                score = (new_board.count("@") - new_board.count("o")) * float("inf")
                possibles.append((move, score))
            else:
                score = self.maxmin3(new_board, next_player, depth - 1, alpha, beta)[1]
                possibles.append((move, score))
            if player == "@":
                alpha = max(alpha, score)
            elif player == "o":
                beta = min(beta, score)
            if alpha >= beta:
                break
        return best[player](possibles, key=lambda x: x[1])

    @staticmethod
    def score_board2(board):
        return board.count("@") - board.count("o")

    def best_strategy(self, board, player, best_move, running):
        time.sleep(1)
        move = 61 - board.count(".")
        if move <= 5:
            if move == 1:
                best_move.value = 34
            elif move == 2:
                best_move.value = self.move_2[board]
            elif move == 3:
                best_move.value = self.move_3[board]
            elif move == 4:
                best_move.value = self.move_4[board]
            else:
                best_move.value = self.move_5[board]
        elif move >= 52:
            best_move.value = self.maxmin3(board, player, 61 - move, float("-inf"), float("inf"))[0]
        else:
            for a in range(1, 64):
                best_move.value = self.maxmin2(board, player, a, float("-inf"), float("inf"))[0]
        # for a in range(1, 64):
        #      best_move.value = self.maxmin2(board, player, a, float("-inf"), float("inf"))[0]
