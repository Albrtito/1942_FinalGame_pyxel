"""
Projectile manager class, this class is created in order to manage all the projectiles from the player and the enemies
When anyone shoots, a method will call this class creating a projectile
"""
# We need to import the player class and the enemies classes+
# from player import Player
from projectile import Projectile, PlayerProjectile, EnemyProjectile


class ProjectileManager:
    def __int__(self):
        self.player_projectiles = []
        self.enemy_projectiles = []

    def update(self):
        if len(self.player_projectiles) != 0:
            for projectile in self.player_projectiles:
                projectile.update()
        if len(self.enemy_projectiles) != 0:
            for projectile in self.enemy_projectiles:
                projectile.update()
    def draw(self):
        if len(self.player_projectiles) != 0:
            for projectile in self.player_projectiles:
                projectile.draw()
        if len(self.enemy_projectiles) != 0:
            for projectile in self.enemy_projectiles:
                projectile.draw()

    # This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile, depending on the projectile_type attribute (must be a string)
    def create_projectile(self, position_x: int, position_y: int, speed: int, projectile_type: str):
        if projectile_type == "PlayerProjectile":
            self.player_projectiles.append(PlayerProjectile(position_x, position_y, speed))
        if projectile_type == "EnemyProjectile":
            self.enemy_projectiles.append(EnemyProjectile(position_x, position_y, speed))