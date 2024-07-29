def print_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    # Check if the board is completely filled (draw)
    for row in board:
        if " " in row:
            return False
    return True

def ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        return empty_cells[0]  # Basic random move (choose the first empty cell)
    return None

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    user_symbol = "X"
    ai_symbol = "O"

    while True:
        print_board(board)
        row, col = map(int, input("Enter row (0-2) and column (0-2): ").split())

        # Validate input
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = user_symbol
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, user_symbol):
            print("You win!")
            break

        ai_next_move = ai_move(board)
        if ai_next_move:
            ai_row, ai_col = ai_next_move
            board[ai_row][ai_col] = ai_symbol

        if check_win(board, ai_symbol):
            print("AI wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

    print("Game over!")

if __name__ == "__main__":
    main()

        
 
