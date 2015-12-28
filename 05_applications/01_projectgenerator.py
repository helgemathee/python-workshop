# this script generates a two dimensional folder structure based on the configuration
# 01_mood
#   01_references
#   02_2d
#   03_3d
# 02_modeling
#   01_references
#   02_2d
#   03_3d
#
# The base path of the project should be provided as an additional command line argument.
# If the user forgets to provide the argument, an error message with the right usage syntax
# Should be displayed

import os
import sys

if len(sys.argv) != 2:
  print "The syntax for this script is: python script projectFolder"
  print "For example: python 01_projectgenerator.py c:\\temp\\project"
  exit()

mainFolders = [
  'mood',
  'modeling',
  'animation',
  'rendering',
  'fromClient',
  'toClient'
]

subFolders = [
  'references',
  '2d',
  '3d'
]

baseFolder = sys.argv[1]
if os.path.exists(baseFolder):
  print "Target folder "+baseFolder+" already exists. Aborting."
  exit()

def decorate(folder, index):
  return str(index).rjust(2, '0') + '_' + folder

m = 1
for mainFolder in mainFolders:
  s = 1
  for subFolder in subFolders:
    path = os.path.join(baseFolder, decorate(mainFolder, m), decorate(subFolder, s))
    path = os.path.abspath(path)
    os.makedirs(path)
    s = s + 1
  m = m + 1

print 'Project '+baseFolder+' successfully created.'

# # Alternatively you could also 
# std3DFolders = ['2d', '3d', 'textures', 'renders']
# folders = {
#   'mood': ['2d', '3d'],
#   'fromClient': ['reference'],
#   'modeling': std3DFolders,
#   'animation': std3DFolders
# }
# for key in folders:
#   subFolders = folders[key]
#   for subFolder in subFolders:
#     path = os.path.join(baseFolder, key, subFolder)
#     ....
