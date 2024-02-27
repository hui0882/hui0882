import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 设定屏幕尺寸
WIDTH, HEIGHT = 640, 480

# 设置游戏参数
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# 创建屏幕和时钟
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇测试")
clock = pygame.time.Clock()

# 定义蛇和食物
snake = [(5, 5), (4, 5), (3, 5)]
food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1), random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))
direction = (1, 0)


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * BLOCK_SIZE, food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

                # 移动蛇
    head = snake[0]
    new_head = ((head[0] + direction[0]) % (WIDTH // BLOCK_SIZE), (head[1] + direction[1]) % (HEIGHT // BLOCK_SIZE))
    snake.insert(0, new_head)

    # 检查是否吃到食物
    if new_head == food:
        food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1), random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))
    else:
        snake.pop()

        # 检查是否撞到自己
    if len(snake) > 2:
        for segment in snake[1:]:
            if new_head == segment:
                running = False

                # 清屏
    screen.fill(WHITE)

    # 绘制蛇和食物
    draw_snake(snake)
    draw_food(food)

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(SNAKE_SPEED)

pygame.quit()