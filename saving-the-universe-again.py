def calculateDamage(program):
  chars = list(program)
  totalDamage = 0
  beamDamage = 1
  for char in chars:
    if char == 'S':
      totalDamage += beamDamage
    elif char == 'C':
      beamDamage *= 2
  return totalDamage

def hack(program):
  chars = list(program)
  programLength = len(program)
  for idx, val in enumerate(reversed(chars)):
    if idx == programLength - 1:
      return program
    elif chars[idx] == "C" and chars[idx + 1] == "S":
      chars[idx] = "S"
      chars[idx + 1] = "C"
      return ''.join(chars)
  return program

def solve(program, maxDamage):
  prev = program
  hacks = 0
  while calculateDamage(program) > maxDamage:
    prev = program
    program = hack(program)
    if program == prev:
      return("IMPOSSIBLE")
    hacks += 1
  else:
    return hacks

t = int(input())
for i in range(1, t + 1):
  line = input().split(" ")
  maxDamage = int(line[0])
  program = line[1]
  print("Case #{}: {}".format(i, solve(program, maxDamage)))