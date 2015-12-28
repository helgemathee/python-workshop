# if elif and else can be used to execute code based on conditions

name = "Matthias"

if len(name) > 5:
  print "A pretty long name: " + name
elif len(name) == 0:
  print "That's ridiculous."
else:
  print "A rather short name: " + name

