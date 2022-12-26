import sys
from random import choices
from .ball import Ball
from .paddle import Paddle
from .powerups import *
from .config import *


class PongVerse:
    def __init__(self, vanilla: bool, settings: GlobalSettings):
        # Load the game settings
        self.settings = settings
        # Set the game version
        self.vanilla = vanilla
        # Set if a powerup is visible
        self.powerup_visible: any = None
        # Set if a powerup is active
        self.powerup_active: any = None
        # Set the time for the powerup icon to be visible
        self.powerup_visible_time: any = None
        # Set the time a powerup affects a player
        self.powerup_active_time: any = None
        # Create a list that contains all the sprites used in game
        self.all_sprites_list = pygame.sprite.Group()
        # Create a list that contains additional balls
        self.additional_balls: list[Ball] = []
        # Set the ball owner
        self.ball_owner: any = None
        # Set the powerup owner
        self.powerup_owner: any = None
        # Opens a new window
        self.screen = pygame.display.set_mode(settings.resolution)
        # Set the Default Font
        self.default_font = pygame.font.Font(settings.FONT_TYPE_DEFAULT, settings.FONT_SIZE_DEFAULT)
        # Set the PowerUp Font
        self.powerup_font = pygame.font.Font(settings.FONT_TYPE_DEFAULT, settings.FONT_SIZE_POWERUP)
        # Set a small Powerup Font
        self.small_powerup_font = pygame.font.Font(settings.FONT_TYPE_MENU, settings.FONT_SIZE_SMALL_POWERUP)
        # Create a clock that controls FPS
        self.clock = pygame.time.Clock()
        # Set scores to 0
        self.scoreA: int = 0
        self.scoreB: int = 0
        # Set trigger for the ball to be reset
        self.triggered: bool = False

    def display_win_condition_instructions(self, body_font, subtitle_font, left_x_alignment):
        # Display the win condition subtitle
        win_condition_title = subtitle_font.render('Win Condition', True, self.settings.LIGHT_BLUE)
        self.screen.blit(win_condition_title,
                         (left_x_alignment, self.settings.height * 0.6))
        # Display the win condition text
        win_condition_body = body_font.render(f'First player to hit {self.settings.WIN_SCORE} points wins!', True,
                                              self.settings.WHITE)
        self.screen.blit(win_condition_body,
                         (left_x_alignment, self.settings.height * 0.67))

    def display_powerups_instructions(self, body_font, small_body_font, subtitle_font):
        # Check if the game is not vanilla
        if not self.vanilla:
            # Display the powerups subtitle
            powerup_class_title = subtitle_font.render('Powerups', True, self.settings.LIGHT_BLUE)
            self.screen.blit(powerup_class_title,
                             (self.settings.RIGHT_X_ALIGNMENT, self.settings.height * 0.2))
            # Check the powerups dictionary
            for powerup in PowerUps.values():
                # Get icon, name, description and active time of each powerup
                powerup_icon = pygame.transform.smoothscale(pygame.image.load(powerup.icon),
                                                            (self.settings.POWERUP_WIDTH,
                                                             self.settings.POWERUP_HEIGHT))
                powerup_name = subtitle_font.render(powerup.name, True, self.settings.GOLDEN)
                powerup_description = body_font.render(powerup.description, True, self.settings.WHITE)
                powerup_active_time = small_body_font.render(f"{powerup.active_time} seconds active", True,
                                                             self.settings.LIGHT_BLUE)
                # Set the powerup icon position
                icon_pos = self.settings.POWERUP_ICON_POS_LIST[powerup.name]
                # Display the powerup icon
                self.screen.blit(powerup_icon, icon_pos)
                # Display the powerup name
                self.screen.blit(powerup_name, [icon_pos[0] + self.settings.POWERUP_WIDTH * 1.1,
                                                icon_pos[1]])
                # Display the powerup description
                self.screen.blit(powerup_description,
                                 [icon_pos[0] + self.settings.POWERUP_WIDTH * 1.1,
                                  icon_pos[1] + self.settings.POWERUP_WIDTH * 0.45])
                # Display the powerup active time
                self.screen.blit(powerup_active_time,
                                 [icon_pos[0] + self.settings.POWERUP_WIDTH * 1.4,
                                  icon_pos[1] + self.settings.POWERUP_WIDTH * 0.8])

    def display_player_keys_instructions(self, body_font, subtitle_font, left_x_alignment):
        # Display the player keys subtitle
        player_keys_title = subtitle_font.render('Player keys', True, self.settings.LIGHT_BLUE)
        self.screen.blit(player_keys_title,
                         (left_x_alignment, self.settings.height * 0.2))

        # Display the player A keys text
        playerA_keys = body_font.render('Player A - Captain America', True, self.settings.WHITE)
        self.screen.blit(playerA_keys,
                         (left_x_alignment, self.settings.height * 0.27))
        # Display the player A key icons
        self.screen.blit(self.settings.PLAYER_A_UP.convert_alpha(),
                         (left_x_alignment, self.settings.height * 0.32))
        self.screen.blit(self.settings.PLAYER_A_DOWN.convert_alpha(),
                         (left_x_alignment + self.settings.width / 22,
                          self.settings.height * 0.32))

        # Display the player B keys text
        playerB_keys = body_font.render('Player B - Iron Man', True, self.settings.WHITE)
        self.screen.blit(playerB_keys,
                         (left_x_alignment, self.settings.height * 0.42))
        # Display the player B key icons
        self.screen.blit(self.settings.PLAYER_B_UP.convert_alpha(),
                         (left_x_alignment, self.settings.height * 0.47))
        self.screen.blit(self.settings.PLAYER_B_DOWN.convert_alpha(),
                         (left_x_alignment + self.settings.width / 22,
                          self.settings.height * 0.47))

    # Screen to display the instructions
    def instructions(self):
        # Create a loop that carries on until the user exits the instructions screen
        instructionsON: int = 1

        # Set Instructions Fonts
        title_font: pygame.font = pygame.font.Font(self.settings.FONT_TYPE_DEFAULT, self.settings.TITLE_SIZE)
        subtitle_font: pygame.font = pygame.font.Font(self.settings.FONT_TYPE_DEFAULT,
                                                      self.settings.SUBTITLE_SIZE)
        body_font: pygame.font = pygame.font.Font(self.settings.FONT_TYPE_MENU, self.settings.BODY_SIZE)
        small_body_font: pygame.font = pygame.font.Font(self.settings.FONT_TYPE_MENU,
                                                        self.settings.SMALL_BODY_SIZE)

        # -------- Main Program Loop -----------
        while instructionsON:

            # --- Main event loop
            for event in pygame.event.get():

                # If user clicked close
                if event.type == pygame.QUIT:
                    # Close the window and quit
                    pygame.quit(), sys.exit()

                # Or they used the keyboard
                if event.type == pygame.KEYDOWN:
                    # Pressing the Space key will start the game
                    if event.key == pygame.K_SPACE:
                        # Quit the loop
                        instructionsON = 0
                        # Start the game
                        self.play()

                    # Pressing the Escape Key will quit to the main menu
                    if event.key == pygame.K_ESCAPE:
                        # Quit the loop
                        instructionsON = 0

            if self.vanilla:
                # Set the vanilla title of the window/game
                pygame.display.set_caption(self.settings.INSTRUCTIONS_TITLE_VANILLA)
                title = title_font.render('Instructions - Vanilla Edition', True, self.settings.WHITE)
                # Align keys and win text on the right side of the screen
                left_x_alignment = self.settings.RIGHT_X_ALIGNMENT

            else:
                # Set the title of the window/game
                pygame.display.set_caption(self.settings.INSTRUCTIONS_TITLE)
                title = title_font.render('Instructions', True, self.settings.WHITE)
                # Align keys and win text on the left side of the screen
                left_x_alignment = self.settings.LEFT_X_ALIGNMENT

            # Set the background image
            self.screen.blit(self.settings.BACKGROUND_IMG, (0, 0))
            # Display the title on the screen
            self.screen.blit(title, (self.settings.width * 0.07, self.settings.height * 0.05))

            # Display text to return to the main menu
            self.screen.blit(self.settings.ESCAPE_KEY[0].convert_alpha(), self.settings.ESCAPE_KEY[1])
            return_text = small_body_font.render('To return press', True, self.settings.WHITE)
            # Position the text
            self.screen.blit(return_text,
                             (self.settings.width * 0.87, self.settings.height * 0.05))

            # Call a function to display the instructions for the powerups
            self.display_powerups_instructions(body_font, small_body_font, subtitle_font)
            # Call a function to display the player keys
            self.display_player_keys_instructions(body_font, subtitle_font, left_x_alignment)
            # Call a function to display the win condition
            self.display_win_condition_instructions(body_font, subtitle_font, left_x_alignment)

            # Display text to start the game
            start_game_text = body_font.render("Press SPACE to start the game", True, self.settings.WHITE)
            start_game_text_rect = start_game_text.get_rect()
            # Center the text
            self.screen.blit(start_game_text, (self.settings.width / 2 - start_game_text_rect.center[0],
                                               self.settings.height * 0.9))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)

    # Set what keys are used to move the paddles
    def pressed_keys(self, keys, paddleA, paddleB):
        # Move the paddles when the user hits W/S (player A) or up/down (player B)
        if keys[pygame.K_w]:
            paddleA.moveUp(self.settings.PADDLE_SPEED_A)
            self.triggered = True
        if keys[pygame.K_s]:
            paddleA.moveDown(self.settings.PADDLE_SPEED_A, self.settings.height)
            self.triggered = True
        if keys[pygame.K_UP]:
            paddleB.moveUp(self.settings.PADDLE_SPEED_B)
            self.triggered = True
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(self.settings.PADDLE_SPEED_B, self.settings.height)
            self.triggered = True

    # Define when a PowerUp appears, and it appears every 3 goals
    def set_powerup_visible(self):
        # Checks if a powerup is invisible and inactive and if there is a ball owner
        if self.powerup_visible is None and self.powerup_active is None and self.ball_owner is not None:
            # Gets the powerup probability
            PowerUps_Probabilities = [val.probability for val in PowerUps.values()]
            # It checks if the sum of the scores is divisible by 3
            if (self.scoreA + self.scoreB) % 3 == 0 and (self.scoreA + self.scoreB) != 0:
                # It chooses the first chosen random powerup
                chosen_powerup = choices(PowerUps, PowerUps_Probabilities)[0]
                # It creates the powerup
                powerup = chosen_powerup(self.ball_owner, self.settings.POWERUP_WIDTH, self.settings.POWERUP_HEIGHT,
                                         self.settings)
                # It adds the powerup to the list of objects
                self.all_sprites_list.add(powerup)
                # It sets the powerup as visible and sets the powerup visible timer
                self.powerup_visible, self.powerup_visible_time = powerup, pygame.time.get_ticks()

    # Define when a PowerUp icon disappears
    def set_powerup_invisible(self):
        # It erases the powerup icon
        self.powerup_visible.kill()
        # It sets the powerup as invisible
        self.powerup_visible, self.powerup_visible_time = None, None

    # Define when a PowerUp becomes active
    def set_powerup_active(self, paddleA, paddleB):
        # It sets the collided powerup as the active powerup
        self.powerup_active = self.powerup_visible
        # It erases the powerup icon
        self.powerup_visible.kill()
        # It activates the powerup and sets the powerup active timer
        self.powerup_active.run_powerup(paddleA, paddleB)
        self.powerup_active_time = pygame.time.get_ticks()

    # Define when a PowerUp becomes inactive and is effect revert
    def set_powerup_inactive(self, paddleA, paddleB):
        # It reverts the powerup effect
        self.powerup_active.revert_powerup(paddleA, paddleB)
        # It sets the powerup as inactive
        self.powerup_active, self.powerup_active_time, self.powerup_owner = None, None, None

    # Handles the visible powerup to turn it off after a certain time or activate it
    def handle_visible_powerup(self, ball, paddleA, paddleB):
        # Checks if a powerup is visible
        if self.powerup_visible_time is not None:
            # Creates a variable that stores the time the powerup has been visible
            visible = (pygame.time.get_ticks() - self.powerup_visible_time) / 1000
            # It checks if the visible time is not over
            if int(visible) < self.powerup_visible.visible_time:
                # If it is visible, it checks if it collides with the ball
                if pygame.sprite.collide_mask(ball, self.powerup_visible) and self.ball_owner is not None:
                    # Set the powerup owner, that does not change when hitting a paddle
                    self.powerup_owner = self.ball_owner
                    # If it collides, it sets the powerup to be active
                    self.set_powerup_active(paddleA, paddleB)
            else:
                # If the visible time is over, it sets the powerup to be invisible
                self.set_powerup_invisible()

    # Handles the active powerup to turn it off after a certain time
    def handle_active_powerup(self, paddleA, paddleB):
        # Checks if a powerup is active
        if self.powerup_active_time is not None:
            # Creates a variable that stores the time the powerup has been active
            activated = (pygame.time.get_ticks() - self.powerup_active_time) / 1000
            # It checks if the visible time for the name of the active powerup's name is not over
            if int(activated) < self.settings.POWERUP_NAME_VISIBLE_TIME:
                # Displays the powerup active name
                display_powerup_name = self.powerup_font.render(str(self.powerup_active.name), True,
                                                                self.settings.WHITE)
                # Gets the rectangle of the powerup name
                display_powerup_name_rect = display_powerup_name.get_rect()
                self.screen.blit(display_powerup_name, (
                    self.settings.width / 2 - display_powerup_name_rect.center[0],
                    self.settings.height * 0.85))
                # Displays the powerup active description
                display_powerup_name = self.small_powerup_font.render(str(self.powerup_active.description), True,
                                                                      self.settings.WHITE)
                # Gets the rectangle of the powerup name
                display_powerup_name_rect = display_powerup_name.get_rect()
                self.screen.blit(display_powerup_name, (
                    self.settings.width / 2 - display_powerup_name_rect.center[0],
                    self.settings.height * 0.94))
            # It checks if the active time is over
            if int(activated) == self.powerup_active.active_time:
                # If it is over, it sets the powerup to be inactive
                self.set_powerup_inactive(paddleA, paddleB)

    # Handles the additional balls
    def handle_multiple_balls(self, paddleA, paddleB):
        if self.powerup_active is not None and self.powerup_active.name == MultipleBalls.name:
            self.triggered = True  # avoid triggering and stopping the screen if a ball scores
            if len(self.additional_balls) == 0:
                ball_count = randint(self.settings.MIN_ADDITIONAL_BALLS, self.settings.MAX_ADDITIONAL_BALLS)
                for i in range(ball_count):
                    additional_ball = self.instance_new_ball()
                    self.all_sprites_list.add(additional_ball)
                    self.additional_balls.append(additional_ball)
            else:
                for additional_ball in self.additional_balls:
                    additional_ball.handle_ball_collision(self.ball_owner, paddleA, paddleB)
                    self.scoreA, self.scoreB, should_kill = additional_ball.handle_multiple_balls_motion(
                        self.powerup_owner,
                        self.scoreA,
                        self.scoreB)
                    if should_kill:
                        self.additional_balls.remove(additional_ball)
                        self.all_sprites_list.remove(additional_ball)
                if len(self.additional_balls) == 0:
                    self.set_powerup_inactive(paddleA, paddleB)

    # Function to manage who is winning
    def display_scores(self):
        color_A = self.settings.WHITE
        color_B = self.settings.WHITE

        if self.powerup_active is not None:
            color_A = self.settings.RED
            color_B = self.settings.RED
        elif self.scoreA < self.scoreB:
            color_B = self.settings.GOLDEN
        elif self.scoreA > self.scoreB:
            color_A = self.settings.BLUE

        text_A = self.default_font.render(str(self.scoreA), False, color_A)
        text_B = self.default_font.render(str(self.scoreB), False, color_B)
        self.screen.blit(text_A, self.settings.POS_SCORE_A)
        self.screen.blit(text_B, self.settings.POS_SCORE_B)

    # Set and display static elements
    def set_static_elements(self, background_img, playerA_icon, playerB_icon):
        # Scale the background image
        background: any = pygame.transform.scale(background_img, [self.settings.width,
                                                                  self.settings.height])
        # Display background image
        self.screen.blit(background, (0, 0))
        # Player A icon
        self.screen.blit(playerA_icon, self.settings.PLAYER_A_ICON_POS)
        # Player B icon
        self.screen.blit(playerB_icon, self.settings.PLAYER_B_ICON_POS)
        # Field divider
        if self.powerup_active is not None:
            pygame.draw.line(self.screen, self.settings.RED, self.settings.FIELD_DIVIDER_INITIAL_POS,
                             self.settings.FIELD_DIVIDER_MAX_POS, 5)
        else:
            pygame.draw.line(self.screen, self.settings.WHITE, self.settings.FIELD_DIVIDER_INITIAL_POS,
                             self.settings.FIELD_DIVIDER_MAX_POS, 5)

    # Creates the ball
    def instance_new_ball(self):
        # Creates a new ball with width and height
        ball = Ball("img/icons/ball.png", self.settings.BALL_WIDTH, self.settings.BALL_HEIGHT, self.settings)
        # Sets the initial position of the ball
        ball.rect.x, ball.rect.y = (self.settings.INITIAL_POS_X, self.settings.INITIAL_POS_Y)
        return ball

    # Screen to play the game
    def play(self):
        # Create Player A paddle
        paddleA = Paddle(self.settings.BLUE, self.settings.PADDLE_WIDTH_A, self.settings.PADDLE_HEIGHT_A,
                         self.settings.PADDLE_ROUND_CORNERS_A)
        paddleA.rect.x, paddleA.rect.y = (self.settings.INITIAL_POS_X_A, self.settings.INITIAL_POS_Y_A)
        # Create Player B paddle
        paddleB = Paddle(self.settings.GOLDEN, self.settings.PADDLE_WIDTH_B, self.settings.PADDLE_HEIGHT_B,
                         self.settings.PADDLE_ROUND_CORNERS_B)
        paddleB.rect.x, paddleB.rect.y = (self.settings.INITIAL_POS_X_B, self.settings.INITIAL_POS_Y_B)

        # Call a function to create the ball
        ball = self.instance_new_ball()

        # Adds the paddles and the ball to the list of objects
        self.all_sprites_list.add(paddleA, paddleB, ball)

        # Load Background Image
        background_img_load = pygame.image.load("img/background/background_pong.jpg").convert()

        # Load and set Players Icons
        playerA_icon_load: pygame.image = pygame.image.load("img/icons/playerA_icon.png").convert_alpha()
        playerA_icon: any = pygame.transform.scale(playerA_icon_load, self.settings.PLAYER_ICON_SIZE)
        playerB_icon_load: pygame.image = pygame.image.load("img/icons/playerB_icon.png").convert_alpha()
        playerB_icon: any = pygame.transform.scale(playerB_icon_load, self.settings.PLAYER_ICON_SIZE)

        # Create a loop that carries on until the user exits the game
        carryOn: int = 1

        # -------- Main Program Loop -----------
        while carryOn:

            # --- Main event loop
            for event in pygame.event.get():

                # If user clicked close
                if event.type == pygame.QUIT:
                    # Close the window and quit
                    pygame.quit(), sys.exit()

                    # Or they used the keyboard
                elif event.type == pygame.KEYDOWN:
                    # Pressing the Escape Key will quit to the main menu
                    if event.key == pygame.K_ESCAPE:
                        # Quit the loop
                        carryOn = 0

                # Detects if a player hits a win score
                elif self.scoreA >= self.settings.WIN_SCORE or self.scoreB >= self.settings.WIN_SCORE:
                    # Quit the loop
                    carryOn = 0
                    # Calls the win screen
                    self.win_screen()

            # --- Game logic starts here

            # Set the title of the window/game
            if self.vanilla:
                pygame.display.set_caption(self.settings.GAME_TITLE_VANILLA)
            else:
                pygame.display.set_caption(self.settings.GAME_TITLE)

            # Built-in method to save user input on the keyboard
            keys = pygame.key.get_pressed()
            # Calls the function to move the paddles
            self.pressed_keys(keys, paddleA, paddleB)

            # Calls a function to display static elements on the screen
            self.set_static_elements(background_img_load, playerA_icon, playerB_icon)

            # Controls the ball movement
            self.all_sprites_list.update(move=self.triggered)

            # Detect collisions between the ball and the paddles and change its speed accordingly
            self.ball_owner = ball.handle_ball_collision(self.ball_owner, paddleA, paddleB)

            # Calls a function that Handles the ball motion in the screen
            self.scoreA, self.scoreB, self.ball_owner, self.triggered = ball.handle_ball_motion(self.scoreA,
                                                                                                self.scoreB,
                                                                                                self.ball_owner,
                                                                                                self.triggered)

            # Set all the game objects (sprites) to be drawn on the screen
            self.all_sprites_list.draw(self.screen)

            # Calls a function to display the score
            self.display_scores()

            # If is not vanilla mode, display the powerup
            if not self.vanilla:
                # Calls a function that sets a random powerup to be visible
                self.set_powerup_visible()
                # Calls a function to Handle the visible powerup
                self.handle_visible_powerup(ball, paddleA, paddleB)
                # Calls a function to Handle the active powerup
                self.handle_active_powerup(paddleA, paddleB)
                # Calls a function to handle multiple balls on the screen
                self.handle_multiple_balls(paddleA, paddleB)

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 60 frames per second
            self.clock.tick(60)

    # Screen when a player wins
    def win_screen(self):
        # Create a loop that carries on until the user exits the win screen
        win_screenON: int = 1
        # Set the winner
        winner: any = None
        # Set the winner score
        winner_score: int = 0

        # Set Background Image for Win Screen
        backgroundA_img_load: pygame.image = pygame.image.load("img/background/background_winA.jpg").convert()
        backgroundA_img: pygame.transform = pygame.transform.scale(backgroundA_img_load,
                                                                   (self.settings.width,
                                                                    self.settings.height))
        backgroundB_img_load: pygame.image = pygame.image.load("img/background/background_winB.jpg").convert()
        backgroundB_img: pygame.transform = pygame.transform.scale(backgroundB_img_load,
                                                                   (self.settings.width,
                                                                    self.settings.height))

        # Set Icons for each winner
        winnerA_icon_load: pygame.image = pygame.image.load("img/icons/winner_iconA.png").convert_alpha()
        winnerA_icon: pygame.transform = pygame.transform.scale(winnerA_icon_load, self.settings.WINNER_ICON_SIZE)
        winnerB_icon_load: pygame.image = pygame.image.load("img/icons/winner_iconB.png").convert_alpha()
        winnerB_icon: pygame.transform = pygame.transform.scale(winnerB_icon_load, self.settings.WINNER_ICON_SIZE)

        # -------- Main Program Loop -----------
        while win_screenON:

            # --- Main event loop
            for event in pygame.event.get():

                # If user clicked close
                if event.type == pygame.QUIT:
                    # Close the window and quit
                    pygame.quit(), sys.exit()

                # Or they used the keyboard
                if event.type == pygame.KEYDOWN:
                    # Pressing the Escape Key will quit to the main menu
                    if event.key == pygame.K_ESCAPE:
                        # Quit the loop
                        win_screenON = 0

            if self.scoreA > self.scoreB:
                winner = "Captain America"
                winner_score = self.scoreA
                self.screen.blit(backgroundA_img, (0, 0))
                self.screen.blit(winnerA_icon,
                                 (self.settings.width * 0.15, self.settings.height * 0.7))
            elif self.scoreA < self.scoreB:
                winner = 'Iron Man'
                winner_score = self.scoreB
                self.screen.blit(backgroundB_img, (0, 0))
                self.screen.blit(winnerB_icon,
                                 (self.settings.width * 0.3, self.settings.height * 0.7))

            winner_text = self.default_font.render(winner + " your team wins!", False, self.settings.WHITE)
            lastScore = self.powerup_font.render('Best Score: ' + str(winner_score), False, (255, 255, 255))
            self.screen.blit(lastScore, (700 / 2, 500 / 2))
            self.screen.blit(winner_text, (700 / 3, 500 / 3))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 30 frames per second
            self.clock.tick(30)
