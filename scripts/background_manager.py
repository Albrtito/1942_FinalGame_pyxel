import pyxel
import constants


class BackgroundManager:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Variables for the different stages of the game
        self.initial_screen = True
        self.game_over = False
        self.level = 0
        # Variables for the movement of the background and graphics
        self.background_roll = 0
        # Screen attributes
        self.score = 0
        self.best_score = 20



    @property
    def game_over(self):
        return self.__game_over

    @game_over.setter
    def game_over(self, game_over: bool):
        if type(game_over) != bool:
            raise TypeError("Game over must be a bool")
        self.__game_over = game_over

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

    def update(self):
        # The background only actualizes if we are not in the initial screen or the game has not reached to an end
        if (not self.initial_screen) and (not self.game_over):
            self.background_roll += 1

    def draw(self):
        # If not true that the game has ended, we go through the other different stages
        if not self.game_over:
            # Check if we are at the initial screen, if we are, draw it
            if self.initial_screen:
                # Background: Initial screen
                pyxel.cls(0)
                # Load images that are going to be used for the background
                pyxel.bltm(x=0, y=0, tm=0, u=0, v=240*8, w=self.screen_width, h=self.screen_height)
                pyxel.text(self.screen_width / 8, self.screen_height / 8, f"PRESS ENTER TO START:", 7)
            else:
                # Background: The roll is not well done but works
                pyxel.cls(0)
                pyxel.bltm(x=0, y=0, tm=0, u=0, v=240 * 8 - self.background_roll, w=self.screen_width,
                           h=self.screen_height)
                pyxel.text(30, 1, f"Highest Score: {self.best_score}", 7)
                pyxel.text(30, 7, f"Current Score: {self.score}", 7)
                pyxel.text(30, 120, f"LIVES: {constants.player_lives}", 7)
        else:
            self.when_game_over()

    def when_game_over(self):
        pyxel.cls(0)
        pyxel.bltm(x=0, y=0, tm=0, u=240 * 8, v=0, w=self.screen_width, h=self.screen_height)
        # pyxel.text(30, 1, f"GAME OVER ", 7)
