#!/usr/bin/python3
import pygame
import pygame_textinput
pygame.init()

# Create TextInput-object
input = pygame_textinput.TextInput()

fg = 250,240,230
bg = 5,5,5
font = pygame.font.Font(None, 80)
text = 'Fonty'
size = font.size(text)
screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    input.update(events)
    # Blit its surface onto the screen
    screen.blit(input.get_surface(), (10, 10))

    a_sys_font = pygame.font.SysFont("BaBa", 60)
    a_sys_font.set_bold(1)
    mytext = input.get_text()
    ren = a_sys_font.render(mytext , 1 , fg, bg)
    screen.blit(ren, (0,60))
    a_sys_font.set_bold


    pygame.display.update()
    clock.tick(30)
