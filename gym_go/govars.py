ANYONE = None
NOONE = -1

BLACK = 0
WHITE = 1
TURN_CHNL = 2
INVD_CHNL = 3
PASS_CHNL = 4
DONE_CHNL = 5

NUM_CHNLS = 6


class Group:
    def __init__(self):
        self.locations = set()
        self.liberties = set()