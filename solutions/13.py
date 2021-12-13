f = open("../input/13.txt", "r")
lines = f.readlines()

vals = []
instructions = []
max_x = 0
max_y = 0
for line in lines:
  if ',' in line:
    x, y = line.strip().split(',')
    x = int(x)
    y = int(y)
    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y
    vals.append((x, y))
  elif 'fold' in line:
    axis, val = line.strip().split('=')
    instructions.append((axis[-1], int(val)))
grid = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]
for val in vals:
  grid[val[0]][val[1]] = 1

def fold(grid, axis, val):
  if axis == 'y':
    grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
  first_half_grid = grid[:val]
  second_half_grid = grid[val + 1:]
  len_first = len(first_half_grid)
  len_second = len(second_half_grid)
  if len_first > len_second:
    for _ in range(len_first - len_second):
      second_half_grid.append([0 for _ in range(len(second_half_grid[0]))])
  elif len_second > len_first:
    for _ in range(len_second - len_first):
      first_half_grid.insert(0, [0 for _ in range(len(first_half_grid[0]))])
  second_half_grid.reverse()
  new_grid = []
  for i in range(len(first_half_grid)):
    row = []
    for j in range(len(first_half_grid[0])):
      val = first_half_grid[i][j] + second_half_grid[i][j]
      row.append(val)
    new_grid.append(row)
  
  if axis == 'y':
    new_grid = [[row[i] for row in new_grid] for i in range(len(new_grid[0]))]
  return new_grid

def part1(grid, instructions):
  new_grid = fold(grid, instructions[0][0], instructions[0][1])
  total = 0
  for row in new_grid:
    for val in row:
      if val != 0:
        total += 1
  return total

def part2(grid, instructions):
  for instruction in instructions:
    grid = fold(grid, instruction[0], instruction[1])
  grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
  for row in grid:
    s = ''
    for val in row:
      s += 'X' if val > 0 else ' '
    print(s)

print(part1(grid, instructions))
part2(grid, instructions)