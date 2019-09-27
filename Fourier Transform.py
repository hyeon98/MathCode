# Import a library of functions called 'pygame'
import pygame
from random import *
import time
import math

def FT(x):
    result = 20*math.sin(x*0.1)
    return result

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
GARY  = (200, 200, 200)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

pygame.init()

screenWidth = 500
screenHeight = 500
size   = [screenWidth, screenHeight]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Title")

screen.fill(WHITE)

cut = 50
myfont = pygame.font.SysFont('Comic Sans MS', (int)(cut / 5)
centor = (screenWidth / 2) - 1
abc = 1
for tempN in range(0, screenWidth):
    if tempN % cut == cut - 1:
        pygame.draw.line(screen, GARY, [tempN , 0], [tempN, screenHeight], 1)
        pygame.draw.line(screen, GARY, [0 , tempN], [screenWidth, tempN], 1)
        
        textsurface = myfont.render(str((tempN - screenWidth / 2 + 1) / cut), True, (0, 0, 0))
        screen.blit(textsurface, (tempN + 3, screenHeight / 2))

pygame.draw.line(screen, BLACK, [0, centor], [screenWidth, centor], 2)
pygame.draw.line(screen, BLACK, [centor, 0], [centor, screenHeight], 2)

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('JHS', True, (0, 0, 0))
screen.blit(textsurface, (10, 0))

count = 0.01
for i in range(1, 1000):
    tempX = count
    tempY = math.log(tempX)
    # print(tempX, ", ", tempY)

    drawX = (tempX * cut) + centor
    drawY = screenHeight - ((tempY * cut) + centor)
    # print(drawX, ", ", drawY)

    pygame.draw.rect(screen, RED, [drawX, drawY, 1, 1])

    count += 0.01

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
start = time.time()  # 시작 시간 저장

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    pygame.display.flip()

pygame.quit()


# # Initialize the game engine
# pygame.init()
 
# # Define the colors we will use in RGB format
# BLACK = (  0,   0,   0)
# WHITE = (255, 255, 255)
# BLUE  = (  0,   0, 255)
# GREEN = (  0, 255,   0)
# RED   = (255,   0,   0)
 
# # Set the height and width of the screen
# screenWidth = 400
# screenHeight = 400
# size   = [screenWidth, screenHeight]
# screen = pygame.display.set_mode(size)
  
# pygame.display.set_caption("Title")

# screen.fill(WHITE)
# pygame.draw.line(screen, BLACK, [0, screenHeight / 2], [screenWidth, screenHeight / 2], 2)
# pygame.draw.line(screen, BLACK, [screenWidth / 2, 0], [screenWidth / 2, screenHeight], 2)
  
# #Loop until the user clicks the close button.
# done = False
# clock = pygame.time.Clock()
# start = time.time()  # 시작 시간 저장
# count = 0.1

# while not done:
#     for event in pygame.event.get(): # User did something
#         if event.type == pygame.QUIT: # If user clicked close
#             done=True # Flag that we are done so we exit this loop
    
#     # clock.tick(25)
    
#     tempX = count/1
#     tempY = math.log(tempX) * screenHeight / 2
#     # print(count, ":", tempY)
#     result = tempY + screenHeight/2
#     # result = FT(i) + screenHeight/2
#     pygame.draw.rect(screen, RED, [count + screenWidth / 2, result, 1, 1])
#     pygame.display.flip()

#     if (tempX % 2) == 0:
#         pygame.draw.line(screen, BLACK, [screenWidth + tempX / 2, 0], [screenWidth + tempX / 2, screenHeight], 1)

#     if count >= screenWidth / 2:
#         count = 1
#         screen.fill(WHITE)
#         pygame.draw.line(screen, BLACK, [0, screenHeight / 2], [screenWidth, screenHeight / 2], 2)
#         pygame.draw.line(screen, BLACK, [screenWidth / 2, 0], [screenWidth / 2, screenHeight], 2)

#         clock.tick(0.5)
#     else:
#         count += 1

# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

# pygame.quit()
  
# Be IDLE friendly
