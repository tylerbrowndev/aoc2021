f = open("../input/14.txt", "r")
lines = f.readlines()

def part1(lines):
  sequence = lines[0].strip()
  d = {}
  for line in lines[2:]:
    key, val = line.strip().split(' -> ')
    d[key] = val

  for _ in range(10):
    new_sequence = ''
    for i in range(len(sequence) - 1):
      key = sequence[i:i + 2]
      if i == 0:
        new_sequence += key[0]
      new_sequence += d[key] + key[1]
    sequence = new_sequence
  chars = [c for c in sequence]
  max_char = max(set(chars), key=chars.count)
  min_char = min(set(chars), key=chars.count)
  return sequence.count(max_char) - sequence.count(min_char)

def part2(lines):
  def copy_dict(d):
    new_dict = {}
    for key, val in d.items():
      new_dict[key] = val
    return new_dict

  sequence = lines[0].strip()
  d = {}
  for line in lines[2:]:
    key, val = line.strip().split(' -> ')
    d[key] = val

  freqs = {}
  for i in range(len(sequence) - 1):
      key = sequence[i:i + 2]
      if key in freqs:
        freqs[key] += 1
      else:
        freqs[key] = 1

  for _ in range(40):
    new_freqs = copy_dict(freqs)

    for key, val in freqs.items():
      if val == 0:
        continue
      c = d[key]
      first_pair = key[0] + c
      second_pair = c + key[1]
      new_freqs[key] -= val
      if first_pair in new_freqs:
        new_freqs[first_pair] += val
      else:
        new_freqs[first_pair] = val
      if second_pair in new_freqs:
        new_freqs[second_pair] += val
      else:
        new_freqs[second_pair] = val

    freqs = copy_dict(new_freqs)

  counts = {}
  for key, val in freqs.items():
    if key[1] in counts:
      counts[key[1]] += val
    else:
      counts[key[1]] = val
  counts[sequence[0]] += 1
  return max(counts.values()) - min(counts.values())

print(part1(lines))
print(part2(lines))