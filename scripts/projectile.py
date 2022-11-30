import time
import pyxel


# Mother class for all projectiles,both the enemy`s and the player`s
class Projectile:
    def __init__(self, position_x: int, position_y: int, speed: int):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        # Time until a projectile is deleted (seg)
        self.lifespan = 3
        self.created_time = time.time()
        self.is_alive = True

    # Property and setter for the direction_x
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: int):
        # Only change the direction_x to float values
        if type(position_x) != int:
            raise TypeError("The position must be a int")
        else:
            self.__position_x = position_x

    # Property and setter for the direction_y
    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y: int):
        # Only change the direction_y to float values
        if type(position_y) != int:
            raise TypeError("The position must be a int")
        else:
            self.__position_y = position_y

    # Property and setter for the speed
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        # Only change the direction_y to float values
        if type(speed) != int:
            raise TypeError("The speed must be a int")
        else:
            self.__speed = speed

    # This is a read only property
    @property
    def in_screen(self):
        return self.__in_screen

    # Methods for the Projectile mother class, things all projectiles do
    def update(self):
        # Update method, changes the position of the projectile
        self.position_y -= self.speed
        # Check if the projectile needs to be deleted
        self.is_alive = self.check_delete(self.lifespan,self.created_time)

    def draw(self):
        # The position at wich a projectile has to be deleted will
        # vary when we are creating a movement in the background
        if self.position_y >= -10:
            pyxel.blt(self.position_x, self.position_y, 0, 0, 16, 16, 16, colkey=8)

    def check_delete(self,lifespan,created_time):
        if (created_time + lifespan) <= time.time():
            return False
        else:
            return True

# Child classes of clss Projectile, difference is only in the sprite
class PlayerProjectile(Projectile):
    ...


class EnemyProjectile(Projectile):
   ...
