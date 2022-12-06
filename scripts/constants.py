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
# Hit-box magnitudes for basic sprite
hitbox_x = 16
hitbox_y = 16


def draw_list(list):
    for i in range(len(list)):
        list[i].draw()


def update_list_and_delete(list):
    for index in range(len(list) - 1, -1, -1):
        if list[index].is_alive:
            list[index].update()
        else:
            del (list[index])
