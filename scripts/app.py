import time

import pyxel
from sprite import Sprite
from player import Player
from projectileManager import ProjectileManager
from enemyManager import EnemyManager
from enemy import Enemy, RegularEnemy
from background_manager import BackgroundManager

# enemy_visible = False
HEIGHT = 128
WIDTH = 128
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16
x = 0

#Cambios hechos, primera version
#Version Ignacio
class App:
    def __init__(self):
        # Classes attribute
        self.background_manager = BackgroundManager(WIDTH, HEIGHT)
        self.projectile_manager = ProjectileManager()
        self.player = Player(int(WIDTH / 2), int(HEIGHT / 2), self.projectile_manager)
        self.enemymanager = EnemyManager(0.0, 20.0, "Regular", self.projectile_manager)

        # Variables of the game loop:
        self.game_loop = False
        # Initialize pyxel
        pyxel.init(WIDTH, HEIGHT, title="Pyxel 1942")
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
            self.projectile_manager.update()
            self.enemymanager.update()
            self.enemymanager.create_enemy()
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
            # Draw Enemy
            self.enemymanager.draw()
        else:
            self.background_manager.draw()

        # Draw enemies
        # self.test_enemy.draw()

    # When the game ends, everything but the background stops ( game_loop = False )
    def game_over(self):
        self.background_manager.game_over = True
        self.game_loop = False


App()
