import sys
import math

def factorInt(n):
  nsqrt = math.ceil(math.sqrt(n))
  solution = False
  val = int(nsqrt)
  while not solution:
    val2 = int(n/val)
    if val2 * val == float(n):
      solution = True
    else:
      val-=1
  return val, val2

def solve(plot, width, height, x, y, pX, pY):
  if pX > -1 and pY > -1:
    plot[pY][pX] = 1
  while plot[y][x] == 1:
    if x + 1 > width - 1:
      y += 1
      x = 0
    else:
      x += 1
  plotX, plotY = toPlot(x, y, width, height)
  print(plotX+1, plotY+1)
  sys.stdout.flush()
  gX, gY = map(int, input().split(" "))
  if gX == -1 and gY == -1:
    return
  elif gX == 0 and gY == 0:
    return
  else:
    solve(plot, width, height, x, y, gX-1, gY-1)

def toPlot(x, y, width, height):
  plotX = x
  plotY = y
  if x == 0:
    plotX = 1
  if y == 0:
    plotY = 1
  if x == width-1:
    plotX = width - 2
  if y == height-1:
    plotY = height - 2
  
  return plotX, plotY

T = int(input())
for _ in range(T):
  size = int(input())
  width, height = factorInt(size)
  while width < 3 or height < 3:
    size += 1
    width, height = factorInt(size)
  plot = [[0 for x in range(width)] for y in range(height)]
  solve(plot, width, height, 0, 0, -1, -1)