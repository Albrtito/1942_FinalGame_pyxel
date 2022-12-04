"""
Projectile manager class, this class is created in order to manage all the projectiles from the player and the enemies
When anyone shoots, a method will call this class creating a projectile
"""
# We need to import the player class and the enemies classes+
# from player import Player
from projectile import Projectile, PlayerProjectile, EnemyProjectile
import resources


class ProjectileManager:

    # For future problems, this parameters should be properties, and be read only
    def __init__(self):
        self.player_projectiles = []
        self.enemy_projectiles = []

    def update(self):
        # Update the projectiles in each player and enemy list. Delete the projectile
        # if more than 5 seconds have passed since its creation
        # for player projectiles
        for elem in self.player_projectiles:
            if elem.is_alive:
                elem.update()
            else:
                del elem
        # for enemy projectiles
        for elem in self.enemy_projectiles:
            if elem.isalive:
                elem.update()
            else:
                del elem

    def draw(self):
        # Draw the projectiles in a list using the method from resources
        resources.draw_list(self.player_projectiles)
        resources.draw_list(self.enemy_projectiles)

    # This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile, depending on
    # the projectile_type attribute (must be a string)
    def create_projectile(self, position_x: int, position_y: int, projectile_type: str):
        if projectile_type == "PlayerProjectile":
            self.player_projectiles.append(PlayerProjectile(position_x, position_y))
        if projectile_type == "EnemyProjectile":
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y))
