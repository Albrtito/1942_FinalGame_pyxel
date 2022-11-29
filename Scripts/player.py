import time
import pyxel
from projectile import Projectile
from projectile import PlayerProjectile

player = None
HEIGHT = 128
WIDTH = 128
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16
class Player:

    def __init__(self, position_x= 0, position_y= 0):
        self.position_x = position_x
        self.position_y = position_y
        self.player_projectiles = []
        # The player can shoot every some ms
        self.rate_of_fire = 500
        self.next_shot_time = 0
    # Property and setter for position_x
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: float):
        # Only change the position_x to float values
        if type(position_x) != float:
            raise TypeError("The position must be a float")
        else:
            self.__position_x = position_x
    # Property and setter for position_y
    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y: float):
        # Only change the position_y to float values
        if type(position_y) != float:
            raise TypeError("The position must be a float")
        else:
            self.__position_y = position_y
    def update(self):
        # code for the movement of the player
        if pyxel.btn(pyxel.KEY_LEFT) and self.position_x != 0:
            self.position_x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.position_x < WIDTH-PLAYER_WIDTH:
            self.position_x += 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.position_y < HEIGHT-PLAYER_HEIGHT:
            self.position_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.position_y != 0:
            self.position_y -= 1

        # code for the shooting of the player
        if time.time() > self.next_shot_time and pyxel.btn(pyxel.KEY_SPACE):
            self.next_shot_time = time.time() + self.rate_of_fire / 1000
            self.player_projectiles.append(self.create_projectile())

        if len(self.player_projectiles) != 0:
            for projectile in self.player_projectiles:
                projectile.update()
    def draw(self):
        pyxel.blt(self.position_x, self.position_y, 0, 24, 0, PLAYER_WIDTH, PLAYER_HEIGHT, colkey=0)
        if len(self.player_projectiles) != 0:
            for projectile in self.player_projectiles:
                projectile.draw()
    # Methods for player class
    def create_projectile(self):
        return Projectile(self.position_x,self.position_y,5.0)