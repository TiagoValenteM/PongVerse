import os
import sys

import main
from .config import *
from .pong import PongVerse


class Interface:
    def __init__(self, settings: GlobalSettings):
        # initiating pygames
        pygame.init()
        # Opens a new window
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.resolution)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        # Set the Game icon
        icon: pygame.image = pygame.image.load("img/icons/main_icon.png").convert_alpha()
        pygame.display.set_icon(icon)
        # Set background Image
        background_img_load: any = pygame.image.load("img/background/background_interface.jpg").convert()
        self.background_img: any = pygame.transform.scale(background_img_load, (self.width,
                                                                                self.height))
        # Set Instructions Fonts title_font: pygame.font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT,
        # InstructionsSettings.TITLE_SIZE) subtitle_font: pygame.font = pygame.font.Font(
        # GameSettings.FONT_TYPE_DEFAULT, InstructionsSettings.SUBTITLE_SIZE) body_font: pygame.font =
        # pygame.font.Font(GameSettings.FONT_TYPE_MENU, InstructionsSettings.BODY_SIZE) Set the Default Font
        self.default_font = pygame.font.Font(settings.FONT_TYPE_DEFAULT, settings.FONT_SIZE_DEFAULT)
        # Set the font for the menu options
        self.menu_font = pygame.font.Font(settings.FONT_TYPE_MENU, settings.SUBTITLE_SIZE)
        # Creating Screen positions and Sizes
        self.button_width_center: int = int(self.width * 0.5 - settings.BUTTON_WIDTH * 0.5)
        self.button_height_pos: int = int(self.height * 0.3)
        self.width_center: int = int(self.width / 2)

    def drawRect(self, color, width, height, default_size):
        if default_size:
            # Draw the rectangle with position and size
            return pygame.draw.rect(self.screen, color,
                                    [width, height, self.settings.BUTTON_WIDTH, self.settings.BUTTON_HEIGHT],
                                    border_radius=15)
        else:
            # Draw the rectangle with position and size
            return pygame.draw.rect(self.screen, color,
                                    [width, height, self.settings.SMALL_BUTTON_WIDTH,
                                     self.settings.SMALL_BUTTON_HEIGHT],
                                    border_radius=15)

    def displayReturnButton(self, mouse_pos, return_rect, return_text_rect, return_text):
        if return_rect.collidepoint(mouse_pos):
            self.drawRect(self.settings.RED, self.width * 0.85,
                          self.height * 0.88, False)
        else:
            self.drawRect(self.settings.GRAY, self.width * 0.85,
                          self.height * 0.88, False)
        self.screen.blit(return_text,
                         (self.width - return_rect.width - return_text_rect.center[0],
                          self.height * 0.885))

    def setTitle(self, title):
        text_title = self.default_font.render(title, True, self.settings.RED)
        title_rect = text_title.get_rect()
        return text_title, title_rect

    def mainProgramLoop(self, main_loop, return_rect):
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        if pygame.event.get(pygame.QUIT):
            # press on exit button
            pygame.quit(), sys.exit()
            # press on return button
        if return_rect.collidepoint(mouse_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            # Mouse click on return button
            main_loop = 0 and self.mainMenu()
        return main_loop, mouse_pos

    def getResolutionDict(self):
        # Set height position for Resolutions
        resolution_rect_list = []
        resolution_pos_height = self.height * 0.18
        for resolution_name, resolution in Screen_Resolution.items():
            resolution_pos_height += self.settings.BUTTON_GAP
            resolution_text = self.menu_font.render(resolution_name, True, self.settings.WHITE)
            resolution_text_rect = resolution_text.get_rect()
            resolution_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                            resolution_pos_height, True)
            resolution_rect_list.append(
                (resolution_text, resolution_text_rect, resolution_rect, resolution_pos_height, resolution))
        return resolution_rect_list

    # Creating a function that creates the GUI
    def mainMenu(self):
        # Create a loop that carries on until the user exits the game
        mainMenuOn: int = 1

        # Create text-labels and get their rectangle
        # Title
        text_title, title_rect = self.setTitle('The PongVerse - OOP PyGame')

        # PongVerse
        text_play_pongVerse = self.menu_font.render('The PongVerse', True, self.settings.WHITE)
        play_pong_rect = text_play_pongVerse.get_rect()
        play_pongVerse_rect = self.drawRect(self.settings.GRAY, self.button_width_center, self.button_height_pos, True)

        # PongVerse Vanilla Edition
        text_play_pongVerse_vanilla = self.menu_font.render('PongVerse - Vanilla', True, self.settings.WHITE)
        play_pong_vanilla_rect = text_play_pongVerse_vanilla.get_rect()
        play_pongVerse_vanilla_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                                    self.button_height_pos + self.settings.BUTTON_GAP, True)
        # Settings
        text_settings = self.menu_font.render('Settings', True, self.settings.WHITE)
        settings_text_rect = text_settings.get_rect()
        settings_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                      self.button_height_pos + self.settings.BUTTON_GAP * 2, True)
        # Creators
        text_creators = self.menu_font.render('Creators', True, self.settings.WHITE)
        creators_text_rect = text_creators.get_rect()
        creators_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                      self.button_height_pos + self.settings.BUTTON_GAP * 3, True)
        # Quit
        text_quit = self.menu_font.render('Quit', True, self.settings.WHITE)
        quit_text_rect = text_quit.get_rect()
        quit_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                  self.button_height_pos + self.settings.BUTTON_GAP * 4, True)

        # -------- Main Program Loop -----------
        while mainMenuOn:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Get an input from the user
            # Press the exit button
            if pygame.event.get(pygame.QUIT):
                pygame.quit(), sys.exit()
                # Press the mouse button
            if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                # Mouse click on Pong button
                if play_pongVerse_rect.collidepoint(mouse_pos):
                    PongVerse(vanilla=False, settings=self.settings).instructions()
                # Mouse click on Vanilla Pong button
                elif play_pongVerse_vanilla_rect.collidepoint(mouse_pos):
                    PongVerse(vanilla=True, settings=self.settings).instructions()
                # Mouse click on Settings button
                elif settings_rect.collidepoint(mouse_pos):
                    self.load_settings()
                # Mouse click on Creators button
                elif creators_rect.collidepoint(mouse_pos):
                    self.creators()
                # Mouse click on quit button
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit(), sys.exit()

            # --- Main Menu logic starts here

            # Set the title of the window
            pygame.display.set_caption(self.settings.MENU_TITLE)
            # background image
            self.screen.blit(self.background_img, (0, 0))

            # Display the title of the game
            self.screen.blit(text_title, (
                self.width / 2 - title_rect.center[0],
                self.height * 0.05))

            # On Hover, button changes color
            # Play PongVerse Button
            if play_pongVerse_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center, self.button_height_pos, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center, self.button_height_pos, True)
            self.screen.blit(text_play_pongVerse,
                             (self.width_center - play_pong_rect.center[0],
                              self.button_height_pos + self.settings.BUTTON_GAP * 0.05))
            # Play PongVerse Vanilla Edition Button
            if play_pongVerse_vanilla_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP, True)
            self.screen.blit(text_play_pongVerse_vanilla,
                             (self.width_center - play_pong_vanilla_rect.center[0],
                              self.button_height_pos + self.settings.BUTTON_GAP * 1.05))
            # Enter Settings Button
            if settings_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP * 2, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP * 2, True)
            self.screen.blit(text_settings,
                             (self.width_center - settings_text_rect.center[0],
                              self.button_height_pos + self.settings.BUTTON_GAP * 2.05))
            # Enter Creators Button
            if creators_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP * 3, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP * 3, True)
            self.screen.blit(text_creators,
                             (self.width_center - creators_text_rect.center[0],
                              self.button_height_pos + self.settings.BUTTON_GAP * 3.05))
            # Quit Button
            if quit_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.RED, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP * 4, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.BUTTON_GAP * 4, True)
            self.screen.blit(text_quit,
                             (self.width_center - quit_text_rect.center[0],
                              self.button_height_pos + self.settings.BUTTON_GAP * 4.05))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)

    def creators(self):
        # Create a loop that carries on until the user exits the main menu
        creatorsON: int = 1

        # Create specific fonts for the creators
        creators_body_font = pygame.font.Font(self.settings.FONT_TYPE_MENU, self.settings.SUBTITLE_SIZE)
        nova_text_font = pygame.font.Font(self.settings.FONT_TYPE_MENU, self.settings.BODY_SIZE)

        # Create specific alignments for the creators names
        name_height_pos: int = int(self.height * 0.35)

        # Create specific alignments for the creators icons
        creator_icon_rect = self.settings.CREATOR_1_IMG_LOAD.get_rect()
        left_icon_alignment = self.width * 0.07
        right_icon_alignment = self.width * 0.93 - creator_icon_rect.width
        top_icon_alignment = self.height * 0.25
        bottom_icon_alignment = self.height * 0.75 - creator_icon_rect.height

        # Create text-labels and get their rectangle
        # Title
        text_title, title_rect = self.setTitle('Our Team of Creators')

        # Body
        # Professors text
        professors_text = nova_text_font.render('Base code provided by our well Respected Professors', True,
                                                self.settings.WHITE)
        professors_text_rect = professors_text.get_rect()

        # Creators text
        creator_1 = creators_body_font.render('Leonor Costa | 20211649@novaims.unl.pt', True, self.settings.WHITE)
        creator_1_rect = creator_1.get_rect()
        creator_2 = creators_body_font.render('Osmáiny Raimundo | e20191506@novaims.unl.pt', True, self.settings.WHITE)
        creator_2_rect = creator_2.get_rect()
        creator_3 = creators_body_font.render('Sara Lyra | 20211565@novaims.unl.pt', True, self.settings.WHITE)
        creator_3_rect = creator_3.get_rect()
        creator_4 = creators_body_font.render('Tiago Valente | 20211650@novaims.unl.pt', True, self.settings.WHITE)
        creator_4_rect = creator_4.get_rect()

        # Return text
        return_text = self.menu_font.render('Return', True, self.settings.WHITE)
        return_text_rect = return_text.get_rect()
        return_rect = self.drawRect(self.settings.GRAY, self.width * 0.85,
                                    self.height * 0.88, False)

        # Nova IMS text
        novaims_text = nova_text_font.render('NovaIMS - Information Management School', True,
                                             self.settings.WHITE)

        # -------- Main Program Loop -----------
        while creatorsON:
            creatorsON, mouse_pos = self.mainProgramLoop(creatorsON, return_rect)

            # --- Creators screen logic starts here

            # Set the title of the window
            pygame.display.set_caption(self.settings.CREDITS_TITLE)

            # Display Background image
            self.screen.blit(self.background_img, (0, 0))

            # Display Title text
            self.screen.blit(text_title, (
                self.width / 2 - title_rect.center[0],
                self.height * 0.05))

            # Display Professors text
            self.screen.blit(professors_text, (self.width / 2 - professors_text_rect.center[0],
                                               self.height * 0.17))

            # Display Creators text
            # Creator 1
            self.screen.blit(creator_1, (self.width_center - creator_1_rect.center[0], name_height_pos))
            # Creator 2
            self.screen.blit(creator_2, (
                self.width_center - creator_2_rect.center[0],
                name_height_pos + self.settings.BUTTON_GAP * 0.75))
            # Creator 3
            self.screen.blit(creator_3, (
                self.width_center - creator_3_rect.center[0],
                name_height_pos + self.settings.BUTTON_GAP * 1.5))
            # Creator 4
            self.screen.blit(creator_4, (
                self.width_center - creator_4_rect.center[0],
                name_height_pos + self.settings.BUTTON_GAP * 2.25))

            # Display Creators Icons
            # Creator 1
            self.screen.blit(self.settings.CREATOR_1_IMG_LOAD, (left_icon_alignment, top_icon_alignment))
            # Creator 2
            self.screen.blit(self.settings.CREATOR_2_IMG_LOAD, (left_icon_alignment, bottom_icon_alignment))
            # Creator 3
            self.screen.blit(self.settings.CREATOR_3_IMG_LOAD, (right_icon_alignment, top_icon_alignment))
            # Creator 4
            self.screen.blit(self.settings.CREATOR_4_IMG_LOAD, (right_icon_alignment, bottom_icon_alignment))
            # Display Return button
            self.displayReturnButton(mouse_pos, return_rect, return_text_rect, return_text)

            # Display NovaIMS text and Icon
            novaims_img_rect = self.settings.NOVAIMS_IMG_LOAD.get_rect()
            self.screen.blit(self.settings.NOVAIMS_IMG_LOAD.convert_alpha(), (
                self.width * 0.03,
                self.height * 0.97 - novaims_img_rect.height))
            self.screen.blit(novaims_text, (self.width * 0.03 + novaims_img_rect.width,
                                            self.height * 1.04 - novaims_img_rect.height))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)

    def load_settings(self):
        # Create a loop that carries on until the user exits the main menu
        settingsOn: int = 1

        # Create text-labels and get their rectangle
        # Title
        text_title, title_rect = self.setTitle('Settings')

        # Return text
        return_text = self.menu_font.render('Return', True, self.settings.WHITE)
        return_text_rect = return_text.get_rect()
        return_rect = self.drawRect(self.settings.GRAY, self.width * 0.85,
                                    self.height * 0.88, False)

        resolutions_rect_list = self.getResolutionDict()

        # -------- Main Program Loop -----------
        while settingsOn:
            settingsOn, mouse_pos = self.mainProgramLoop(settingsOn, return_rect)
            # mouse_pos = pygame.mouse.get_pos()
            # --- Settings screen logic starts here

            # background image
            self.screen.blit(self.background_img, (0, 0))

            # Set the title of the window
            pygame.display.set_caption(self.settings.SETTINGS_TITLE)
            # Display the title of the game
            self.screen.blit(text_title, (
                self.width / 2 - title_rect.center[0],
                self.height * 0.05))

            for screen_resolution_text, screen_resolution_text_rect, \
                    screen_resolution_rect, screen_resolution_pos_height, screen_resolution in resolutions_rect_list:
                if screen_resolution_rect.collidepoint(mouse_pos):
                    self.drawRect(self.settings.BLUE, self.button_width_center, screen_resolution_pos_height, True)
                    if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                        sys.argv = [sys.argv[0], int(screen_resolution[0]), int(screen_resolution[1])]
                        os.execv(main.main(), sys.argv)
                else:
                    self.drawRect(self.settings.GRAY, self.button_width_center, screen_resolution_pos_height, True)
                self.screen.blit(screen_resolution_text, (
                    self.width_center - screen_resolution_text_rect.center[0],
                    screen_resolution_pos_height + self.settings.BUTTON_GAP * 0.05))

            # Quit Button
            self.displayReturnButton(mouse_pos, return_rect, return_text_rect, return_text)

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)
