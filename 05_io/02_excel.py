# you might want to install tablib :-)
# command line: pip install tablib

import tablib

# create a table
table = tablib.Dataset()

# create headers
table.headers = ['Index', 'Name']

# fill in rows (dimensions have to match)
for i in range(10):
  table.append([i, 'Test'])

# write the xls content to disc
# wb is for write binary
open('test.xls', 'wb').write(table.xls)

#-----------------------------------------------
# now let's read the file back
table = tablib.Dataset()
table.xls = open('test.xls', 'rb').read()

rows = table.dict
for row in rows:
  print row
  print row['Index']
