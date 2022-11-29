import pygame
from abc import ABC, abstractmethod
from random import randint

#TODO: Implement an abstract class called PowerUp. This class will contain at least two
# abstract methods called affect_player_A and affect_player_B
BLACK = (0, 0, 0)
class PowerUp(pygame.sprite.Sprite):  # sprite-Simple base class for visible game objects

    def __init__(self,  width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])

    @abstractmethod
    def __init__(self, affect_player_A):
        self.affect_player_A= affect_player_A

    @abstractmethod
    def __int__(self, affect_player_B):
        self.affect_player_B= affect_player_B


    #TODO: set ball owner, but how??
    #TODO: Set timer for the powerups


#TODO: Implement the specific "Power-ups" as children of the mother class PowerUp.
#For the power ups, my idea is to set an interval of random numbers and set the powerups equal to some of these???
#TODO: Mandatory Power Ups

#Shrink/Enlarge: The Shrink/Enlarge "Power-up" reduces the size of the opponent’s
# racket or enlarges the size of the player’s racket for a certain amount of time
class Antman(PowerUp):

    """def __init__(self, position, velocity=(0, 0), width=POWERUP_SIZE, height=POWERUP_SIZE):
        super(Shrink, self).__init__(position, velocity, width, height)
        self.image = pygame.transform.scale(pygame.image.load(resources.get_sprite("shrink.png")).convert(),
                                            (width, height))

    def update(self, delta):
        pass

    def apply(self, state, ball):
        if ball.owner is not None:
            ball.owner.pad.position.y += ball.owner.pad.height * (1 - POWERUP_SHRINK_FACTOR) / 2
            ball.owner.pad.height *= POWERUP_SHRINK_FACTOR"""

    pass

#Freeze: The Freeze "Power-up" freezes the size of the player’s racket for a very
# small amount of time
class Freeze(PowerUp):
    pass

class Multipleballs(PowerUp):
    pass


#TODO: Optional Power ups

class Quicksilver(PowerUp):
    #increase paddle speed
    pass

class Doublescore(PowerUp):
    pass

class Shield(PowerUp):
    pass



#TODO: Implement different "looks" for different "Power-ups".

#TODO: Implement the appearance of a "Power-up" in the game based on a certain probability.


#TODO: Implement the necessary visual modifications so it is clear there is a "Power-up" in
# play and who is benefiting or suffering from it.
