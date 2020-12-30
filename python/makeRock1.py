# -*- coding: utf-8 -*-
import random
import maya.cmds as cmds

# http://www.not-enough.org/abe/manual/maya-python-aa07/rock1.html
def makeRock1(): # サンプル石の描画
    val = random.uniform(0.5, 2.0)
    poly = cmds.polySphere(r=val)
    x = random.uniform(0.8, 1.5)
    y = random.uniform(0.8, 1.5)
    z = random.uniform(0.8, 1.5)
    cmds.scale(x, y, z)
    ver = cmds.polyListComponentConversion(poly[0], toVertex=True)
    verE = cmds.filterExpand(ver, selectionMask=31)
    for obj in verE:
        x = random.uniform(-0.1, 0.1)
        y = random.uniform(-0.1, 0.1)
        z = random.uniform(-0.1, 0.1)
        cmds.select(obj, r=True)
        cmds.move(x, y, z, r=True)