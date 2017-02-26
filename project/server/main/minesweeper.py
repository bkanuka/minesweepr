# coding: utf-8

import numpy as np

def get_mask(m, n, i):
    """Builds an m by n (flattened) minesweeper grid
    with 1 if a square surrounds square i, 0 otherwise """

    row = i // n
    col = i % n
    
    ind = np.arange(m*n)
    
    mask = np.bitwise_and(np.abs(ind % n - col) <= 1, # indicies are 1 (or less) columns away
                          np.abs(ind // n - row) <= 1) # and indicies are 1 (or less) rows away
    mask = mask.astype(int)
    return mask

def make_grid(m, n, k):
    """Makes an m rows, n columns minesweeper grid 
    with k mines (-1 for mine)"""

    #TODO: enforce k < m*n. silently set k = m*n?
    
    grid = np.zeros(m*n)
    
    mine_indecies = np.arange(m*n)
    np.random.shuffle(mine_indecies)
    mine_indecies = mine_indecies[:k]
    
    #print('mine_indecies:', mine_indecies)
    #print(np.arange(m*n).reshape((m,n)))
    
    for i in mine_indecies:
        mask = get_mask(m, n, i)
        #print(mask.reshape((m,n)))
        grid = grid + mask
    
    grid[mine_indecies] = -1
    #grid.resize((m,n))
    return grid

def new_game(m, n, k):
    grid = make_grid(m, n, k).astype(int).tolist()
    covered = np.ones_like(grid).astype(int).tolist()
    game = {"rows": m,
            "cols": n,
            "grid": grid,
            "covered": covered,
            "current": True,
            }
    return game

if __name__ == "__main__":
    grid = make_grid(8,8,10)
    grid.resize((m,n))
    print(grid)
