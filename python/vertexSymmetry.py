import maya.cmds as cmds
import maya.api.OpenMaya as om

# closestPointを取得する関数
def getClosestPoint(thisPt,searchMesh,ID) :    
    # セレクションリストからメッシュの関数セットに代入
    sl = om.MSelectionList()
    sl.add(searchMesh)
    dagPath = sl.getDagPath(0)
    meshFn = om.MFnMesh(dagPath)

    # ワールドスペース空間指定
    space = om.MSpace.kWorld

    # 最近接頂点を取得
    closestPoint, faceId = meshFn.getClosestPoint(thisPt, space)

    # フェイスが持つVertexのポイントを取得
    meshFaceIt = om.MItMeshPolygon(dagPath)
    meshFaceIt.setIndex(faceId)
    meshPts = meshFaceIt.getPoints(space)
    meshVtxIt = meshFaceIt.getVertices() #頂点番号
    
    # 最近接頂点を探して、closestPointに結果を入れる
    minLen = None
    closestPoint = None
    for pt in meshVtxIt:
        pointer = meshFn.getPoint(pt,space)
        len = (pointer - thisPt).length()
        if minLen is None or len < minLen :
            minLen = len
            closestPoint = pointer
            vtxID = pt
    if ID == 0:
        return list(closestPoint)[:3]
    elif ID == 1:
        return vtxID


# ノードの定義
def setClosestPoint(direction="x"):
    vtx = []
    sel = cmds.ls(sl=True,fl=True)
    if sel == []:
        cmds.error(u"頂点を選択してください。")
    searchMesh = sel[0].split(".vtx")[0]
    
    for sels in sel:
        # 選択した頂点の反対側の頂点位置を取得
        point = cmds.xform(sels,q=True,ws=True,t=True)
        if direction == "x":points = [-point[0],point[1],point[2]]
        elif direction == "y":points = [point[0],-point[1],point[2]]
        elif direction == "z":points = [point[0],point[1],-point[2]]
        thisPt = om.MPoint(points)
    
        # 反対側の最近接頂点を取得
        closestPoint = getClosestPoint(thisPt,searchMesh,0)
        vtxID = getClosestPoint(thisPt,searchMesh,1)
        reClosestPoint = cmds.xform(searchMesh+".vtx[%d]"%vtxID, q=True, ws=True, t=True)
        
        # closestPointの位置に移動させる
        cmds.xform(searchMesh+".vtx[%d]"%vtxID, ws=True, t=points)
        len = [points[0] - reClosestPoint[0] , points[1] - reClosestPoint[1] , points[2] - reClosestPoint[2]]
        
        if len == [0,0,0]:
            pass
        else:
            vtx.append(searchMesh+".vtx[%d]"%vtxID)
    if vtx != []:
        cmds.select(vtx)
    elif vtx == []:
        cmds.select(searchMesh)
        cmds.select(cl=True)
    return vtx

#引数(x,y,z)でミラー方向を指定。ワールド座標限定。
setClosestPoint("x")