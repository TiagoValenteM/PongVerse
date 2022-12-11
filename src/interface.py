from .pong import PongVerse
from .config import *


class Interface:
    def __init__(self):
        # initiating pygames
        pygame.init()
        # Set the Game icon
        pygame.display.set_icon(InterfaceSettings.ICON)
        # Opens a new window
        self.screen = pygame.display.set_mode(InterfaceSettings.WINDOW_SIZE)
        # Set width of the screen
        self.width = self.screen.get_width()
        # Set height of the screen
        self.height = self.screen.get_height()
        # Set the Default Font
        self.default_font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT, GameSettings.FONT_SIZE_DEFAULT)
        # Set the font for the menu options
        self.menu_font = pygame.font.Font(GameSettings.FONT_TYPE_MENU, GameSettings.FONT_SIZE_MENU)

    # Creating a function that creates the GUI
    def mainMenu(self):
        # Set the title of the window
        pygame.display.set_caption(InterfaceSettings.MENU_TITLE)

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
            # get the mouse position
            mouse = pygame.mouse.get_pos()
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
                        self.credits()
                # pressing the pong button
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if width / 8 <= mouse[0] <= width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
                        PongVerse(vanilla=False).instructions()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 5 * width / 8 <= mouse[0] <= 5 * width / 8 + 140 and height / 3 <= mouse[1] <= height / 3 + 60:
                        PongVerse(vanilla=True).instructions()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if width / 8 <= mouse[0] <= width / 8 + 140 and 4 * height / 6 <= mouse[1] <= 4 * height / 6 + 60:
                        self.settings()

            # setting the background color as black
            self.screen.fill(GameSettings.BLACK)
            # print the buttons text and the box(color changing)
            # game 1 text
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
                InterfaceSettings.WINDOW_WIDTH / 2 - title_text.center[0],
                InterfaceSettings.WINDOW_HEIGHT * 0.05))
            # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
            pygame.display.update()

    def credits(self):
        # Set the title of the window
        pygame.display.set_caption(InterfaceSettings.CREDITS_TITLE)

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

    def settings(self):
        # Set the title of the window
        pygame.display.set_caption(InterfaceSettings.SETTINGS_TITLE)
        oi = False
        back_text = self.menu_font.render('  back', True, GameSettings.BLUE)

        while True:
            # Get the mouse position
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # press on exit button
                if event.type == pygame.QUIT:
                    pygame.quit()
                # press on quit button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 5 * self.width / 8 <= mouse[0] <= 5 * self.width / 8 + 140 and 5 * self.height / 6 <= mouse[
                        1] <= 5 * self.height / 6 + 60:
                        self.mainMenu()

            self.screen.fill((0, 0, 0))

            # Set height position for Resolutions
            resolutions_pos_y = self.height * 0.2
            if not oi:
                for resolution_name, resolution in Screen_Resolution.items():
                    print(resolution[0],resolution[1])
                    resolutions_pos_y += self.height * 0.07
                    screen_resolution = self.menu_font.render(resolution_name, True, GameSettings.WHITE)
                    screen_resolution_rect = screen_resolution.get_rect()
                    resolution_final = self.screen.blit(screen_resolution, (
                        self.width / 2 - screen_resolution_rect.center[0], resolutions_pos_y))
                    oi = True

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if resolution_final.collidepoint(mouse):
                                self.width, InterfaceSettings.WINDOW_WIDTH = resolution[0], resolution[0]
                                self.height, InterfaceSettings.WINDOW_HEIGHT = resolution[1], resolution[1]
                                self.screen = pygame.display.set_mode((self.width, self.height))

            # back text
            if 5 * self.width / 8 <= mouse[0] <= 5 * self.width / 8 + 140 and 5 * self.height / 6 <= mouse[
                1] <= 5 * self.height / 6 + 60:
                pygame.draw.rect(self.screen, GameSettings.RED, [5 * self.width / 8, 5 * self.height / 6, 140, 60])
            else:
                pygame.draw.rect(self.screen, GameSettings.WHITE, [5 * self.width / 8, 5 * self.height / 6, 140, 60])
            self.screen.blit(back_text, (5 * self.width / 8, 5 * self.height / 6))

            pygame.display.update()
