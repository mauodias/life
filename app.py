import pygame
from cell import Cell

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

cell = Cell(250, 250)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pygame.draw.circle(screen, cell.color, cell.position, cell.size)

    pygame.display.flip()

    cell.walk(30)

pygame.quit()
