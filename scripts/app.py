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

# main version, only enemies and final touches needed
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
        print(self.game_loop)
        """
        If the variable game loop is true, the main game loop will be executed, in this loop all objects are
        updated. The quit key is checked and the game over function is checked if the player lives are 0
        and the explosion is done
        """
        if self.game_loop:
            # The game will quit when Q is pressed
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            # The player explosion variable determines when the explosion of the player is done and
            # the game can go through with the game over screen or starting with one less live
            if self.player.explosion_done:
                if constants.player_lives <= 0:
                    self.game_over()
                self.background_manager.initial_screen = True
                self.game_loop = False
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
            # The dev mode is a way of easily checking for mistakes in game during development.
            self.dev_mode()

        else:
            """
            This state of the game is reached in two occasions: 
            + At the start of the game the initial screen will disappear once return is pressed. The game loop starts.
            + This also checks if that we are at the post-game over moment, 
                 the player has lost a live but has not died yet, the game is set back into the initial screen and shows
                 that a live has been lost
            """
            if constants.player_lives > 0:
                # When the player looses a live
                if pyxel.btnp(pyxel.KEY_RETURN):
                    self.game_loop = True
                    constants.player_is_alive = True
                    self.player.explosion_done = False
                    self.background_manager.initial_screen = False

            self.background_manager.update()


    def draw(self):
        if self.game_loop:
            # Draw background
            self.background_manager.draw()
            # Draw bullets
            self.projectile_manager.draw()
            # Draw the player
            self.player.draw()
            # Draw all enemies
            self.enemy_manager.draw()

        else:
            self.background_manager.draw()

        # Draw enemies
        # self.test_enemy.draw()

    # When the game ends, everything but the background stops ( game_loop = False )
    def game_over(self):
        """
        We now open the high-score file and check if the high score obtained during the game is greater than the max
        high score ever played, if that's the case, the in-game score is written in the file as the new high score.
        """
        # Open the file as read only
        r = open("../assets/high_score.txt", "r")
        # Evaluate the file high score vs the in-game actual high score
        if int(r.read()) < constants.player_score:
            # If the actual high score is grater, se that as the new high score in constants in order to present it
            # later in the game-over background
            constants.high_score = constants.player_score
            # Write the new high score in the .txt file
            w = open("../assets/high_score.txt", "w")
            w.write(str(constants.player_score))
            w.close()
        r.close()
        self.background_manager.game_over = True
        self.game_loop = False

    def dev_mode(self):
        if pyxel.btnp(pyxel.KEY_E):
            self.enemy_manager.create_enemy(0, 0, "Red")
        if pyxel.btnp(pyxel.KEY_P):
            constants.player_is_alive = False
        if pyxel.btnp(pyxel.KEY_G):
            constants.player_lives = 0
            self.game_over()

App()
