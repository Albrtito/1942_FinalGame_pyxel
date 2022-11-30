class Sprite:
    def __init__(self, position_u: int, position_v: int, width: int, height: int, transparent=8):
        self.position_u = position_u
        self.position_v = position_v
        self.width = width
        self.height = height
        self.transparent = transparent
