import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Три кубика с привязкой")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Параметры кубиков
CUBE_SIZE = 40
DISTANCE = 60  # фиксированное расстояние между центрами кубиков

# Начальные позиции трёх кубиков (центры)
positions = [
    [WIDTH // 2, HEIGHT // 2],          # первый (ведущий)
    [WIDTH // 2 - DISTANCE, HEIGHT // 2], # второй
    [WIDTH // 2 - 2 * DISTANCE, HEIGHT // 2] # третий
]

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Первый кубик движется за мышью (без нажатия)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Ограничиваем, чтобы центр кубика не выходил за границы экрана
    positions[0][0] = max(CUBE_SIZE // 2, min(WIDTH - CUBE_SIZE // 2, mouse_x))
    positions[0][1] = max(CUBE_SIZE // 2, min(HEIGHT - CUBE_SIZE // 2, mouse_y))

    # Обновление позиций второго и третьего кубиков (подтягивание)
    for i in range(1, 3):
        # Вектор от текущего кубика к предыдущему
        dx = positions[i-1][0] - positions[i][0]
        dy = positions[i-1][1] - positions[i][1]
        dist = (dx**2 + dy**2) ** 0.5

        if dist > DISTANCE and dist != 0:
            # Нормализуем вектор и перемещаем текущий кубик на DISTANCE ближе к предыдущему
            ratio = DISTANCE / dist
            positions[i][0] = positions[i-1][0] - dx * ratio
            positions[i][1] = positions[i-1][1] - dy * ratio

    # Отрисовка
    screen.fill(WHITE)

    # Рисуем линии между кубиками
    pygame.draw.line(screen, BLACK, positions[0], positions[1], 2)
    pygame.draw.line(screen, BLACK, positions[1], positions[2], 2)

    # Рисуем кубики (прямоугольники от верхнего левого угла)
    for idx, pos in enumerate(positions):
        rect = pygame.Rect(pos[0] - CUBE_SIZE//2, pos[1] - CUBE_SIZE//2, CUBE_SIZE, CUBE_SIZE)
        if idx == 0:
            pygame.draw.rect(screen, RED, rect)
        elif idx == 1:
            pygame.draw.rect(screen, GREEN, rect)
        else:
            pygame.draw.rect(screen, BLUE, rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
