import pygame
import sys
from .pong import PongVerse


# Creating a function that creates the GUI
def interface():
    # initiating pygames
    pygame.init()
    # creating the screen 720x720 pixels
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    # creating some colors (RGB scale)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some text-labels
    corbelfont = pygame.font.SysFont('Corbel', 50)
    game1_text = corbelfont.render('pong', True, blue)
    game2_text = corbelfont.render('game2', True, blue)
    game3_text = corbelfont.render('game3', True, blue)
    credits_text = corbelfont.render('credits', True, blue)
    quit_text = corbelfont.render('   quit', True, blue)
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 50)
    title_text = comicsansfont.render('Computation III - Project', True, yellow)
    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[1] <= 5 * height / 6 + 60:
                    pygame.quit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 4 * height / 6 <= mouse[1] <= 4 * height / 6 + 60:
                    credits_()
            # pressing the pong button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 8 <= mouse[0] <= width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
                    PongVerse().play()
        # setting the background color as black
        screen.fill(black)
        # print the buttons text and the box(color changing)
        # game 1 text
        mouse = pygame.mouse.get_pos()
        # when the mouse is on the box it changes color
        if width / 8 <= mouse[0] <= width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
            pygame.draw.rect(screen, green, [width / 8, height / 3, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [width / 8, height / 3, 140, 60])
        screen.blit(game1_text, (width / 8, height / 3))
        # SAME FOR ALL THE OTHER BUTTONS
        # game 2 text
        if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
            pygame.draw.rect(screen, green, [5 * width / 8, height / 3, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [5 * width / 8, height / 3, 140, 60])
        screen.blit(game2_text, (5 * width / 8, height / 3))
        # game 3 text
        if width / 8 <= mouse[0] <= width / 8 + 140 and 4 * height / 6 <= mouse[1] <= 4 * height / 6 + 60:
            pygame.draw.rect(screen, green, [width / 8, 4 * height / 6, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [width / 8, 4 * height / 6, 140, 60])
        screen.blit(game3_text, (width / 8, 4 * height / 6))
        # credits text
        if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 4 * height / 6 <= mouse[1] <= 4 * height / 6 + 60:
            pygame.draw.rect(screen, yellow, [5 * width / 8, 4 * height / 6, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [5 * width / 8, 4 * height / 6, 140, 60])
        screen.blit(credits_text, (5 * width / 8, 4 * height / 6))
        # quit text
        if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[1] <= 5 * height / 6 + 60:
            pygame.draw.rect(screen, red, [5 * width / 8, 5 * height / 6, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [5 * width / 8, 5 * height / 6, 140, 60])
        screen.blit(quit_text, (5 * width / 8, 5 * height / 6))
        # TITLE TEXT
        # pygame.draw.rect(screen, color_dark, [52, 0, 612, 100])
        screen.blit(title_text, (55, 0))
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()


def credits_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    corbelfont = pygame.font.SysFont('Corbel', 50)
    back_text = corbelfont.render('   back', True, blue)
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    line1_text = comicsansfont.render('Davide Farinati, dfarinati@novaims.unl.pt', True, yellow)
    line2_text = comicsansfont.render('Ilya Bakurov, ibakurov@novaims.unl.pt', True, yellow)
    line3_text = comicsansfont.render('Liah Rosenfeld, lrosenfeld@novaims.unl.pt', True, yellow)

    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[1] <= 5 * height / 6 + 60:
                    interface()
        screen.fill((0, 0, 0))
        # credits text
        screen.blit(line1_text, (0, 0))
        screen.blit(line2_text, (0, 25))
        screen.blit(line3_text, (0, 50))
        # back text
        if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[1] <= 5 * height / 6 + 60:
            pygame.draw.rect(screen, red, [5 * width / 8, 5 * height / 6, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [5 * width / 8, 5 * height / 6, 140, 60])
        screen.blit(back_text, (5 * width / 8, 5 * height / 6))

        pygame.display.update()
