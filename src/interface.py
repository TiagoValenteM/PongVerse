import os, sys, main

import pygame.mixer

from .config import *
from .pong import PongVerse


class Interface:
    def __init__(self, settings: GlobalSettings):
        # initiating pygame and pygame mixer
        pygame.init(), pygame.mixer.init()
        # Define settings for the game
        self.settings: GlobalSettings = settings
        # Music and Sound Effects
        if self.settings.music_on:
            pygame.mixer.music.load('sound/main_theme.mp3')
            pygame.mixer.music.play(-1)
        # Opens a new window
        self.screen: pygame.display = pygame.display.set_mode(settings.resolution)
        self.clock: pygame.time = pygame.time.Clock()
        # Set the Game icon
        icon: pygame.image = pygame.image.load("img/icons/main_icon.png").convert_alpha()
        pygame.display.set_icon(icon)
        # Set background Image
        background_img_load: pygame.image = pygame.image.load("img/background/background_interface.jpg").convert()
        self.background_img: pygame.transform = pygame.transform.scale(background_img_load, (self.settings.width,
                                                                                             self.settings.height))
        self.default_font = pygame.font.Font(settings.FONT_TYPE_DEFAULT, settings.font_size_default)
        # Set the font for the menu options
        self.menu_font = pygame.font.Font(settings.FONT_TYPE_MENU, settings.subtitle_size)
        # Creating Screen positions and Sizes
        self.button_width_center: int = int(self.settings.width * 0.5 - settings.button_width * 0.5)
        self.button_height_pos: int = int(self.settings.height * 0.3)
        self.width_center: int = int(self.settings.width / 2)

    def clickSound(self):
        if self.settings.music_on:
            pygame.mixer.Sound('sound/click_sound.wav').play()

    def drawRect(self, color, width, height, default_size):
        if default_size:
            # Draw the rectangle with position and size
            return pygame.draw.rect(self.screen, color,
                                    [width, height, self.settings.button_width, self.settings.button_height],
                                    border_radius=15)
        else:
            # Draw the rectangle with position and size
            return pygame.draw.rect(self.screen, color,
                                    [width, height, self.settings.small_button_width,
                                     self.settings.small_button_height],
                                    border_radius=15)

    def displayReturnButton(self, mouse_pos, return_rect, return_text_rect, return_text):
        if return_rect.collidepoint(mouse_pos):
            self.drawRect(self.settings.RED, self.settings.width * 0.85,
                          self.settings.height * 0.88, False)
        else:
            self.drawRect(self.settings.GRAY, self.settings.width * 0.85,
                          self.settings.height * 0.88, False)
        self.screen.blit(return_text,
                         (self.settings.width - return_rect.width - return_text_rect.center[0],
                          self.settings.height * 0.885))

    def setTitle(self, title):
        text_title = self.default_font.render(title, True, self.settings.RED)
        title_rect = text_title.get_rect()
        return text_title, title_rect

    @staticmethod
    def setWindowTitle(title):
        pygame.display.set_caption(title)

    def mainProgramLoop(self, main_loop, return_rect):
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        if pygame.event.get(pygame.QUIT):
            # press on exit button
            pygame.quit(), sys.exit()
            # press on return button
        if return_rect.collidepoint(mouse_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            self.clickSound()
            # Mouse click on return button
            main_loop = 0 and self.mainMenu()
        return main_loop, mouse_pos

    def getResolutionDict(self):
        # Set height position for Resolutions
        resolution_rect_list = []
        resolution_pos_height = self.settings.height * 0.18
        for resolution_name, resolution in Screen_Resolution.items():
            resolution_pos_height += self.settings.button_gap
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
                                                    self.button_height_pos + self.settings.button_gap, True)
        # Settings
        text_settings = self.menu_font.render('Settings', True, self.settings.WHITE)
        settings_text_rect = text_settings.get_rect()
        settings_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                      self.button_height_pos + self.settings.button_gap * 2, True)
        # Creators
        text_creators = self.menu_font.render('Creators', True, self.settings.WHITE)
        creators_text_rect = text_creators.get_rect()
        creators_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                      self.button_height_pos + self.settings.button_gap * 3, True)
        # Quit
        text_quit = self.menu_font.render('Quit', True, self.settings.WHITE)
        quit_text_rect = text_quit.get_rect()
        quit_rect = self.drawRect(self.settings.GRAY, self.button_width_center,
                                  self.button_height_pos + self.settings.button_gap * 4, True)

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
                    self.clickSound(), PongVerse(vanilla=False, settings=self.settings).instructions()
                # Mouse click on Vanilla Pong button
                elif play_pongVerse_vanilla_rect.collidepoint(mouse_pos):
                    self.clickSound(), PongVerse(vanilla=True, settings=self.settings).instructions()
                # Mouse click on Settings button
                elif settings_rect.collidepoint(mouse_pos):
                    self.clickSound(), self.settingsScreen()
                # Mouse click on Creators button
                elif creators_rect.collidepoint(mouse_pos):
                    self.clickSound(), self.creatorsScreen()
                # Mouse click on quit button
                elif quit_rect.collidepoint(mouse_pos):
                    self.clickSound(), pygame.quit(), sys.exit()

            # --- Main Menu logic starts here

            # Set the title of the window
            self.setWindowTitle(self.settings.MENU_TITLE)
            # background image
            self.screen.blit(self.background_img, (0, 0))

            # Display the title of the game
            self.screen.blit(text_title, (
                self.settings.width / 2 - title_rect.center[0],
                self.settings.height * 0.05))

            # On Hover, button changes color
            # Play PongVerse Button
            if play_pongVerse_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center, self.button_height_pos, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center, self.button_height_pos, True)
            self.screen.blit(text_play_pongVerse,
                             (self.width_center - play_pong_rect.center[0],
                              self.button_height_pos + self.settings.button_gap * 0.05))
            # Play PongVerse Vanilla Edition Button
            if play_pongVerse_vanilla_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap, True)
            self.screen.blit(text_play_pongVerse_vanilla,
                             (self.width_center - play_pong_vanilla_rect.center[0],
                              self.button_height_pos + self.settings.button_gap * 1.05))
            # Enter Settings Button
            if settings_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap * 2, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap * 2, True)
            self.screen.blit(text_settings,
                             (self.width_center - settings_text_rect.center[0],
                              self.button_height_pos + self.settings.button_gap * 2.05))
            # Enter Creators Button
            if creators_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap * 3, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap * 3, True)
            self.screen.blit(text_creators,
                             (self.width_center - creators_text_rect.center[0],
                              self.button_height_pos + self.settings.button_gap * 3.05))
            # Quit Button
            if quit_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.RED, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap * 4, True)
            else:
                self.drawRect(self.settings.GRAY, self.button_width_center,
                              self.button_height_pos + self.settings.button_gap * 4, True)
            self.screen.blit(text_quit,
                             (self.width_center - quit_text_rect.center[0],
                              self.button_height_pos + self.settings.button_gap * 4.05))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)

    def creatorsScreen(self):
        # Create a loop that carries on until the user exits the main menu
        creatorsON: int = 1

        # Create specific fonts for the creators
        creators_body_font = pygame.font.Font(self.settings.FONT_TYPE_MENU, self.settings.subtitle_size)
        nova_text_font = pygame.font.Font(self.settings.FONT_TYPE_MENU, self.settings.body_size)

        # Create specific alignments for the creators names
        name_height_pos: int = int(self.settings.height * 0.35)

        # Create specific alignments for the creators icons
        creator_icon_rect = self.settings.creator_1_img_load.get_rect()
        left_icon_alignment = self.settings.width * 0.07
        right_icon_alignment = self.settings.width * 0.93 - creator_icon_rect.width
        top_icon_alignment = self.settings.height * 0.25
        bottom_icon_alignment = self.settings.height * 0.75 - creator_icon_rect.height

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
        return_rect = self.drawRect(self.settings.GRAY, self.settings.width * 0.85,
                                    self.settings.height * 0.88, False)

        # Nova IMS text
        novaims_text = nova_text_font.render('NovaIMS - Information Management School', True,
                                             self.settings.WHITE)

        # -------- Main Program Loop -----------
        while creatorsON:
            creatorsON, mouse_pos = self.mainProgramLoop(creatorsON, return_rect)

            # --- Creators screen logic starts here

            # Set the title of the window
            self.setWindowTitle(self.settings.CREDITS_TITLE)

            # Display Background image
            self.screen.blit(self.background_img, (0, 0))

            # Display Title text
            self.screen.blit(text_title, (
                self.settings.width / 2 - title_rect.center[0],
                self.settings.height * 0.05))

            # Display Professors text
            self.screen.blit(professors_text, (self.settings.width / 2 - professors_text_rect.center[0],
                                               self.settings.height * 0.17))

            # Display Creators text
            # Creator 1
            self.screen.blit(creator_1, (self.width_center - creator_1_rect.center[0], name_height_pos))
            # Creator 2
            self.screen.blit(creator_2, (
                self.width_center - creator_2_rect.center[0],
                name_height_pos + self.settings.button_gap * 0.75))
            # Creator 3
            self.screen.blit(creator_3, (
                self.width_center - creator_3_rect.center[0],
                name_height_pos + self.settings.button_gap * 1.5))
            # Creator 4
            self.screen.blit(creator_4, (
                self.width_center - creator_4_rect.center[0],
                name_height_pos + self.settings.button_gap * 2.25))

            # Display Creators Icons
            # Creator 1
            self.screen.blit(self.settings.creator_1_img_load, (left_icon_alignment, top_icon_alignment))
            # Creator 2
            self.screen.blit(self.settings.creator_2_img_load, (left_icon_alignment, bottom_icon_alignment))
            # Creator 3
            self.screen.blit(self.settings.creator_3_img_load, (right_icon_alignment, top_icon_alignment))
            # Creator 4
            self.screen.blit(self.settings.creator_4_img_load, (right_icon_alignment, bottom_icon_alignment))
            # Display Return button
            self.displayReturnButton(mouse_pos, return_rect, return_text_rect, return_text)

            # Display NovaIMS text and Icon
            novaims_img_rect = self.settings.novaims_img_load.get_rect()
            self.screen.blit(self.settings.novaims_img_load.convert_alpha(), (
                self.settings.width * 0.03,
                self.settings.height * 0.97 - novaims_img_rect.height))
            self.screen.blit(novaims_text, (self.settings.width * 0.03 + novaims_img_rect.width,
                                            self.settings.height * 1.04 - novaims_img_rect.height))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)

    def settingsScreen(self):
        # Create a loop that carries on until the user exits the main menu
        settingsOn: int = 1

        # Create text-labels and get their rectangle
        # Title
        text_title, title_rect = self.setTitle('Settings')

        # Return text
        return_text = self.menu_font.render('Return', True, self.settings.WHITE)
        return_text_rect = return_text.get_rect()
        return_rect = self.drawRect(self.settings.GRAY, self.settings.width * 0.85,
                                    self.settings.height * 0.88, False)

        # Sound On/Off text
        sound_text = self.menu_font.render('On/Off', True, self.settings.WHITE)
        sound_text_rect = return_text.get_rect()
        sound_rect = self.drawRect(self.settings.GRAY, self.settings.width * 0.04,
                                   self.settings.height * 0.88, False)

        resolutions_rect_list = self.getResolutionDict()

        # -------- Main Program Loop -----------
        while settingsOn:
            settingsOn, mouse_pos = self.mainProgramLoop(settingsOn, return_rect)

            # --- Settings screen logic starts here

            # background image
            self.screen.blit(self.background_img, (0, 0))

            # Set the title of the window
            self.setWindowTitle(self.settings.SETTINGS_TITLE)

            # Display the title of the game
            self.screen.blit(text_title, (
                self.settings.width / 2 - title_rect.center[0],
                self.settings.height * 0.05))

            # Display Resolution buttons
            for screen_resolution_text, screen_resolution_text_rect, \
                    screen_resolution_rect, screen_resolution_pos_height, screen_resolution in resolutions_rect_list:
                if screen_resolution_rect.collidepoint(mouse_pos):
                    self.drawRect(self.settings.BLUE, self.button_width_center, screen_resolution_pos_height, True)
                    if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                        self.clickSound()
                        sys.argv = [sys.argv[0], int(screen_resolution[0]), int(screen_resolution[1]),
                                    self.settings.music_on]
                        os.execv(main.main(), sys.argv)
                else:
                    self.drawRect(self.settings.GRAY, self.button_width_center, screen_resolution_pos_height, True)
                self.screen.blit(screen_resolution_text, (
                    self.width_center - screen_resolution_text_rect.center[0],
                    screen_resolution_pos_height + self.settings.button_gap * 0.05))

            # Display Sound On/Off icon
            self.screen.blit(self.settings.sound_on_img_load.convert_alpha(),
                             (sound_rect.width * 1.5, self.settings.height * 0.885))

            # Display Sound On/Off button
            if sound_rect.collidepoint(mouse_pos):
                self.drawRect(self.settings.BLUE, self.settings.width * 0.04, self.settings.height * 0.88, False)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    if self.settings.music_on:
                        pygame.mixer.music.pause()
                        pygame.mixer.stop()
                        self.settings.music_on = False
                    else:
                        pygame.mixer.music.unpause()
                        self.settings.music_on = True
            else:
                self.drawRect(self.settings.GRAY, self.settings.width * 0.04, self.settings.height * 0.88, False)
            self.screen.blit(sound_text,
                             (sound_rect.center[0] - sound_text_rect.center[0], self.settings.height * 0.885))

            # Quit Button
            self.displayReturnButton(mouse_pos, return_rect, return_text_rect, return_text)

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)
