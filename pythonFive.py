import pygame
pygame.init()

white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snakes! Why did it have to be Snakes!')


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    # where you want to draw, colour, -> list: coordinates, width and height
    pygame.draw.rect(gameDisplay, black, [400, 300, 10, 100])
    pygame.draw.rect(gameDisplay, red, [400, 300, 10, 10])
    pygame.display.update()


pygame.quit()
quit()
