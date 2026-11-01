import pygame
import sys
from game_logic import TicTacToeGame
from ai.random_ai import RandomAI
from ai.minimax_ai import MinimaxAI
from sound_manager import SoundManager

# Инициализация
pygame.init()
pygame.font.init()

# Размеры экрана

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800



BOARD_SIZE = WINDOW_WIDTH
PANEL_HEIGHT = WINDOW_HEIGHT - WINDOW_WIDTH

screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
WIDTH, HEIGHT = screen.get_size()

WIDTH = BOARD_SIZE
HEIGHT = BOARD_SIZE + PANEL_HEIGHT


LINE_WIDTH = 8
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = BOARD_SIZE // BOARD_COLS

# Цветовая палитра
BG_COLOR = (20, 24, 33)
PANEL_BG = (14, 17, 23)
LINE_COLOR = (38, 45, 61)
X_COLOR = (255, 46, 99)
O_COLOR = (0, 225, 255)
OVERLAY_COLOR = (15, 18, 26)
TEXT_MUTED = (110, 120, 140)
BTN_ACTIVE_BG = (35, 45, 60)
BTN_INACTIVE_BG = (22, 26, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe: Cyber Edition')

FONT_MAIN = pygame.font.SysFont('Arial', 40, bold=True)
FONT_SUB = pygame.font.SysFont('Arial', 20, bold=False)
FONT_PANEL_TITLE = pygame.font.SysFont('Arial', 14, bold=True)
FONT_PANEL_VALUE = pygame.font.SysFont('Arial', 18, bold=True)
FONT_BTN = pygame.font.SysFont('Arial', 14, bold=True)

# Настройка игры
game = TicTacToeGame()

ai_modes = {
    "easy": {"bot": RandomAI(ai_player_num=2), "name": "RANDOM BOT"},
    "hard": {"bot": MinimaxAI(ai_player_num=2), "name": "MINIMAX v1.0"}
}
current_mode = "hard"
ai_bot = ai_modes[current_mode]["bot"]

# Координаты кнопок
btn_easy_rect = pygame.Rect( int(BOARD_SIZE * 0.04) , BOARD_SIZE + 90, int(BOARD_SIZE * 0.40), 40)
btn_hard_rect = pygame.Rect( int(BOARD_SIZE * 0.56) , BOARD_SIZE + 90, int(BOARD_SIZE * 0.40), 40)


def draw_grid():
    pygame.draw.rect(screen, BG_COLOR, (0, 0, BOARD_SIZE, BOARD_SIZE))
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (20, i * SQUARE_SIZE), (BOARD_SIZE - 20, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 20), (i * SQUARE_SIZE, BOARD_SIZE - 20), LINE_WIDTH)


def draw_bottom_panel():
    pygame.draw.rect(screen, PANEL_BG, (0, BOARD_SIZE, WIDTH, PANEL_HEIGHT))
    pygame.draw.line(screen, LINE_COLOR, (0, BOARD_SIZE), (WIDTH, BOARD_SIZE), 4)

    lbl_enemy = FONT_PANEL_TITLE.render("ПРОТИВНИК:", True, TEXT_MUTED)
    screen.blit(lbl_enemy, (25, BOARD_SIZE + 20))
    val_enemy = FONT_PANEL_VALUE.render(ai_modes[current_mode]["name"], True, (255, 255, 255))
    screen.blit(val_enemy, (25, BOARD_SIZE + 42))

    lbl_status = FONT_PANEL_TITLE.render("СТАТУС ИГРЫ:", True, TEXT_MUTED)
    screen.blit(lbl_status, (250, BOARD_SIZE + 20))

    if game.game_over:
        status_text = "ЗАВЕРШЕНА"
        status_color = X_COLOR
    elif game.current_player == 1:
        status_text = "ВАШ ХОД"
        status_color = (46, 254, 157)
    else:
        status_text = "ИИ ДУМАЕТ..."
        status_color = O_COLOR

    val_status = FONT_PANEL_VALUE.render(status_text, True, status_color)
    screen.blit(val_status, (250, BOARD_SIZE + 42))

    # Легкий режим
    easy_bg = BTN_ACTIVE_BG if current_mode == "easy" else BTN_INACTIVE_BG
    easy_border = O_COLOR if current_mode == "easy" else LINE_COLOR
    pygame.draw.rect(screen, easy_bg, btn_easy_rect, border_radius=6)
    pygame.draw.rect(screen, easy_border, btn_easy_rect, width=2, border_radius=6)
    txt_easy = FONT_BTN.render("ЛЕГКИЙ РЕЖИМ", True, O_COLOR if current_mode == "easy" else TEXT_MUTED)
    screen.blit(txt_easy, txt_easy.get_rect(center=btn_easy_rect.center))

    # Сложный режим
    hard_bg = BTN_ACTIVE_BG if current_mode == "hard" else BTN_INACTIVE_BG
    hard_border = X_COLOR if current_mode == "hard" else LINE_COLOR
    pygame.draw.rect(screen, hard_bg, btn_hard_rect, border_radius=6)
    pygame.draw.rect(screen, hard_border, btn_hard_rect, width=2, border_radius=6)
    txt_hard = FONT_BTN.render("СЛОЖНЫЙ РЕЖИМ", True, X_COLOR if current_mode == "hard" else TEXT_MUTED)
    screen.blit(txt_hard, txt_hard.get_rect(center=btn_hard_rect.center))


def draw_glow_circle(surface, color, center, radius, width):
    cx, cy = center
    glow_surf = pygame.Surface((radius * 2 + 20, radius * 2 + 20), pygame.SRCALPHA)
    pygame.draw.circle(glow_surf, (*color, 40), (radius + 10, radius + 10), radius + 4, width + 4)
    surface.blit(glow_surf, (cx - radius - 10, cy - radius - 10))
    pygame.draw.circle(surface, color, center, radius, width)


