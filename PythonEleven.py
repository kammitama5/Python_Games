import pygame
pygame.init()

white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snakes! Why did it have to be Snakes!')


gameExit = False

lead_x = 300
lead_y = 300

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

# main game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            #left and right movement
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                
            #up and down movement  
            elif event.key == pygame.K_UP:
                lead_y_change = -10
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                
        
    #logic loop
    lead_x += lead_x_change
    lead_y += lead_y_change
    
    #background draw
    # where you want to draw, colour, -> list: coordinates, width and height
    gameDisplay.fill(white)
    
    # draw black rectangle/dot
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(15)


pygame.quit()
quit()

