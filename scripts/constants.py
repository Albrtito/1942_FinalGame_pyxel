"""
This class is used to save methods that are used in more than one class

"""
# Player variables throughout the game
player_lives = 3
player_score = 0
player_run_score = 0
# Game variables: App variables
screen_width = 128
screen_height = 128
normal_sprite_width = 16
normal_sprite_height = 16

def draw_list(list):
    for i in range(len(list)):
        list[i].draw()
