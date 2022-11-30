import time
import pyxel
from projectileManager import ProjectileManager


player = None
HEIGHT = 160
WIDTH = 120
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16


class Player:

    def __init__(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):
        # Position variables
        self.position_x = position_x
        self.position_y = position_y
        # The speed right now is constant but could be named as an attribute
        self.player_speed = 2
        # self.player_projectiles = []
        # The player can shoot every some ms(rate of fire)
        # The time_between_shots is a timer in order to shoot every rate of fire(ms)
        self.rate_of_fire = 500
        self.time_between_shots = 0
        # The projectile manager for the shots fired by the player
        self.projectile_manager = projectile_manager
    # Property and setter for position_x
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: int):
        # Only change the position_x to float values
        if type(position_x) != int:
            raise TypeError("The position must be an int")
        else:
            self.__position_x = position_x

    # Property and setter for position_y
    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y: int):
        # Only change the position_y to float values
        if type(position_y) != int:
            raise TypeError("The position must be an int")
        else:
            self.__position_y = position_y

    def update(self):
        # Calls a function that will move the player
        self.move(self.position_x, self.position_y)

        # code for the shooting of the player: If the time since the next shot is bigger than the time between shots
        # and the space key is pressed, shoot
        if time.time() > self.time_between_shots and pyxel.btn(pyxel.KEY_SPACE):
            self.time_between_shots = time.time() + self.rate_of_fire / 1000
            self.shoot()

    def draw(self):
        pyxel.blt(self.position_x, self.position_y, 0, 0, 0, PLAYER_WIDTH, PLAYER_HEIGHT, colkey=8)

    # Methods for player class

    # Shoot method creates a player projectile in the projectileManager class
    def shoot(self):
        self.projectile_manager.create_projectile(self.position_x, self.position_y, self.player_speed, "PlayerProjectile")

    # This function moves the player given an input in the keyboard keys
    def move(self, position_x, position_y):
        if pyxel.btn(pyxel.KEY_LEFT) and self.position_x != 0:
            self.position_x -= self.player_speed
        if pyxel.btn(pyxel.KEY_RIGHT) and self.position_x < WIDTH - PLAYER_WIDTH:
            self.position_x += self.player_speed
        if pyxel.btn(pyxel.KEY_DOWN) and self.position_y < HEIGHT - PLAYER_HEIGHT:
            self.position_y += self.player_speed
        if pyxel.btn(pyxel.KEY_UP) and self.position_y != 0:
            self.position_y -= self.player_speed
