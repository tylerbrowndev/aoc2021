f = open("../input/3.txt", "r")
lines = f.readlines()

def part1(lines):
  a = [[c for c in line.strip()] for line in lines]
  a_t = [[row[i] for row in a] for i in range(len(a[0]))]
  gamma = ''
  epsilon = ''
  for col in a_t:
    zeros = col.count('0')
    ones = len(col) - zeros
    if zeros > ones:
      gamma += '0'
      epsilon += '1'
    else:
      gamma += '1'
      epsilon += '0'
  return int(gamma, 2) * int(epsilon, 2)

def part2(lines):

  def filter_matrix(a, col, index, type):
    zeros = col.count('0')
    ones = len(col) - zeros
    most_frequent = '0' if zeros > ones else '1'
    b = []      
    for row in a:
      if type == 'generator' and row[index] == most_frequent:
        b.append(row)
      elif type == 'scrubber' and row[index] != most_frequent:
        b.append(row)
    return b

  a = [[c for c in line.strip()] for line in lines]
  a_t = [[row[i] for row in a] for i in range(len(a[0]))]

  generator = a
  generator_t = a_t
  i = 0
  while len(generator) > 1 and i < len(generator_t):
    generator = filter_matrix(generator, generator_t[i], i, 'generator')
    generator_t = [[row[j] for row in generator] for j in range(len(generator[0]))]
    i += 1

  scrubber = a
  scrubber_t = a_t
  i = 0
  while len(scrubber) > 1 and i < len(scrubber_t):
    scrubber = filter_matrix(scrubber, scrubber_t[i], i, 'scrubber')
    scrubber_t = [[row[j] for row in scrubber] for j in range(len(scrubber[0]))]
    i += 1

  return int(''.join(generator[0]), 2) * int(''.join(scrubber[0]), 2)

print(part1(lines))
print(part2(lines))
