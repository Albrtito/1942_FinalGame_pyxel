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
            raise TypeError("player must be an object of class EnemyManger")
        self.__enemy_manager = enemy_manager

    # Methods of the class
    def update(self):
        self.enemy_with_player_projectile()
        self.player_with_enemy_projectile()
        self.player_with_enemies()

    # Methods for checking collisions: -> Right now checking collisions for points not squares

    # Player collisions with the rest
    def player_with_enemies(self):
        for index in range(len(self.enemy_manager.enemy_list) - 1, -1):
            if (self.player.position_x == self.enemy_manager.enemy_list[index].position_x) and \
                    (self.player.position_y == self.enemy_manager.enemy_list[index].position_y):
                constants.player_lives -= 1

    def player_with_enemy_projectile(self):
        for index in range(len(self.projectile_manager.enemy_projectiles)-1, -1, -1):
            if (self.player.position_x == self.projectile_manager.enemy_projectiles[index].position_x) and\
                    (self.player.position_y == self.projectile_manager.enemy_projectiles[index].position_y):
                constants.player_lives -= 1

    # Enemy collisions with the player bullets
    def enemy_with_player_projectile(self):
        for player_index in range(len(self.projectile_manager.player_projectiles)-1, -1, -1):
            for enemy_index in range(len(self.enemy_manager.enemy_list)-1,-1,-1):
                if (self.enemy_manager.enemy_list[enemy_index].position_x == self.projectile_manager.player_projectiles[player_index].position_x)\
                        and (self.enemy_manager.enemy_list[enemy_index].position_y == self.projectile_manager.player_projectiles[player_index].position_y):
                    self.enemy_manager.enemy_list[enemy_index].is_alive = False
                    constants.player_score += 10



