import random
import time

import pyxel
from sprite import Sprite
from projectile import EnemyProjectile


# Enemy parent class.Contains all common attributes for all enemies
class Enemy(Sprite):
    # Declaration of the Enemy init method with all the attributes from the class

    def __int__(self, position_x: float, position_y: float, projectile: EnemyProjectile):
        self.position_x = position_x
        self.position_y = position_y
        self.projectile = projectile

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

    # Property and setter for projectile
    @property
    def projectile(self):
        return self.__projectile

    @projectile.setter
    def projectile(self, projectile: EnemyProjectile):
        if type(projectile) != EnemyProjectile:
            raise TypeError("Projectile must be an object of class EnemyProjectile")
        else:
            self.__projectile = projectile

    # Basic methods for the enemy class:

    # Update method -> Has to be called every frame -> Is update method inside a class used as the move method??

    # Enemy inherits from Sprite, so we can draw it using all the attributes of sprite
    def draw(self):
        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, self.position_v, self.width, self.height,
                  colkey=self.transparent)


# Enemy child classes. Each will contain a sprite specific for each class.
class RegularEnemy(Enemy):
    def __int__(self, position_x: float, position_y: float,projectile:EnemyProjectile,acceleration = 3,):
        self.acceleration = acceleration
        super().__init__(position_x, position_y, projectile)

    def update(self):
        self.position_x = self.acceleration * time
        self.position_y = self.acceleration * time


class RedEnemy(Enemy):
    def __int__(self, position_x: float, position_y: float, projectile: EnemyProjectile):
        super().__init__(position_x, position_y, projectile)


class Bombardier(Enemy):
    def __int__(self, position_x: float, position_y: float, projectile: EnemyProjectile):
        super().__init__(position_x, position_y, projectile)

    def draw(self):
        pyxel.blt(30, 10, 0, 73, 3, 14, 11, colkey=0)


class SuperBombardier(Enemy):
    def __int__(self, position_x: float, position_y: float, projectile: EnemyProjectile):
        super().__init__(position_x, position_y, projectile)

    def draw(self):
        pyxel.blt(10, 10, 0, 89, 0, 14, 16, colkey=0)
