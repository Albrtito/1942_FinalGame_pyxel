"""
Projectile manager class, this class is created in order to manage all the projectiles from the player and the enemies
When anyone shoots, a method will call this class creating a projectile
"""
import pyxel

# We need to import the player class and the enemies classes+
# from player import Player
from projectile import Projectile, PlayerProjectile, EnemyProjectile
import constants


class ProjectileManager:

    # For future problems, this parameters should be properties, and be read only
    def __init__(self):
        self.player_projectiles = []
        self.enemy_projectiles = []

    def update(self):
        """This function updates every frame"""
        # Update the projectiles in each player and enemy list.
        constants.update_list_and_delete(self.player_projectiles)
        constants.update_list_and_delete(self.enemy_projectiles)
    def draw(self):
        """Draw the projectiles in a list using the method from resources"""
        constants.draw_list(self.player_projectiles)
        constants.draw_list(self.enemy_projectiles)
    def create_projectile(self, position_x: int, position_y: int, projectile_type: str):
        """This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile"""
        if projectile_type == "PlayerProjectile":
            self.player_projectiles.append(PlayerProjectile(position_x, position_y))
        if projectile_type == "EnemyProjectile":
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,3))
        if projectile_type == "BombardierProjectile":
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,2))
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,-2))
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,2,-2))
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,-2,-2))
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,2,2))
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,-2,2))
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,0,-2))
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y,0,-2))
