# Monochromatic Squares

# DEFINITION: A square Q with side length n € N is subdivided into n^2 squares of side length 1 that are all parallel to Q. 
# Each one of the small squares is either colored grey or white.

# GOAL: The goal is to determine the side length and the position of the biggest square in Q that is completely colored in 
# white and parallel to Q. 
# NOTE: In case there is more than one such square, any one of those may be chosen.

# ASSUME: Upper left corner of the square is at (0, 0) and the lower right corner is at (n, n). 
# Going down increases the x-coordinate and going right increases the y-coordinate.
# S.t. it will have the same structure as the list representation of a 2D array => Easier debugging.

import matplotlib.pyplot as plt
import random

def create_square_grid(grid_size):
    h = w = grid_size
    fig, ax = plt.subplots()
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect('equal')
    # Draw vertical grid lines
    for x in range(w + 1):
        ax.axvline(x, color='black', linewidth=1)
    # Draw horizontal grid lines
    for y in range(h + 1):
        ax.axhline(y, color='black', linewidth=1)
    # Remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    # Set background color to white
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    return fig, ax

def paint_square_grey(loc):
    x, y = loc
    ax = plt.gca()
    # Create a grey rectangle at (y, grid_size - x - 1) with no border
    rect = plt.Rectangle((y, grid_size - x - 1), 1, 1, color='grey', linewidth=0)
    ax.add_patch(rect)

def create_selection_square(lower_right_loc, side_length, color='red', facecolor='none'):
    x, y = lower_right_loc
    ax = plt.gca()
    # Calculate the upper left corner from the lower right corner
    upper_left_x = x - side_length + 1
    upper_left_y = y - side_length + 1
    # Create a rectangle with thick borders around the selected area
    rect = plt.Rectangle((upper_left_y, grid_size - upper_left_x - side_length), side_length, side_length, linewidth=3, edgecolor=color, facecolor=facecolor)
    ax.add_patch(rect)

# we will start the search from upper left corner and go towards the lower right corner
def find_largest_white_square(grid_size, grey_squares):
    A = [[0 for _ in range(grid_size)] for _ in range(grid_size)] # side length of the biggest white square that has its lower left corner at (i, j)
    for i in range(grid_size):
        if (i, 0) not in grey_squares:
            A[i][0] = 1
        if (0, i) not in grey_squares:
            A[0][i] = 1

    for i in range(1, grid_size):
        for j in range(1, grid_size):
            if (i, j) not in grey_squares:
                A[i][j] = min(A[i-1][j], A[i][j-1], A[i-1][j-1]) + 1 # If the current square is white, then look at the left, top and top-left squares (note that we are coming from the upper left corner). To form a square, current white square must extend towards left, top and diagonally. So, we take the minimum of these three and add 1 to it because minimum will be the bottleneck for the square to extend. And plus 1 because it extends all previous squares by 1.
    
    max_side_length = 0
    max_side_length_loc = (0, 0)
    for i in range(grid_size):
        for j in range(grid_size):
            if A[i][j] > max_side_length:
                max_side_length = A[i][j]
                max_side_length_loc = (i, j)

    return max_side_length, max_side_length_loc

if __name__ == "__main__":
    grid_size = 30
    n_grey_squares = 200

    # Setup the grid
    fig, ax = create_square_grid(grid_size)
    grey_squares = [(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(n_grey_squares)]
    for square in grey_squares:
        paint_square_grey(square)
    
    print("Grey squares:", grey_squares)

    # Find the largest white square
    max_side_length, max_side_length_loc = find_largest_white_square(grid_size, grey_squares)

    create_selection_square(max_side_length_loc, max_side_length)

    plt.show()