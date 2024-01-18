import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True, row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True, board[0][2]

    # Check for a tie
    if all(all(cell != ' ' for cell in row) for row in board):
        return True, 'Tie'

    return False, None

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if check_winner(board)[0]:
        winner = check_winner(board)[1]
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        else:
            return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while not check_winner(board)[0]:
        print_board(board)

        if player == 'X':
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player = 'O'
            else:
                print("Cell is already taken. Try again.")
        else:
            print("AI's turn:")
            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = 'O'
            player = 'X'

    print_board(board)
    winner = check_winner(board)[1]

    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    play_game()