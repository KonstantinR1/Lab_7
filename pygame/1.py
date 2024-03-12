import pygame
import sys
import math
from datetime import datetime

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
CLOCK_RADIUS = min(WIDTH, HEIGHT) // 2 - 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple_Clock")
clock = pygame.time.Clock()

def draw_clock():
    # Draw clock face
    pygame.draw.circle(screen, WHITE, CENTER, CLOCK_RADIUS)
    
    # Draw Mickey's hands
    draw_hand(CENTER, get_seconds_angle(), CLOCK_RADIUS - 20, 2, BLACK)  # Left hand for seconds
    draw_hand(CENTER, get_minutes_angle(), CLOCK_RADIUS - 30, 4, BLACK)  # Right hand for minutes

def draw_hand(center, angle, length, width, color):
    x = center[0] + length * math.cos(math.radians(angle))
    y = center[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, center, (x, y), width)

def get_seconds_angle():
    return 90 - 6 * datetime.now().second

def get_minutes_angle():
    return 90 - 6 * datetime.now().minute

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_clock()

    pygame.display.flip()
    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
sys.exit()