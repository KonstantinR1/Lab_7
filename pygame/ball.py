import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 25
BALL_DIAMETER = BALL_RADIUS * 2
BALL_COLOR = (255, 0, 0)  # Red color

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

# Initial position of the ball
ball_x = (WIDTH - BALL_DIAMETER) // 2
ball_y = (HEIGHT - BALL_DIAMETER) // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y > 0:
        ball_y -= 20
    if keys[pygame.K_DOWN] and ball_y < HEIGHT - BALL_DIAMETER:
        ball_y += 20
    if keys[pygame.K_LEFT] and ball_x > 0:
        ball_x -= 20
    if keys[pygame.K_RIGHT] and ball_x < WIDTH - BALL_DIAMETER:
        ball_x += 20

    screen.fill((255, 255, 255))  # White background

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)