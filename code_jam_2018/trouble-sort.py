t = int(input())
for i in range(1, t + 1):
  length = int(input())
  numbers = [int(s) for s in input().split()]
  odds = sorted(numbers[0::2])
  evens = sorted(numbers[1::2])

  result = [None]*length
  result[::2] = odds
  result[1::2] = evens

  for idx in range(len(result)-1):
    if result[idx] > result[idx+1]:
      print("Case #{}: {}".format(i, idx))
      break
  else:
    print("Case #{}: {}".format(i, "OK"))