f = open("../input/4.txt", "r")
lines = f.readlines()

vals = [int(x.strip()) for x in lines.pop(0).split(',')]
lines.pop(0)

boards = []
board = []
for line in lines:
  if line == '\n':
    continue
  if len(board) == 5:
    boards.append(board)
    board = []
  row = [int(x.strip()) for x in line.split()]
  board.append(row)

board_sets = []
for board in boards:
  row_sets = []
  for row in board:
    row_sets.append(frozenset(row))
  board_t = [[row[i] for row in board] for i in range(len(board[0]))]
  for col in board_t:
    row_sets.append(frozenset(col))
  board_sets.append(row_sets)


def part1(vals, board_sets):
  drawn_vals = set()
  for n in vals:
    drawn_vals.add(n)
    for board_set in board_sets:
      for row_set in board_set:
        if row_set.difference(drawn_vals) == set():
          unioned_row_sets = set()
          for row_set in board_set:
            unioned_row_sets = unioned_row_sets.union(row_set)
          undrawn_sum = sum(unioned_row_sets.difference(drawn_vals))
          return undrawn_sum * n
  return False

def part2(vals, board_sets):  
  drawn_vals = set()
  for n in vals:
    drawn_vals.add(n)
    i = 0
    while i < len(board_sets):
      board_set = board_sets[i]
      for row_set in board_set:
        if row_set.difference(drawn_vals) == set():
          if len(board_sets) > 1:
            board_sets.pop(i)
            i -= 1
            break
          else:
            unioned_row_sets = set()
            for row_set in board_set:
              unioned_row_sets = unioned_row_sets.union(row_set)
            undrawn_sum = sum(unioned_row_sets.difference(drawn_vals))
            return undrawn_sum * n
      i += 1
  return False


print(part1(vals, board_sets))
print(part2(vals, board_sets))