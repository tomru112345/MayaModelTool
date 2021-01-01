# -*- coding: utf-8 -*-
import random
import maya.cmds as cmds

coordinates = [] # 作成したオブジェクトの座標をリストに格納する

def CubeMake(x, y, z, random_w, random_h, random_d): # 立方体作成関数
	cmds.polyCube(w = random_w, h = random_h, d = random_d)
	cmds.move(x, y, z)

def Auto_city():# Random Create
    object = 0
    while object != 100:
        x = random.uniform(-10.0, 10.0)
        z = random.uniform(-10.0, 10.0)
        w = random.uniform(0.8, 1.5)
        h = random.uniform(1.5, 5.0)
        d = random.uniform(0.8, 1.5)
        CubeMake(x, 0, z, w, h, d)
        object = object + 1
        get_coordinates(w, d)
    print(coordinates)

def get_coordinates(w, d):
    name = cmds.ls(sl = True)
    x = cmds.getAttr(name[0] + ".tx")
    y = cmds.getAttr(name[0] + ".ty")
    z = cmds.getAttr(name[0] + ".tz")
    coordinates.append([x,y,z,w,d])


Auto_city()

