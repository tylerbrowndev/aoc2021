import sys
import heapq
sys.setrecursionlimit(10**6)

f = open("../input/15.txt", "r")
lines = f.readlines()

risk_map = []
for line in lines:
  risk_map.append([int(c) for c in line.strip()])

def part1(risk_map):
  def traverse(i, j):
    visited.add(str(i) + '-' + str(j))
    adjacents = []
    if i > 0:
      adjacents.append((i - 1, j))
    if i < m - 1:
      adjacents.append((i + 1, j))
    if j > 0:
      adjacents.append((i, j - 1))
    if j < n - 1:
      adjacents.append((i, j + 1))

    for adjacent in adjacents:
      new_distance = distances[str(i) + '-' + str(j)] + risk_map[adjacent[0]][adjacent[1]]
      if new_distance < distances[str(adjacent[0]) + '-' + str(adjacent[1])]:
        distances[str(adjacent[0]) + '-' + str(adjacent[1])] = new_distance

    lowest_risk = (str(m - 1) + '-' + str(n - 1), float('inf'))
    for key, val in distances.items():
      if val < lowest_risk[1] and key not in visited:
        lowest_risk = (key, val)
    i, j = lowest_risk[0].split('-')
    i, j = int(i), int (j)
    if i == m - 1 and j == n - 1:
      return distances[str(i) + '-' + str(j)]
    return traverse(i, j)

  m = len(risk_map)
  n = len(risk_map[0])
  visited = set()
  distances = {}
  for i in range(m):
    for j in range(n):
      distances[str(i) + '-' + str(j)] = float('inf')
  distances['0-0'] = 0
  risk = traverse(0, 0)
  return risk

def part2(risk_map):
  def traverse(i, j):
    while pq:
      risk, key = heapq.heappop(pq)
      i, j = key[0], key[1]

      adjacents = []
      if i > 0:
        adjacents.append((i - 1, j))
      if i < m - 1:
        adjacents.append((i + 1, j))
      if j > 0:
        adjacents.append((i, j - 1))
      if j < n - 1:
        adjacents.append((i, j + 1))

      for adjacent in adjacents:
        new_distance = distances[(i, j)] + expanded_risk_map[adjacent[0]][adjacent[1]]
        if new_distance < distances[(adjacent[0], adjacent[1])]:
          distances[(adjacent[0], adjacent[1])] = new_distance
          heapq.heappush(pq, (new_distance, (adjacent[0], adjacent[1])))

  m = len(risk_map)
  n = len(risk_map[0])
  expanded_risk_map = []
  for _ in range(len(risk_map) * 5):
    expanded_risk_map.append([0 for _ in range(len(risk_map[0]) * 5)])
  for i in range(len(expanded_risk_map)):
    for j in range(len(expanded_risk_map[0])):
      dist = i // m + j // n
      val = risk_map[i % m][j % n] + dist
      if val >= 10:
        val = (val % 10) + 1
      expanded_risk_map[i][j] = val

  m = len(expanded_risk_map)
  n = len(expanded_risk_map[0])
  distances = {}
  pq = [(0, (0, 0))]
  heapq.heapify(pq)
  for i in range(m):
    for j in range(n):
      distances[(i, j)] = float('inf')
  distances[(0, 0)] = 0
  traverse(0, 0)
  return distances[(m - 1, n - 1)]

print(part1(risk_map))
print(part2(risk_map))
