tic_tac_toe = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
players = ["X", "O"]
turn = 0


def set_game_stage(stage):
    for c in range(len(stage)):
        tic_tac_toe[c // 3][c % 3] = stage[c]


def get_display():
    display = "---------\n| "
    for i in range(len(tic_tac_toe)):
        for j in range(len(tic_tac_toe[i])):
            display += tic_tac_toe[i][j] + " "
            if j == len(tic_tac_toe[i]) - 1:
                display += "|"
        display += "\n"
        if i < len(tic_tac_toe) - 1:
            display += "| "
    display += "---------"
    return display


def is_player_winner(player):
    three_in_a_row = 3 * player
    if three_in_a_row == (tic_tac_toe[0][0] + tic_tac_toe[1][1] + tic_tac_toe[2][2]):  # check backslash \
        return True
    if three_in_a_row == (tic_tac_toe[0][2] + tic_tac_toe[1][1] + tic_tac_toe[2][0]):  # check slash /
        return True
    for i in range(3):
        if three_in_a_row == "".join(tic_tac_toe[i]):  # check rows
            return True
        if three_in_a_row == (tic_tac_toe[0][i] + tic_tac_toe[1][i] + tic_tac_toe[2][i]):  # check cols
            return True
    return False


def is_possible():
    count_x = 0
    count_o = 0
    if is_player_winner("X") and is_player_winner("O"):
        return False
    for row in tic_tac_toe:
        for cel in row:
            if cel == "X":
                count_x += 1
            elif cel == "O":
                count_o += 1
    if abs(count_x - count_o) > 1:
        return False
    return True


def is_game_finished():
    for row in tic_tac_toe:
        for cel in row:
            if cel == "_":
                return False
    return True


def analyze_move(move):
    coordinates = move.split()
    coordinate_x = coordinates[0]
    coordinate_y = coordinates[1]
    if not coordinate_x.isdigit() or not coordinate_y.isdigit():
        return False, "You should enter numbers!"
    else:
        i = int(coordinate_x) - 1
        j = int(coordinate_y) - 1
        if not 0 <= i <= 2 or not 0 <= j <= 2:
            return False, "Coordinates should be from 1 to 3!"
        elif tic_tac_toe[i][j] != "_":
            return False, "This cell is occupied! Choose another one!"
    return True, [i, j]


def do_move(i, j, player):
    tic_tac_toe[i][j] = player


def try_to_move():
    analyzed_move = analyze_move(input())
    if analyzed_move[0]:
        do_move(analyzed_move[1][0], analyzed_move[1][1], players[turn % 2])
        print(get_display())
    else:
        print(analyzed_move[1])
        try_to_move()


def lets_play():
    global turn
    if any([is_player_winner(player) for player in players]):
        print(f"{players[(turn + 1) % 2]} wins")
    elif not is_game_finished():
        if turn == 0:
            print(get_display())
        try_to_move()
        turn += 1
        lets_play()
    else:
        print("Draw")


def start_from_input():
    set_game_stage(input())
    if is_possible():
        # MISSING SET THE TURN ACCORD THE NUMBER OF "X" and "O"
        lets_play()
    else:
        start_from_input()


lets_play()
