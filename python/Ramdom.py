# -*- coding: utf-8 -*-
import random
import maya.cmds as cmds

def Ramdom(): # 簡単なランダム座標での描画
	for i in range(10): # 10回繰り返す
		x = random.random() # ランダム x 座標
		y = random.random() # ランダム y 座標
		z = random.random() # ランダム z 座標
		CubeMake(x, y, z, 0.1, 0.1, 0.1) # 立方体作成関数

def CubeMake(x, y, z, random_w, random_h, random_d): # 立方体作成関数
	cmds.polyCube(w = random_w, h = random_h, d = random_d)
	cmds.move(x, y, z)