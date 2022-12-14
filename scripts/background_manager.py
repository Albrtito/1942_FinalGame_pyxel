import pyxel
import constants
from wave_manager import WaveManager


class BackgroundManager:
    def __init__(self, screen_width: int, screen_height: int, wave_manager: WaveManager):
        # Graphics variables
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position_v = 240 * 8

        # Variables for the different stages of the game
        self.game_over = False
        self.first_screen = True
        self.initial_screen = False
        # Wave manager is only used inside the class -> private
        self.__wave_manager = wave_manager

        # Variables for the movement of the background and graphics
        # Private variable as it is only used inside the class
        self.__background_roll_step = 1

    # Properties and setters for width and height of the screen
    @property
    def screen_width(self):
        return self.__screen_width

    @screen_width.setter
    def screen_width(self, screen_width: bool):
        # Only change if giving an int
        if type(screen_width) != int:
            raise TypeError("Screen width must be an int")
        self.__screen_width = screen_width

    @property
    def screen_height(self):
        return self.__screen_height

    @screen_height.setter
    def screen_height(self, screen_height: int):
        if type(screen_height) != int:
            raise TypeError("Screen height must be an int")
        self.__screen_height = screen_height

    # Property and setter for position_v -> It`s changed in App.class
    @property
    def position_v(self):
        return self.__position_v

    @position_v.setter
    def position_v(self, position_v: int):
        if type(position_v) != int:
            raise TypeError("Position_v must be an int")
        self.__position_v = position_v

    # Property and setter for game_over
    @property
    def game_over(self):
        return self.__game_over

    @game_over.setter
    def game_over(self, game_over: bool):
        if type(game_over) != bool:
            raise TypeError("Game over must be a bool")
        self.__game_over = game_over

    # Property and setter for initial_screen
    @property
    def initial_screen(self):
        return self.__initial_screen

    @initial_screen.setter
    def initial_screen(self, initial_screen: bool):
        if type(initial_screen) != bool:
            raise TypeError("Initial screen must be a bool")
        self.__initial_screen = initial_screen

    # Methods for background_manager class
    def update(self):
        """Update: This method is repeated every frame while the game is played. BackgroundManager.update: Is
        called in app, updates the background of the game when the states change"""
        # The background only actualizes if we are not in the initial screen or the game has not reached to an end
        if (not self.initial_screen) and (not self.game_over):
            # We actualize the background to change. Rolls 1 pixel every frame
            self.position_v -= self.__background_roll_step
            # If the background has reached position_v = 0 then it rolls back to its initial position
            if self.position_v == 0:
                self.position_v = 240 * 8

    def draw(self):
        """Draw: This method is repeated every frame, in it all the objects are drawn in screen. BackgroundManager.draw:
        Draws the background"""
        # If not true that the game has ended, we go through the other different stages
        if not self.game_over:
            # Check if we are at the initial screen, if we are, draw it
            if self.first_screen:
                pyxel.bltm(x=0, y=0, tm=0, u=0, v=110 * 8, w=self.screen_width, h=self.screen_height)
                pyxel.bltm(x=0, y=0, tm=0, u=48 * 8, v=240 * 8, w=self.screen_width, h=self.screen_height, colkey=2)
                if pyxel.frame_count % 5 == 0:
                    pyxel.text(23, 129, f"Insert coin (press i)", 10)
                else:
                    pyxel.text(23, 129, f"Insert coin (press i)", 9)
                pyxel.text(40, 70, f"Controls: ", 0)
                pyxel.text(25, 80, f" * Move: Arrow keys ", 0)
                pyxel.text(25, 90, f" * Shoot: Space ", 0)
                pyxel.text(25, 100, f" * Loop: Z key ", 0)
            elif self.initial_screen:
                # Background: Initial screen
                pyxel.cls(0)
                # Draw the initial screen and the text boxes on top of that in order to see the text when displayed
                pyxel.bltm(x=0, y=0, tm=0, u=0, v=240 * 8, w=self.screen_width, h=self.screen_height)
                pyxel.bltm(x=0, y=0, tm=0, u=32 * 8, v=240 * 8, w=self.screen_width, h=self.screen_height, colkey=2)
                if pyxel.frame_count % 20 == 0:
                    if constants.player_lives == 3:
                        pyxel.text(20, 17, f"PRESS ENTER TO START:", 7)
                    else:
                        pyxel.text(40, 17, f"Start again", 7)
                else:
                    if constants.player_lives == 3:
                        pyxel.text(20, 17, f"PRESS ENTER TO START:", 0)
                    else:
                        pyxel.text(40, 17, f"Start again", 0)
                pyxel.text(45, 55, f" Score:{constants.player_score} ", 0)
                pyxel.text(25, 65, f" Enemies killed: {constants.enemies_killed} ", 0)
                pyxel.text(35, 75, f"High Score: {constants.high_score}", 0)
                self.paint_lives()
            # If we are not in the initial screen  we draw the background of the game
            else:
                # The background roll is changed in the update method.
                pyxel.cls(0)
                # Draw background
                pyxel.bltm(x=0, y=0, tm=0, u=0, v=self.position_v, w=self.screen_width,
                           h=self.screen_height)
                # Draw black box to present lives, scores and other text
                pyxel.bltm(x=0, y=0, tm=0, u=16 * 8, v=239 * 8, w=self.screen_width,
                           h=self.screen_height + 1, colkey=2)
                # Call the method that paints the hearts as lives and changes them
                self.paint_lives()
                # Draw the text
                pyxel.text(80, 130, f"Score: {constants.player_score}", 7)
                pyxel.text(50, 130, f"Wave: {self.__wave_manager.wave}", 5)

        # If the game is over, then the when_game_over method is called
        else:
            self.when_game_over()

    def when_game_over(self):
        """When_game_over: Displays the game over screen with the high score and your score"""
        pyxel.cls(0)
        pyxel.bltm(x=0, y=0, tm=0, u=240 * 8, v=0, w=self.screen_width, h=self.screen_height)
        pyxel.text(40, 55, f" Score:{constants.player_score} ", 7)
        pyxel.text(25, 65, f" Enemies killed: {constants.enemies_killed} ", 7)
        if constants.new_highscore:
            # pyxel.text(25, 85, f"NEW HIGH SCORE: {constants.local_high_score}", 10)
            pyxel.text(25, 85, f"NEW HIGH SCORE: {constants.high_score}", 10)
        else:
            # pyxel.text(30, 75, f"High Score: {constants.local_high_score}", 7)
            pyxel.text(30, 75, f"High Score: {constants.high_score}", 7)
        pyxel.text(10, 100, f"Thanks for playing : )", 2)
        pyxel.text(10, 115, f"ENTER to go again", 2)

    def paint_lives(self):
        """Paint_lives: This method paints hearts in the bottom left corner,the hearts painted vary in the lives the player
        has"""
        # position to pain the hearts in
        position_x = 0
        # we pain a number of hearts based on how many lives we have
        for i in range(constants.player_lives):
            pyxel.blt(position_x, 128, 1, 0, 64, 8, 8, colkey=0)
            position_x += 16
