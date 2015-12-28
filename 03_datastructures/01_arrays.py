# in python there are three types of arrays
#  - arrays
#  - lists
#  - tuples
# for simplicity's sake let's just look at arrays

a = [] # an empty array
b = ['helge', 'mick', 'dominic'] # three elements
c = ['helge', 1.2, b]

print b[0] # the first element
print b[1] # the second element
print b[-1] # the last segment
print b[-2] # the previous to the last element
print b[0:2] # start at the first element and use two elements
print b[1:] # start at the second element and use all remaining elements

b[1] = 'tom'
print b

d = [1, 2, 3]
e = [4, 5, 6]
f = d + e
g = e + d

print d
print e
print f
print g

d.reverse()
print d

d.insert(1, 7)
print d
