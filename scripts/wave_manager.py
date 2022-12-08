import pyxel
import constants

from projectileManager import ProjectileManager
from enemyManager import EnemyManager


class WaveManager:
    def __init__(self, enemy_manager: EnemyManager):
        self.enemy_manager = enemy_manager

    def update(self):
        if constants.player_lives > 0:
            self.wave_1()

    def wave_1(self):
        if pyxel.frame_count % 200 == 0:
            print("created")
            self.enemy_manager.create_enemy(0,0,"Red")
