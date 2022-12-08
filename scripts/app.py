import time

import pyxel
import constants
from Waves import Waves
from sprite import Sprite
from player import Player
from enemy import Enemy, RegularEnemy
from projectileManager import ProjectileManager
#from collisionManager import CollisionManager
from enemyManager import EnemyManager
from background_manager import BackgroundManager


class App:
    def __init__(self):
        # Classes attribute
        self.background_manager = BackgroundManager(constants.screen_width, constants.screen_height)
        self.projectile_manager = ProjectileManager()
        self.wave1 = Waves(self.projectile_manager)
        self.player = Player(int(constants.screen_width / 2), int(constants.screen_height / 2), self.projectile_manager)
        #self.collision_manager = CollisionManager(self.player,self.wave1,self.projectile_manager)

        self.enemies = []

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
            if pyxel.btnp(pyxel.KEY_G):
                self.game_over()
            # Update of the game objects
            self.background_manager.update()
            self.player.update()
            self.wave1.update()
            self.projectile_manager.update()
            #self.collision_manager.update()
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
            # Draw an enemy wave
            self.wave1.draw()
        else:
            self.background_manager.draw()

        # Draw enemies
        # self.test_enemy.draw()

    # When the game ends, everything but the background stops ( game_loop = False )
    def game_over(self):
        self.background_manager.game_over = True
        self.game_loop = False


    def dev_mode(self):
        if pyxel.btnp(pyxel.KEY_E):
            self.enemy_manager.create_enemy(64,0,self.projectile_manager)
App()
