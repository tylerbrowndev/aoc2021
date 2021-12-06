f = open("../input/6.txt", "r")
input = f.readlines()

vals = [int(n) for n in input[0].strip().split(',')]

def part1(vals):
  fish_breeding_groups = []
  for i in range(9):
    fish_breeding_groups.append({
      'cycle': i,
      'count': 0
    })
  
  for val in vals:
    fish_breeding_groups[val]['count'] += 1
  
  for _ in range(80):
    new_fish_breeding_groups = []
    for group in fish_breeding_groups:
      if group['cycle'] == 0:
        new_fish_breeding_groups.append({
          'cycle': 8,
          'count': group['count']
        })
        new_fish_breeding_groups.append({
          'cycle': 6,
          'count': group['count']
        })
      else:
        new_fish_breeding_groups.append({
          'cycle': group['cycle'] - 1,
          'count': group['count']
        })
    fish_breeding_groups = new_fish_breeding_groups
  total = 0
  for group in fish_breeding_groups:
    total += group['count']

  return total

def part2(vals):
  fish_breeding_groups = [0 for _ in range(7)]

  for val in vals:
    fish_breeding_groups[val] += 1

  offset = 0
  fish_queue = [0, 0]
  for i in range(256):
    fish_queue.append(fish_breeding_groups[offset])
    fish_breeding_groups[offset] += fish_queue.pop(0)
    offset = (offset + 1) % 7

  for leftover_fish in fish_queue:
    fish_breeding_groups[offset] += leftover_fish
    offset = (offset + 1) % 7

  return sum(fish_breeding_groups)

print(part1(vals))
print(part2(vals))