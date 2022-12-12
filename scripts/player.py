import time
import pyxel
import constants
from projectileManager import ProjectileManager


class Player:
    """Class player: Creates objects with all the properties of the player, the controls, shooting method and animations
    of the player are run on this class"""

    def __init__(self, position_x: int, position_y: int, projectile_manager: ProjectileManager):
        """The player init method is declared with 3 parameters, two for the initial position in which the player is
        positioned and the last one is an object of type ProjectileManager, this object handles the projectiles created
        by the player"""

        # Player parameters:

        # Position variables
        self.position_x = position_x
        self.position_y = position_y
        # The speed right now is constant but could be named as an attribute
        self.player_speed = 2
        # Draw variables of the player -> Position on the image bank (u and v), both private because they are only used
        # in this class, width and height of the sprite on bank
        self.__position_u = 0
        self.__position_v = 0
        # Boolean properties for game states: They are both properties as other classes outside need changing them
        self.loop = False
        self.explosion_done = False
        # The player can shoot every some ms(rate of fire) : Private value of the player
        # The time_between_shots is a timer in order to shoot every rate of fire(ms) : Private value of the player
        self.__rate_of_fire = 500
        self.__time_between_shots = 0
        # The projectile manager for the shots fired by the player. Does not need a setter, its private for the player
        self.__projectile_manager = projectile_manager
        # Loop cooldown in seconds: Defines the time between loops
        self.__loop_cooldown = 2

    # Property and setter for position_x: It can only be given an int.
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

    # Property and setter for position_y: It can only be given an int
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

    # Property for sprite width: This property is read only, it doesn`t have a setter
    @property
    def width(self):
        return constants.normal_sprite_width

    # Property for sprite height: This property is read only, it doesn`t have a setter
    @property
    def height(self):
        return constants.normal_sprite_height

    # Property and setter for loop: This property is only read outside the player file, but is changed in methods from
    # player, so it needs a setter
    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, loop: bool):
        # Only change loop if it's a bool
        if type(loop) != bool:
            raise TypeError("Loop must be a bool")
        else:
            self.__loop = loop

    # Property for the boolean that determines if the player is exploding: True when exploding
    @property
    def explosion_done(self):
        return self.__explosion_done

    @explosion_done.setter
    def explosion_done(self, explosion_done: bool):
        # Only change loop if it's a bool
        if type(explosion_done) != bool:
            raise TypeError("Loop must be a bool")
        else:
            self.__explosion_done = explosion_done

    def update(self):
        """Update: This method is repeated every frame while the game is played. Player.update:Is called in
        App.update """
        # If the player is in the alive state it can move,shoot and do loops.
        if constants.player_is_alive:
            # If the key Z is pressed, then the player is in a loop, everything else stops
            if pyxel.btnp(pyxel.KEY_Z):
                print("loop")
                self.loop = True

            # When the player is in a loop we call the animate_move_method, which animates and moves the player in
            # the loop.
            if self.loop:
                # This method not only moves the player but also changes animations even though
                # it shares properties with the update and the draw methods.
                # Because of the changes in the x, y position we have implemented it in the update method
                self.animate_move_loop()

            # If the player is not doing a loop then it can move freely using the keys and shoot using space.
            if not self.loop:
                # Calls a function that will move the player
                self.move()

                # code for the shooting of the player: If the time since the next shot is bigger than the time
                # between shots and the space key is pressed, shoot
                if time.time() > self.__time_between_shots and pyxel.btn(pyxel.KEY_SPACE):
                    self.__time_between_shots = time.time() + self.__rate_of_fire / 1000
                    # Function for shooting
                    self.shoot()

    def draw(self):
        """Draw: This method is repeated every frame, in it all the objects are drawn in screen. Player.draw:
        The function draw of the player is called inside app.draw"""
        # As in the player update method, if the player is alive then it`s drawn in the screen
        if constants.player_is_alive:
            # If the player is not in the loop, then the animations for its movement are given by the player_animations
            # method
            if not self.loop:
                # Method for the animations of the player, changes the variable position_u
                self.player_animations()
        # If the player is not alive, then it means it has either lost a live or died finally, for both of those
        # occasions an explosion is painted in the screen where the player was
        else:
            self.animate_explosion_restart()
        # The animations methods(player_animations, animate_explosion_restart and loop) only change the position_u and
        # position_v of the player sprite, then this line draws the player given those parameters
        pyxel.blt(self.position_x, self.position_y, 0, self.__position_u, self.__position_v, self.width, self.height,
                  colkey=8)

    # Methods for player class


    def shoot(self):
        """ Shoot: creates a player projectile with the projectile_manager object"""
        self.__projectile_manager.create_projectile(self.position_x, self.position_y, "PlayerProjectile")


    def move(self):
        """Move: This function moves the player given an input in the keyboard key and the speed"""
        if pyxel.btn(pyxel.KEY_LEFT) and self.position_x != 0:
            self.position_x -= self.player_speed
        if pyxel.btn(pyxel.KEY_RIGHT) and self.position_x < constants.screen_width - self.width:
            self.position_x += self.player_speed
        if pyxel.btn(pyxel.KEY_DOWN) and self.position_y < constants.screen_height - self.height:
            self.position_y += self.player_speed
        if pyxel.btn(pyxel.KEY_UP) and self.position_y != 0:
            self.position_y -= self.player_speed

    #
    # print(self.position_x,self.position_y)
    def player_animations(self):
        if constants.cheats:
            self.__position_v = 144
        """Player animations: This functions changes the variables of self.position_u and self.position_v. This two
        variables determine which sprite to show, so changing these variables we can change the sprite of the plane
        that is showing depending on what the plane is doing """
        # Update the helix movement every frame. Changes between 0 and 16 in position_u
        if self.__position_u == 0:
            self.__position_u = 16
        else:
            self.__position_u = 0

    def animate_move_loop(self):
        if constants.cheats:
            self.__position_v = 0
        """Animate_move_loop: Moves and animates the player to do a loop, changes position_x, position_y, position_v
        and position_u"""
        # We set the player to the starting position(it starts in the movement animation)
        if self.__position_u == 16:
            self.__position_u += 16
        # We pass through each of the animations, one every x frames, stated in the update method
        # Each animation changes the position of the plane by some amount. The plane ends up in the same position
        # so it doesn´t go off-screen

        # The animation will be run every 7 frames
        if pyxel.frame_count % 7 == 0:
            if self.__position_u < 80:
                if self.__position_u == 32:
                    self.position_y -= 10
                elif self.__position_u == 48:
                    self.position_y -= 10
                elif self.__position_u == 64:
                    self.position_y += 20
                elif self.__position_u == 80:
                    self.position_y -= 20
                self.__position_u += 16
            # When the loop is done, we end it by setting the variable loop to false, everything goes back to normal
            else:
                self.loop = False

    def animate_explosion_restart(self):
        """animate_explosion_restart: Animates the explosion of the player. When the explosion is done
        the explosion_done variable turns to true and the position of the player sprite in
         the bank is returned to 0,0 and its position in-game is returned to the initial position"""
        # The animation will be run every 3 frames
        if pyxel.frame_count % 3 == 0:
            self.__position_v = 128
            # The position_u is updated every 3 frames to plus 16 from last one
            if self.__position_u < 96:
                self.__position_u += 16
            else:
                self.explosion_done = True
                self.__position_u = 0
                self.__position_v = 0
                # When the player explodes, it has to reappear later, for it to reappear in the right place we need to
                # change the position to the initial position
                self.position_x = 60
                self.position_y = 100
