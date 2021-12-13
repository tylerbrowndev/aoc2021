f = open("../input/12.txt", "r")
lines = f.readlines()


def part1(lines):
  def traverse(cave, path):
    new_path = [x for x in path]
    if cave == 'end':
      new_path.append(cave)
      paths.append(new_path)
      return
    if cave.lower() == cave:
      if cave in new_path:
        return
    new_path.append(cave)
    for c in routes[cave]:
      traverse(c, new_path)

  routes = {}
  paths = []
  for line in  lines:
    start_cave, end_cave = line.strip().split('-')
    if start_cave in routes:
      routes[start_cave].append(end_cave)
    else:
      routes[start_cave] = [end_cave]
    if end_cave in routes:
      routes[end_cave].append(start_cave)
    else:
      routes[end_cave] = [start_cave]

  traverse('start', [])

  return len(paths)

def part2(lines):
  def traverse(cave, path, small_cave):
    new_path = [x for x in path]
    if cave == 'end':
      new_path.append(cave)
      if small_cave:
        if new_path.count(small_cave) > 1:
          paths.append(new_path)
      else:
        paths.append(new_path)
      return
    if cave.lower() == cave:
      if cave in new_path:
        if cave == small_cave:
          if new_path.count(cave) > 1:
            return
        else:
          return
    new_path.append(cave)
    for c in routes[cave]:
      traverse(c, new_path, small_cave)

  routes = {}
  paths = []
  for line in  lines:
    start_cave, end_cave = line.strip().split('-')
    if start_cave in routes:
      routes[start_cave].append(end_cave)
    else:
      routes[start_cave] = [end_cave]
    if end_cave in routes:
      routes[end_cave].append(start_cave)
    else:
      routes[end_cave] = [start_cave]

  small_caves = []
  for key in routes.keys():
    if key.lower() == key and key != 'start' and key != 'end':
      small_caves.append(key)
  traverse('start', [], '')
  for cave in small_caves:
    traverse('start', [], cave)

  return len(paths)

print(part1(lines))
print(part2(lines))