def draw_figures():
    padding = 40
    for row in range(BOARD_ROWS):
        y_center = row * SQUARE_SIZE + SQUARE_SIZE // 2
        for col in range(BOARD_COLS):
            x_center = col * SQUARE_SIZE + SQUARE_SIZE // 2
            x_start = col * SQUARE_SIZE + padding
            x_end = col * SQUARE_SIZE + SQUARE_SIZE - padding
            y_start = row * SQUARE_SIZE + padding
            y_end = row * SQUARE_SIZE + SQUARE_SIZE - padding

            if game.board[row, col] == 1:
                pygame.draw.line(screen, X_COLOR, (x_start, y_end), (x_end, y_start), 12)
                pygame.draw.line(screen, X_COLOR, (x_start, y_start), (x_end, y_end), 12)
            elif game.board[row, col] == 2:
                draw_glow_circle(screen, O_COLOR, (x_center, y_center), SQUARE_SIZE // 2 - padding, 10)


def draw_winning_line():
    if not game.game_over or game.win_line is None:
        return
    line_type, idx = game.win_line
    color = X_COLOR if game.winner == 1 else O_COLOR
    start_pos, end_pos = (0, 0), (0, 0)
    if line_type == 'row':
        y = idx * SQUARE_SIZE + SQUARE_SIZE // 2
        start_pos = (15, y)
        end_pos = (BOARD_SIZE - 15, y)
    elif line_type == 'col':
        x = idx * SQUARE_SIZE + SQUARE_SIZE // 2
        start_pos = (x, 15)
        end_pos = (x, BOARD_SIZE - 15)
    elif line_type == 'diag':
        if idx == 0:
            start_pos = (20, 20)
            end_pos = (BOARD_SIZE - 20, BOARD_SIZE - 20)
        else:
            start_pos = (20, BOARD_SIZE - 20)
            end_pos = (BOARD_SIZE - 20, 20)

    glow_surf = pygame.Surface((BOARD_SIZE, BOARD_SIZE), pygame.SRCALPHA)
    pygame.draw.line(glow_surf, (*color, 60), start_pos, end_pos, 22)
    pygame.draw.line(glow_surf, (*color, 150), start_pos, end_pos, 14)
    screen.blit(glow_surf, (0, 0))
    pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos, 4)


def draw_game_over_screen():
    if not game.game_over:
        return
    overlay = pygame.Surface((BOARD_SIZE, BOARD_SIZE), pygame.SRCALPHA)
    overlay.fill((*OVERLAY_COLOR, 128))
    screen.blit(overlay, (0, 0))

    if game.winner == 1:
        text_str, text_color = "ПОБЕДА!", (46, 254, 157)
    elif game.winner == 2:
        text_str, text_color = "ПОРАЖЕНИЕ", X_COLOR
    else:
        text_str, text_color = "НИЧЬЯ", (255, 215, 0)

    text_surface = FONT_MAIN.render(text_str, True, text_color)
    text_rect = text_surface.get_rect(center=(BOARD_SIZE // 2, BOARD_SIZE // 2 - 20))
    screen.blit(text_surface, text_rect)

    sub_surface = FONT_SUB.render("Кликните для новой игры", True, (255, 255, 255))
    sub_rect = sub_surface.get_rect(center=(BOARD_SIZE // 2, BOARD_SIZE // 2 + 30))
    screen.blit(sub_surface, sub_rect)


def check_panel_clicks(pos):
    """Вынесенная функция обработки кликов по нижней панели для исключения ошибок отступов"""
    global current_mode, ai_bot, sound_played
    if btn_easy_rect.collidepoint(pos) and current_mode != "easy":
        current_mode = "easy"
        ai_bot = ai_modes[current_mode]["bot"]
        game.reset()
        sound_played = False
        sounds.play_click()
        draw_grid()
        draw_bottom_panel()
    elif btn_hard_rect.collidepoint(pos) and current_mode != "hard":
        current_mode = "hard"
        ai_bot = ai_modes[current_mode]["bot"]
        game.reset()
        sound_played = False
        sounds.play_click()
        draw_grid()
        draw_bottom_panel()


# Первичный рендеринг
draw_grid()
draw_bottom_panel()
pygame.display.update()

sounds = SoundManager()
sound_played = False

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos

            # Клик по игровому полю
            if mouseY < BOARD_SIZE:
                if game.game_over:
                    game.reset()
                    sound_played = False
                    sounds.play_click()
                    draw_grid()
                    draw_bottom_panel()
                elif game.current_player == 1:
                    clicked_row = mouseY // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE

                    if game.make_move(clicked_row, clicked_col):
                        sounds.play_click()
                        draw_grid()
                        draw_figures()
                        draw_bottom_panel()

            # Безболезненный клик по нижней панели через внешнюю функцию
            if mouseY >= BOARD_SIZE:
                check_panel_clicks(event.pos)

    # Ход ИИ
    if game.current_player == 2 and not game.game_over:
        draw_bottom_panel()
        pygame.display.update()

        pygame.time.wait(350)
        ai_row, ai_col = ai_bot.get_move(game.board)

        if game.make_move(ai_row, ai_col):
            sounds.play_ai()
            draw_grid()
            draw_figures()
            draw_bottom_panel()

    # Финал
    if game.game_over:
        draw_winning_line()
        draw_game_over_screen()

        if not sound_played:
            if game.winner == 1:
                sounds.play_win()
            elif game.winner == 2:
                sounds.play_lose()
            else:
                sounds.play_click()
            sound_played = True
        draw_bottom_panel()

    pygame.display.update()
