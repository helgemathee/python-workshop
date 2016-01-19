
# defining a new object
class asset(object):

  __assetType = None # private

  def __init__(self, assetType):
    self.__assetType = assetType

  def getAssetType(self):
    return self.__assetType

a = asset(assetType = "generic")

print a
print a.getAssetType()
