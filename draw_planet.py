# Солнечная система
# Отображает солнечную систему и позволяет перемещаться между планетами

import pygame
import math

# Инициализация Pygame
pygame.init()

# Окно
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Солнечная система")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Солнце
SUN_RADIUS = 50
sun_x = WINDOW_SIZE[0] // 2
sun_y = WINDOW_SIZE[1] // 2

# Планеты
PLANETS = [
    {"name": "Меркурий", "color": WHITE, "radius": 10, "distance": 80, "speed": 3, "angle": 0},
    {"name": "Венера", "color": YELLOW, "radius": 20, "distance": 120, "speed": 2, "angle": 0},
    {"name": "Земля", "color": BLUE, "radius": 25, "distance": 160, "speed": 1, "angle": 0},
    {"name": "Марс", "color": RED, "radius": 15, "distance": 200, "speed": 0.5, "angle": 0}
]

# Функция для отображения планеты
def draw_planet(planet):
    angle_rad = math.radians(planet["angle"])
    x = sun_x + planet["distance"] * math
