import random

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
        self.bombardier = False
        self.super_bombardier = False
        self.player_invincible = False

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
        elif constants.player_lives > 0 and self.wave == 4:
            if len(self.enemy_manager.enemy_list) <= 5:
                self.wave_appear = True
            if self.wave_appear:
                self.wave_4()
            if len(self.enemy_manager.enemy_list) >= 30:
                self.wave_appear = False
            if not constants.player_is_alive and not self.player_invincible:
                self.wave -= 1
                self.enemy_manager.enemy_list.clear()
                self.player_invincible = True
            elif constants.player_is_alive:
                self.player_invincible = False
        print(len(self.enemy_manager.enemy_list),self.wave, constants.player_lives)

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
        if not self.bombardier:
            self.enemy_manager.create_enemy(random.randint(10,120),100,"Bombardier")
            self.bombardier = True
    def wave_3(self):
        if (pyxel.frame_count % 10 == 0):
            self.enemy_manager.create_enemy(0,0,"Regular")
        if (pyxel.frame_count % 20 == 0):
            self.enemy_manager.create_enemy(0,0,"Red")
        if not self.bombardier:
            self.enemy_manager.create_enemy(random.randint(10,120),100,"Bombardier")
            self.bombardier = True
        if not self.super_bombardier:
            self.enemy_manager.create_enemy(constants.screen_width//2,0,"Superbombardier")
            self.super_bombardier = True
    def wave_4(self):
        if (pyxel.frame_count % 10 == 0):
            self.enemy_manager.create_enemy(0,0,"Regular")
        if (pyxel.frame_count % 20 == 0):
            self.enemy_manager.create_enemy(0,0,"Red")
        if (pyxel.frame_count % 100 == 0):
            self.enemy_manager.create_enemy(random.randint(10,120),100,"Bombardier")
        if not self.super_bombardier:
            self.enemy_manager.create_enemy(constants.screen_width//2,0,"Superbombardier")
            self.super_bombardier = True