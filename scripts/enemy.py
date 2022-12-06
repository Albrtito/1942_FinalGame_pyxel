import random

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


# Enemy parent class.Contains all common attributes for all enemies
class Enemy:
    # Declaration of the Enemy init method with all the attributes from the class

    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        self.position_x = position_x
        self.position_y = position_y
        self.projectile_manager = projectile_manager

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
    def projectile_manager(self):
        return self.__projectile_manager

    @projectile_manager.setter
    def projectile(self, projectile_manager: ProjectileManager):
        if type(projectile_manager) != ProjectileManager:
            raise TypeError("Projectile manager must be an object of class ProjectileManager")
        else:
            self.__projectile_manager = projectile_manager

    # Basic methods for the enemy class:

    # Update method -> Has to be called every frame -> Is update method inside a class used as the move method??

    # Enemy inherits from Sprite, so we can draw it using all the attributes of sprite
    def draw(self):
        ...

    def update(self):
        ...


# Enemy child classes. Each will contain a sprite specific for each class.
class RegularEnemy(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager, acceleration=3, ):
        super().__init__(position_x, position_y, projectile_manager)
        self.acceleration = acceleration

    def update(self):
        self.position_x = self.acceleration * time
        self.position_y = self.acceleration * time


class RedEnemy(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        super().__init__(position_x, position_y, projectile_manager)


class Bombardier(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        super().__init__(position_x, position_y, projectile_manager)

    def draw(self):
        pyxel.blt(30, 10, 0, 73, 3, 14, 11, colkey=0)


class SuperBombardier(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        super().__init__(position_x, position_y, projectile_manager)

    def draw(self):
        pyxel.blt(10, 10, 0, 89, 0, 14, 16, colkey=0)
