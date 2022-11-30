"""
This class is used to save methods that are used in more than one class

"""


def update_list(list):
    for elem in list:
        elem.update()


def draw_list(list):
    for elem in list:
        elem.draw()
