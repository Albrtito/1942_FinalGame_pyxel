import time
import pyxel
import constants


# Mother class for all projectiles,both the enemy`s and the player`s
class Projectile:
    def __init__(self, position_x: int, position_y: int):
        # Sprite related variables of the projectile
        self.position_u = 0
        self.position_v = 16
        self.width = constants.normal_sprite_width
        self.height = constants.normal_sprite_height
        # Basic variables for projectile
        self.position_x = position_x
        self.position_y = position_y
        # Basic speed for all projectiles, can change for player and enemy projectiles
        self.speed = 3
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

    # This setter is only for the case that the speed changes in player and enemies projectiles
    @speed.setter
    def speed(self, speed: int):
        # Only change the direction_y to float values
        if type(speed) != int:
            raise TypeError("The speed must be a int")
        else:
            self.__speed = speed

    # Methods for the Projectile mother class, things all projectiles do
    def update(self):
        """This function will update every frame"""
        # Update method, changes the position of the projectile
        self.position_y -= self.speed
        # Check if the projectile needs to be deleted
        self.is_alive = self.check_delete(self.lifespan, self.created_time)

    def draw(self):
        """This function draws the projectiles"""
        # The position at which a projectile has to be deleted will
        # vary when we are creating a movement in the background
        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, self.position_v,
                  self.width, self.height, colkey=0)

    def check_delete(self, lifespan, created_time):
        """This functions checks that the projectiles are still alive"""
        if (created_time + lifespan) <= time.time():
            return False
        else:
            return True


# Child classes of class Projectile, difference is only in the sprite
class PlayerProjectile(Projectile):
    def __init__(self, position_x: int, position_y: int):
        super(PlayerProjectile, self).__init__(position_x, position_y)
        self.speed = 4
        # The sprite variables from projectile are the basic for playerProjectile


class EnemyProjectile(Projectile):
    def __init__(self, position_x: int, position_y: int, speed_y: int, speed_x=0):
        super(EnemyProjectile, self).__init__(position_x, position_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        # We offset the position of the draw method by 4 on the x-axis so its centered when drawn
        self.position_x = position_x + 4
        # We change sprite variables of projectile so that it shows the enemy projectile instead of the player
        # and the hitbox is not as big
        self.position_u = 16
        self.width = 8
        self.height = 8

    def update(self):
        """This function will update every frame"""
        self.position_x += self.speed_x
        self.position_y += self.speed_y
