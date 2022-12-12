# Import the pygame library and initialise the game engine
from random import choices
from .paddle import Paddle
from .ball import Ball
from .powerups import *


class PongVerse:
    def __init__(self, vanilla):
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
        self.screen = pygame.display.set_mode(InterfaceSettings.WINDOW_SIZE)
        # Create a clock that controls FPS
        self.clock = pygame.time.Clock()
        # Set the Default Font
        self.default_font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT, GameSettings.FONT_SIZE_DEFAULT)
        # Set the PowerUp Font
        self.powerup_font = pygame.font.Font(GameSettings.FONT_TYPE_DEFAULT, GameSettings.FONT_SIZE_POWERUP)
        # Set scores to 0
        self.scoreA: int = 0
        self.scoreB: int = 0
        # Set trigger for the ball to be reset
        self.triggered: bool = False

    # Set what keys are used to move the paddles
    def pressed_keys(self, keys, paddleA, paddleB):
        # Move the paddles when the user hits W/S (player A) or up/down (player B)
        if keys[pygame.K_w]:
            paddleA.moveUp(PaddleSettings.PADDLE_SPEED_A)
            self.triggered = True
        if keys[pygame.K_s]:
            paddleA.moveDown(PaddleSettings.PADDLE_SPEED_A, InterfaceSettings.WINDOW_HEIGHT)
            self.triggered = True
        if keys[pygame.K_UP]:
            paddleB.moveUp(PaddleSettings.PADDLE_SPEED_B)
            self.triggered = True
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(PaddleSettings.PADDLE_SPEED_B, InterfaceSettings.WINDOW_HEIGHT)
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
                powerup = chosen_powerup(self.ball_owner, PowerUpSettings.POWERUP_WIDTH, PowerUpSettings.POWERUP_HEIGHT)
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
                    # Set the powerup owner
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
            if int(activated) < PowerUpSettings.POWERUP_NAME_VISIBLE_TIME:
                # Displays the powerup active name
                display_powerup_name = self.powerup_font.render(str(self.powerup_active.name), True, GameSettings.RED)
                # Gets the rectangle of the powerup name
                display_powerup_name_rect = display_powerup_name.get_rect()
                self.screen.blit(display_powerup_name, (
                    InterfaceSettings.WINDOW_WIDTH / 2 - display_powerup_name_rect.center[0],
                    InterfaceSettings.WINDOW_HEIGHT * 0.85))
            # It checks if the active time is over
            if int(activated) == self.powerup_active.active_time:
                # If it is over, it sets the powerup to be inactive
                self.set_powerup_inactive(paddleA, paddleB)

    # Handles the additional balls
    def handle_multiple_balls(self, paddleA, paddleB):
        if self.powerup_active is not None and self.powerup_active.name == MultipleBalls.name:
            self.triggered = True  # avoid triggering and stopping the screen if a ball scores
            if len(self.additional_balls) == 0:
                ball_count = randint(BallSettings.MIN_ADDITIONAL_BALLS, BallSettings.MAX_ADDITIONAL_BALLS)
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
        color_A = GameSettings.WHITE
        color_B = GameSettings.WHITE

        if self.scoreA > self.scoreB:
            color_A = GameSettings.BLUE
        elif self.scoreA < self.scoreB:
            color_B = GameSettings.GOLDEN

        text_A = self.default_font.render(str(self.scoreA), True, color_A)
        text_B = self.default_font.render(str(self.scoreB), True, color_B)
        self.screen.blit(text_A, GameSettings.POS_SCORE_A)
        self.screen.blit(text_B, GameSettings.POS_SCORE_B)

    # Set and display static elements
    def set_static_elements(self):
        # background image
        self.screen.blit(GameSettings.BACKGROUND_IMG, (0, 0))
        # Player A icon
        self.screen.blit(GameSettings.PLAYER_A_ICON, GameSettings.PLAYER_A_ICON_POS)
        # Player B icon
        self.screen.blit(GameSettings.PLAYER_B_ICON, GameSettings.PLAYER_B_ICON_POS)
        # Field divider
        pygame.draw.line(self.screen, GameSettings.WHITE, GameSettings.FIELD_DIVIDER_INITIAL_POS,
                         GameSettings.FIELD_DIVIDER_MAX_POS, 5)

    # Creates the ball
    @staticmethod
    def instance_new_ball():
        # Creates a new ball with width and height
        ball = Ball("img/icons/ball.png", BallSettings.BALL_WIDTH, BallSettings.BALL_HEIGHT)
        # Sets the initial position of the ball
        ball.rect.x, ball.rect.y = (BallSettings.INITIAL_POS_X, BallSettings.INITIAL_POS_Y)
        return ball

    def instructions(self):
        # Create a loop that carries on until the user exits the win screen
        instructionsON: bool = True
        while instructionsON:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    instructionsON = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        instructionsON = False
                        self.play()
                    if event.key == pygame.K_ESCAPE:
                        instructionsON = False

            # Set the title of the window/game
            if self.vanilla:
                pygame.display.set_caption(InstructionsSettings.INSTRUCTIONS_TITLE_VANILLA)
            else:
                pygame.display.set_caption(InstructionsSettings.INSTRUCTIONS_TITLE)

            self.screen.blit(InstructionsSettings.BACKGROUND_IMG, (0, 0))
            instructions = self.default_font.render("Press SPACE to start the game", True, GameSettings.WHITE)
            instructions_rect = instructions.get_rect()
            self.screen.blit(instructions, (InterfaceSettings.WINDOW_WIDTH / 2 - instructions_rect.center[0],
                                            InterfaceSettings.WINDOW_HEIGHT * 0.85))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 60 frames per second
            self.clock.tick(60)

    # Screen when a player wins
    def win_screen(self):
        # Create a loop that carries on until the user exits the win screen
        win_screenON: bool = True
        # Set the winner
        winner: any = None
        # Set the winner score
        winner_score: int = 0

        # -------- Main Program Loop -----------
        while win_screenON:

            # --- Main event loop
            for event in pygame.event.get():

                # If user clicked close
                if event.type == pygame.QUIT:
                    # Flag that we are done so we exit this loop
                    win_screenON = False
                    # Close the window and quit
                    pygame.quit()

                # Or they used the keyboard
                if event.type == pygame.KEYDOWN:
                    # Pressing the Escape Key will quit to the main menu
                    if event.key == pygame.K_ESCAPE:
                        # Quit the loop
                        win_screenON = False

            if self.scoreA > self.scoreB:
                winner = "Captain America"
                winner_score = self.scoreA
                self.screen.blit(GameSettings.WIN_SCREEN_A_IMG, (0, 0))
                self.screen.blit(GameSettings.WINNER_ICON_A,
                                 (InterfaceSettings.WINDOW_WIDTH * 0.15, InterfaceSettings.WINDOW_HEIGHT * 0.7))
            elif self.scoreA < self.scoreB:
                winner = 'Iron Man'
                winner_score = self.scoreB
                self.screen.blit(GameSettings.WIN_SCREEN_B_IMG, (0, 0))
                self.screen.blit(GameSettings.WINNER_ICON_B,
                                 (InterfaceSettings.WINDOW_WIDTH * 0.3, InterfaceSettings.WINDOW_HEIGHT * 0.7))

            winner_text = self.default_font.render(winner + " your team wins!", True, GameSettings.WHITE)
            lastScore = self.powerup_font.render('Best Score: ' + str(winner_score), True, (255, 255, 255))
            self.screen.blit(lastScore, (700 / 2, 500 / 2))
            self.screen.blit(winner_text, (700 / 3, 500 / 3))

            # --- Update the screen with what was drawn
            pygame.display.update()

            # --- Limit the game to 60 frames per second
            self.clock.tick(60)

    def play(self):

        # Create Player A paddle
        paddleA = Paddle(GameSettings.BLUE, PaddleSettings.PADDLE_WIDTH_A, PaddleSettings.PADDLE_HEIGHT_A,
                         PaddleSettings.PADDLE_ROUND_CORNERS_A)
        paddleA.rect.x, paddleA.rect.y = (PaddleSettings.INITIAL_POS_X_A, PaddleSettings.INITIAL_POS_Y_A)
        # Create Player B paddle
        paddleB = Paddle(GameSettings.GOLDEN, PaddleSettings.PADDLE_WIDTH_B, PaddleSettings.PADDLE_HEIGHT_B,
                         PaddleSettings.PADDLE_ROUND_CORNERS_B)
        paddleB.rect.x, paddleB.rect.y = (PaddleSettings.INITIAL_POS_X_B, PaddleSettings.INITIAL_POS_Y_B)

        # Call a function to create the ball
        ball = self.instance_new_ball()

        # Adds the paddles and the ball to the list of objects
        self.all_sprites_list.add(paddleA, paddleB, ball)

        # Create a loop that carries on until the user exits the game
        carryOn: bool = True

        # -------- Main Program Loop -----------
        while carryOn:

            # --- Main event loop
            for event in pygame.event.get():

                # If user clicked close
                if event.type == pygame.QUIT:
                    # Flag that we are done so we exit this loop
                    carryOn = False
                    # Close the window and quit
                    pygame.quit()

                    # Or they used the keyboard
                elif event.type == pygame.KEYDOWN:
                    # Pressing the Escape Key will quit to the main menu
                    if event.key == pygame.K_ESCAPE:
                        # Quit the loop
                        carryOn = False

                # Detects if a player hits a win score
                elif self.scoreA >= GameSettings.WIN_SCORE or self.scoreB >= GameSettings.WIN_SCORE:
                    # Quit the loop
                    carryOn = False
                    # Calls the win screen
                    self.win_screen()

            # --- Game logic starts here

            # Set the title of the window/game
            if self.vanilla:
                pygame.display.set_caption(GameSettings.GAME_TITLE_VANILLA)
            else:
                pygame.display.set_caption(GameSettings.GAME_TITLE)

            # Built-in method to save user input on the keyboard
            keys = pygame.key.get_pressed()
            # Calls the function to move the paddles
            self.pressed_keys(keys, paddleA, paddleB)

            # Calls a function to display static elements on the screen
            self.set_static_elements()

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

# TODO: Solve problem with ball owner
