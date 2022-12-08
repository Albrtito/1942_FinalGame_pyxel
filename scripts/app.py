import time
from sprite import Sprite
import random
import pyxel
import constants
from wave_manager import WaveManager
from player import Player
from projectileManager import ProjectileManager
from collisionManager import CollisionManager
from background_manager import BackgroundManager
from enemyManager import EnemyManager

class App:
    def __init__(self):
        # Classes attribute
        self.background_manager = BackgroundManager(constants.screen_width, constants.screen_height)
        self.projectile_manager = ProjectileManager()
        self.enemy_manager = EnemyManager(self.projectile_manager)
        self.wave_manager = WaveManager(self.enemy_manager)
        self.player = Player(int(constants.screen_width / 2), int(constants.screen_height / 2), self.projectile_manager)
        self.collision_manager = CollisionManager(self.player, self.enemy_manager, self.projectile_manager)
        # Variables of the game loop:
        self.game_loop = False
        # Initialize pyxel
        pyxel.init(constants.screen_width, constants.screen_height, title="Pyxel 1942")
        pyxel.load('../assets/App.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.background_manager.initial_screen = False
            self.game_loop = True
        if self.game_loop:
            # The game will quit when Q is pressed
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            if pyxel.btnp(pyxel.KEY_G) or constants.player_lives <= 0:
                self.game_over()
            # Update of the game objects
            self.collision_manager.update()
            self.background_manager.update()
            self.player.update()
            # Update of the enemies
            self.enemy_manager.update()
            # Creation of the enemies
            self.wave_manager.update()
            self.projectile_manager.update()
            self.collision_manager.update()
            # self.dev_mode()
        else:
            self.background_manager.update()

    def draw(self):
        if self.game_loop:
            # Draw background
            self.background_manager.draw()
            # Draw bullets
            self.projectile_manager.draw()
            # Draw player
            self.player.draw()
            # Draw all enemies
            self.enemy_manager.draw()
        else:
            self.background_manager.draw()

        # Draw enemies
        # self.test_enemy.draw()

    # When the game ends, everything but the background stops ( game_loop = False )
    def game_over(self):
        self.background_manager.game_over = True
        self.game_loop = False

    """
    def dev_mode(self):
        if pyxel.btnp(pyxel.KEY_E):
            self.enemy_manager.create_enemy(random.randint(5,123), random.randint(0,64), self.projectile_manager)

    """
App()
