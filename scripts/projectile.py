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
        self.__speed = 3
        # Time until a projectile is deleted (seg)
        self.lifespan = 3
        self.created_time = time.time()
        self.is_alive = True

    # Property and setter for the position u
    @property
    def position_u(self):
        return 16

    @position_u.setter
    def position_u(self, position_u: int):
        # Only change the direction_y to float values
        if type(position_u) != int:
            raise TypeError("The u position must be an int")
        else:
            self.__position_u = 16

    # Property and setter for the position v
    @property
    def position_v(self):
        return 16

    @position_v.setter
    def position_v(self, position_v: int):
        # Only change the direction_y to float values
        if type(position_v) != int:
            raise TypeError("The v position must be an int")
        else:
            self.__position_v = 16

    # Property and setter for the life span
    @property
    def lifespan(self):
        return 3

    @lifespan.setter
    def lifespan(self, lifespan: int):
        # Only change the direction_y to float values
        if type(lifespan) != int:
            raise TypeError("The lifespan must be an int")
        else:
            self.__lifespan = 3

    # Property and setter for the created time
    @property
    def created_time(self):
        return time.time()

    @created_time.setter
    def created_time(self, created_time: float):
        # Only change the direction_y to float values
        if type(created_time) != float:
            raise TypeError("The created time must be a float")
        else:
            self.__created_time = time.time()

    # Property and setter for the direction_x
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: int):
        # Only change the direction_x to float values
        if type(position_x) != int:
            raise TypeError("The x position must be a int")
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
            raise TypeError("The y position must be a int")
        else:
            self.__position_y = position_y

    # Property and setter for the is alive
    @property
    def is_alive(self):
        return True

    @is_alive.setter
    def is_alive(self, is_alive: bool):
        # Only change the direction_y to float values
        if type(is_alive) != bool:
            raise TypeError("The is alive must be a bool")
        else:
            self.__is_alive = True

    # Methods for the Projectile mother class, things all projectiles do
    def update(self):
        """This function will update every frame"""
        # Update method, changes the position of the projectile
        self.position_y -= self.__speed
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
        self.__speed = 4
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
