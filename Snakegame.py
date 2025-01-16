import pygame
import time
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)


block_size = 20
snake_speed = 15


clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def show_score(score):
    value = score_font.render(f"Your Score: {score}", True, GREEN)
    screen.blit(value, [0, 0])


def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], block_size, block_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    game_over = False
    game_close = False

   
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

   
    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size

    while not game_over:
        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q to Quit or C to Play Again", RED)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -block_size, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = block_size, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -block_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, block_size

       
        x += dx
        y += dy

        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, block_size, block_size])

        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        show_score(length_of_snake - 1)
        pygame.display.update()

       
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
