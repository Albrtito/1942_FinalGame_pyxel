"""
Projectile manager class, this class is created in order to manage all the projectiles from the player and the enemies
When anyone shoots, a method will call this class creating a projectile
"""
# We need to import the player class and the enemies classes+
# from player import Player
from projectile import Projectile, PlayerProjectile, EnemyProjectile
import resources


class ProjectileManager:
    def __init__(self):
        self.player_projectiles = []
        self.enemy_projectiles = []


    """
    @enemy_projectiles.setter
    def player_projectiles(self, enemy_projectiles: list):
        if type(enemy_projectiles) != list:
            raise TypeError("player_projectiles must be a list")
        self.__enemy_projectiles = enemy_projectiles

    """

    def update(self):
        # Update the projectiles in a list using the method from resources
        resources.update_list(self.player_projectiles)
        resources.update_list(self.enemy_projectiles)

    def draw(self):
        # Draw the projectiles in a list using the method from resources
        resources.draw_list(self.player_projectiles)
        resources.draw_list(self.enemy_projectiles)
    
    # This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile, depending on
    # the projectile_type attribute (must be a string)
    def create_projectile(self, position_x: int, position_y: int, speed: int, projectile_type: str):
        if projectile_type == "PlayerProjectile":
            self.player_projectiles.append(Projectile(position_x,position_y,speed))
        if projectile_type == "EnemyProjectile":
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y, speed))

