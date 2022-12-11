import math

import constants
from enemy import Enemy,RegularEnemy,RedEnemy,SuperBombardier,Bombardier
from player import Player
from enemyManager import EnemyManager
from projectileManager import ProjectileManager


class CollisionManager:
    """This clas manages the collisions between the player and the enemies, it does so by checking if any of the enemies,
    or it`s bullets are at the position of the player. It also checks if any of the player bullets are at the position of
    the enemies """

    def __init__(self, player: Player, enemy_manager: EnemyManager, projectile_manager: ProjectileManager):
        """CollisionManager.innit : This method declares the parameters for the CollisionManager class."""
        self.__player = player
        self.__enemy_manager = enemy_manager
        self.__projectile_manager = projectile_manager

    # Methods of the class
    # Update all the possible collisions
    def update(self):
        """Update: This method is repeated every frame while the game is played. CollisionManager.update:Is called in
                App.update """
        # If the player is alive the collisions are checked in the game
        if constants.player_is_alive:
            self.enemy_with_player_projectile()
            self.player_with_enemy_projectile()
            self.player_with_enemies()

    # Methods for checking collisions: All based in the standard collision method defined at the end of this class

    def player_with_enemies(self):
        """Player_with_enemies: Checks collisions between player and enemies."""
        for index in range(len(self.__enemy_manager.enemy_list) - 1, -1, -1):
            if self.collision(self.__player, self.__enemy_manager.enemy_list[index]):
                # We only subtract a live if the player is not doing a loop, if the player is doing a loop then its
                # kind of indestructible. Same happens with whatever should be destroyed but with the reversed logic
                if not self.__player.loop:
                    constants.player_lives -= 1
                    constants.player_is_alive = False
                    self.__enemy_manager.enemy_list[index].is_alive = False

    # This method is altered so the player is invincible
    def player_with_enemy_projectile(self):
        """Player_with_enemy_projectile: Checks collisions between player and enemies projectiles"""
        for index in range(len(self.__projectile_manager.enemy_projectiles) - 1, -1, -1):
            if self.collision(self.__player, self.__projectile_manager.enemy_projectiles[index]):
                # We only subtract a live if the player is not doing a loop, if the player is doing a loop then its
                # kind of indestructible. Same happens with whatever should be destroyed but with the reversed logic
                if not self.__player.loop:
                    constants.player_lives -= 0
                    constants.player_is_alive = True
                    self.__projectile_manager.enemy_projectiles[index].is_alive = False

    def enemy_with_player_projectile(self):
        """Enemy_with_player_projectiles: Checks collisions between the enemies and the player projectiles"""
        # For every player projectile we check if it's colliding with every enemy in the enemy list
        for player_index in range(len(self.__projectile_manager.player_projectiles) - 1, -1, -1):
            for enemy_index in range(len(self.__enemy_manager.enemy_list) - 1, -1, -1):
                if self.collision(self.__enemy_manager.enemy_list[enemy_index],
                                  self.__projectile_manager.player_projectiles[player_index]):
                    # If it`s colliding the enemy has one live less, and we delete the projectile that hit the enemy.
                    self.__enemy_manager.enemy_list[enemy_index].lives -= 1
                    self.__projectile_manager.player_projectiles[player_index].is_alive = False
                    # Depending on the type of enemy we killed, the points given to the player vary.
                    if type(self.__enemy_manager.enemy_list[enemy_index]) == RegularEnemy:
                        constants.player_score += 10
                    elif type(self.__enemy_manager.enemy_list[enemy_index]) == RedEnemy:
                        constants.player_score += 20
                    elif type(self.__enemy_manager.enemy_list[enemy_index]) == Bombardier:
                        constants.player_score += 40
                    elif type(self.__enemy_manager.enemy_list[enemy_index]) == SuperBombardier:
                        constants.player_score += 80

    def collision(self, object_1, object_2):
        """Collision: Checks collision of two objects using their positions (x and y) and their sprite dimensions.
        Uses pitagoras theorem to compute the distance between them, if that distance is equal or smaller than the sum
        of both widths, then it's a collision.
        True when collision, false when not colliding
        NOTE: This works because every object is a square of dimension object. width"""
        distance = math.sqrt(((object_1.position_x - object_2.position_x) ** 2) +
                             ((object_1.position_y - object_2.position_y) ** 2))
        if distance < (object_1.width + object_2.width) / 2:
            print("collision")
            return True
        else:
            return False
