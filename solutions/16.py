f = open("../input/16.txt", "r")
lines = f.readlines()
hex = lines[0]
binary_string = bin(int('1' + hex, 16))[3:]

VERSION_SIZE = 3
TYPE_SIZE = 3
LITERAL_SIZE = 4
TOTAL_LENGTH_INFO_SIZE = 15
NUM_SUBPACKETS_INFO_SIZE = 11

def part1(binary_string):
  def parse(b):
    i = 0
    version = b[i:i + VERSION_SIZE]
    i += VERSION_SIZE
    type = b[i:i + TYPE_SIZE]
    i += TYPE_SIZE
    if type == '100':
      len_literal = 0
      literal = ''
      last_group = False
      while not last_group:
        last_group = b[i] == '0'
        i += 1
        literal += b[i:i + LITERAL_SIZE]
        i += LITERAL_SIZE
        len_literal += 1 + LITERAL_SIZE
      packets.append((version, type, literal))
      return VERSION_SIZE + TYPE_SIZE + len_literal
    else:
      length_type_id = b[i]
      i += 1
      if length_type_id == '1':
        num_subpackets = int(b[i:i + NUM_SUBPACKETS_INFO_SIZE], 2)
        i += NUM_SUBPACKETS_INFO_SIZE
        packets.append((version, type, b[i:]))
        len_subpackets = 0
        for _ in range(num_subpackets):
          len_subpacket = parse(b[i:])
          i += len_subpacket
          len_subpackets += len_subpacket
        return VERSION_SIZE + TYPE_SIZE + NUM_SUBPACKETS_INFO_SIZE + len(length_type_id) + len_subpackets
      else:
        len_subpackets = int(b[i:i + TOTAL_LENGTH_INFO_SIZE], 2)
        i += TOTAL_LENGTH_INFO_SIZE
        packets.append((version, type, b[i:]))
        bits_parsed = 0
        while bits_parsed < len_subpackets:
          len_subpacket = parse(b[i:])
          bits_parsed += len_subpacket
          i += len_subpacket
        return VERSION_SIZE + TYPE_SIZE + TOTAL_LENGTH_INFO_SIZE + len(length_type_id) + len_subpackets

  packets = []
  parse(binary_string)
  version_sum = 0
  for packet in packets:
    version_sum += int(packet[0], 2)
  return version_sum

def part2(binary_string):
  def custom_reduce(type, vals):
    if type == '000':
      return sum(vals)
    elif type == '001':
      val = 1
      for v in vals:
        val *= v
      return val
    elif type == '010':
      return min(vals)
    elif type == '011':
      return max(vals)
    elif type == '101':
      return 1 if vals[0] > vals[1] else 0
    elif type == '110':
      return 1 if vals[0] < vals[1] else 0
    elif type == '111':
      return 1 if vals[0] == vals[1] else 0

  def parse(b):
    i = 0
    version = b[i:i + VERSION_SIZE]
    i += VERSION_SIZE
    type = b[i:i + TYPE_SIZE]
    i += TYPE_SIZE
    if type == '100':
      len_literal = 0
      literal = ''
      last_group = False
      while not last_group:
        last_group = b[i] == '0'
        i += 1
        literal += b[i:i + LITERAL_SIZE]
        i += LITERAL_SIZE
        len_literal += 1 + LITERAL_SIZE
      return VERSION_SIZE + TYPE_SIZE + len_literal, int(literal, 2)
    else:
      length_type_id = b[i]
      i += 1
      if length_type_id == '1':
        num_subpackets = int(b[i:i + NUM_SUBPACKETS_INFO_SIZE], 2)
        i += NUM_SUBPACKETS_INFO_SIZE
        len_subpackets = 0
        vals = []
        for _ in range(num_subpackets):
          len_subpacket, val = parse(b[i:])
          i += len_subpacket
          len_subpackets += len_subpacket
          vals.append(val)
        val = custom_reduce(type, vals)
        return VERSION_SIZE + TYPE_SIZE + NUM_SUBPACKETS_INFO_SIZE + len(length_type_id) + len_subpackets, val
      else:
        len_subpackets = int(b[i:i + TOTAL_LENGTH_INFO_SIZE], 2)
        i += TOTAL_LENGTH_INFO_SIZE
        bits_parsed = 0
        vals = []
        while bits_parsed < len_subpackets:
          len_subpacket, val = parse(b[i:])
          bits_parsed += len_subpacket
          i += len_subpacket
          vals.append(val)
        val = custom_reduce(type, vals)
        return VERSION_SIZE + TYPE_SIZE + TOTAL_LENGTH_INFO_SIZE + len(length_type_id) + len_subpackets, val

  return parse(binary_string)[1]

print(part1(binary_string))
print(part2(binary_string))