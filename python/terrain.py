# coding:utf-8
import random
import maya.cmds as cmds

def Create_field():
    cmds.polyPlane(h=200, w=200, cuv=2, sy=100, sx=100, ch=1, ax=(0, 1, 0))
    # 平らな表面を作成 
    sl_mesh = cmds.ls(sl=True) # オブジェクトの存在確認
    sl_plane = cmds.rename(sl_mesh, 'terrain_mdl') # オブジェクトが新しい名前に変更

    # マテリアル作成
    cmds.shadingNode('lambert', asShader=1)
    # asShader(asShader) : カレントの DG ノードをシェーダとして分類
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
    # asTexture(at) : カレントの DG ノードをテクスチャとして分類
    cmds.connectAttr('noise1.outColor', 'textureDeformer1.texture', force=1)

Create_field()