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

    def __init__(self, position_x: int, position_y: int):
        self.position_x = position_x
        self.position_y = position_y
        #self.projectile_manager = projectile_manager
        self.is_alive = True

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

    '''@projectile_manager.setter
    def projectile(self, projectile_manager: ProjectileManager):
        if type(projectile_manager) != ProjectileManager:
            raise TypeError("Projectile manager must be an object of class ProjectileManager")
        else:
            self.__projectile_manager = projectile_manager
'''
    # Basic methods for the enemy class:

    # Update method -> Has to be called every frame -> Is update method inside a class used as the move method??

    # Enemy inherits from Sprite, so we can draw it using all the attributes of sprite
    def draw(self):
        pyxel.blt(self.position_x,self.position_y,0,self.position_u,self.position_v,self.width,self.height,self.transparent_color)

    def update(self):
        ...


# Enemy child classes. Each will contain a sprite specific for each class.
class RegularEnemy(Enemy):
    def __init__(self, position_x: int, position_y: int):
        self.position_u = 0
        self.position_v = 32
        self.height = 16
        self.width = 16
        self.transparent_color = 4
        super().__init__(position_x, position_y)
        ''', projectile_manager)'''

    def update(self):
        #Detecta que el enmigo este 10 pixeles fuera de la pantalla, para que haya la opcion de que un enemigo salga
        #momentaneamente de la pantalla
        if self.position_x >= constants.screen_width + constants.normal_sprite_width + 10 or self.position_y >= constants.screen_height + constants.normal_sprite_height + 10:
            self.is_alive = False
        else:
            self.position_x += 1
            # Whe take a formula m(x-64)**2 + n=Y making a parabola with centre in x=64 if we make a full parabola whe can adjust m for the width and 64 for the centre
            self.position_y = int(self.position_x*(2-self.position_x/64))
            #self.position_y = int(-self.position_x**2/16+8*self.position_x-192)
    def draw(self):
        if self.position_y <= 45:
            ...

class RedEnemy(Enemy):
    def __init__(self, position_x: int, position_y: int):
        self.position_u = 0
        self.position_v = 48
        self.height = 16
        self.width = 16
        self.transparent_color = 11
        super().__init__(position_x, position_y)
        ''', projectile_manager)'''
    def update(self):
        #Detecta que el enmigo este 10 pixeles fuera de la pantalla, para que haya la opcion de que un enemigo salga
        #momentaneamente de la pantalla
        if self.position_x >= constants.screen_width + constants.normal_sprite_width + 10 or self.position_y >= constants.screen_height + constants.normal_sprite_height + 10:
            self.is_alive = False
        else:
            self.position_y += 1
            # Whe take a formula m(x-64)**2 + n=Y making a parabola with centre in x=64 if we make a full parabola whe can adjust m for the width and 64 for the centre
            self.position_x = int(0.005*self.position_y**3-0.05*self.position_y**2)
            #self.position_y = int(-self.position_x**2/16+8*self.position_x-192)



class Bombardier(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        self.position_u = 0
        self.position_v = 64
        self.height = 16
        self.width = 16
        self.transparent_color = 0
        super().__init__(position_x, position_y)
        '''', projectile_manager)


class SuperBombardier(Enemy):
    def __init__(self, position_x: float, position_y: float, projectile_manager: ProjectileManager):
        self.position_u = 0
        self.position_v = 80
        self.height = 32
        self.width = 16
        self.transparent_color = 0
        super().__init__(position_x, position_y, projectile_manager)

'''