import random
import math

"""Comentarios de Alberto que esta haciendo el detector de colisiones: 
+ Los enemigos necesitan tener una variable 
booleana llamada is_alive, esta variable es True hasta q mueran y entonces es false 
+ Cuando is_alive es False el 
enemyManager deberá de eliminar a ese enemigo de la lista de enemigos, prefeiblemente en el mismo loop q usa para 
actualizar,(comprueba q este vivo y actualiza, sino no actualice) 

"""
import time
import pyxel
from projectileManager import ProjectileManager
import constants


# Enemy parent class.Contains all common attributes for all enemies
class Enemy:
    # Declaration of the Enemy init method with all the attributes from the class

    def __init__(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):
        # Basic variables of enemy
        self.position_x = position_x
        self.position_y = position_y
        self.width = constants.normal_sprite_width
        self.height = constants.normal_sprite_height
        # Other variables
        self.projectile_manager = projectile_manager
        # In game important variables of each enemy
        self.is_alive = True
        self.lives = 1

        @property
        def lives(self):
            return 1

        @lives.setter
        def lives(self, lives: int):
            # Only change the position_x to float values
            if type(lives) != int:
                raise TypeError("The lives must be an int")
            else:
                self.__lives = 1
        @property
        def is_alive(self):
            return True
        @is_alive.setter
        def is_alive(self, is_alive: bool):
            # Only change the position_x to float values
            if type(is_alive) != bool:
                raise TypeError("The is alive must be a bool")
            else:
                self.__is_alive = True
    # Property for height and width
        @property
        def height(self):
            return self.__height
        @property
        def width(self):
            return self.__width
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

        # Property and setter for projectile

        @property
        def projectile_manager(self):
            return self.__projectile_manager

        @projectile_manager.setter
        def projectile(self, projectile_manager: ProjectileManager):
            if type(projectile_manager) != ProjectileManager:
                raise TypeError("Projectile manager must be an object of class ProjectileManager")
            self.__projectile_manager = projectile_manager

    # Check if the enemy should be deleted (die)
    def check_delete(self):
        if self.lives <= 0:
            self.is_alive = False
        else:
            self.is_alive = True


# Enemy child classes. Each will contain a sprite specific for each class.
class RegularEnemy(Enemy):
    def __init__(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):
        super().__init__(position_x, position_y, projectile_manager)
        self.position_u = 0
        self.position_v = 32
        self.height = 16
        self.width = 16
        self.transparent_color = 4
        self.change_sprite = 1
        self.change_sprite_2 = 0
        self.direction = 1

    def update(self):
        """This function will update every frame"""
        # Check if the enemy has to be deleted -> All enemy update methods need to have this:
        self.check_delete()
        # Si se acerca al extremo del mapa cambia su direccion
        if self.position_x >= 120:
            self.direction = -1
            self.change_sprite = 1
            self.change_sprite_2 = 0
        elif self.position_x <= 0:
            self.direction = 1
            self.change_sprite = 1
            self.change_sprite_2 = 0
        self.position_x += self.direction
        # Whe take a formula m(x-64)**2 + n=Y making a parabola with centre in x=64 if we make a full parabola
        # whe can adjust m for the width and 64 for the centre
        self.position_y = int(self.position_x * (2 - self.position_x / 64))

    def draw(self):
        """This function draws and animates the regular enemy"""
        # We have two states when doing a loop it will change according to the parabola
        # When not in loop it will alternate between both sprites of the plane moving the helices
        # Animate off the loop
        if self.position_y < 45:
            if self.change_sprite_2 == 0:
                if self.change_sprite % 2 == 0:
                    self.position_u = 0
                    self.change_sprite += 1
                else:
                    self.position_u = 16
                    self.change_sprite += 1
            elif self.change_sprite == 0:
                if self.change_sprite % 2 == 0:
                    self.position_u = 32
                    self.change_sprite += 1
                else:
                    self.position_u = 48
                    self.change_sprite += 1
        # Animate on the loop
        if 62 > self.position_y >= 58 and self.change_sprite_2 == 0:
            self.position_u = 64
            self.change_sprite_2 = 1
        elif self.position_y >= 62:
            self.position_u = 80
        elif 62 > self.position_y >= 58 and self.change_sprite_2 == 1:
            self.position_u = 96
            self.change_sprite = 0
            # Draw the plane
        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, self.position_v, self.width, self.height,
                  self.transparent_color)


