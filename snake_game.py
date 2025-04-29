import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
            random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
speed = 15

# Clock
clock = pygame.time.Clock()

def game_over():
    """Display game over and quit."""
    font = pygame.font.SysFont('times new roman', 35)
    msg = font.render('Game Over!', True, RED)
    screen.blit(msg, (WIDTH // 4, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.sleep(2)
    pygame.quit()
    quit()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not direction == 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and not direction == 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and not direction == 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and not direction == 'LEFT':
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update snake's direction
    direction = change_to

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                    random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    # Check collisions
    if (snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10 or
            snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10):
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Draw elements
    screen.fill(WHITE)
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.update()
    clock.tick(speed)
