"""
This class is used to save methods that are used in more than one class

"""
# Player variables throughout the game
# The player_is_alive variable changes every time a life of the player is taken away.
# When the lives reach 0, then its game over
player_is_alive = True
player_lives = 3
player_score = 0
enemies_killed = 0
f = open("../assets/high_score.txt", "r")
high_score = f.read()
f.close()
new_highscore = False
# Game variables: App variables
screen_width = 128
screen_height = 128
normal_sprite_width = 16
normal_sprite_height = 16
# Hit-box magnitudes for basic sprite
hitbox_x = 16
hitbox_y = 16
# The file saving the high-score
"""
high_score_file_write = open('high_score.txt', "w")
high_score_file_read = open("high_score.txt","r")
"""


# Takes a list and draws all the elements
def draw_list(list):
    for i in range(len(list)):
        list[i].draw()

# Takes a list checks and removes all elements that have is alive false
def update_list_and_delete(list):
    for index in range(len(list) - 1, -1, -1):
        if list[index].is_alive:
            list[index].update()
        else:
            del (list[index])
