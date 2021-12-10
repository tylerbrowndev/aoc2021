f = open("../input/10.txt", "r")
lines = f.readlines()

def part1(lines):
  score = 0
  corrupt_lines = []
  for i in range(len(lines)):
    line = lines[i]
    stack = []
    for c in line:
      if c in '([{<':
        stack.append(c)
      elif c in ')]}>':
        match = stack.pop()
        if c == ')' and match != '(':
          score += 3
          corrupt_lines.append(i)
          break
        elif c == ']' and match != '[':
          score += 57
          corrupt_lines.append(i)
          break
        elif c == '}' and match != '{':
          score += 1197
          corrupt_lines.append(i)
          break
        elif c == '>' and match != '<':
          score += 25137
          corrupt_lines.append(i)
          break  
  return score, corrupt_lines

def part2(lines, corrupt_lines):
  scores = []
  for i in range(len(lines)):
    if i in corrupt_lines:
      continue
    score = 0
    line = lines[i]
    stack = []
    for c in line:
      if c in '([{<':
        stack.append(c)
      elif c in ')]}>':
        stack.pop()
    while len(stack):
      c = stack.pop()
      score *= 5
      if c == '(':
        score += 1
      elif c == '[':
        score += 2
      elif c == '{':
        score += 3
      elif c == '<':
        score += 4
    scores.append(score)
  scores.sort()
  return scores[len(scores) // 2]

score, corrupt_lines = part1(lines)
print(score)
print(part2(lines, corrupt_lines))
