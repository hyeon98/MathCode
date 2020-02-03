# Import a library of functions called 'pygame'
import pygame
from random import *
import time

SelectDisplay = False

def update(array):
    RbRW = 1
    screen.fill(WHITE)
    for i in range(0,maxNum):
        point1 = (i * RbRW, screenHeight)
        point2 = (i * RbRW, screenHeight - array[i])
        pygame.draw.line(screen, BLACK, point1, point2) 

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

            if SelectDisplay:
                update(arr)
                    
    return arr

def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]

            if SelectDisplay:
                update(array)    

    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return

    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)
    return array

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)

def test_sort(array):
    count1 = 0
    verifyCount = 0
    done = False
    while not done:
        if array[count1] > array[count1 + 1]:
            temp = array[count1]
            array[count1] = array[count1 + 1]
            array[count1 + 1] = temp

            if SelectDisplay:
                update(num)

            verifyCount = 0
        else:
            verifyCount += 1
            
        count1 += 1
        if count1 > len(num) - 2:
            count1 = 0

        if verifyCount > len(num) - 3:
            done = True

    return array


def random_sort(array):
    temp = 0
    count1 = 0
    checkCount = 0
    done = False
    
    while not done:
        tempIndex = randint(count1, len(array) - 1)
        if array[count1] > array[tempIndex]:
            temp = array[count1]
            array[count1] = array[tempIndex]
            array[tempIndex] = temp

            if SelectDisplay:
                update(array)

            checkCount = 0
        else:
            checkCount += 1
            if checkCount > len(array) * 2 - 1:
                done = True

        count1 += 1
        if count1 > len(array) - 1:
            count1 = 0

    return array


# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
 
# Set the height and width of the screen
screenWidth = 1600
screenHeight = 400
size   = [screenWidth, screenHeight]
screen = pygame.display.set_mode(size)
  
pygame.display.set_caption("Game Title")
  
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

maxNum = 1600

num = []
for i in range(0,maxNum):
    num.append(randint(0,300))

start = time.time()  # 시작 시간 저장

SelectDisplay = True

num = random_sort(num)
num = test_sort(num)

# num = quick_sort(num)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

pygame.quit()
  
# Be IDLE friendly
