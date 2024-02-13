# Game of life 

import random
import time
import sys

def print_grid(grid):
  for x in range(grid_size):
    for y in range(grid_size):
      if grid[x][y]:
        print('■', end='')
      else:
        print('□', end='')
    print()

def count_neighbors(grid, x, y):
  neighbors = 0
  for x_diff in [-1,0,1]:
    if (x + x_diff) < 0 or (x + x_diff) > (grid_size - 1):
      continue
    for y_diff in [-1,0,1]:
      if (y + y_diff) < 0 or (y + y_diff) > (grid_size - 1):
        continue
      if x_diff == 0 and y_diff == 0:
        continue
      if grid[x + x_diff][y + y_diff]:
        neighbors += 1
  return neighbors

def dead_or_alive(grid, x, y):
  current_cell = grid[x][y]
  neighbors = count_neighbors(grid, x, y)
  if current_cell:
      if neighbors < 2:
        return 0
      elif 2 <= neighbors <= 3:
        return 1
      elif neighbors > 3:
        return 0
  else:
    if neighbors == 3:
      return 1
    else:
      return 0
      

def iterate(grid):
  return [[dead_or_alive(grid, x, y) for y in range(grid_size)] for x in range(grid_size)]

def move_cursor(num_lines):
  sys.stdout.write(f"\033[{num_lines}A")  # Move cursor up
  # Overwrite the lines with new message
  sys.stdout.write('\r')
  sys.stdout.flush()


grid_size = int(sys.argv[1])
grid = [[random.choice([0,1]) for y in range(grid_size)] for x in range(grid_size)]
iterations = int(sys.argv[2])
for x in range(iterations):
  print("\r")
  grid = iterate(grid)
  print_grid(grid)
  print("\n")
  time.sleep(0.5)
  if x < (iterations - 1):
    move_cursor(grid_size + 3)

