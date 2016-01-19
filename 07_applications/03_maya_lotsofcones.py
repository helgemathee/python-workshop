from maya import cmds

for i in range(25):
    results = cmds.polyCone(height = 5)
    transform = results[0]
    cmds.move(i, 0, 0, transform)