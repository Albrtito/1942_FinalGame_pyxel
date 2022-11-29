import pyxel
from player import Player
from enemy import Enemy
from projectile import Projectile
from projectile import PlayerProjectile
enemy_visible = False
player = None
HEIGHT = 128
WIDTH = 128
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16
score = 0
highscore = 20
class App:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT)
        pyxel.load('../assets/App.pyxres')
        global player
        player = Player(float(WIDTH/2-PLAYER_WIDTH/2),float(HEIGHT-PLAYER_HEIGHT))
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        player.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(x=0, y=0, tm=0, u=0, v=0, w=WIDTH, h=HEIGHT)
        pyxel.text(30,1, f"Highest Score: {highscore}",7)
        pyxel.text(30,7, f"Current Score: {score}",7)
        player.draw()
        if pyxel.btn(pyxel.KEY_S):
            global enemy
            enemy = Enemy
            pyxel.blt(10, 10, 0, 44, 4, 8, 8, colkey=0)
            pyxel.blt(70, 10, 0, 59, 4, 10, 9, colkey=0)
            pyxel.blt(30,10,0,73,3,14,11,colkey=0)
            pyxel.blt(50, 10, 0, 89, 0, 14, 16, colkey=0)

App()