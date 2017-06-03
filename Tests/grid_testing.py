"""
    Grid Testing Suite

    Contains all tests for my block grid, using the
    testing framework PyTest.
"""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from grid import BlockGrid, GAME_BLOCK_UNIT

@pytest.fixture
def unit_grid():
    return BlockGrid(0, 0, 10 * GAME_BLOCK_UNIT, 10 * GAME_BLOCK_UNIT, None)

@pytest.mark.usefixtures('unit_grid')
class TestGrid(object):
    def test_init(self, unit_grid):
        assert unit_grid.sqx == 1
        assert unit_grid.sqy == 1
        assert unit_grid.grid == [[0]]
        assert unit_grid.topleftx == 0
        assert unit_grid.toplefty == 0
        assert unit_grid.score == 0
        assert unit_grid.fblock is not None

    def test_update(self, unit_grid):
        pass


class TestRendering(object):
    pass