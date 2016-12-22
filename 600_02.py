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

# img defined -> set path
img = pygame.image.load('snakehead.png')

clock = pygame.time.Clock()

# set block-size and fps
block_size = 20
FPS = 15

# set direction -> movement -> set up head-rotation
direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def game_intro():
    
    intro = True

# intro screen logic -> c or quit

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro =  False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Snakes! Why did it have to be Snakes!",
                          green,
                          -100,
                          "small")
        
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)
        message_to_screen("The more apples you eat, the longer you get.",
                          black,
                          10)
        
        message_to_screen("If you run into yourself or the edges, you die.",
                          black,
                          50)
        message_to_screen("Press C to play or Q to quit",
                          red,
                          180)
        
        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:    
    # draw black rectangle/dot
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])
        pygame.display.update()

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()
    
# function -> display to screen, text (displacement from centre)
def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    
    # crappy text
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])

    textRect.center = (display_width/ 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)
    
def gameLoop():

    global direction
    
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    # make snake and apple line up in size
    randAppleX = round(random.randrange(0, display_width - block_size)) # / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size)) # / 10.0) * 10.0

    
    # main game loop
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              y_displace= -50,
                              size = "large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size = "medium")
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    
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
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                #up and down movement  
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
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
        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        # snake append to itself -> references SnakeList
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # tail for snake
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # if you run into yourself, game over!!
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        # run snake function
        snake(block_size, snakeList)
        
        pygame.display.update()
        
##        # make apple accessible not just top left for eating apple
##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##        
##                    randAppleX = round(random.randrange(0, display_width - block_size)) # / 10.0) * 10.0
##                    randAppleY = round(random.randrange(0, display_height - block_size)) # / 10.0) * 10.0
##                    snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                
                randAppleX = round(random.randrange(0, display_width - block_size)) # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size)) # / 10.0) * 10.0
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                
                randAppleX = round(random.randrange(0, display_width - block_size)) # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size)) # / 10.0) * 10.0
                snakeLength += 1

        
            
        clock.tick(FPS)
        
    
    pygame.quit()
    quit()
    
game_intro()
gameLoop()
