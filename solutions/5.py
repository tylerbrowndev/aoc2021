f = open("../input/5.txt", "r")
lines = f.readlines()
n = 1000

def parse_line(line):
  p1, p2 = line.strip().split(' -> ')
  x1, y1 = p1.split(',')
  x1, y1 = int(x1), int(y1)
  x2, y2 = p2.split(',')
  x2, y2 = int(x2), int(y2)
  return x1, y1, x2, y2

def get_danger_zones(grid):
  danger_zones = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] > 1:
        danger_zones += 1
  return danger_zones

def part1(lines):
  grid = [[0 for _ in range(n)] for _ in range(n)]
  for line in lines:
    x1, y1, x2, y2 = parse_line(line)

    if x1 == x2:
      if y1 > y2:
        y1, y2 = y2, y1
      for i in range(y1, y2 + 1):
        grid[i][x1] += 1
    elif y1 == y2:
      if x1 > x2:
        x1, x2 = x2, x1
      for i in range(x1, x2 + 1):
        grid[y1][i] += 1
  return get_danger_zones(grid)

def part2(lines):
  grid = [[0 for _ in range(n)] for _ in range(n)]
  for line in lines:
    x1, y1, x2, y2 = parse_line(line)

    if x1 == x2:
      if y1 > y2:
        y1, y2 = y2, y1
      for i in range(y1, y2 + 1):
        grid[i][x1] += 1
    elif y1 == y2:
      if x1 > x2:
        x1, x2 = x2, x1
      for i in range(x1, x2 + 1):
        grid[y1][i] += 1
    else:
      if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
      direction = 1
      if y1 > y2:
        direction = -1
      c = 0
      for i in range(y1, y2 + direction, direction):
        grid[i][x1 + c] += 1
        c += 1
  return get_danger_zones(grid)

print(part1(lines))
print(part2(lines))
