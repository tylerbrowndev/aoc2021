f = open("../input/25.txt", "r")
lines = f.readlines()

cucumber_map = []
for line in lines:
  cucumber_map.append([c for c in line.strip()])

def part1(cucumber_map):
  m = len(cucumber_map)
  n = len(cucumber_map[0])
  step = 0
  cucumber_moved = True
  while cucumber_moved:
    cucumber_moved = False
    new_cucumber_map = [row[:] for row in cucumber_map]
    for i in range(m):
      for j in range(n):
        if cucumber_map[i][j] == '>':
          if cucumber_map[i][(j + 1) % n] == '.':
            cucumber_moved = True
            new_cucumber_map[i][j] = '.'
            new_cucumber_map[i][(j + 1) % n] = '>'
    cucumber_map = new_cucumber_map
    new_cucumber_map = [row[:] for row in cucumber_map]
    for i in range(m):
      for j in range(n):
        if cucumber_map[i][j] == 'v':
          if cucumber_map[(i + 1) % m][j] == '.':
            cucumber_moved = True
            new_cucumber_map[i][j] = '.'
            new_cucumber_map[(i + 1) % m][j] = 'v'
    cucumber_map = new_cucumber_map
    step += 1
  return step

print(part1(cucumber_map))
