from projectileManager import ProjectileManager
from enemyManager import EnemyManager

class Waves:
    def __init__(self, projectile_manager: ProjectileManager):
        self.projectile_manager = projectile_manager
        self.regular = EnemyManager(0,0,5,"Regular",self.projectile_manager)
        self.red = EnemyManager(0,0,2,"Red",self.projectile_manager)
    def update(self):
        self.regular.update()
        self.red.update()
    def draw(self):
        self.regular.draw()
        self.red.draw()

