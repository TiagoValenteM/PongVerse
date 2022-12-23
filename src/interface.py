import sys

from .config import *
from .pong import PongVerse


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
        # Set Instructions Fonts title_font: pygame.font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT,
        # InstructionsSettings.TITLE_SIZE) subtitle_font: pygame.font = pygame.font.Font(
        # GameSettings.FONT_TYPE_DEFAULT, InstructionsSettings.SUBTITLE_SIZE) body_font: pygame.font =
        # pygame.font.Font(GameSettings.FONT_TYPE_MENU, InstructionsSettings.BODY_SIZE) Set the Default Font
        self.default_font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT, GameSettings.FONT_SIZE_DEFAULT)
        # Set the font for the menu options
        self.menu_font = pygame.font.Font(GameSettings.FONT_TYPE_MENU, InstructionsSettings.SUBTITLE_SIZE)
        # Creating Screen positions and Sizes
        self.button_width_center: int = int(InterfaceSettings.WINDOW_WIDTH * 0.5 - InterfaceSettings.BUTTON_WIDTH * 0.5)
        self.button_height_pos: int = int(InterfaceSettings.WINDOW_HEIGHT * 0.3)
        self.width_center: int = int(InterfaceSettings.WINDOW_WIDTH / 2)

    def drawRect(self, color, width, height, default_size):
        if default_size:
            # Draw the rectangle with position and size
            return pygame.draw.rect(self.screen, color,
                                    [width, height, InterfaceSettings.BUTTON_WIDTH, InterfaceSettings.BUTTON_HEIGHT],
                                    border_radius=15)
        else:
            # Draw the rectangle with position and size
            return pygame.draw.rect(self.screen, color,
                                    [width, height, InterfaceSettings.SMALL_BUTTON_WIDTH,
                                     InterfaceSettings.SMALL_BUTTON_HEIGHT],
                                    border_radius=15)

    def display_return_button(self, mouse_pos, return_rect, return_text_rect, return_text):
        if return_rect.collidepoint(mouse_pos):
            self.drawRect(GameSettings.RED, InterfaceSettings.WINDOW_WIDTH * 0.85,
                          InterfaceSettings.WINDOW_HEIGHT * 0.88, False)
        else:
            self.drawRect(GameSettings.GRAY, InterfaceSettings.WINDOW_WIDTH * 0.85,
                          InterfaceSettings.WINDOW_HEIGHT * 0.88, False)
        self.screen.blit(return_text,
                         (InterfaceSettings.WINDOW_WIDTH - return_rect.width - return_text_rect.center[0],
                          InterfaceSettings.WINDOW_HEIGHT * 0.885))

    # Creating a function that creates the GUI
    def mainMenu(self):
        # Create a loop that carries on until the user exits the main menu
        mainMenuOn: int = 1

        # Create text-labels and get their rectangle
        # PongVerse
        text_play_pongVerse = self.menu_font.render('The PongVerse', True, GameSettings.WHITE)
        play_pong_rect = text_play_pongVerse.get_rect()
        play_pongVerse_rect = self.drawRect(GameSettings.GRAY, self.button_width_center, self.button_height_pos, True)

        # PongVerse Vanilla Edition
        text_play_pongVerse_vanilla = self.menu_font.render('PongVerse - Vanilla', True, GameSettings.WHITE)
        play_pong_vanilla_rect = text_play_pongVerse_vanilla.get_rect()
        play_pongVerse_vanilla_rect = self.drawRect(GameSettings.GRAY, self.button_width_center,
                                                    self.button_height_pos + InterfaceSettings.BUTTON_GAP, True)
        # Settings
        text_settings = self.menu_font.render('Settings', True, GameSettings.WHITE)
        settings_text_rect = text_settings.get_rect()
        settings_rect = self.drawRect(GameSettings.GRAY, self.button_width_center,
                                      self.button_height_pos + InterfaceSettings.BUTTON_GAP * 2, True)
        # Creators
        text_creators = self.menu_font.render('Creators', True, GameSettings.WHITE)
        creators_text_rect = text_creators.get_rect()
        creators_rect = self.drawRect(GameSettings.GRAY, self.button_width_center,
                                      self.button_height_pos + InterfaceSettings.BUTTON_GAP * 3, True)
        # Quit
        text_quit = self.menu_font.render('Quit', True, GameSettings.WHITE)
        quit_text_rect = text_quit.get_rect()
        quit_rect = self.drawRect(GameSettings.GRAY, self.button_width_center,
                                  self.button_height_pos + InterfaceSettings.BUTTON_GAP * 4, True)
        # Title
        text_title = self.default_font.render('The PongVerse - OOP PyGame', True, GameSettings.RED)
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
                self.drawRect(GameSettings.BLUE, self.button_width_center, self.button_height_pos, True)
            else:
                self.drawRect(GameSettings.GRAY, self.button_width_center, self.button_height_pos, True)
            self.screen.blit(text_play_pongVerse,
                             (self.width_center - play_pong_rect.center[0],
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 0.05))
            # Play PongVerse Vanilla Edition Button
            if play_pongVerse_vanilla_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.BLUE, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP, True)
            else:
                self.drawRect(GameSettings.GRAY, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP, True)
            self.screen.blit(text_play_pongVerse_vanilla,
                             (self.width_center - play_pong_vanilla_rect.center[0],
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 1.05))
            # Enter Settings Button
            if settings_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.BLUE, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 2, True)
            else:
                self.drawRect(GameSettings.GRAY, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 2, True)
            self.screen.blit(text_settings,
                             (self.width_center - settings_text_rect.center[0],
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 2.05))
            # Enter Creators Button
            if creators_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.BLUE, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 3, True)
            else:
                self.drawRect(GameSettings.GRAY, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 3, True)
            self.screen.blit(text_creators,
                             (self.width_center - creators_text_rect.center[0],
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 3.05))
            # Quit Button
            if quit_rect.collidepoint(mouse_pos):
                self.drawRect(GameSettings.RED, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 4, True)
            else:
                self.drawRect(GameSettings.GRAY, self.button_width_center,
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 4, True)
            self.screen.blit(text_quit,
                             (self.width_center - quit_text_rect.center[0],
                              self.button_height_pos + InterfaceSettings.BUTTON_GAP * 4.05))

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
        creators_body_font = pygame.font.Font(GameSettings.FONT_TYPE_MENU, InstructionsSettings.SUBTITLE_SIZE)
        nova_text_font = pygame.font.Font(GameSettings.FONT_TYPE_MENU, InstructionsSettings.BODY_SIZE)

        # Create text-labels and get their rectangle
        # Return
        return_text = self.menu_font.render('Return', True, GameSettings.WHITE)
        return_text_rect = return_text.get_rect()
        return_rect = self.drawRect(GameSettings.GRAY, InterfaceSettings.WINDOW_WIDTH * 0.85,
                                    InterfaceSettings.WINDOW_HEIGHT * 0.88, False)

        # Title
        text_title = self.default_font.render('Our Team of Creators', True, GameSettings.LIGHT_BLUE)
        title_rect = text_title.get_rect()

        creator_1 = creators_body_font.render('Leonor Costa | 20211649@novaims.unl.pt', True, GameSettings.GOLDEN)
        creator_1_rect = creator_1.get_rect()
        creator_2 = creators_body_font.render('Osmáiny Raimundo | e20191506@novaims.unl.pt', True, GameSettings.GOLDEN)
        creator_2_rect = creator_2.get_rect()
        creator_3 = creators_body_font.render('Sara Lyra | 20211565@novaims.unl.pt', True, GameSettings.GOLDEN)
        creator_3_rect = creator_3.get_rect()
        creator_4 = creators_body_font.render('Tiago Valente | 20211650@novaims.unl.pt', True, GameSettings.GOLDEN)
        creator_4_rect = creator_4.get_rect()

        novaims_text = nova_text_font.render('NovaIMS - Information Management School', True,
                                             GameSettings.WHITE)

        while True:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                # press on exit button
                if ev.type == pygame.QUIT:
                    pygame.quit()
                # press on quit button
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Mouse click on quit button
                    if return_rect.collidepoint(mouse_pos):
                        self.mainMenu()

            # Set the title of the window
            pygame.display.set_caption(InterfaceSettings.CREDITS_TITLE)

            # background image
            self.screen.blit(self.background_img, (0, 0))

            # Title text
            self.screen.blit(text_title, (
                InterfaceSettings.WINDOW_WIDTH / 2 - title_rect.center[0],
                InterfaceSettings.WINDOW_HEIGHT * 0.05))

            # credits text
            self.screen.blit(creator_1, (self.width_center - creator_1_rect.center[0], self.button_height_pos))
            self.screen.blit(creator_2, (
                self.width_center - creator_2_rect.center[0],
                self.button_height_pos + InterfaceSettings.BUTTON_GAP * 0.75))
            self.screen.blit(creator_3, (
                self.width_center - creator_3_rect.center[0],
                self.button_height_pos + InterfaceSettings.BUTTON_GAP * 1.5))
            self.screen.blit(creator_4, (
                self.width_center - creator_4_rect.center[0],
                self.button_height_pos + InterfaceSettings.BUTTON_GAP * 2.25))

            # Quit Button
            self.display_return_button(mouse_pos, return_rect, return_text_rect, return_text)

            NOVAIMS_IMG_RECT = InterfaceSettings.NOVAIMS_IMG_LOAD.get_rect()
            self.screen.blit(InterfaceSettings.NOVAIMS_IMG_LOAD.convert_alpha(), (
                InterfaceSettings.WINDOW_WIDTH * 0.03,
                InterfaceSettings.WINDOW_HEIGHT * 0.97 - NOVAIMS_IMG_RECT.height))
            self.screen.blit(novaims_text, (InterfaceSettings.WINDOW_WIDTH * 0.03 + NOVAIMS_IMG_RECT.width,
                                            InterfaceSettings.WINDOW_HEIGHT * 1.04 - NOVAIMS_IMG_RECT.height))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 60 frames per second
            self.clock.tick(30)

    def settings(self):
        # Create text-labels and get their rectangle
        # Return
        return_text = self.menu_font.render('Return', True, GameSettings.WHITE)
        return_text_rect = return_text.get_rect()
        return_rect = self.drawRect(GameSettings.GRAY, InterfaceSettings.WINDOW_WIDTH * 0.85,
                                    InterfaceSettings.WINDOW_HEIGHT * 0.88, False)

        while True:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # press on exit button
                if event.type == pygame.QUIT:
                    pygame.quit()
                # press on quit button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Mouse click on quit button
                    if return_rect.collidepoint(mouse_pos):
                        self.mainMenu()

            # background image
            self.screen.blit(self.background_img, (0, 0))

            # Set the title of the window
            pygame.display.set_caption(InterfaceSettings.SETTINGS_TITLE)

            # Set height position for Resolutions
            resolutions_pos_y = self.height * 0.2
            for resolution_name, resolution in Screen_Resolution.items():
                resolutions_pos_y += self.height * 0.07
                screen_resolution = self.menu_font.render(resolution_name, True, GameSettings.WHITE)
                screen_resolution_rect = screen_resolution.get_rect()
                resolution_final = self.screen.blit(screen_resolution, (
                    self.width / 2 - screen_resolution_rect.center[0], resolutions_pos_y))

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if resolution_final.collidepoint(mouse_pos):
                            self.width, InterfaceSettings.WINDOW_WIDTH = resolution[0], resolution[0]
                            self.height, InterfaceSettings.WINDOW_HEIGHT = resolution[1], resolution[1]
                            self.screen = pygame.display.set_mode((self.width, self.height))

            # Quit Button
            self.display_return_button(mouse_pos, return_rect, return_text_rect, return_text)

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 60 frames per second
            self.clock.tick(30)
