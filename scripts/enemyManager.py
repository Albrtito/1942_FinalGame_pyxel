"""
Enemy manager class, this class is created in order to manage all the enemies
"""
# We need to import the player class and the enemies classes+
# from player import Player
import time
from enemy import Enemy, RegularEnemy, RedEnemy
import constants
from projectileManager import ProjectileManager


class EnemyManager:

    # For future problems, this parameters should be properties, and be read only
    def __init__(self, position_x: int, position_y: int, number_enemies, enemy_type: str,projectile_manager : ProjectileManager):
        self.position_x = position_x
        self.position_y = position_y
        self.enemy_type = enemy_type
        self.number_enemies = number_enemies
        self.enemy_distance = 0
        self.enemy_appearence_rate = 0.3
        #self.projectile_manager = projectile_manager
        self.enemy_list = []
    def update(self):
        constants.update_list_and_delete(self.enemy_list)
        if len(self.enemy_list) < self.number_enemies and time.time() > self.enemy_distance:
            self.create_enemy()
            self.enemy_distance = time.time() + self.enemy_appearence_rate
    def draw(self):
        # Draw the projectiles in a list using the method from resources
        constants.draw_list(self.enemy_list)

    # This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile, depending on
    # the projectile_type attribute (must be a string)
    def create_enemy(self):
            if self.enemy_type == "Regular":
                self.enemy_list.append(RegularEnemy(self.position_x, self.position_y))
            if self.enemy_type == "Red":
                self.enemy_list.append(RedEnemy(self.position_x, self.position_y))
