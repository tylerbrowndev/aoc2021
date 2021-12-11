f = open("../input/11.txt", "r")
lines = f.readlines()

part1_grid = []
part2_grid = []
for line in lines:
  part1_grid.append([int(x) for x in line.strip()])
  part2_grid.append([int(x) for x in line.strip()])


def part1(grid):
  def flash(i, j):
    if str(i) + '-' + str(j) in flashers:
      return 0
    flashes = 1
    flashers.add(str(i) + '-' + str(j))
    for k in range(-1, 2):
      for l in range(-1, 2):
        if i + k >= 0 and i + k < len(grid) and j + l >= 0 and j + l < len(grid[0]):
          grid[i + k][j + l] += 1
          if grid[i + k][j + l] > 9:
            flashes += flash(i + k, j + l)
    return flashes

  flashes = 0
  for _ in range(100):
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        grid[i][j] += 1

    flashers = set()
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] > 9:
          flashes += flash(i, j)

    for flasher in flashers:
      i, j = flasher.split('-')
      grid[int(i)][int(j)] = 0

  return flashes

def part2(grid):
  def flash(i, j):
    if str(i) + '-' + str(j) in flashers:
      return
    flashers.add(str(i) + '-' + str(j))
    for k in range(-1, 2):
      for l in range(-1, 2):
        if i + k >= 0 and i + k < len(grid) and j + l >= 0 and j + l < len(grid[0]):
          grid[i + k][j + l] += 1
          if grid[i + k][j + l] > 9:
            flash(i + k, j + l)

  step = 0
  while True:
    all_flashed = True
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] != 0:
          all_flashed = False
          break
    if all_flashed:
      return step

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        grid[i][j] += 1

    flashers = set()
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] > 9:
          flash(i, j)

    for flasher in flashers:
      i, j = flasher.split('-')
      grid[int(i)][int(j)] = 0
    step += 1

print(part1(part1_grid))
print(part2(part2_grid))