import time
import pyxel


# Mother class for all projectiles,both the enemy`s and the player`s
class Projectile:
    def __init__(self, position_x: float, position_y: float, speed: float):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed



    # Property and setter for the direction_x
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: float):
        # Only change the direction_x to float values
        if type(position_x) != float:
            raise TypeError("The position must be a float")
        else:
            self.__position_x = position_x

    # Property and setter for the direction_y
    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y: float):
        # Only change the direction_y to float values
        if type(position_y) != float:
            raise TypeError("The position must be a float")
        else:
            self.__position_y = position_y

    # Property and setter for the speed
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        # Only change the direction_y to float values
        if type(speed) != float:
            raise TypeError("The speed must be a float")
        else:
            self.__speed = speed

    # Methods for the Projectile mother class, things all projectiles do
    def update(self):
        # The position at wich a projectile has to be deleted will
        # vary when we are creating a movement in the background
        if self.position_y >= -10:
                self.position_y -= self.speed


    def draw(self):
        # The position at wich a projectile has to be deleted will
        # vary when we are creating a movement in the background
        if self.position_y >= -10:
            pyxel.blt(self.position_x, self.position_y, 0, 0, 16, 16, 16, colkey=0)



# Child classes of clss Projectile, difference is only in the sprite
class PlayerProjectile(Projectile):
    def __init__(self, position_x: float, position_y: float, speed: float):
        super().__init__(self, position_x, position_y, speed)
        ...


class EnemyProjectile(Projectile):
    def __int__(self, direction_x: int, direction_y: int):
        super().__init__(self, direction_x, direction_y)
