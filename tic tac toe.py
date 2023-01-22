import pygame

# Initialize pygame and create a window
pygame.init()
win = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Tic Tac Toe")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game variables
board = [[None, None, None], [None, None, None], [None, None, None]]
player = "X"
game_over = False

# Function to check if a player has won
def check_win():
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None:
        return board[2][0]
    return None

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 150
            col = x // 150
            if board[row][col] is None:
                board[row][col] = player
                player = "X" if player == "O" else "O"
                winner = check_win()
                if winner is not None:
                    print(f"{winner} wins!")
                    game_over = True
                elif not any(None in row for row in board):
                    print("It's a draw!")
                    game_over = True

    # Draw the game board
    win.fill(BLACK)
    for i in range(3):
        for j in range(3):
            x = j * 150
            y = i * 150
            pygame.draw.rect(win, WHITE, (x, y, 150, 150), 5)
            if board[i][j] is None:
                continue
            elif board[i][j] == "X":
                pygame.draw.line(win, RED, (x+25, y+25), (x+125, y+125), 5)
                pygame.draw.line(win, RED, (x+125, y+25), (x+25, y+125), 5)
            else:
                pygame.draw.circle(win, WHITE, (x + 75, y + 75), 50, 5)
    pygame.display.update()

# Exit pygame
pygame.quit()