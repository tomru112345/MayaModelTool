import maya.cmds as cmds
import random

cmds.polySphere(constructionHistory=True, object=True, radius=3.0)

# Deforms whatever is currently on the selection list
# and set the attributes value for the deformer node
#cmds.textureDeformer(envelope=0.8, strength=1.0, offset=1.0, direction="Normal", pointSpace="World")
cmds.textureDeformer(envelope=0.8, offset=1.0, direction="Vector", pointSpace="UV", strength=20, vectorSpace="Object")
#cmds.textureDeformer(vectorStrength=(1, 1, 1), exclusive="", direction="Handle", strength=random.uniform(1, 20), envelope=1, vectorOffset=(0, 0, 0), vectorSpace="Object", offset=0, pointSpace="UV")
poly = cmds.select('textureDeformerHandle1', r=1)
print(poly)
poly = cmds.shadingNode('noise', asTexture= True)
print(poly)
cmds.connectAttr('noise1.outColor', 'textureDeformer1.texture', force= True)