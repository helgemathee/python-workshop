# a recursion is a function which invocates itself

def fac(n):
  print "fac(" + str(n) + ')'
  if n <= 1:
    return 1
  else:
    return n * fac(n-1)

print fac(12)
