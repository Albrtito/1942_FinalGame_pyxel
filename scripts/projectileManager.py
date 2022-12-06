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
        # Update the projectiles in each player and enemy list. Delete the projectile
        # if more than 5 seconds have passed since its creation
        # for player projectiles
        if pyxel.frame_count % 20 == 0:
            print(len(self.player_projectiles))
        for index in range(len(self.player_projectiles) - 1, -1, -1):
            if self.player_projectiles[index].is_alive:
                self.player_projectiles[index].update()
            else:
                del (self.player_projectiles[index])

        # for enemy projectiles
        for index in range(len(self.enemy_projectiles - 1, -1, -1)):
            if self.enemy_projectiles[index].is_alive:
                self.enemy_projectiles[index].update()
            else:
                del self.enemy_projectiles[index]

    def draw(self):
        # Draw the projectiles in a list using the method from resources
        constants.draw_list(self.player_projectiles)
        constants.draw_list(self.enemy_projectiles)

    # This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile, depending on
    # the projectile_type attribute (must be a string)
    def create_projectile(self, position_x: int, position_y: int, projectile_type: str):
        if projectile_type == "PlayerProjectile":
            self.player_projectiles.append(PlayerProjectile(position_x, position_y))
        if projectile_type == "EnemyProjectile":
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y))
