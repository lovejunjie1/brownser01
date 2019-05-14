import os
import sys
import maya.cmds as cmds
from maya.OpenMayaUI import MQtUtil



def getAssetManagerPath():
    version = 'interfaces'
    filePath = 'D:\\AssetManegerSystem_publish'
    iconPath = filePath+'\\icon'
    dataPath = filePath+'\\data'
    binPath = filePath+'\\' + version + '\\bin'
    modelPath = filePath+'\\' + version + '\\MODEL'
    commonPath = filePath+'\\' + version + '\\COMMON'
    layoutPath = filePath+'\\' + version + '\\LAYOUT'
    rigPath = filePath+'\\' + version + '\\RIG'
    writerPath = filePath+'\\' + version + '\\bin\\ext'
    return {'writter': writerPath,'main':filePath,'icon':iconPath,'data':dataPath,'bin':binPath,'model':modelPath,'rig':rigPath,'common':commonPath,'layout':layoutPath }

def getPyFileUnderPath(path):
    files = []
    binDirs = os.listdir(path)
    for d in binDirs:
        absPath = os.path.join(path, d)
        if os.path.isfile(absPath):
            spname = d.split('.')
            if ('py' == spname[-1] or 'pyc' == spname[-1]) and '__init__' != spname[0]:
                files.append(absPath)

    return files

def loadPyFileToCache():
    path = getAssetManagerPath()
    files = []
    for key,itm in path.items():
        print key
        if os.path.exists(itm):
            thefile = getPyFileUnderPath(itm)
            files += thefile
    
    return files

def addBtn(label, icon="test.png", command='', doubleCommand=''):
    cmds.setParent('Custom')
    pathDict = getAssetManagerPath()
    if icon:
        icon = pathDict['icon'] + '\\' +  icon
    cmds.shelfButton(width=32, height=32, image=icon, l=label, command=command, dcc=doubleCommand, imageOverlayLabel=label, olb=(1.0,1.0,1.0,0.5,), olc=(0.1,0.1,0.1))

def setupMODEL():
    addBtn('model',command = 'ModelManaBUI=assetManager_ModelBoxUI()\nModelManaBUI.Op_Ui()')
    
def setupRIG():
    addBtn('rig',command = 'RigManaBUI=assetManager_RigBoxUI()\nRigManaBUI.Op_Ui()')
    
def setupTEXTURE():
    addBtn('texture',command = 'TextureManaBUI= textureAssetManager ()\nTextureManaBUI.Op_Ui()')
    
def setupSHADE():
    addBtn('shade',command = 'ShadeManaBUI = shaderAssetManager()\nShadeManaBUI.Op_Ui()')


def setupToolBox():
    addBtn('tBox',icon = "icon_tool.png",command = 'MDtoolBUI=MDtoolBoxUI()\nMDtoolBUI.Op_Ui()')

AMS_setupPath = getAssetManagerPath()['main']
if AMS_setupPath not in sys.path:
    sys.path.append(AMS_setupPath)


'''
files = loadPyFileToCache()
print '=============='
print ' assetManager'
print '=============='
for r in range(3):
    for i in files:
        print i
        try:
            execfile(i)
            print 'loaded'
        except:
            print 'failur'
    print ''

Mstyle=RedBlackStyleSheet()
Mstyle.setIconPath(getAssetManagerPath()['icon'])
'''
if not cmds.commandPort(':4434', q=True):
    cmds.commandPort(n=':4434')




