passes = {
  'BEAUTY': {
    'partitions': ['cutout', 'foreground'],
    'overrides': [],
  },
  'SPEC': {
    'overrides': [],
  }
}

for passName in passes:
  Application.CreatePass("", passName, "")

  partitions = passes[passName].get('partitions', [])
  for partitionName in partitions:
    Application.CreatePartition("Passes."+passName, partitionName)
    
  overrides = passes[passName.get('overrides', [])
  for override in overrides:
    Application.LogMessage('bla')