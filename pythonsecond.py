import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snakes! Why did it have to be Snakes!')

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
    


pygame.quit()
quit()
