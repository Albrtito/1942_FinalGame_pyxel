"""
Enemy manager class, this class is created in order to manage all the enemies
"""
# We need to import the player class and the enemies classes+
# from player import Player
import time
from enemy import Enemy, RegularEnemy, RedEnemy, Bombardier, SuperBombardier
import constants
from projectileManager import ProjectileManager


class EnemyManager:

    # For future problems, this parameters should be properties, and be read only
    def __init__(self,projectile_manager:ProjectileManager):
        self.projectile_manager = projectile_manager
        self.enemy_list = []

    def update(self):
        constants.update_list_and_delete(self.enemy_list)

    def draw(self):
        # Draw the projectiles in a list using the method from resources
        constants.draw_list(self.enemy_list)

    # This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile, depending on
    # the projectile_type attribute (must be a string)
    def create_enemy(self,position_x, position_y,enemy_type:str):
        if enemy_type == "Regular":
            self.enemy_list.append(RegularEnemy(position_x, position_y,self.projectile_manager))
        if enemy_type == "Red":
            self.enemy_list.append(RedEnemy(position_x, position_y,self.projectile_manager))
        if enemy_type == "Bombardier":
            self.enemy_list.append(Bombardier(position_x, position_y, self.projectile_manager))
        if enemy_type == "Superbombardier":
            self.enemy_list.append(SuperBombardier(position_x, position_y, self.projectile_manager))
