import random

"""Comentarios de Alberto que esta haciendo el detector de colisiones: 
+ Los enemigos necesitan tener una variable 
booleana llamada is_alive, esta variable es True hasta q mueran y entonces es false 
+ Cuando is_alive es False el 
enemyManager deberá de eliminar a ese enemigo de la lista de enemigos, prefeiblemente en el mismo loop q usa para 
actualizar,(comprueba q este vivo y actualiza, sino no actualice) 

"""
import constants
import time
import pyxel
from projectileManager import ProjectileManager


# Enemy parent class.Contains all common attributes for all enemies
class Enemy:
    # Declaration of the Enemy init method with all the attributes from the class

    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        # Basic variables of enemy
        self.position_x = position_x
        self.position_y = position_y
        self.width = constants.normal_sprite_width
        self.height = constants.normal_sprite_height
        # Other variables
        self.projectile_manager = projectile_manager
        # In game important variables of each enemy
        self.is_alive = True
        self.lives = 2

    # Property and setter for position_x
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: int):
        # Only change the position_x to float values
        if type(position_x) != int:
            raise TypeError("The position must be a int")
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
            raise TypeError("The position must be a int")
        else:
            self.__position_y = position_y

    # Property and setter for projectile
    """
    @property
    def projectile_manager(self):
        return self.__projectile_manager
    
    @projectile_manager.setter
    def projectile(self, projectile_manager: ProjectileManager):
        if type(projectile_manager) != ProjectileManager:
            raise TypeError("Projectile manager must be an object of class ProjectileManager")
        self.__projectile_manager = projectile_manager
    """

    # Basic methods for the enemy class:

    # Update method -> Has to be called every frame -> Is update method inside a class used as the move method??

    # Enemy inherits from Sprite, so we can draw it using all the attributes of sprite
    def draw(self):
        pyxel.blt(self.position_x, self.position_y, 0, 0, 32, constants.normal_sprite_width,
                  constants.normal_sprite_height,
                  colkey=0)

    def update(self):
        self.is_alive = self.check_delete()
        if pyxel.frame_count % random.randint(100, 200) == 0:
            self.projectile_manager.create_projectile(self.position_x, self.position_y, "EnemyProjectile")

    # Check if the enemy should be deleted (die)
    def check_delete(self):
        if self.lives <= 0:
            return False
        else:
            return True


# Enemy child classes. Each will contain a sprite specific for each class.
class RegularEnemy(Enemy):
    ...


class RedEnemy(Enemy):
    ...


class Bombardier(Enemy):
    ...


class SuperBombardier(Enemy):
    ...
