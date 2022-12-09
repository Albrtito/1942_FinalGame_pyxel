import pyxel
import constants

from projectileManager import ProjectileManager
from enemyManager import EnemyManager


class WaveManager:
    def __init__(self, enemy_manager: EnemyManager):
        self.enemy_manager = enemy_manager
        self.wave_list = []
        self.wave = 1
        self.wave_appear = False

    def update(self):
        if constants.player_lives > 0 and self.wave == 1:
            self.wave_1()
            if len(self.enemy_manager.enemy_list) >= 10:
                self.wave = 2
        elif constants.player_lives > 0 and self.wave == 2:
            if len(self.enemy_manager.enemy_list) == 0:
                self.wave_appear = True
            if self.wave_appear:
                self.wave_2()
            if len(self.enemy_manager.enemy_list) >= 20:
                self.wave = 3
        print(len(self.enemy_manager.enemy_list), self.wave)

        if not constants.player_is_alive:
            self.wave = 1
            self.enemy_manager.enemy_list.clear()
            self.enemy_manager.projectile_manager.enemy_projectiles.clear()

    def wave_1(self):
        if pyxel.frame_count % 10 == 0:
            self.enemy_manager.create_enemy(0, 0, "Regular")
        if pyxel.frame_count % 20 == 0:
            self.enemy_manager.create_enemy(0, 0, "Red")

    def wave_2(self):
        if pyxel.frame_count % 10 == 0:
            self.enemy_manager.create_enemy(0, 0, "Regular")
        if pyxel.frame_count % 20 == 0:
            self.enemy_manager.create_enemy(0, 0, "Red")
        if len(self.enemy_manager.enemy_list) <= 5:
            self.enemy_manager.create_enemy(0, 100, "Bombardier")
