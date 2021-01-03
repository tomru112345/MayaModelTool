# coding:utf-8
import random
import maya.cmds as cmds

coordinates = []

def Create_random_terrain(): # ランダム
    poly = cmds.polyPlane(h=200.0, w=200.0, cuv=2, sy=100, sx=100, ch=1, ax=(0, 1, 0))
    ver = cmds.polyListComponentConversion(poly[0], toVertex=True)
    verE = cmds.filterExpand(ver, selectionMask=31)
    for obj in verE:
        x = random.uniform(-2.0, 2.0)
        y = random.uniform(0.0, 3.0)
        z = random.uniform(-2.0, 2.0)
        cmds.select(obj, r=True)
        cmds.move(x, y, z, r=True)

def Create_noise_terrain(): # ノイズ
    cmds.polyPlane(h=200, w=200, cuv=2, sy=100, sx=100, ch=1, ax=(0, 1, 0))
    cmds.textureDeformer(vectorStrength=(1, 1, 1), exclusive="", direction="Handle", strength=random.uniform(1, 20), envelope=1, vectorOffset=(0, 0, 0), vectorSpace="Object", offset=0, pointSpace="UV")
    cmds.select('textureDeformerHandle1', r=1)
    cmds.shadingNode('noise', asTexture=1)
    cmds.connectAttr('noise1.outColor', 'textureDeformer1.texture', force=1)

def Create_alpha_terrain(): #ノイズ
    poly = cmds.polyPlane(h=200, w=200, cuv=2, sy=100, sx=100, ch=1, ax=(0, 1, 0))
    cmds.textureDeformer(vectorStrength=(1, 1, 1), exclusive="", direction="Handle", strength=random.uniform(4, 20), envelope=1, vectorOffset=(0, 0, 0), vectorSpace="Object", offset=0, pointSpace="UV")
    cmds.select('textureDeformerHandle1', r=1)
    cmds.shadingNode('noise', asTexture=1)
    cmds.connectAttr('noise1.outColor', 'textureDeformer1.texture', force=1)
    ver = cmds.polyListComponentConversion(poly[0], toVertex=True)
    verE = cmds.filterExpand(ver, selectionMask=31)
    for obj in verE:
        cmds.select(obj, r=True)
        pos = cmds.pointPosition(obj)
        pos_x = pos[0]
        pos_y = pos[1]
        pos_z = pos[2]
        coordinates.append([pos_x, pos_y, pos_z])


def CubeMake(x, y, z, random_w, random_h, random_d): # 立方体作成関数
	cmds.polyCube(w = random_w, h = random_h, d = random_d)
	cmds.move(x, y, z)

def Auto_city(x, y, z):# Random Create
    object = 0
    random_ob = random.random()
    if random_ob > 0.5:
        if y >= 0 and y <= 4:
            w = random.uniform(1.0, 2.0)
            h = random.uniform(2.0, 7.0)
            d = random.uniform(1.0, 2.0)
            CubeMake(x, y, z, w, h, d)
            object = object + 1

# https://note.com/tara_panda/n/n09fef30a06e9

Create_alpha_terrain()
for i in coordinates:
    Auto_city(i[0], i[1], i[2])
print(coordinates)