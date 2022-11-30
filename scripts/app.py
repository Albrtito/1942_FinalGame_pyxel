import pyxel
from player import Player
from projectileManager import ProjectileManager
from enemy import Enemy



# enemy_visible = False
HEIGHT = 128
WIDTH = 128
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16


# score = 0
# highscore = 20
class App:
    def __init__(self):
        # Classes attribute
        self.projectile_manager = ProjectileManager()
        self.player = Player(int(WIDTH / 2), int(HEIGHT / 2),self.projectile_manager)



        # Screen attributes
        self.score = 0
        self.best_score = 20

        # Initialize pyxel
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load('../assets/App.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        # The game will quit when Q is pressed
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Update of the game objects
        self.player.update()
        self.projectile_manager.update()

    def draw(self):
        # Background:
        pyxel.cls(0)
        pyxel.bltm(x=0, y=0, tm=0, u=0, v=0, w=WIDTH, h=HEIGHT)
        pyxel.text(30, 1, f"Highest Score: {self.best_score}", 7)
        pyxel.text(30, 7, f"Current Score: {self.score}", 7)

        # Draw all the objects on screen
        # Making the enemies appear
        """
        if pyxel.btn(pyxel.KEY_S):
            global enemy
            enemy = Enemy
            pyxel.blt(10, 10, 0, 44, 4, 8, 8, colkey=0)
            pyxel.blt(70, 10, 0, 59, 4, 10, 9, colkey=0)
            pyxel.blt(30,10,0,73,3,14,11,colkey=0)
            pyxel.blt(50, 10, 0, 89, 0, 14, 16, colkey=0)
"""

        # Draw player
        self.player.draw()
        # Draw bullets
        self.projectile_manager.draw()


App()
