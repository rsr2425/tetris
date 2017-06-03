"""
    Block Testing Suite

    Contains all tests for the Tetromino pieces in tetris, using the
    testing framework PyTest.
"""
import os, sys
sys.path.append(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))))

import pytest
from blocks import Tetromino, Directions as D

@pytest.fixture
def block():
    return Tetromino()

@pytest.fixture
def stationary_block():
    t = Tetromino()
    t.falling = False
    return t

@pytest.mark.usefixtures('block','stationary_block')
class TestTetromino(object):
    def test_creation(self, block):
        """
        Test the initial conditions of newly created blocks.

        :param block: Fixture with newly created, unmodified Tetromino() obj.
        :sig: block -> ()
        """
        assert (block._orientation == D.UP)
        assert (block.falling == True)
        assert (block._prev_loc == block._loc)

    def test_static_block(self, stationary_block):
        """
        Test a block that is no longer falling.

        :sig: () -> ()
        """
        assert stationary_block.falling == False
        orig_loc = stationary_block._loc
        stationary_block.down()
        assert stationary_block._loc == orig_loc
        stationary_block.right()
        assert stationary_block._loc == orig_loc
        stationary_block.left()
        assert stationary_block._loc == orig_loc
        stationary_block.clockwise()
        assert stationary_block._loc == orig_loc
        stationary_block.counterclockwise()
        assert stationary_block._loc == orig_loc

    def test_rotate(self, block):
        block.clockwise()
        assert block._orientation == D.RIGHT
        block._orientation = D.LEFT
        block.clockwise()
        assert block._orientation == D.UP

        block.counterclockwise()
        assert block._orientation == D.LEFT

