f = open("../input/17.txt", "r")
lines = f.readlines()
input = lines[0].strip()
x, y = input.split(', ')
_, x = x.split('=')
x_min, x_max = x.split('..')
x_min, x_max = int(x_min), int(x_max)
_, y = y.split('=')
y_min, y_max = y.split('..')
y_min, y_max = int(y_min), int(y_max)

def part1(x_min, x_max, y_min, y_max):
  def hits_target(x_velocity, y_velocity):
    x = 0
    y = 0
    highest_y = 0
    while x < x_max and y > y_min:
      x += x_velocity
      y += y_velocity
      if y > highest_y:
        highest_y = y
      if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
        return highest_y
      if x_velocity > 0:
        x_velocity -= 1
      y_velocity -= 1
    return -1

  x_start_velocity = 0
  highest_y = 0

  while sum(range(x_start_velocity)) < x_min:
    x_start_velocity += 1

  for x_velocity in range(x_start_velocity - 1, x_max + 1):
    y = y_min
    while y < 150:
      val = hits_target(x_velocity, y)
      if val >= 0:
        if val > highest_y:
          highest_y = val
      y += 1
  return highest_y

def part2(x_min, x_max, y_min, y_max):
  def hits_target(x_velocity, y_velocity):
    x = 0
    y = 0
    while x < x_max and y > y_min:
      x += x_velocity
      y += y_velocity
      if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
        return True
      if x_velocity > 0:
        x_velocity -= 1
      y_velocity -= 1
    return False

  successful_velocities = 0
  x_start_velocity = 0

  while sum(range(x_start_velocity)) < x_min:
    x_start_velocity += 1

  for x_velocity in range(x_start_velocity - 1, x_max + 1):
    y_velocity = y_min
    while y_velocity < 150:
      if hits_target(x_velocity, y_velocity):
        successful_velocities += 1
      y_velocity += 1

  return successful_velocities


print(part1(x_min, x_max, y_min, y_max))
print(part2(x_min, x_max, y_min, y_max))
