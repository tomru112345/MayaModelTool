import maya.cmds as cmds

cmds.polyCube(w = 1, h = 1, d = 1, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)

def Move(object, X, Y, Z):
    object.move(X, Y, Z)

Move(cmds, 0, 10, 1)

cmds.selectPref(tso = True) #tsoはtrackSelectionOrderの略
component = cmds.ls(os = True)
sel_ID = cmds.ls(sl = True, uuid = True)
cmds.ls(sel_ID)
print(component)