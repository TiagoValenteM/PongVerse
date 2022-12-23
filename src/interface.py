from .pong import PongVerse
from .config import *
import sys


class Interface:
    def __init__(self):
        # initiating pygames
        pygame.init()
        # Opens a new window
        self.screen = pygame.display.set_mode(InterfaceSettings.WINDOW_SIZE)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        # Set the Game icon
        icon: pygame.image = pygame.image.load("img/icons/main_icon.png").convert_alpha()
        pygame.display.set_icon(icon)
        # Set background Image
        background_img_load: any = pygame.image.load("img/background/background_interface.jpg").convert()
        self.background_img: any = pygame.transform.scale(background_img_load, (InterfaceSettings.WINDOW_WIDTH,
                                                                                InterfaceSettings.WINDOW_HEIGHT))
        # Set Instructions Fonts
        title_font: pygame.font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT, InstructionsSettings.TITLE_SIZE)
        subtitle_font: pygame.font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT,
                                                      InstructionsSettings.SUBTITLE_SIZE)
        body_font: pygame.font = pygame.font.Font(GameSettings.FONT_TYPE_MENU, InstructionsSettings.BODY_SIZE)
        # Set the Default Font
        self.default_font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT, GameSettings.FONT_SIZE_DEFAULT)
        # Set the font for the menu options
        self.menu_font = pygame.font.Font(GameSettings.FONT_TYPE_MENU, GameSettings.FONT_SIZE_MENU)

    def drawRect(self, color, width, height):
        # Draw the rectangle with position and size
        return pygame.draw.rect(self.screen, color,
                                [width, height, InterfaceSettings.BUTTON_WIDTH, InterfaceSettings.BUTTON_HEIGHT],
                                border_radius=15)

    # Creating a function that creates the GUI
    def mainMenu(self):
        # Create a loop that carries on until the user exits the main menu
        mainMenuOn: int = 1

        # Creating Screen positions and Sizes
        button_width_center: int = int(InterfaceSettings.WINDOW_WIDTH * 0.5 - InterfaceSettings.BUTTON_WIDTH * 0.5)
        button_height_pos: int = int(InterfaceSettings.WINDOW_HEIGHT * 0.3)

        # Create text-labels and get their rectangle
        # PongVerse
        text_play_pongVerse = self.menu_font.render('The PongVerse', True, GameSettings.BLUE)
        play_pongVerse_rect = self.drawRect(GameSettings.WHITE, button_width_center, button_height_pos)
        # PongVerse Vanilla Edition
        text_play_pongVerse_vanilla = self.menu_font.render('Vanilla Pong', True, GameSettings.BLUE)
        play_pongVerse_vanilla_rect = self.drawRect(GameSettings.WHITE, button_width_center,
                                                    button_height_pos + InterfaceSettings.BUTTON_GAP)
        # Settings
        text_settings = self.menu_font.render('Settings', True, GameSettings.BLUE)
        settings_rect = self.drawRect(GameSettings.WHITE, button_width_center,
                                      button_height_pos + InterfaceSettings.BUTTON_GAP * 2)
        # Creators
        text_creators = self.menu_font.render('Creators', True, GameSettings.BLUE)
        creators_rect = self.drawRect(GameSettings.WHITE, button_width_center,
                                      button_height_pos + InterfaceSettings.BUTTON_GAP * 3)
        # Quit
        text_quit = self.menu_font.render('Quit', True, GameSettings.BLUE)
        quit_rect = self.drawRect(GameSettings.WHITE, button_width_center,
                                  button_height_pos + InterfaceSettings.BUTTON_GAP * 4)
        # Title
        text_title = self.default_font.render('The PongVerse - OOP PyGame', True, GameSettings.LIGHT_BLUE)
        title_rect = text_title.get_rect()

        # interface loop
        while mainMenuOn:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Get an input from the user
            for event in pygame.event.get():
                # Press the exit button
                if event.type == pygame.QUIT:
                    pygame.quit(), sys.exit()
                # Press the mouse button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Mouse click on quit button
                    if quit_rect.collidepoint(mouse_pos):
                        pygame.quit(), sys.exit()
                    # Mouse click on Creators button
                    if creators_rect.collidepoint(mouse_pos):
                        self.creators()
                    # Mouse click on Pong button
                    if play_pongVerse_rect.collidepoint(mouse_pos):
                        PongVerse(vanilla=False).instructions()
                    # Mouse click on Vanilla Pong button
                    if play_pongVerse_vanilla_rect.collidepoint(mouse_pos):
                        PongVerse(vanilla=True).instructions()
                    # Mouse click on Settings button
                    if settings_rect.collidepoint(mouse_pos):
                        self.settings()

            # Set the title of the window
            pygame.display.set_caption(InterfaceSettings.MENU_TITLE)
            # background image
            self.screen.blit(self.background_img, (0, 0))

            # On Hover, button changes color
            # Play PongVerse Button
            if play_pongVerse_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.GREEN, button_width_center, button_height_pos)
            else:
                self.drawRect(GameSettings.WHITE, button_width_center, button_height_pos)
            self.screen.blit(text_play_pongVerse, (button_width_center, button_height_pos))
            # Play PongVerse Vanilla Edition Button
            if play_pongVerse_vanilla_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.GREEN, button_width_center, button_height_pos + InterfaceSettings.BUTTON_GAP)
            else:
                self.drawRect(GameSettings.WHITE, button_width_center, button_height_pos + InterfaceSettings.BUTTON_GAP)
            self.screen.blit(text_play_pongVerse_vanilla,
                             (button_width_center, button_height_pos + InterfaceSettings.BUTTON_GAP))
            # Enter Settings Button
            if settings_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.GREEN, button_width_center,
                              button_height_pos + InterfaceSettings.BUTTON_GAP * 2)
            else:
                self.drawRect(GameSettings.WHITE, button_width_center,
                              button_height_pos + InterfaceSettings.BUTTON_GAP * 2)
            self.screen.blit(text_settings,
                             (button_width_center, button_height_pos + InterfaceSettings.BUTTON_GAP * 2))
            # Enter Creators Button
            if creators_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.GREEN, button_width_center,
                              button_height_pos + InterfaceSettings.BUTTON_GAP * 3)
            else:
                self.drawRect(GameSettings.WHITE, button_width_center,
                              button_height_pos + InterfaceSettings.BUTTON_GAP * 3)
            self.screen.blit(text_creators,
                             (button_width_center, button_height_pos + InterfaceSettings.BUTTON_GAP * 3))
            # Quit Button
            if quit_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.GREEN, button_width_center,
                              button_height_pos + InterfaceSettings.BUTTON_GAP * 4)
            else:
                self.drawRect(GameSettings.WHITE, button_width_center,
                              button_height_pos + InterfaceSettings.BUTTON_GAP * 4)
            self.screen.blit(text_quit,
                             (button_width_center, button_height_pos + InterfaceSettings.BUTTON_GAP * 4))

            # TITLE TEXT
            # pygame.draw.rect(screen, color_dark, [52, 0, 612, 100])
            # Gets the rectangle of the powerup name
            self.screen.blit(text_title, (
                InterfaceSettings.WINDOW_WIDTH / 2 - title_rect.center[0],
                InterfaceSettings.WINDOW_HEIGHT * 0.05))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)

    def creators(self):

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

            # Set the title of the window
            pygame.display.set_caption(InterfaceSettings.CREDITS_TITLE)

            # background image
            self.screen.blit(self.background_img, (0, 0))
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

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 60 frames per second
            self.clock.tick(30)

    def settings(self):
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

            # background image
            self.screen.blit(self.background_img, (0, 0))

            # Set the title of the window
            pygame.display.set_caption(InterfaceSettings.SETTINGS_TITLE)

            # Set height position for Resolutions
            resolutions_pos_y = self.height * 0.2
            for resolution_name, resolution in Screen_Resolution.items():
                print(resolution[0], resolution[1])
                resolutions_pos_y += self.height * 0.07
                screen_resolution = self.menu_font.render(resolution_name, True, GameSettings.WHITE)
                screen_resolution_rect = screen_resolution.get_rect()
                resolution_final = self.screen.blit(screen_resolution, (
                    self.width / 2 - screen_resolution_rect.center[0], resolutions_pos_y))

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

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 60 frames per second
            self.clock.tick(30)
