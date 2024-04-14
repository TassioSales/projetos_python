import pygame

# Inicialização do Pygame
pygame.init()

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configurações da tela
BOARD_WIDTH = 300
BOARD_HEIGHT = 300
SCORE_X_POS = BOARD_WIDTH + 40
SCORE_Y_POS = 50
SCORE_FONT_SIZE = 32
TIE_FONT_SIZE = 24

WIDTH = BOARD_WIDTH + SCORE_X_POS + 20
HEIGHT = max(BOARD_HEIGHT, SCORE_Y_POS + 4 * SCORE_FONT_SIZE + 70)
FPS = 30

# Configurações do tabuleiro
BOARD_SIZE = 3
CELL_SIZE = BOARD_WIDTH // BOARD_SIZE
CELL_PADDING = 10

# Inicialização da tela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")
clock = pygame.time.Clock()


def draw_board(board):
    screen.fill(BLACK)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * (CELL_SIZE + CELL_PADDING) + CELL_PADDING
            y = row * (CELL_SIZE + CELL_PADDING) + CELL_PADDING
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))

            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (x + 10, y + 10), (x + CELL_SIZE - 10, y + CELL_SIZE - 10), 4)
                pygame.draw.line(screen, RED, (x + CELL_SIZE - 10, y + 10), (x + 10, y + CELL_SIZE - 10), 4)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, RED, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 10, 4)


def check_win(board, player):
    for row in range(BOARD_SIZE):
        if all(cell == player for cell in board[row]):
            return True

    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True

    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True

    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True

    return False


def get_empty_cells(board):
    empty_cells = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == '':
                empty_cells.append((row, col))
    return empty_cells


def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if check_win(board, 'X'):
        return scores['X']
    elif check_win(board, 'O'):
        return scores['O']
    elif len(get_empty_cells(board)) == 0:
        return scores['tie']

    if maximizing_player:
        max_score = float('-inf')
        for empty_cell in get_empty_cells(board):
            row, col = empty_cell
            board[row][col] = 'X'
            score = minimax(board, depth + 1, False)
            board[row][col] = ''
            max_score = max(max_score, score)
        return max_score
    else:
        min_score = float('inf')
        for empty_cell in get_empty_cells(board):
            row, col = empty_cell
            board[row][col] = 'O'
            score = minimax(board, depth + 1, True)
            board[row][col] = ''
            min_score = min(min_score, score)
        return min_score


def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for empty_cell in get_empty_cells(board):
        row, col = empty_cell
        board[row][col] = 'X'
        score = minimax(board, 0, False)
        board[row][col] = ''
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


def draw_scores(scores):
    font = pygame.font.Font(None, SCORE_FONT_SIZE)
    tie_font = pygame.font.Font(None, TIE_FONT_SIZE)

    x_score_text = font.render(f"X: {scores['X']}", True, WHITE)
    o_score_text = font.render(f"O: {scores['O']}", True, WHITE)
    tie_score_text = tie_font.render(f"Empates: {scores['tie']}", True, WHITE)

    screen.blit(x_score_text, (SCORE_X_POS, SCORE_Y_POS))
    screen.blit(o_score_text, (SCORE_X_POS, SCORE_Y_POS + SCORE_FONT_SIZE))
    screen.blit(tie_score_text, (SCORE_X_POS, SCORE_Y_POS + 2 * SCORE_FONT_SIZE))


def reset_board(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            board[row][col] = ''


def game():
    board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    scores = {'X': 0, 'O': 0, 'tie': 0}
    player_turn = True  # True: jogador, False: IA

    restart_button = pygame.Rect(SCORE_X_POS, SCORE_Y_POS + 3 * SCORE_FONT_SIZE + 20, 100, 50)
    restart_text = pygame.font.Font(None, 24).render("Reiniciar", True, WHITE)

    exit_button = pygame.Rect(SCORE_X_POS, SCORE_Y_POS + 3 * SCORE_FONT_SIZE + 80, 100, 50)
    exit_text = pygame.font.Font(None, 24).render("Sair", True, WHITE)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                if event.button == 1:  # Botão esquerdo do mouse
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // (CELL_SIZE + CELL_PADDING)
                    col = pos[0] // (CELL_SIZE + CELL_PADDING)
                    if row < BOARD_SIZE and col < BOARD_SIZE and board[row][col] == '':
                        board[row][col] = 'O'
                        player_turn = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    pos = pygame.mouse.get_pos()
                    if restart_button.collidepoint(pos):
                        reset_board(board)
                        player_turn = True
                    elif exit_button.collidepoint(pos):
                        running = False

        if not player_turn:
            if len(get_empty_cells(board)) > 0:
                row, col = get_best_move(board)
                board[row][col] = 'X'
                player_turn = True

        draw_board(board)
        draw_scores(scores)

        pygame.draw.rect(screen, RED, restart_button)
        screen.blit(restart_text, (SCORE_X_POS + 10, SCORE_Y_POS + 3 * SCORE_FONT_SIZE + 35))

        pygame.draw.rect(screen, RED, exit_button)
        screen.blit(exit_text, (SCORE_X_POS + 25, SCORE_Y_POS + 3 * SCORE_FONT_SIZE + 95))

        pygame.display.flip()

        if check_win(board, 'O'):
            scores['O'] += 1
            pygame.time.wait(100)  # Espera 1 segundo antes de reiniciar o jogo
            reset_board(board)
        elif check_win(board, 'X'):
            scores['X'] += 1
            pygame.time.wait(100)  # Espera 1 segundo antes de reiniciar o jogo
            reset_board(board)
        elif len(get_empty_cells(board)) == 0:
            scores['tie'] += 1
            pygame.time.wait(100)  # Espera 1 segundo antes de reiniciar o jogo
            reset_board(board)


# Executar o jogo
game()
