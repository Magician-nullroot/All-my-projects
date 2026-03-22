import pygame
import sys
import random

pygame.init()
w, h = 400, 600
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

bird_x = 80
bird_y = 250
bird_vel = 0
gravity = 0.5
jump = -8

pipe_gap = 150
pipe_width = 70
pipes = []
spawn_timer = 0
score = 0

def spawn_pipe():
    top = random.randint(50, h - pipe_gap - 50)
    pipes.append([w, top])

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                bird_vel = jump

    screen.fill((135, 206, 235))

    bird_vel += gravity
    bird_y += bird_vel
    pygame.draw.rect(screen, (255, 255, 0), (bird_x, bird_y, 30, 30))

    spawn_timer += 1
    if spawn_timer > 90:
        spawn_pipe()
        spawn_timer = 0

    new_pipes = []
    for px, top in pipes:
        px -= 3

        pygame.draw.rect(screen, (34, 139, 34), (px, 0, pipe_width, top))
        bottom_y = top + pipe_gap
        pygame.draw.rect(screen, (34, 139, 34), (px, bottom_y, pipe_width, h - bottom_y))

        if px + pipe_width < bird_x and (px + pipe_width) >= (bird_x - 3):
            score += 1

        if px + pipe_width > 0:
            new_pipes.append([px, top])

        if bird_x < px + pipe_width and bird_x + 30 > px:
            if bird_y < top or bird_y + 30 > top + pipe_gap:
                pygame.quit()
                sys.exit()

    pipes = new_pipes

    if bird_y < 0 or bird_y + 30 > h:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)
