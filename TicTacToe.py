board = [["", "", ""], ["", "", ""], ["", "", ""]]

win_combos = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

print(board[0])
print(board[1])
print(board[2])

winner = False


def check_win(winner):
    print("------------------")
    for combo in win_combos:
        collective = []
        for x, y in combo:
            collective.append(board[x][y])
            if ''.join(collective) == "XXX" or ''.join(collective) == "OOO":
                winner = True
                print('you win')
                return True
    return winner


def playerX():
    x_horiz = int(input("Player X - choose your x coordinate"))
    x_vert = int(input("Player X - choose your y coordinate"))
    while board[x_vert][x_horiz] != "X":
        if len(board[x_vert][x_horiz]) == 0:
            board[x_vert][x_horiz] = "X"
            print(board[0])
            print(board[1])
            print(board[2])
            break
    else:
        print("spot taken")
        x_horiz = int(input("Player X - choose your x coordinate"))
        x_vert = int(input("Player X - choose your y coordinate"))


def playerO():
    o_horiz = int(input("Player O - choose your x coordinate"))
    o_vert = int(input("Player O - choose your y coordinate"))
    while board[o_vert][o_horiz] != "O":
        if len(board[o_vert][o_horiz]) == 0:
            board[o_vert][o_horiz] = "O"
            print(board[0])
            print(board[1])
            print(board[2])
            break
        else:
            print("spot taken")
            o_horiz = int(input("Player O - choose your x coordinate"))
            o_vert = int(input("Player O - choose your y coordinate"))


while not winner:
    playerX()
    winner = (check_win(winner))
    playerO()
    winner = (check_win(winner))
print(board)
