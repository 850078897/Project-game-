import pygame
import pygame_textinput
import test_game
from pygame.locals import *

from pygame.compat import unichr_, unicode_

import sys

import locale


from itertools import chain


def truncline(text, font, maxwidth):
    real = len(text)
    stext = text
    l = font.size(text)[0]
    cut = 0
    a = 0
    done = 1
    old = None
    while l > maxwidth:
        a = a + 1
        n = text.rsplit(None, a)[0]
        if stext == n:
            cut += 1
            stext = n[:-cut]
        else:
            stext = n
        l = font.size(stext)[0]
        real = len(stext)
        done = 0
    return real, done, stext


def wrapline(text, font, maxwidth):
    done = 0
    wrapped = []

    while not done:
        nl, done, stext = truncline(text, font, maxwidth)
        wrapped.append(stext.strip())
        text = text[nl:]
    return wrapped


def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

pygame.init()

display_width = 800
display_height = 533


clock = pygame.time.Clock()
crashed= False
intro_page= pygame.image.load('space.jpg')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('lubenwei')

textinput = pygame_textinput.TextInput()

fg = 250,240,230
bg = 5,5,5
font = pygame.font.Font(None, 80)
text = 'Fonty'
size = font.size(text)


black = (0,0,0)
white = (255,255,255)

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

while not crashed:
    events = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

            x += x_change

    gameDisplay.fill(white)

    gameDisplay.blit(intro_page, (0, 0))

    # load font, prepare values

    font = pygame.font.Font(None, 80)

    text = test_game.newbee

    textlist = wrapline(text,font,20)

    size = font.size(text)

    # no AA, no transparancy, normal

    ren = font.render(text, 0, fg, bg)

    gameDisplay.blit(ren, (10, 10))

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    gameDisplay.blit(textinput.get_surface(), (10, 10))

    a_sys_font = pygame.font.SysFont("BaBa", 60)
    a_sys_font.set_bold(1)
    mytext = textinput.get_text()
    ren = a_sys_font.render(mytext , 1 , fg, bg)
    gameDisplay.blit(ren, (0,60))
    a_sys_font.set_bold

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

