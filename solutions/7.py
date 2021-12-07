f = open("../input/7.txt", "r")
input = f.readlines()

vals = [int(n) for n in input[0].strip().split(',')]

def part1(vals):
  vals.sort()
  target = vals[len(vals) // 2]
  fuel = 0
  for val in vals:
    fuel += abs(val - target)

  return fuel

def part2(vals):
  target = int(round(sum(vals) / (len(vals) * 1.0)))

  min_fuel = -1
  for i in range(target - 1, target + 1):
    fuel = 0
    for val in vals:
      diff = abs(val - i)
      fuel += sum(range(diff + 1))
    if min_fuel == -1 or fuel < min_fuel:
      min_fuel = fuel
  return min_fuel

print(part1(vals))
print(part2(vals))
