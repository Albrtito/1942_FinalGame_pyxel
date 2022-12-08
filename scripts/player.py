import time
import pyxel
import constants
from projectileManager import ProjectileManager
from sprite import Sprite

HEIGHT = 128
WIDTH = 128




# Class player inherits from sprite, this means all basic characteristics of sprites,
# are at first set to the general sprite

class Player:

    def __init__(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):
        # Position variables
        self.position_x = position_x
        self.position_y = position_y
        self.width = constants.normal_sprite_width
        self.height = constants.normal_sprite_height
        # The speed right now is constant but could be named as an attribute
        self.player_speed = 2
        # Draw variables of the player -> make something so this works with class sprite
        self.position_u = 0
        self.loop = False
        # The player can shoot every some ms(rate of fire)
        # The time_between_shots is a timer in order to shoot every rate of fire(ms)
        self.rate_of_fire = 500
        self.time_between_shots = 0
        # The projectile manager for the shots fired by the player
        self.projectile_manager = projectile_manager

    # Property and setter for position_x
    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: int):
        # Only change the position_x to float values
        if type(position_x) != int:
            raise TypeError("The position must be an int")
        else:
            self.__position_x = position_x

    # Property and setter for position_y
    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y: int):
        # Only change the position_y to float values
        if type(position_y) != int:
            raise TypeError("The position must be an int")
        else:
            self.__position_y = position_y

    def update(self):
        # If the key Z is pressed, then the player is in a loop, everything else stops
        if pyxel.btnp(pyxel.KEY_Z):
            print("loop")
            self.loop = True

        # When the player is in a loop we call the animate_move_method, which animates and moves the player in the loop.
        if self.loop and (pyxel.frame_count % 7 == 0):
            self.animate_move_loop()

        if not self.loop:
            # Calls a function that will move the player
            self.move()

            # code for the shooting of the player: If the time since the next shot is bigger than the time between shots
            # and the space key is pressed, shoot
            if time.time() > self.time_between_shots and pyxel.btn(pyxel.KEY_SPACE):
                self.time_between_shots = time.time() + self.rate_of_fire / 1000
                self.shoot()

    def draw(self):
        # If the player is not in the loop, then the animations for its movement are normal
        if not self.loop:
            # Method for the animations of the player, changes the variable position_u
            self.player_animations()

        pyxel.blt(self.position_x, self.position_y, 0, self.position_u, 0, self.width, self.height,
                  colkey=8)

    # Methods for player class

    # Shoot method creates a player projectile in the projectileManager class
    def shoot(self):
        self.projectile_manager.create_projectile(self.position_x, self.position_y, "PlayerProjectile")

    # This function moves the player given an input in the keyboard keys
    def move(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.position_x != 0:
            self.position_x -= self.player_speed
        if pyxel.btn(pyxel.KEY_RIGHT) and self.position_x < constants.screen_width - self.width:
            self.position_x += self.player_speed
        if pyxel.btn(pyxel.KEY_DOWN) and self.position_y < constants.screen_height - self.height:
            self.position_y += self.player_speed
        if pyxel.btn(pyxel.KEY_UP) and self.position_y != 0:
            self.position_y -= self.player_speed
    # This functions changes the variables of self.position_u and self.position_v. This two variables determine which
    # sprite to show, so changing these variables we can change the sprite of the plane that is showing depending on
    # what the plane is doing
        #print(self.position_x,self.position_y)
    def player_animations(self):
        # Update the helix movement every frame
        if self.position_u == 0:
            self.position_u = 16
        else:
            self.position_u = 0

    # Function for the animation and movement of a player when its inside a loop
    def animate_move_loop(self):
        # We set the player to the starting position(it starts in the movement animation)
        if self.position_u == 16:
            self.position_u += 16
        # We pass through each of the animations, one every x frames, stated in the update method
        # Each animation changes the position of the plane by some amount. The plane ends up in the same position
        # so it doesn´t go off-screen
        if self.position_u < 80:
            if self.position_u == 32:
                self.position_y -= 10
            elif self.position_u == 48:
                self.position_y -= 10
            elif self.position_u == 64:
                self.position_y += 20
            elif self.position_u == 80:
                self.position_y -= 20
            self.position_u += 16
        # When the loop is done, we end it by setting the variable loop to false, everything goes back to normal
        else:
            self.loop = False
