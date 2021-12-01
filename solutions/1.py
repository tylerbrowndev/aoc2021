f = open("../input/1.txt", "r")
lines = f.readlines()

vals = [int(x.strip()) for x in lines]

def part1(vals):
  increases = 0

  prev = vals.pop(0)
  for val in vals:
    if val > prev:
      increases += 1
    prev = val
  return increases

def part2(vals):
  l = len(vals)
  prev =  0
  increases = -1
  for i in range(l):
    if i + 2 < l:
      group_sum = sum(vals[i:i+3])
      if group_sum > prev:
        increases += 1
      prev = group_sum
  return increases

print(part1(vals))
print(part2(vals))