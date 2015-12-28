# dictionaries are lists which can use anything as an index
# for loops in dictionaries operator on the IndexError

settings = {}
settings['length'] = 8.0
settings['width'] = 12.0
settings[7] = 14.0

print settings
print settings.has_key('height')
print settings.keys()
print settings.values()

