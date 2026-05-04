import pygame
import random
import time

# 初始化游戏
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇 - 按方向键开始")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 游戏参数
snake_size = 15
snake_speed = 15

clock = pygame.time.Clock()


def game_loop():
    game_over = False
    game_close = False

    # 初始位置
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    dx = 0
    dy = 0

    snake_body = []
    snake_length = 1

    # 生成食物
    food_x = round(random.randrange(0, WIDTH - snake_size) / snake_size) * snake_size
    food_y = round(random.randrange(0, HEIGHT - snake_size) / snake_size) * snake_size

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            font = pygame.font.SysFont('arial', 30)
            text = font.render("游戏结束！按 Q-退出 或 C-重玩", True, RED)
            screen.blit(text, (WIDTH / 2 - 200, HEIGHT / 2))
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
                if event.key == pygame.K_LEFT and dx != snake_size:
                    dx = -snake_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -snake_size:
                    dx = snake_size
                    dy = 0
                elif event.key == pygame.K_UP and dy != snake_size:
                    dy = -snake_size
                    dx = 0
                elif event.key == pygame.K_DOWN and dy != -snake_size:
                    dy = snake_size
                    dx = 0

        # 边界检测
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += dx
        y1 += dy
        screen.fill(BLACK)

        # 绘制食物
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

        # 更新蛇身
        snake_head = [x1, y1]
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        # 自碰检测
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        # 绘制蛇身
        for segment in snake_body:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_size, snake_size])

        pygame.display.update()

        # 吃到食物
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / snake_size) * snake_size
            food_y = round(random.randrange(0, HEIGHT - snake_size) / snake_size) * snake_size
            snake_length += 1
            snake_speed += 0.5

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()