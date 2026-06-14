# first pip install pygame
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
particles = []

running = True
while running:
    screen.fill((0, 0, 0)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        for _ in range(5):
            particles.append([mx, my, random.uniform(-2, 2), random.uniform(-2, 2), 255])

    for p in particles[:]:
        p[0] += p[2]; p[1] += p[3]; p[4] -= 3 # Move and fade
        if p[4] <= 0: particles.remove(p)
        else:
            # glowing circle
            pygame.draw.circle(screen, (p[4], p[4]//2, 255), (int(p[0]), int(p[1])), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
