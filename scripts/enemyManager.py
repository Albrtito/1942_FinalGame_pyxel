"""
Enemy manager class, this class is created in order to manage all the enemies
"""
# We need to import the player class and the enemies classes+
# from player import Player
from enemy import Enemy, RegularEnemy, RedEnemy, Bombardier, SuperBombardier
import constants
from projectileManager import ProjectileManager


class EnemyManager:

    def __init__(self, projectile_manager: ProjectileManager):
        """The init function of the class that will manage all the enemy objects"""
        self.enemy_list = []
        self.projectile_manager = projectile_manager

    def update(self):
        """This function will execute every frame"""
        # It wil check that the enemies on the list are alive
        constants.update_list_and_delete(self.enemy_list)

    def draw(self):
        """This function will be executed every frame"""
        # Draw the projectiles in a list using the method from resources
        constants.draw_list(self.enemy_list)

    def create_enemy(self, position_x, position_y, enemy_type: str):
        """This method will create the enemy of the class determined by the enemy_type string"""
        if enemy_type == "Regular":
            self.enemy_list.append(RegularEnemy(position_x, position_y, self.projectile_manager))
        if enemy_type == "Red":
            self.enemy_list.append(RedEnemy(position_x, position_y, self.projectile_manager))
        if enemy_type == "Bombardier":
            self.enemy_list.append(Bombardier(position_x, position_y, self.projectile_manager))
        if enemy_type == "Superbombardier":
            self.enemy_list.append(SuperBombardier(position_x, position_y, self.projectile_manager))
