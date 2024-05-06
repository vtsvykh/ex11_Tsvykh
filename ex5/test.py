import random
import pygame
import brown_motion

pygame.init()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

num_molecules = 50
molecules = [brown_motion.Molecule(
    x=random.randint(0, window_width),
    y=random.randint(0, window_height),
    radius=random.randint(1, 20),
    color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
) for molecule in range(num_molecules)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for molecule in molecules:
        molecule.move(800, 600)

    window.fill((255, 255, 255))
    for molecule in molecules:
        pygame.draw.circle(window, molecule.color, (molecule.x, molecule.y), molecule.radius)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
