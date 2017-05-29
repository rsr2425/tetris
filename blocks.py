#!/usr/bin/env python
"""
 Tetris

 [Write desc. here]
"""

class Tetromino(object):
    UP, DOWN, LEFT, RIGHT, CLOCKWISE, COUNTERCLOCKWISE = range(6)

    def __init__(self, x=0, y=0, g=None):
        self._loc = x, y

        # 0 - up, 1 - right, 2 - down, 3, left
        self._orient = 0

        self.bgrid = g
        self.falling = True
        self._prev_loc = x,y

    def move(self, input):
        # Pieces that have stopped falling shouldn't move
        if not self.falling:
            #pdb.set_trace()
            return None

        self._prev_loc = self._loc

        if input == self.DOWN:
            self.down()
        elif input == self.RIGHT:
            self.right()
        elif input == self.LEFT:
            self.left()
        elif input == self.CLOCKWISE:
            self.clockwise()
        elif input == self.COUNTERCLOCKWISE:
            self.counterclockwise()

    def clockwise(self):
        self._orient = (self._orient + 1) % 4
        print (self._orient)

    def counterclockwise(self):
        self.clockwise()
        self.clockwise()
        self.clockwise()

    # FYI there's no bounds check here yet
    def up(self):
        fx, fy = self._loc
        self._loc = (fx, fy-1)

    def down(self):
        pass

    def right(self):
        pass

    def left(self):
        pass

    def get_grid_loc(self):
        raise NotImplemented()

    def in_grid(self):
        raise NotImplemented()

    def backtrack(self):
        self._loc = self._prev_loc


class BoxTetro(Tetromino):
    def down(self):
        fx, fy = self._loc
        if fy + 1 < self.bgrid.sqy - 1:
            self._loc = (fx, fy+1)
        else:
            self.falling = False

    def right(self):
        fx, fy = self._loc
        if fx + 1 >= self.bgrid.sqx - 1:
            self._loc = (0, fy)
        else:
            self._loc = (fx+1, fy)

    def left(self):
        fx, fy = self._loc
        if fx - 1 < 0:
            self._loc = self.bgrid.sqx - 2, fy
        else:
            self._loc = (fx-1, fy)

    def get_grid_loc(self):
        x, y = self._loc
        return [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]


class TTetro(Tetromino):
    def down(self):
        fx, fy = self._loc
        if fy + 1 < self.bgrid.sqy - 1:
            self._loc = (fx, fy+1)
        else:
            self.falling = False

    def right(self):
        fx, fy = self._loc
        if fx + 1 >= self.bgrid.sqx - 1:
            self._loc = (0, fy)
        else:
            self._loc = (fx+1, fy)

    def left(self):
        fx, fy = self._loc
        if fx - 2 < 0:
            self._loc = self.bgrid.sqx - 2, fy
        else:
            self._loc = (fx-1, fy)

    def get_grid_loc(self):
        if self._orient == 0:
            x, y = self._loc
            return [(x,y), (x+1,y), (x-1,y), (x,y+1)]
        if self._orient == 1:
            x, y = self._loc
            return [(x,y), (x,y-1), (x,y+1), (x-1,y)]
        if self._orient == 2:
            x, y = self._loc
            return [(x,y), (x,y-1), (x-1,y), (x+1,y)]
        if self._orient == 3:
            x, y = self._loc
            return [(x,y), (x+1,y), (x,y-1), (x,y+1)]


class STetro(Tetromino):
    def down(self):
        fx, fy = self._loc
        if fy + 1 < self.bgrid.sqy - 1:
            self._loc = (fx, fy+1)
        else:
            self.falling = False

    def right(self):
        fx, fy = self._loc
        if fx + 1 >= self.bgrid.sqx - 1:
            self._loc = (0, fy)
        else:
            self._loc = (fx+1, fy)

    def left(self):
        fx, fy = self._loc
        if fx - 2 < 0:
            self._loc = self.bgrid.sqx - 2, fy
        else:
            self._loc = (fx-1, fy)

    def get_grid_loc(self):
        x, y = self._loc
        return [(x,y), (x+1,y), (x,y+1), (x-1,y+1)]

class ZTetro(Tetromino):
    def down(self):
        fx, fy = self._loc
        if fy + 1 < self.bgrid.sqy - 1:
            self._loc = (fx, fy+1)
        else:
            self.falling = False

    def right(self):
        fx, fy = self._loc
        if fx + 1 >= self.bgrid.sqx - 1:
            self._loc = (0, fy)
        else:
            self._loc = (fx+1, fy)

    def left(self):
        fx, fy = self._loc
        if fx - 2 < 0:
            self._loc = self.bgrid.sqx - 2, fy
        else:
            self._loc = (fx-1, fy)

    def get_grid_loc(self):
        x, y = self._loc
        return [(x,y), (x-1,y), (x,y+1), (x+1,y+1)]

class LTetro(Tetromino):
    def down(self):
        fx, fy = self._loc
        if fy + 1 < self.bgrid.sqy - 1:
            self._loc = (fx, fy+1)
        else:
            self.falling = False

    def right(self):
        fx, fy = self._loc
        if fx + 1 >= self.bgrid.sqx - 1:
            self._loc = (0, fy)
        else:
            self._loc = (fx+1, fy)

    def left(self):
        fx, fy = self._loc
        if fx - 1 < 0:
            self._loc = self.bgrid.sqx - 2, fy
        else:
            self._loc = (fx-1, fy)

    def get_grid_loc(self):
        x, y = self._loc
        return [(x,y), (x,y-1), (x,y+1), (x+1,y+1)]

class ITetro(Tetromino):
    def down(self):
        fx, fy = self._loc
        if fy + 1 < self.bgrid.sqy - 2:
            self._loc = (fx, fy+1)
        else:
            self.falling = False

    def right(self):
        fx, fy = self._loc
        if fx + 1 >= self.bgrid.sqx:
            self._loc = (0, fy)
        else:
            self._loc = (fx+1, fy)

    def left(self):
        fx, fy = self._loc
        if fx - 1 < 0:
            self._loc = self.bgrid.sqx - 2, fy
        else:
            self._loc = (fx-1, fy)

    def get_grid_loc(self):
        x, y = self._loc
        return [(x,y), (x,y-1), (x,y+1), (x,y+2)]