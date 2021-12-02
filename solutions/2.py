f = open("../input/2.txt", "r")
lines = f.readlines()

def part1(lines):
  x = 0
  y = 0
  for line in lines:
    parts = line.split()
    direction = parts[0]
    val = int(parts[1])

    if direction == 'forward':
      x += val
    elif direction == 'down':
      y += val
    else:
      y -= val
  return x * y

def part2(lines):
  x = 0
  y = 0
  aim = 0
  for line in lines:
    parts = line.split()
    direction = parts[0]
    val = int(parts[1])

    if direction == 'forward':
      x += val
      y += aim * val
    elif direction == 'down':
      aim += val
    else:
      aim -= val
  return x * y

print(part1(lines))
print(part2(lines))