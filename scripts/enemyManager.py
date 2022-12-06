"""
Enemy manager class, this class is created in order to manage all the enemies
"""
# We need to import the player class and the enemies classes+
# from player import Player
from enemy import Enemy, RegularEnemy, RedEnemy
import resources


class EnemyManager:

    # For future problems, this parameters should be properties, and be read only
    def __init__(self, position_x: int, position_y: int, enemy_type: str):
        self.position_x = position_x
        self.position_y = position_y
        self.enemy_type = enemy_type
        self.enemy_list = []
    def update(self):
        # Update the projectiles in each player and enemy list. Delete the projectile
        # if more than 5 seconds have passed since its creation
        # for player projectiles
        for elem in self.enemy_list:
            if elem.is_alive:
                elem.update()
            else:
                del elem

    def draw(self):
        # Draw the projectiles in a list using the method from resources
        resources.draw_list(self.enemy_list)

    # This method returns an object of class projectile, subclass PlayerProjectile or EnemyProjectile, depending on
    # the projectile_type attribute (must be a string)
    def create_enemy(self):
        for e in range(3):
            if self.enemy_type == "Regular":
                self.enemy_list.append(RegularEnemy(self.position_x, self.position_y, projectile_manager))
                print('yes',self.enemy_list)
                self.position_x += 10
                self.position_y += 10
            if self.enemy_type == "Red":
                self.enemy_projectiles.append(Enemy.RedEnemy(self.position_x, self.position_y))
