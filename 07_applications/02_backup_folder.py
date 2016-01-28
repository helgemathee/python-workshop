# this script generates a zip file while filtering the contents
#
# The base path of the project should be provided as an additional command line argument.
# If the user forgets to provide the argument, an error message with the right usage syntax
# Should be displayed

import os
import sys
import zipfile

if len(sys.argv) < 3:
  print "The syntax for this script is: python script zipfile content1 content2 ..."
  print "For example: python 02_backup_folder.py test.zip c:\\temp"
  exit()

zipPath = sys.argv[1]
contentFolders = sys.argv[2:]
basePath = os.path.abspath('.')

# open the zip file
z = zipfile.ZipFile(zipPath, 'w')

for contentFolder in contentFolders:
  for root, directories, fileNames in os.walk(contentFolder):
    for fileName in fileNames:
      f = os.path.join(root, fileName)
      if f.find('.git') > -1:
        continue
      relPath = os.path.relpath(f, basePath)
      print 'Storing %s' % relPath
      z.write(f, relPath)

# close the zip file
z.close()
