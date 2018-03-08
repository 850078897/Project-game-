import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('NEWBEE')
clock = pygame.time.Clock()

carImg = pygame.image.load('space.jpg')


pygame.quit()
quit()