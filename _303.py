import pygame
import time
import random

pygame.init()

# colours defined
white = (255,255,255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# display width and height in vars 
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snakes! Why did it have to be Snakes!')


clock = pygame.time.Clock()

# set block-size and fps
block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakeList):

    for XnY in snakeList:
        
    # draw black rectangle/dot
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])
        pygame.display.update()



    
# function -> display to screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    
def gameLoop():
    
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 10

    randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    
    # main game loop
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over. Press C to play again or Q to quit.", blue)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                #left and right movement
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                #up and down movement  
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # if you go off screen, use game logic to end game            
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            
        #logic loop
        lead_x += lead_x_change
        lead_y += lead_y_change

        
        #background draw
        # where you want to draw, colour, -> list: coordinates, width and height
        gameDisplay.fill(white)

        # draw apple
        pygame.draw.rect(gameDisplay, green, [randAppleX, randAppleY, block_size, block_size])

        # snake append to itself -> references SnakeList
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        # run snake function
        snake(block_size, snakeList)
        pygame.display.update()
        
        # if you catch apple, replace it with new one (randomly placed)
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

        clock.tick(FPS)
        
    
    pygame.quit()
    quit()

gameLoop()
