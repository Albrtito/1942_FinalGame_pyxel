import random

import pyxel
import constants

from projectileManager import ProjectileManager
from enemyManager import EnemyManager


class WaveManager:
    def __init__(self, enemy_manager: EnemyManager):
        self.enemy_manager = enemy_manager
        self.wave = 1
        self.wave_appear = False
        self.__bombardier = False
        self.__super_bombardier = False
        self.__player_invincible = False

    def update(self):
        """This function updates every frame"""
        # It will create a new wave everytime the previous wave is over
        if constants.player_lives > 0 and self.wave == 1:
            self.wave_1()
            if self.wave == 1 and len(self.enemy_manager.enemy_list) == 0:
                self.wave_1()
            if len(self.enemy_manager.enemy_list) >= 10:
                self.wave = 2
        elif constants.player_lives > 0 and self.wave == 2:
            if len(self.enemy_manager.enemy_list) == 0:
                self.wave_appear = True
            if self.wave_appear:
                self.wave_2()
            if len(self.enemy_manager.enemy_list) >= 15:
                self.wave = 3
                self.wave_appear = True
        elif constants.player_lives > 0 and self.wave == 3:
            if len(self.enemy_manager.enemy_list) == 0:
                self.wave_appear = True
            if self.wave_appear:
                self.wave_3()
            if len(self.enemy_manager.enemy_list) >= 20:
                self.wave = 4
        elif constants.player_lives > 0 and self.wave == 4:
            if len(self.enemy_manager.enemy_list) <= 5:
                self.wave_appear = True
            if self.wave_appear:
                self.wave_4()
            if len(self.enemy_manager.enemy_list) >= 30:
                self.wave_appear = False
        # This will make the player invincible when he looses a live
        if not constants.player_is_alive and not self.__player_invincible:
            if self.wave != 0:
                self.wave -= 1
            # clear the enemies from the screen and the enemy projectiles from the screen so that when te player
            # reappears it doesn`t die
            self.enemy_manager.enemy_list.clear()
            self.enemy_manager.projectile_manager.enemy_projectiles.clear()
            self.__bombardier = False
            self.__super_bombardier = False
            self.__player_invincible = True
        elif constants.player_is_alive:
            self.__player_invincible = False
        print(len(self.enemy_manager.enemy_list), self.wave, constants.player_lives)

    def wave_1(self):
        """"The first wave will have Regular and Red planes"""
        if pyxel.frame_count % 10 == 0:
            self.enemy_manager.create_enemy(0, 0, "Regular")
        if pyxel.frame_count % 30 == 0:
            self.enemy_manager.create_enemy(0, 0, "Red")

    def wave_2(self):
        """"The first wave will have Regular and Red planes and a Bombardier"""
        if pyxel.frame_count % 10 == 0:
            self.enemy_manager.create_enemy(0, 0, "Regular")
        if pyxel.frame_count % 30 == 0:
            self.enemy_manager.create_enemy(0, 0, "Red")
        if not self.__bombardier:
            self.enemy_manager.create_enemy(random.randint(10, 120), 100, "Bombardier")
            self.__bombardier = True

    def wave_3(self):
        """"The first wave will have Regular and Red planes and a Bombardier and a SuperBombardier"""
        if pyxel.frame_count % 10 == 0:
            self.enemy_manager.create_enemy(0, 0, "Regular")
        if pyxel.frame_count % 30 == 0:
            self.enemy_manager.create_enemy(0, 0, "Red")
        if not self.__bombardier:
            self.enemy_manager.create_enemy(random.randint(10, 120), 100, "Bombardier")
            self.__bombardier = True
        if not self.__super_bombardier:
            self.enemy_manager.create_enemy(constants.screen_width // 2, 0, "Superbombardier")
            self.__super_bombardier = True

    def wave_4(self):
        """"The first wave will have Regular and Red planes and a Bombardier and a SuperBombardier"""
        if pyxel.frame_count % 10 == 0:
            self.enemy_manager.create_enemy(0, 0, "Regular")
        if pyxel.frame_count % 30 == 0:
            self.enemy_manager.create_enemy(0, 0, "Red")
        if pyxel.frame_count % 100 == 0:
            self.enemy_manager.create_enemy(random.randint(10, 120), 100, "Bombardier")
        if not self.__super_bombardier:
            self.enemy_manager.create_enemy(constants.screen_width // 2, 0, "Superbombardier")
            self.__super_bombardier = True
