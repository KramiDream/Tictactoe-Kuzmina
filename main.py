#Проверка для победителя
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

#сетка для игры
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("__" * 5)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != " ":
            print("Cell is already taken. Try again.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    tic_tac_toe()