# Import the pygame library and initialise the game engine
import pygame
from .constants import *
from random import choices
from .paddle import Paddle
from .ball import Ball
from .powerups import *

# Sets if a powerup is active
powerup_active: any = None
# Sets the time when the powerup was activated
powerup_active_time: any = None


def play_pong():
    # Initialize pygames
    pygame.init()
    pygame.display.set_icon(GameSettings.GAME_ICON)
    triggered = False
    ball_owner = None

    # Opens a new window
    screen = pygame.display.set_mode(GameSettings.WINDOW_SIZE)
    # Set the title of the window/game
    pygame.display.set_caption(GameSettings.GAME_TITLE)

    # LET'S CREATE THE TWO PADDLES AND THE BALL, USING THE BEFORE-CREATED CLASSES
    paddleA = Paddle(GameSettings.BLUE, PaddleSettings.PADDLE_WIDTH_A, PaddleSettings.PADDLE_HEIGHT_A)
    paddleA.rect.x, paddleA.rect.y = (PaddleSettings.INITIAL_POS_X_A, PaddleSettings.INITIAL_POS_Y_A)

    paddleB = Paddle(GameSettings.MAGENTA, PaddleSettings.PADDLE_WIDTH_B, PaddleSettings.PADDLE_HEIGHT_B)
    paddleB.rect.x, paddleB.rect.y = (PaddleSettings.INITIAL_POS_X_B, PaddleSettings.INITIAL_POS_Y_B)

    # setting up the ball and its initial position
    ball = Ball("img/ball.png", BallSettings.BALL_WIDTH, BallSettings.BALL_HEIGHT)
    ball.rect.x, ball.rect.y = (BallSettings.INITIAL_POS_X, BallSettings.INITIAL_POS_Y)

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    # Add the 2 paddles and the ball to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)
    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # Initialise player scores
    scoreA = 0
    scoreB = 0

    # Define when a PowerUp appears
    # It appears every 3 goals
    def powerup_visible():
        # Gets the global variables
        global powerup_active
        global powerup_active_time
        # Gets the powerup probability
        PowerUps_Probabilities = [val.probability for val in PowerUps.values()]

        # It checks if the sum of the scores is divisible by 3
        if (scoreA + scoreB) % 3 == 0 and (scoreA + scoreB) != 0:
            # It chooses the first chosen random powerup
            chosen_powerup = choices(PowerUps, PowerUps_Probabilities)[0]
            # It creates the powerup
            powerup = ShrinkEnlarge(ball_owner, GameSettings.POWERUP_WIDTH, GameSettings.POWERUP_HEIGHT)
            # It adds the powerup to the list of objects
            all_sprites_list.add(powerup)
            powerup_active = powerup
            # It sets the powerup timer
            powerup_active_time = pygame.time.get_ticks()
        return powerup_active, powerup_active_time

    def powerup_invisible():
        # Gets the global variables
        global powerup_active
        global powerup_active_time

        # It checks if the powerup is active
        visible = (pygame.time.get_ticks() - powerup_active_time) / 1000
        if int(visible) == powerup_active.visible_time:
            powerup_active.kill()
            powerup_active = None
            powerup_active_time = None

    # Resets Ball position
    def reset_ball():
        # Initial position of the ball
        ball.rect.x, ball.rect.y = (BallSettings.INITIAL_POS_X, BallSettings.INITIAL_POS_Y)

    def show_go_screen():
        screen.fill(GameSettings.BLUE)
        font = pygame.font.SysFont('comicsans', 25)  # creates a font object
        lastScore = font.render('Best Score: ' + str(scoreA), True, (255, 255, 255))
        screen.blit(lastScore, (700 / 2, 500 / 2))
        pygame.display.flip()

    # Function to manage who is winning
    def display_scores(font_Score, score_A, score_B):
        color_A = GameSettings.WHITE
        color_B = GameSettings.WHITE

        if score_A > score_B:
            color_A = GameSettings.BLUE
        elif score_A < score_B:
            color_B = GameSettings.MAGENTA

        text_A = font_Score.render(str(score_A), 1, color_A)
        text_B = font_Score.render(str(score_B), 1, color_B)
        screen.blit(text_A, GameSettings.POS_SCORE_A)
        screen.blit(text_B, GameSettings.POS_SCORE_B)

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        # User did something
        for event in pygame.event.get():

            # If user clicked close
            if event.type == pygame.QUIT:
                # Flag that we are done so we exit this loop
                carryOn = False

                # Or he used the keyboard
            elif event.type == pygame.KEYDOWN:
                # Pressing the x Key will quit the game
                if event.key == pygame.K_x:
                    # quit the loop
                    carryOn = False
        # Moving the paddles when the user uses the keys
        keys = pygame.key.get_pressed()  # this built-in method saves the user input from the keyboard

        # moving the paddles when the user hits W/S (player A) or up/down (player B)
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
            triggered = True
        if keys[pygame.K_s]:
            paddleA.moveDown(5, GameSettings.WINDOW_HEIGHT, PaddleSettings.PADDLE_HEIGHT_A)
            triggered = True
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
            triggered = True
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5, GameSettings.WINDOW_HEIGHT, PaddleSettings.PADDLE_WIDTH_B)
            triggered = True

            # --- Game logic should go here
        all_sprites_list.update(move=triggered)

        # Checking if the ball was scored and changing speed accordingly
        if ball.rect.x >= GameSettings.WINDOW_WIDTH + BallSettings.BALL_WIDTH:
            scoreA += 1
            reset_ball()
            ball_owner = None
            triggered = False
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0 - BallSettings.BALL_WIDTH:
            scoreB += 1
            reset_ball()
            ball_owner = None
            triggered = False
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y >= GameSettings.WINDOW_HEIGHT - BallSettings.BALL_HEIGHT:
            ball.bounce_up_down()
        if ball.rect.y <= 0:
            ball.bounce_up_down()

        # Detects if a player hits a win score
        if scoreA >= GameSettings.WIN_SCORE or scoreB >= GameSettings.WIN_SCORE:
            show_go_screen()
            break

        # Detect collisions between the ball and the paddles and change its speed accordingly(use the method we created)
        if pygame.sprite.collide_mask(ball, paddleA):
            ball_owner = paddleA
            ball.bounce()
        if pygame.sprite.collide_mask(ball, paddleB):
            ball_owner = paddleB
            ball.bounce()
        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(BLACK)

        # Draw the net A WHITE LINE FROM TOP TO BOTTOM (USE PYGAME BUILT-IN METHOD)
        pygame.draw.line(screen, GameSettings.WHITE, [GameSettings.WINDOW_WIDTH / 2, 0],
                         [GameSettings.WINDOW_WIDTH / 2, GameSettings.WINDOW_HEIGHT], 5)
        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Display scores:
        # Defines the font used
        font = pygame.font.Font(None, GameSettings.FONT_SIZE)
        # Calls display_scores function to manage colors according to who is winning
        display_scores(font, scoreA, scoreB)

        # Checks if a powerup is invisible
        if powerup_active is None:
            # Sets a random powerup to be visible
            powerup_visible()

        # Checks if a powerup is visible
        if powerup_active_time is not None:
            # If it is visible, it checks if it collides with the ball
            if pygame.sprite.collide_mask(ball, powerup_active) and ball_owner is not None:
                # It activates the powerup
                powerup_active.run_powerup(paddleA, paddleB, ball)
                # It kills the activated powerup
                powerup_active.kill()
            # Sets the powerup to be invisible
            powerup_invisible()

        # USE PY-GAME BUILT IN METHODS,  SELECT THE POSITION THAT YOU PREFER

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

# TODO: the game starts with white paddle and colors change for the last one that scored
