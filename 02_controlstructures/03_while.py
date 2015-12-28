# the while loop continues based on a condition

def fac(n):
  result = 1
  while(n > 0):
    # print n
    result = result * n
    n = n - 1
  return result

print fac(4)
