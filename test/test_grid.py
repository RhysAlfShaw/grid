from ..grid import Grid

def test_grid_empty():
    grid = Grid(4, 4)
    grid.fill(0,0)
    grid.empty(0,0)
    assert grid.nFilled() == 0

def test_grid_fill():
    grid = Grid(4, 4)
    grid.fill(0,0)
    assert grid.nFilled() == 1