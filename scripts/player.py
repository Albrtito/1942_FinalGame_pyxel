import time
import pyxel
from projectileManager import ProjectileManager
from sprite import Sprite

player = None
HEIGHT = 128
WIDTH = 128
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16


# Class player inherits from sprite, this means all basic characteristics of sprites,
# are at first set to the general sprite

class Player:

    def __init__(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):

        # Position variables
        self.position_x = position_x
        self.position_y = position_y
        # The speed right now is constant but could be named as an attribute
        self.player_speed = 2
        # Draw variables of the player -> make something so this works with class sprite
        self.position_u = 0
        self.loop = False
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
        if not self.loop:
            # Calls a function that will move the player
            self.move()

            # code for the shooting of the player: If the time since the next shot is bigger than the time between shots
            # and the space key is pressed, shoot
            if time.time() > self.time_between_shots and pyxel.btn(pyxel.KEY_SPACE):
                self.time_between_shots = time.time() + self.rate_of_fire / 1000
                self.shoot()

    def draw(self):
        if pyxel.btnp(pyxel.KEY_Z):
            print("loop")
            self.loop = True
        if not self.loop:
            print("draw, move")
            self.player_animations()
        else:
            self.animate_loop()

        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, 0, PLAYER_WIDTH, PLAYER_HEIGHT,
                  colkey=8)
    # Methods for player class

    # Shoot method creates a player projectile in the projectileManager class
    def shoot(self):
        self.projectile_manager.create_projectile(self.position_x, self.position_y,"PlayerProjectile")

    # This function moves the player given an input in the keyboard keys
    def move(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.position_x != 0:
            self.position_x -= self.player_speed
        if pyxel.btn(pyxel.KEY_RIGHT) and self.position_x < WIDTH - PLAYER_WIDTH:
            self.position_x += self.player_speed
        if pyxel.btn(pyxel.KEY_DOWN) and self.position_y < HEIGHT - PLAYER_HEIGHT:
            self.position_y += self.player_speed
        if pyxel.btn(pyxel.KEY_UP) and self.position_y != 0:
            self.position_y -= self.player_speed

    # This functions changes the variables of self.position_u and self.position_v. This two variables determine which
    # sprite to show, so changing these variables we can change the sprite of the plane that is showing depending on
    # what the plane is doing
    def player_animations(self):
        # Update the helix movement every frame
        if self.position_u == 0:
            self.position_u = 16
        else:
            self.position_u = 0

    def animate_loop(self):

        if self.position_u < 80:
            print("done loop")
            if self.position_u == 32:
                self.position_y -= 1
            if self.position_u == 48:
                self.position_y += 0
            if self.position_u == 64:
                self.position_y += 1
                self.position_u += 16
            if self.position_u == 80:
                self.position_y -= 1
            self.position_u += 16
            time.sleep(.5)
        else:
            self.loop = False




