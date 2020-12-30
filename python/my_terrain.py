# -*- coding: utf-8 -*-
import random
import maya.cmds as cmds

def Create_terrain():
    poly = cmds.polyPlane(h=100.0, w=100.0, cuv=2, sy=50, sx=50, ch=1, ax=(0, 1, 0))
    ver = cmds.polyListComponentConversion(poly[0], toVertex=True)
    verE = cmds.filterExpand(ver, selectionMask=31)
    for obj in verE:
        x = random.uniform(-0.1, 0.1)
        y = random.uniform(0.0, 2.0)
        z = random.uniform(-0.1, 0.1)
        cmds.select(obj, r=True)
        cmds.move(x, y, z, r=True)

def Create_mountain(): # 未完成
    poly = cmds.polyPyramid(w=10.0, cuv=2, ch=1, ax=(0, 1, 0))
    ver = cmds.polyListComponentConversion(poly[0], toVertex=True)
    verE = cmds.filterExpand(ver, selectionMask=31)
    for obj in verE:
        x = random.uniform(-0.1, 0.1)
        y = random.uniform(-1.0, 1.0)
        z = random.uniform(-0.1, 0.1)
        cmds.select(obj, r=True)
        cmds.move(x, y, z, r=True)

#Create_terrain()
Create_mountain()
