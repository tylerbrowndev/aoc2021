f = open("../input/9.txt", "r")
lines = f.readlines()

heightmap = []
for line in lines:
  heightmap.append([int(c) for c in line.strip()])

def part1(heightmap):
  risk = 0
  for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
      val = heightmap[i][j]
      smallest = True
      if i > 0 and val >= heightmap[i - 1][j]:
        smallest = False
      if i < len(heightmap) - 1 and val >= heightmap[i + 1][j]:
        smallest = False
      if j > 0 and val >= heightmap[i][j - 1]:
        smallest = False
      if j < len(heightmap[0]) - 1 and val >= heightmap[i][j + 1]:
        smallest = False
      if smallest:
        risk += val + 1
  return risk

def part2(heightmap):
  def find_basin_size(i, j):
    val = heightmap[i][j]
    if (str(i) + '-' + str(j)) in visited or val == 9:
      return 0
    size = 1
    visited.add(str(i) + '-' + str(j))

    if i > 0:
      size += find_basin_size(i - 1, j)
    if i < m - 1:
      size += find_basin_size(i + 1, j)
    if j > 0:
      size += find_basin_size(i, j - 1)
    if j < n - 1:
      size += find_basin_size(i, j + 1)
    return size

  m = len(heightmap)
  n = len(heightmap[0])
  basin_sizes = []
  visited = set()

  for i in range(m):
    for j in range(n):
      size = find_basin_size(i, j)
      if size == 1:
        print(i, j)
      if size != 0:
        basin_sizes.append(size)
  basin_sizes.sort(reverse = True)
  return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


print(part1(heightmap))
print(part2(heightmap))