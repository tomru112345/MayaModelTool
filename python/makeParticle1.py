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

def Create_field():
    cmds.polyPlane(h=200, w=200, cuv=2, sy=100, sx=100, ch=1, ax=(0, 1, 0))
    # 平らな表面を作成 
    sl_mesh = cmds.ls(sl=True) # オブジェクトの存在確認
    sl_plane = cmds.rename(sl_mesh, 'terrain_mdl') # オブジェクトが新しい名前に変更

    # マテリアル作成
    cmds.shadingNode('lambert', asShader=1)
    
    sl_mat = cmds.ls(sl=True)
    cmds.rename(sl_mat, 'terrain')
    cmds.sets(renderable=True, empty=1, noSurfaceShader=True, name='terrainSG')
    cmds.connectAttr('terrain.outColor', 'terrainSG.surfaceShader', f=1)

    # マテリアルアサイン
    cmds.select(sl_plane)
    cmds.sets(forceElement='terrainSG', e=1)

    # デフォームテクスチャ作成
    cmds.textureDeformer(vectorStrength=(1, 1, 1), exclusive="", direction="Handle", strength=10, envelope=1, vectorOffset=(0, 0, 0), vectorSpace="Object", offset=0, pointSpace="UV")
    cmds.select('textureDeformerHandle1', r=1)

    # テクスチャのかわりにとりあえずノイズをアサイン
    cmds.shadingNode('noise', asTexture=1)
    cmds.connectAttr('noise1.outColor', 'textureDeformer1.texture', force=1)
    


def get_coordinates(w, d):
    name = cmds.ls(sl = True)
    x = cmds.getAttr(name[0] + ".tx")
    y = cmds.getAttr(name[0] + ".ty")
    z = cmds.getAttr(name[0] + ".tz")
    coordinates.append([x,y,z,w,d])


Auto_city()

