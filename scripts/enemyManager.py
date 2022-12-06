import constants
from enemy import Enemy
from projectileManager import ProjectileManager


class EnemyManager:
    def __init__(self):
        self.enemy_list = []

    def update(self):
        for i in range(len(self.enemy_list)):
            if self.enemy_list[i].is_alive:
                self.enemy_list[i].update()
            else:
                del self.enemy_list[i]

        constants.draw_list(self.enemy_list)

    def create_enemy(self, position_x: int, position_y: int, projectile_manager:ProjectileManager):
        self.enemy_list.append(Enemy(position_x, position_y, self.projectile_manager))
