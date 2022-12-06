import constants
from enemy import Enemy
from projectileManager import ProjectileManager


class EnemyManager:
    def __init__(self):
        self.enemy_list = []

    def update(self):
        print(len(self.enemy_list))
        constants.update_list_and_delete(self.enemy_list)

    def draw(self):
        constants.draw_list(self.enemy_list)

    def create_enemy(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):
        self.enemy_list.append(Enemy(position_x, position_y, projectile_manager))
