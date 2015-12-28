# function are blocks of code which are named
# functions can have parameters

def pi():
  return 3.14

def circumFerence(radius = 1.0):
  result = radius * 2.0 * pi()
  return result

print circumFerence(4.0)
print circumFerence()
print circumFerence(radius = 3.0)

