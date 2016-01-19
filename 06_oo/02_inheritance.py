import shutil

# defining a base object
class asset(object):

  __assetType = None # private

  def __init__(self, assetType):
    self.__assetType = assetType

  def getAssetType(self):
    return self.__assetType

# -------------------------------------------------------------------------


# defining an inheriting object
class fileBasedAsset(asset):

  __fileName = None # private

  def __init__(self, fileName, assetType = 'fileBased'):

    # call the method above
    super(fileBasedAsset, self).__init__(assetType)

    # initiate my own members
    self.__fileName = fileName

  def getFileName(self):
    return self.__fileName

  def getExtension(self):
    return self.__fileName.rpartition('.')[2]

  def copyTo(self, newFileName):
    shutil.copyfile(self.__fileName, newFileName)
    self.__fileName = newFileName

# -------------------------------------------------------------------------


# defining an inheriting object
class imageAsset(fileBasedAsset):

  def __init__(self, fileName):

    # call the method above
    super(imageAsset, self).__init__(fileName, assetType = 'image')

  # here we could be implementing image specific methods
  # such as getting the width and height of an image, number of channels
  # etc (google for imagemagick if you are interested)

a = imageAsset("c:/temp/test.jpg")

print a
print a.getAssetType()
print a.getFileName()
print a.getExtension()

a.copyTo("c:/temp/test2.jpg")
print a.getFileName()
print a.getExtension()
