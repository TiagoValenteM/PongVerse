from .pong import PongVerse
from .config import *


class Interface:
    def __init__(self):
        # initiating pygames
        pygame.init()
        # Opens a new window
        self.screen = pygame.display.set_mode(GameSettings.WINDOW_SIZE)
        # Set the Default Font
        self.default_font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT, GameSettings.FONT_SIZE_DEFAULT)
        # Set the font for the menu options
        self.menu_font = pygame.font.Font(GameSettings.FONT_TYPE_MENU, GameSettings.FONT_SIZE_MENU)

    # Creating a function that creates the GUI
    def mainMenu(self):
        # saving the screen sizes
        width = self.screen.get_width()
        height = self.screen.get_height()
        # creating some text-labels
        game1_text = self.menu_font.render('The PongVerse', True, GameSettings.BLUE)
        game2_text = self.menu_font.render('Vanilla Pong', True, GameSettings.BLUE)
        game3_text = self.menu_font.render('Settings', True, GameSettings.BLUE)
        credits_text = self.menu_font.render('credits', True, GameSettings.BLUE)
        quit_text = self.menu_font.render('quit', True, GameSettings.BLUE)
        title = self.default_font.render('Computation III - Project', True, GameSettings.GOLDEN)
        # interface loop
        while True:
            # getting the input of the user
            for ev in pygame.event.get():
                # press on exit button
                if ev.type == pygame.QUIT:
                    pygame.quit()
                # press on quit button
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[
                        1] <= 5 * height / 6 + 60:
                        pygame.quit()
                # press the credits button
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 4 * height / 6 <= mouse[
                        1] <= 4 * height / 6 + 60:
                        self.credits_()
                # pressing the pong button
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if width / 8 <= mouse[0] <= width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
                        PongVerse(vanilla=False).instructions()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
                        PongVerse(vanilla=True).instructions()

            # setting the background color as black
            self.screen.fill(GameSettings.BLACK)
            # print the buttons text and the box(color changing)
            # game 1 text
            mouse = pygame.mouse.get_pos()
            # when the mouse is on the box it changes color
            if width / 8 <= mouse[0] <= width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
                pygame.draw.rect(self.screen, GameSettings.GREEN, [width / 8, height / 3, 140, 60])
            else:
                pygame.draw.rect(self.screen, GameSettings.WHITE, [width / 8, height / 3, 140, 60])
            self.screen.blit(game1_text, (width / 8, height / 3))
            # SAME FOR ALL THE OTHER BUTTONS
            # game 2 text
            if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
                pygame.draw.rect(self.screen, GameSettings.GREEN, [5 * width / 8, height / 3, 140, 60])
            else:
                pygame.draw.rect(self.screen, GameSettings.WHITE, [5 * width / 8, height / 3, 140, 60])
            self.screen.blit(game2_text, (5 * width / 8, height / 3))
            # game 3 text
            if width / 8 <= mouse[0] <= width / 8 + 140 and 4 * height / 6 <= mouse[1] <= 4 * height / 6 + 60:
                pygame.draw.rect(self.screen, GameSettings.GREEN, [width / 8, 4 * height / 6, 140, 60])
            else:
                pygame.draw.rect(self.screen, GameSettings.WHITE, [width / 8, 4 * height / 6, 140, 60])
            self.screen.blit(game3_text, (width / 8, 4 * height / 6))
            # credits text
            if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 4 * height / 6 <= mouse[1] <= 4 * height / 6 + 60:
                pygame.draw.rect(self.screen, GameSettings.GOLDEN, [5 * width / 8, 4 * height / 6, 140, 60])
            else:
                pygame.draw.rect(self.screen, GameSettings.WHITE, [5 * width / 8, 4 * height / 6, 140, 60])
            self.screen.blit(credits_text, (5 * width / 8, 4 * height / 6))
            # quit text
            if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[1] <= 5 * height / 6 + 60:
                pygame.draw.rect(self.screen, GameSettings.RED, [5 * width / 8, 5 * height / 6, 140, 60])
            else:
                pygame.draw.rect(self.screen, GameSettings.WHITE, [5 * width / 8, 5 * height / 6, 140, 60])
            self.screen.blit(quit_text, (5 * width / 8, 5 * height / 6))
            # TITLE TEXT
            # pygame.draw.rect(screen, color_dark, [52, 0, 612, 100])
            # Gets the rectangle of the powerup name
            title_text = title.get_rect()
            self.screen.blit(title, (
                GameSettings.WINDOW_WIDTH / 2 - title_text.center[0],
                GameSettings.WINDOW_HEIGHT * 0.05))
            # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
            pygame.display.update()

    def credits_(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        back_text = self.menu_font.render('   back', True, GameSettings.BLUE)
        line1_text = self.menu_font.render('Davide Farinati, dfarinati@novaims.unl.pt', True, GameSettings.GOLDEN)
        line2_text = self.menu_font.render('Ilya Bakurov, ibakurov@novaims.unl.pt', True, GameSettings.GOLDEN)
        line3_text = self.menu_font.render('Liah Rosenfeld, lrosenfeld@novaims.unl.pt', True, GameSettings.GOLDEN)

        while True:
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                # press on exit button
                if ev.type == pygame.QUIT:
                    pygame.quit()
                # press on quit button
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[
                        1] <= 5 * height / 6 + 60:
                        self.mainMenu()
            self.screen.fill((0, 0, 0))
            # credits text
            self.screen.blit(line1_text, (0, 0))
            self.screen.blit(line2_text, (0, 25))
            self.screen.blit(line3_text, (0, 50))
            # back text
            if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and 5 * height / 6 <= mouse[1] <= 5 * height / 6 + 60:
                pygame.draw.rect(self.screen, GameSettings.RED, [5 * width / 8, 5 * height / 6, 140, 60])
            else:
                pygame.draw.rect(self.screen, GameSettings.WHITE, [5 * width / 8, 5 * height / 6, 140, 60])
            self.screen.blit(back_text, (5 * width / 8, 5 * height / 6))

            pygame.display.update()

# TODO: Set Interface titles