class RedEnemy(Enemy):
    def __init__(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):
        super().__init__(position_x, position_y, projectile_manager)
        self.position_u = 0
        self.position_v = 48
        self.height = 16
        self.width = 16
        self.transparent_color = 11
        self.change_sprite = 0
        self.change_sprite_2 = 0
        self.direction = 1

    def update(self):
        """This function will update every frame"""
        # This if the way the Regular enemies will shoot creating a projectile at a random time
        if pyxel.frame_count % random.randint(100, 200) == 0:
            self.projectile_manager.create_projectile(self.position_x, self.position_y, "EnemyProjectile")
        # Check if the enemy has to be deleted -> All enemy update methods need to have this:
        self.check_delete()
        # Si se acerca al extremo del mapa cambia su direccion
        if self.position_y >= 120:
            self.direction = -1
            self.change_sprite = 0
            self.change_sprite_2 = 1
        elif self.position_y <= 0:
            self.direction = 1
            self.change_sprite = 0
            self.change_sprite_2 = 0
        self.position_y += self.direction
        # Whe take a formula m(y-64)**2 + n=X making a parabola with centre in x=64 if we make a full parabola
        # whe can adjust m for the width and 64 for the centre
        self.position_x = int(self.position_y * (2 - self.position_y / 64))

    def draw(self):
        """This function draws and animates the red enemy"""
        # We have two states when doing a loop it will change according to the parabola
        # When not in loop it will alternate between both sprites of the plane moving the helices
        # Animation off the loop
        if self.position_x < 55:
            if self.change_sprite == 1:
                self.position_u = 64
            elif self.change_sprite == 0:
                self.position_u = 0
        # Animation on the loop
        if 58 > self.position_x >= 55 and self.change_sprite == 0:
            self.position_u = 16
            self.change_sprite = 1
        elif self.position_x >= 58 and self.change_sprite == 1:
            if self.change_sprite_2 == 1:
                self.position_u = 80
            elif self.change_sprite_2 == 0:
                self.position_u = 32
        elif 58 > self.position_x >= 55 and self.change_sprite == 1:
            self.position_u = 48
        # Draw the plane
        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, self.position_v, self.width, self.height,
                  self.transparent_color)


class Bombardier(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        super().__init__(position_x, position_y, projectile_manager)
        self.position_u = 0
        self.position_v = 64
        self.height = 16
        self.width = 16
        self.transparent_color = 4
        self.direction = 1
        self.change_direction = 0
        self.lives = 3

    def update(self):
        """This function will update every frame"""
        # Check if the enemy has to be deleted -> All enemy update methods need to have this:
        self.check_delete()
        # It will move until the position y=50 it will stop wait shoot and move until it changes direction
        # and do the same
        if self.position_y != 50:
            self.position_y -= self.direction
        if self.position_y == 50 and (pyxel.frame_count % 100 == 0):
            if (pyxel.frame_count % 400 == 0):
                self.projectile_manager.create_projectile(self.position_x, self.position_y, "BombardierProjectile")
            if (pyxel.frame_count % 3 == 0):
                self.direction = -1
            else:
                self.direction = 1
            self.position_y -= self.direction
        if self.position_y == 100:
            self.direction = 1
        elif self.position_y <= 0:
            self.direction = -1
        if self.position_x >= constants.screen_width + constants.normal_sprite_width + 10 or self.position_y >= constants.screen_height + constants.normal_sprite_height + 10:
            self.is_alive = False

    def draw(self):
        """This function draws and animates the bombardier"""
        # It will alternate between both sprites of the plane moving the helices
        # Draw the bombardier
        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, self.position_v, self.width, self.height,
                  self.transparent_color)
        # Animate the bombardier
        if self.direction < 0:
            self.position_v = 64
            if self.change_direction % 2 == 0:
                self.position_u = 32
                self.change_direction += 1
            else:
                self.position_u = 48
                self.change_direction += 1
        elif self.direction > 0:
            self.position_v = 64
            if self.change_direction % 2 == 0:
                self.position_u = 0
                self.change_direction += 1
            else:
                self.position_u = 16
                self.change_direction += 1


class SuperBombardier(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        super().__init__(position_x, position_y, projectile_manager)
        self.position_u = 0
        self.position_v = 80
        self.height = 16
        self.width = 32
        self.transparent_color = 4
        self.direction = 1
        self.change_direction = 0
        self.lives = 5

    def update(self):
        """This function will update every frame"""
        # Check if the enemy has to be deleted -> All enemy update methods need to have this:
        self.check_delete()
        # It will move until the position y=50 it will stop wait shoot and move until it changes direction
        # and do the same
        if self.position_y != 50:
            self.position_y += self.direction
        if self.position_y == 50 and (pyxel.frame_count % 400 == 0):
            self.projectile_manager.create_projectile(self.position_x, self.position_y, "BombardierProjectile")
            self.position_y += self.direction
        if self.position_y == 100:
            self.direction = -1
        elif self.position_y <= 0:
            self.direction = 1
        if self.position_x >= constants.screen_width + constants.normal_sprite_width + 10 or self.position_y >= constants.screen_height + constants.normal_sprite_height + 10:
            self.is_alive = False

    def draw(self):
        """This function draws and animates the super bombardier"""
        # It will alternate between both sprites of the plane moving the helices
        # Draw the super bombardier
        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, self.position_v, self.width, self.height,
                  self.transparent_color)
        # Animate the super bombardier
        if self.direction < 0:
            self.position_v = 80
            if self.change_direction % 2 == 0:
                self.position_u = 0
                self.change_direction += 1
            else:
                self.position_u = 32
                self.change_direction += 1
        elif self.direction > 0:
            self.position_v = 96
            if self.change_direction % 2 == 0:
                self.position_u = 0
                self.change_direction += 1
            else:
                self.position_u = 32
                self.change_direction += 1
