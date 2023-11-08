import pygame

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (12, 34, 124)

# Определение размеров окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Движение и прыжок")

# Определение начальных координат и скорости игрока
player_x = 50
player_y = SCREEN_HEIGHT - 100
player_vel_x = 1
player_vel_y = -0.001
is_jumping = False
jump_count = 0

# Объявление переменной для препятствия
obstacle_x = 500
obstacle_y = 500
obstacle_width = 50
obstacle_height = 50

# Основной игровой цикл
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_vel_x
    if keys[pygame.K_RIGHT]:
        player_x += player_vel_x
    if keys[pygame.K_SPACE] and not is_jumping:
        player_vel_y = -1.5
        is_jumping = True
        jump_count += 1

    # Применение гравитации
    player_vel_y += 0.005
    player_y += player_vel_y

    # Проверка столкновения с землей
    if player_y >= SCREEN_HEIGHT - 100:
        player_y = SCREEN_HEIGHT - 100
        player_vel_y = 0
        is_jumping = False

    # Проверка столкновения с препятствием
    if player_x < obstacle_x + obstacle_width and player_x + 50 > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + 50 > obstacle_y:
        game_over = True

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка игрока
    pygame.draw.rect(screen, DARK_BLUE, (player_x, player_y, 50, 50))

    # Отрисовка препятствия
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Отрисовка счетчика прыжков
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("Прыжков: " + str(jump_count), True, WHITE)
    screen.blit(text, (0, 0))

    # Если игра окончена, выводим кнопку рестарта
    if game_over:
        font = pygame.font.SysFont("Arial", 48)
        text = font.render("Game Over", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))
        restart_text = font.render("Press R to Restart", True, WHITE)
        screen.blit(restart_text,
                    (SCREEN_WIDTH / 2 - restart_text.get_width() / 2, SCREEN_HEIGHT / 2 + text.get_height()))

        # Обработка нажатия клавиши R для рестарта игры
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Сброс всех значений для рестарта игры
            player_x = 50
            player_y = SCREEN_HEIGHT - 100
            player_vel_x = 1
            player_vel_y = -0.001
            is_jumping = False
            jump_count = 0
            obstacle_x = 500
            obstacle_y = 500
            game_over = False

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()