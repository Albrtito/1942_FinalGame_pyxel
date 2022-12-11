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


# main version: Added pyxres and waves
class App:
    def __init__(self):
        # Parameters: No need for properties or setters as the app class only takes values, it doesn`t give any.

        # Objects:
        self.background_manager = BackgroundManager(constants.screen_width, constants.screen_height)
        self.projectile_manager = ProjectileManager()
        self.enemy_manager = EnemyManager(self.projectile_manager)
        self.wave_manager = WaveManager(self.enemy_manager)
        self.player = Player(int(120), int(120), self.projectile_manager)
        self.collision_manager = CollisionManager(self.player, self.enemy_manager, self.projectile_manager)

        # Variables of the game loop: Game loop is true when player is moving and playing. Its private as it`s only used
        # inside the app class
        self.__game_loop = False

        # Initialize pyxel
        pyxel.init(constants.screen_width, constants.screen_height + 8, title="Pyxel 1942")
        pyxel.load('../assets/App.pyxres')
        pyxel.run(self.update, self.draw)


    def update(self):
        """Update: This method is repeated every frame while the game is played:"""

        """
        If the variable game loop is true, the main game loop will be executed, in this loop all objects are
        updated. The quit key is checked and the game over function is checked if the player lives are 0
        and the explosion is done
        """
        if self.__game_loop:
            # The game will quit when Q is pressed
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            # The player explosion variable determines when the explosion of the player is done and
            # the game can go through with the game over screen or starting with one less live
            if self.player.explosion_done:
                if constants.player_lives <= 0:
                    self.game_over()
                self.background_manager.position_v = 240 * 8
                self.background_manager.initial_screen = True
                self.__game_loop = False
            # Update of the game objects

            # CollisionManager update
            self.collision_manager.update()
            # BackgroundManager update
            self.background_manager.update()
            # Player update
            self.player.update()
            # Update of the enemies: Updates the enemy manager
            self.enemy_manager.update()
            # Creation of the enemies: Updates the wave manager
            self.wave_manager.update()
            # Update of the projectiles from the projectile manager
            self.projectile_manager.update()
            # Update of the collisions from the collision manager
            self.collision_manager.update()
            """ The dev mode is a way of easily checking for mistakes in game during development.When active: 
                    + Press E to create an enemy in 0,0 
                    + Press P to make the player explode and see the animation
                    + Press G to enter the game over screen
            """
            self.dev_mode()

        else:
            """
            This state of the game is reached in two occasions: 
            + At the start of the game the initial screen will disappear once return is pressed. The game loop starts.
            + This also checks if that we are at the post-game over moment, 
                 the player has lost a live but has not died yet, the game is set back into the initial screen and shows
                 that a live has been lost
            """

            # When the player looses a live, if the player looses a live, but It's still alive we allow the restart
            # by pressing return
            if constants.player_lives > 0:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    # When pressed return, the game loop is activated, the player is alive and the explosion is set to
                    # false, we enter the game screen instead of the initial one
                    self.__game_loop = True
                    constants.player_is_alive = True
                    self.player.explosion_done = False
                    self.background_manager.initial_screen = False
            # At any moment during the game the background needs to be showing, so its update is always happening
            self.background_manager.update()

    def draw(self):
        """Draw: This method is repeated every frame, in it all the objects are drawn in screen"""

        # If game loop is true, everything is drawn
        if self.__game_loop:
            # Draw background
            self.background_manager.draw()
            # Draw bullets
            self.projectile_manager.draw()
            # Draw the player
            self.player.draw()
            # Draw all enemies
            self.enemy_manager.draw()

        # If the game loop is false the background is still drawn but every object is not
        else:
            self.background_manager.draw()

    def game_over(self):
        """game_over: This method is executed when the player lives reach 0. It changes the background to the end
        screen, writes the highest score in a file to be kept and sets the game_loop variable to false. The
        difference between entering the game_over method and stating that the game loop is false is the following:
        The game loop might be false, but the player can still have a life, the game then restarts. If the game_over
        method is called, that means the player has no lives left to restart the game """
        """
        We now open the high-score file and check if the high score obtained during the game is greater than the max
        high score ever played, if that's the case, the in-game score is written in the file as the new high score: 
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
        # We change a variable in the background manager: "Sending" the message of game over
        self.background_manager.game_over = True
        self.__game_loop = False

    def dev_mode(self):
        """ The dev mode is a way of easily checking for mistakes in game during development.When active:
                            + Press E to create an enemy in 0,0
                            + Press P to make the player explode and see the animation
                            + Press G to enter the game over screen
        """
        if pyxel.btnp(pyxel.KEY_E):
            self.enemy_manager.create_enemy(0, 0, "Red")
        if pyxel.btnp(pyxel.KEY_P):
            constants.player_is_alive = False
        if pyxel.btnp(pyxel.KEY_G):
            constants.player_lives = 0
            self.game_over()


App()
