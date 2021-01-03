# coding:utf-8
import maya.cmds as cmds

def GetPPosition(*args):
    si_point = cmds.ls(sl=True)
    pos = cmds.pointPosition(si_point[0])
    pos_x = pos[0]
    pos_y = pos[1]
    pos_z = pos[2]
    cmds.floatField('xfield', e=1, v=pos_x)
    cmds.floatField('yfield', e=1, v=pos_y)
    cmds.floatField('zfield', e=1, v=pos_z)

# ウィンドウ作成
cmds.window(title='Get Point Position', mnb=False, mxb=False)
cmds.columnLayout()
cmds.rowLayout(numberOfColumns=6)
cmds.text(label=u'X')
cmds.floatField('xfield', w=70, v=0)
cmds.text(label=u'Y')
cmds.floatField('yfield', w=70, v=0)
cmds.text(label=u'Z')
cmds.floatField('zfield', w=70, v=0)
cmds.setParent('..')
cmds.button(label='Get Point Position', command=GetPPosition)
cmds.showWindow()