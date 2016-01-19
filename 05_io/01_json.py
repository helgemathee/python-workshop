import json

# build a dictionary
a = {}
a['start'] = 10
a['end'] = 100
a['folder'] = 'c:/temp'
a['settings'] = {}
a['settings']['length'] = 1.4
a['names'] = ['juan', 'helge']

# save if to disk
text = json.dumps(a, indent=2)
open("e:/test.json", 'w').write(text)

# load again from disk
text = open("e:/test.json", 'r').read()
b = json.loads(text)

print a
print b
print b['settings']['length']
print b['names']
