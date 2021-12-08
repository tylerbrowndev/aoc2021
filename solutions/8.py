f = open("../input/8.txt", "r")
lines = f.readlines()

def part1(lines):
  total = 0
  for line in lines:
    input, output = line.strip().split(' | ')
    for val in output.split():
      if [2, 3, 4, 7].count(len(val)):
        total += 1
  return total

def part2(lines):
  codes = []
  for line in lines:
    input, output = line.strip().split(' | ')

    partial_inputs = input.split()
    partial_inputs.sort(key=len)
    val_dict = {}
    for partial_input in partial_inputs:
      mystery_val = { c for c in partial_input }
      l = len(mystery_val)
      if l == 2:
        val_dict['1'] = mystery_val
      elif l == 3:
        val_dict['7'] = mystery_val
      elif l == 4:
        val_dict['4'] = mystery_val
      elif l == 5:
        # must be 2, 3, or 5
        if mystery_val.intersection(val_dict['7']) == val_dict['7']:
          val_dict['3'] = mystery_val
        elif len(mystery_val.intersection(val_dict['4'])) == 2:
          val_dict['2'] = mystery_val
        else:
          val_dict['5'] = mystery_val
      elif l == 6:
        # must be 0, 6, or 9
        if mystery_val.intersection(val_dict['4']) == val_dict['4']:
          val_dict['9'] = mystery_val
        elif mystery_val.intersection(val_dict['7']) == val_dict['7']:
          val_dict['0'] = mystery_val
        else:
          val_dict['6'] = mystery_val
      else:
        val_dict['8'] = mystery_val

    partial_outputs = output.split()
    code = ['', '', '', '']
    for i in range(len(partial_outputs)):
      key = ''
      val = partial_outputs[i]
      for k, v in val_dict.items():
        if v == { c for c in val }:
          key = k
      code[i] = key
    codes.append(int(''.join(code)))
  return sum(codes)

print(part1(lines))
print(part2(lines))
