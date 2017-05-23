#
# Blocks Module
#
#

class Tetromino(object):
    def __init__(self, x=0, y=0, g=None):
        self.loc = x, y
        self.orient = 'u'
        self.bgrid = g

    def move(self, input):
        raise NotImplemented()

    def rotate_clockwise(self, curr_pos):
        raise NotImplemented()

    def down(self):
        raise NotImplemented()

    def right(self):
        raise NotImplemented()

    def left(self):
        raise NotImplemented()

    def move(self, input):
        raise NotImplemented()

    def get_grid_loc(self):
        raise NotImplemented()

    def in_grid(self):
        raise NotImplemented()


class BoxTetro(Tetromino):
    def down(self):
        fx, fy = self.loc
        if fy + 1 < self.bgrid.sqy - 2:
            self.loc = (fx, fy+1)

    def right(self):
        fx, fy = self.loc
        if fx + 1 >= self.bgrid.sqx - 1:
            self.loc = (0, fy)
        else:
            self.loc = (fx+1, fy)

    def left(self):
        fx, fy = self.loc
        if fx - 1 < 0:
            self.loc = self.bgrid.sqx - 2, fy
        else:
            self.loc = (fx-1, fy)

    def rotate_clockwise(self):
        pass

    # TODO need to include some kind of bounding checks
    def get_grid_loc(self):
        x, y = self.loc
        return [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]

class TTetro(Tetromino):
    def rotate_clockwise(self, curr_pos):
        raise NotImplemented()

    def down(self):
        fx, fy = self.loc
        if fy + 1 < self.bgrid.sqy - 1:
            self.loc = (fx, fy+1)

    def right(self):
        fx, fy = self.loc
        if fx + 1 >= self.bgrid.sqx - 1:
            self.loc = (0, fy)
        else:
            self.loc = (fx+1, fy)

    def left(self):
        fx, fy = self.loc
        if fx - 2 < 0:
            self.loc = self.bgrid.sqx - 2, fy
        else:
            self.loc = (fx-1, fy)

    def get_grid_loc(self):
        x, y = self.loc
        return [(x,y), (x+1,y), (x-1,y), (x,y+1)]

    def move(self, input):
        if input == "DOWN":
            self.down()
        elif input == "RIGHT":
            self.right()
        elif input == "LEFT":
            self.left()

class STetro(Tetromino):
    pass

class ZTetro(Tetromino):
    pass

class LTetro(Tetromino):
    pass