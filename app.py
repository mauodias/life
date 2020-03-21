import pygame
from cell import Cell

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

cell = Cell(screen, x=250, y=250)
cell2 = Cell(screen, x=250, y=250, speed=-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    cell.tick()
    cell2.tick()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
