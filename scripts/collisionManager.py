import math

import constants

from player import Player
from enemyManager import EnemyManager
from projectileManager import ProjectileManager

"""This clas manages the collisions between the player and the enemies, it does so by checking if any of the enemies, 
or it`s bullets are at the position of the player. It also checks if any of the player bullets are at the position of 
the enemies """


class CollisionManager:
    def __init__(self, player: Player, enemy_manager: EnemyManager, projectile_manager: ProjectileManager):
        self.player = player
        self.enemy_manager = enemy_manager
        self.projectile_manager = projectile_manager

    # Creation of attributes, setter as they will be given every time it's called the class(as it going to be called
    # in an update or draw method)
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        if type(player) != Player:
            raise TypeError("Player must be an object of class player")
        self.__player = player

    @property
    def enemy_manager(self):
        return self.__enemy_manager

    @enemy_manager.setter
    def enemy_manager(self, enemy_manager):
        if type(enemy_manager) != EnemyManager:
            raise TypeError("player must be an object of class EnemyManager")
        self.__enemy_manager = enemy_manager

    # Methods of the class

    # Update all the possible collisions
    def update(self):
        self.enemy_with_player_projectile()
        self.player_with_enemy_projectile()
        self.player_with_enemies()

    # Methods for checking collisions: -> Right now checking collisions for points not squares

    # Player collisions with the rest

    def player_with_enemies(self):
        for index in range(len(self.enemy_manager.enemy_list) - 1, -1, -1):
            if self.collision(self.player, self.enemy_manager.enemy_list[index]):
                # We only subtract a live if the player is not doing a loop, if the player is doing a loop then its
                # kind of indestructible. Same happens with whatever should be destroyed but with the reversed logic
                if not self.player.loop:
                    constants.player_lives -= 1
                    constants.player_is_alive = False
                    self.enemy_manager.enemy_list[index].is_alive = False

    def player_with_enemy_projectile(self):
        for index in range(len(self.projectile_manager.enemy_projectiles) - 1, -1, -1):
            if self.collision(self.player, self.projectile_manager.enemy_projectiles[index]):
                # We only subtract a live if the player is not doing a loop, if the player is doing a loop then its
                # kind of indestructible. Same happens with whatever should be destroyed but with the reversed logic
                if not self.player.loop:
                    constants.player_lives -= 1
                    constants.player_is_alive = False
                    self.projectile_manager.enemy_projectiles[index].is_alive = False

    # Enemy collisions with the player projectiles
    def enemy_with_player_projectile(self):
        for player_index in range(len(self.projectile_manager.player_projectiles) - 1, -1, -1):
            for enemy_index in range(len(self.enemy_manager.enemy_list) - 1, -1, -1):
                if self.collision(self.enemy_manager.enemy_list[enemy_index],
                                  self.projectile_manager.player_projectiles[player_index]):
                    self.enemy_manager.enemy_list[enemy_index].lives -= 1
                    self.projectile_manager.player_projectiles[player_index].is_alive = False
                    constants.player_score += 10

    # Basic distance collision for any two objects:
    def collision(self, object_1, object_2):
        distance = math.sqrt(((object_1.position_x - object_2.position_x) ** 2) +
                             ((object_1.position_y - object_2.position_y) ** 2))
        if distance < (object_1.width + object_2.width) / 2:
            print("collision")
            return True
        else:
            return False
