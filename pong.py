# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball


WIN_SCORE = 5


def play_pong():
    # Initialize pygames
    pygame.init()
    triggered = False
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (37, 150, 190)
    MAGENTA = (204, 51, 139)
    # Open a new window
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The PongVerse")

    # LETS CREATE THE TWO PADDLES AND THE BALL, USING THE AFORE-CREATED CLASSES
    paddleA = Paddle(BLUE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200

    paddleB = Paddle(MAGENTA, 10, 100)
    paddleB.rect.x = 670
    paddleB.rect.y = 200

    # setting up the ball and its position

    ball = Ball(WHITE, 14, 14)
    ball.rect.x = 345
    ball.rect.y = 195

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

    def reset():
        ball.rect.x: int = 345
        ball.rect.y: int = 195

    def show_go_screen():
        screen.fill(BLUE)
        font = pygame.font.SysFont('comicsans', 25)  # creates a font object
        lastScore = font.render('Best Score: ' + str(scoreA), 1, (255, 255, 255))
        screen.blit(lastScore, (700 / 2, 500 / 2))
        pygame.display.flip()

    # Function to manage who is winning
    def display_scores(font, scoreA, scoreB):
        if scoreA > scoreB:
            text = font.render(str(scoreA), 1, BLUE)
            screen.blit(text, (250, 10))
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (429, 10))
        if scoreA < scoreB:
            text = font.render(str(scoreB), 1, MAGENTA)
            screen.blit(text, (429, 10))
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (250, 10))
        if scoreA == scoreB:
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (250, 10))
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (429, 10))

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        # User did something
        for event in pygame.event.get():

            # If user clicked close
            if event.type == pygame.QUIT:
                # Flag that we are done so we exit this loop
                carryOn = False

                # Or he used the key-board
            elif event.type == pygame.KEYDOWN:
                # Pressing the x Key will quit the game
                if event.key == pygame.K_x:
                    # quit the loop
                    carryOn = False
        # Moving the paddles when the user uses the keys
        keys = pygame.key.get_pressed()  # this built-in method saves the user input from the keyboard

        # moving the paddles when the user hits W/S (player A) or up down for player
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
            triggered = True
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
            triggered = True
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
            triggered = True
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)
            triggered = True

            # --- Game logic should go here
        all_sprites_list.update(move=triggered)

        # Checking if the ball was scored and changing speed accordingly
        if ball.rect.x >= 690:
            scoreA += 1
            reset()
            triggered = False
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreB += 1
            reset()
            triggered = False
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y >= 500:
            ball.bounce_up_down()
        if ball.rect.y <= 0:
            ball.bounce_up_down()

        # Detects if a player hits a win score
        if scoreA >= WIN_SCORE or scoreB >= WIN_SCORE:
            show_go_screen()
            break

        # Detect collisions between the ball and the paddles and change its speed accordingly(use the method we created)
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(BLACK)

        # Draw the net A WHITE LINE FROM TOP TO BOTTOM (USE PYGAME BUILT-IN METHOD)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Display scores:
        # Defines the font used
        font = pygame.font.Font(None, 74)
        # Calls display_scores function to manage colors according to who is winning
        display_scores(font, scoreA, scoreB)

        # USE PY-GAME BUILT IN METHODS,  SELECT THE POSITION THAT YOU PREFER

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Once we have exited the main program loop we can stop the game engine:
    input('Press any key to exit...')
    pygame.quit()

# TODO: the game starts with white paddle and colors change for the last one that scored
