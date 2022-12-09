import pyxel
import constants

from projectileManager import ProjectileManager
from enemyManager import EnemyManager


class WaveManager:
    def __init__(self, enemy_manager: EnemyManager):
        self.enemy_manager = enemy_manager
        self.wave_list = []
        self.wave = 3
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
                self.wave_appear = True
        elif constants.player_lives > 0 and self.wave == 3:
            if len(self.enemy_manager.enemy_list) == 0:
                self.wave_appear = True
            if self.wave_appear:
                self.wave_3()
            if len(self.enemy_manager.enemy_list) >= 30:
                self.wave = 4
        print(len(self.enemy_manager.enemy_list),self.wave)

    def wave_1(self):
        if (pyxel.frame_count % 10 == 0):
            self.enemy_manager.create_enemy(0,0,"Regular")
        if (pyxel.frame_count % 20 == 0):
            self.enemy_manager.create_enemy(0,0,"Red")
    def wave_2(self):
        if (pyxel.frame_count % 10 == 0):
            self.enemy_manager.create_enemy(0,0,"Regular")
        if (pyxel.frame_count % 20 == 0):
            self.enemy_manager.create_enemy(0,0,"Red")
        if len(self.enemy_manager.enemy_list) <= 5:
            self.enemy_manager.create_enemy(0,100,"Bombardier")
    def wave_3(self):
        if (pyxel.frame_count % 10 == 0):
            self.enemy_manager.create_enemy(0,0,"Regular")
        if (pyxel.frame_count % 20 == 0):
            self.enemy_manager.create_enemy(0,0,"Red")
        if len(self.enemy_manager.enemy_list) <= 5:
            self.enemy_manager.create_enemy(0,100,"Bombardier")
        if len(self.enemy_manager.enemy_list) >= 25:
            self.enemy_manager.create_enemy(0,100,"SuperBombardier")