# -*- coding: utf-8 -*-
import sys
import os
import logging

logger = logging.getLogger('model_publish_Log')  
logger.setLevel(logging.DEBUG)  
#fh = logging.FileHandler('/tmp/test.log')  
  
# 再创建一个handler，用于输出到控制台    
#ch = logging.StreamHandler()  
#logger.addHandler(ch)
# 定义handler的输出格式formatter    
#formatter = logging.Formatter('%(name)s [%(levelname)s] %(funcName)s  \n %(message)s')  
#fh.setFormatter(formatter)  
#ch.setFormatter(formatter)  


toolPath = r'C:\gitLab\brownser01'
if toolPath not in sys.path:
    sys.path.append(toolPath)


from bin.Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2

if IsPySide:
    from PySide import QtWebKit
elif IsPySide2:
    from PySide2 import QtWebKit

else:
    from PyQt4 import QtWebKit


if IsPySide:
    from shiboken import wrapInstance
elif IsPySide2:
    from shiboken2 import wrapInstance

try:
    import maya.OpenMayaUI as omui
    import maya.OpenMaya as om
    import pymel.core as pm
    import pymel.core.datatypes as dt
    import maya.cmds as cmds
    import maya.mel as mel
    # from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
    from Qt.QtCore import QRect

    def getMayaWindow():
        ptr = omui.MQtUtil.mainWindow()
        return wrapInstance(long(ptr), qw.QWidget)

    MayaParent = getMayaWindow()
except:
    MayaParent = ''

import bin.mainBrowser as mainBrowser
reload(mainBrowser)
import bin.util as util
reload(util)

if 'src.resources' not in sys.modules:
    import src.resources as resources
#reload(src.resources)

class modelBrowser(mainBrowser.Ui_MainWindow):
    scale = 2
    def setupGuild(self):
        
        '''  
        以下是enableList和checkList使用到的项目          
        'Model':'',
        'LookDev':'',
        'Rig':'',
        'Groom':'',
        'GroomMat':'',
        'RigSol':'',
        'LayoutSeq':'',
        'LayoutAni':'',

        'ShotEnv':'',
        'ShotSound':'',
        'Animation':'',
        'CFX':'',
        'FinalShotAssemble':'',
        'KeyLight':'',
        'Lighting':'',
        'Comp':'',
        'ShotDMP':'',
        'SeqDMP':''
        '''

        # 按顺序依次设置
        logger.info('into setupGuild') 
        self.setGuildModule(self.getBrowserModule())  
        self.setGuildEnableList(['Model','LookDev']) # 可以选中的列表
        self.setGuildCheckList(['Model','LookDev']) # 默认选中的列表
        self.setGuildSubListDefaultSelect(0) # 次级列表默认选中的值
        self.setGuildScale(1) # UI缩放值
        self.setGuildAddList(None) # 是否需要追加次级列表项目,可以是字符串，地址和列表
        logger.info('finish setupGuild') 

    def setupActionArea(self):
        testF = qw.QFrame()
        testV = qw.QVBoxLayout()
        testF.setLayout(testV)

        publishBtn = qw.QPushButton()
        publishBtn.setProperty('dep','model')
        publishBtn.setObjectName('publish_button')
        publishBtn.setText('Publish Model')
        testV.addWidget(publishBtn)
        
        publishLabel = qw.QLabel()
        publishLabel.setText('publish as:')
        testV.addWidget(publishLabel)

        publishLineEdit = qw.QLineEdit()
        publishLineEdit.setText('defaultVersion')
        testV.addWidget(publishLineEdit)
        publishBtn.clicked.connect(self.buttonActionPub)
        
        self.addActionArea(testF)

    def buttonActionPub(self):
        logger.info( 'publish action')
        theData = self.getBrowserState()
        #util.getPublishPath = 
        logger.info('make upload files')
        #upFile = makeUploadFiles('hey')
        #upFile.createThumbPic()
        #upFile.createRotatePic()
        logger.info('make json files')
        logger.info('run Events')
        logger.info('make history files')
        logger.info('show finish dialog')
        

    def dbClickedEvent(self,dic):
        dic['serverPath'] = self.getServerPath()
        dic['prjName'] = self.getProjectName()
        dic['_module'] = self.getBrowserModule()
        logger.info(dic)
        
        dataDict = util.getSoftwareConfig()
        _path = dataDict['general']['pipeMainPath'] + '/%(prjName)s/.HistoryInfo/%(_module)s/%(dataType)s/%(name)s/' % dic
        logger.info(_path)
        if not os.path.exists(_path):
            os.makedirs(_path)

    def dbPlayedEvent(self):
        pass  
    def dbAddChartEvent(self):
        pass  

    def main(self):
        self.setupUi()
        self.setupGuild()
        self.setBrowserModule(0)  # 0:assets  1:shots
        self.setServerPath('D:/testDir')
        self.setProjectName('ZZZ')
        self.setupActionArea()
        self.fileVersionPage.hide()
        self.fileColPage.hide()

        styleSheet = QtCore.QFile('C:/gitLab/brownser01/src/qss/AMOLED.qss')        
        styleSheet.open(QtCore.QFile.ReadOnly)   
        self.setStyleSheet(str(styleSheet.readAll())) 
        #print ':/qss/AMOLED.qss'
        #print dir(styleSheet)
        #print str(styleSheet.readAll())


class makeUploadFiles(object):
    """docstring for makeUploadFiles"""
    def __init__(self, arg):
        super(makeUploadFiles, self).__init__()
        self.arg = arg
        
    def createThumbPic(self):
        cmds.viewFit('front',all=True)
        cmds.playblast(f = r'D:\testDir\aa',
            frame=1, 
            format="image", 
            quality=100,
            percent=100,
            w=512,
            h=512,
            compression="jpg",
            viewer=False )

    def createRotatePic(self):
        rotPicPath = os.environ['userprofile']+'/pipelineTemp/rotpic/'
        if not os.path.exists(rotPicPath):
            os.makedirs(rotPicPath)


        fontOc = cmds.getAttr('front.orthographic')
        if fontOc == 1:
            cmds.setAttr('front.orthographic',0)
        cmds.viewFit('front',all=True )
        fVal = cmds.xform('front',ws=1,q=1,t=1)[-1]
        print fVal
        if fontOc == 1:
            cmds.setAttr('front.orthographic',1)


        topOc = cmds.getAttr('top.orthographic')
        if topOc == 1:
            cmds.setAttr('top.orthographic',0)
        cmds.viewFit('topShape',all=True)
        tVal = cmds.xform('top',ws=1,q=1,t=1)[1]
        print tVal
        if topOc == 1:
            cmds.setAttr('top.orthographic',1)

        sideOc = cmds.getAttr('side.orthographic')
        if sideOc == 1:
            cmds.setAttr('side.orthographic',0)
        cmds.viewFit('sideShape',all=True)
        sVal = cmds.xform('side',ws=1,q=1,t=1)[0]
        print sVal
        if sideOc == 1:
            cmds.setAttr('side.orthographic',1)

        maxVal = max([fVal,tVal,sVal])
        print 'maxVal',maxVal

        normalDict = {
        "MFR1": (-0.5, 0.0, 0.866) ,
        "MBR1": (-0.866, 0.0, -0.5) ,
        "MBL1": (0.866, 0.0, -0.5) ,
        "MFL2": (0.866, 0.0, 0.5) ,
        "MFR2": (-0.866, 0.0, 0.5) ,
        "MR": (-1.0, 0.0, 0.0) ,
        "MBR2": (-0.5, 0.0, -0.866) ,
        "MB": (0.0, 0.0, -1.0) ,
        "MBL2": (0.5, 0.0, -0.866) ,
        "ML": (1.0, 0.0, 0.0) ,
        "MFL1": (0.5, 0.0, 0.866) ,
        "MF": (0.0, 0.0, 1.0) ,
        "BFR1": (-0.354, -0.707, 0.612) ,
        "BR": (-0.707, -0.707, 0.0) ,
        "BBR1": (-0.612, -0.707, -0.354) ,
        "BB": (0.0, -0.707, -0.707) ,
        "BBL1": (0.612, -0.707, -0.354) ,
        "BL": (0.707, -0.707, 0.0) ,
        "BFL1": (0.354, -0.707, 0.612) ,
        "BF": (0.0, -0.707, 0.707) ,
        "BFL2": (0.612, -0.707, 0.354) ,
        "BBL2": (0.354, -0.707, -0.612) ,
        "BBR2": (-0.354, -0.707, -0.612) ,
        "BFR2": (-0.612, -0.707, 0.354) ,
        "TF": (0.0, 0.707, 0.707) ,
        "TFL2": (0.612, 0.707, 0.354) ,
        "TL": (0.707, 0.707, 0.0) ,
        "TBL2": (0.354, 0.707, -0.612) ,
        "TB": (0.0, 0.707, -0.707) ,
        "TBR2": (-0.354, 0.707, -0.612) ,
        "TR": (-0.707, 0.707, 0.0) ,
        "TFR2": (-0.612, 0.707, 0.354) ,
        "TFL1": (0.354, 0.707, 0.612) ,
        "TBL1": (0.612, 0.707, -0.354) ,
        "TBR1": (-0.612, 0.707, -0.354) ,
        "TFR1": (-0.354, 0.707, 0.612)
        }

        rotDict = {
        "TB": [135.0, 0.0, 180.0] ,
        "MFL2": [0.0, 60, 0.0] ,
        "MFL1": [0.0, 30, 0.0] ,
        "MR": [0.0, -90, 0.0] ,
        "BBL2": [45, 150, 0.0] ,
        "BBL1": [45, 120, 0.0] ,
        "TFL2": [-45, 60, 0.0] ,
        "TL": [-45, 90.0, 0.0] ,
        "BBR2": [45, 210.0, 0.0] ,
        "BBR1": [45, 240.0, 0.0] ,
        "ML": [0.0, 90.0, 0.0] ,
        "TFR2": [-45.0, -60.0, 0.0] ,
        "MB": [0.0, 180.0, 0.0] ,
        "MFR2": [0.0, -60.0, 0.0] ,
        "MFR1": [0.0, -30.0, 0.0] ,
        "MF": [0.0, 0.0, 0.0] ,
        "MBL2": [0.0, 150.0, 0.0] ,
        "MBL1": [0.0, 120.0, 0.0] ,
        "TBL2": [135.0, 30.0, -180.0] ,
        "BR": [45.0, -90.0, 0.0] ,
        "TBL1": [135.0, 60.0, -180.0] ,
        "TF": [-45.0, 0.0, 0.0] ,
        "BFL2": [45.0, 60.0, 0.0] ,
        "BFL1": [45.0, 30.0, 0.0] ,
        "TFL1": [-45.0, 30.0, 0.0] ,
        "TBR2": [135.0, -30.0, 180.0] ,
        "TBR1": [135.0, -60.0, 180.0] ,
        "BF": [45.0, 0.0, 0.0] ,
        "TR": [-45.0, -90.0, 0.0] ,
        "BL": [45.0, 90.0, 0.0] ,
        "TFR1": [-45.0, -30.0, 0.0] ,
        "BB": [45.0, 180.0, 0.0] ,
        "BFR2": [45.0, -60.0, 0.0] ,
        "MBR2": [0.0, 210.0, 0.0] ,
        "MBR1": [0.0, 240.0, 0.0] ,
        "BFR1": [45.0, -30.0, 0.0]

        }


        cam = cmds.camera(name='paipingcam')
        cmds.setAttr ("%s.displayResolution"%cam[1], 0)
        cmds.setAttr ("%s.displayGateMask"%cam[1], 0)
        cmds.setAttr ("%s.displayFilmGate"%cam[1], 0)
        cmds.setAttr ("%s.overscan"%cam[1], 1)
        cmds.lookThru(cam[0])

        for i in normalDict.keys():
            #print i
            thepos = [normalDict[i][0]*maxVal,
            normalDict[i][1]*maxVal,
            normalDict[i][2]*maxVal]
            therot = rotDict[i]
            #print therot
            cmds.xform(cam,t=thepos,ws=1)
            cmds.xform(cam,ro=rotDict[i],ws=1)

            cmds.playblast(format='image',
                filename=rotPicPath+i,
                frame=1, 
                sequenceTime=0,
                clearCache=1,
                viewer=0,
                showOrnaments =0,
                percent=100,
                os=0,
                compression="jpg",
                quality=100,widthHeight=[512,512])

        cmds.lookThru('persp')
    def getCreatedFileList(self):
        pass

if __name__ == '__main__':
    #import src.createIcon as cion

    #font-family:Verdana;font-size:25px;font-weight:None;font-style:oblique;
    #font-family:Verdana;font-style:oblique;
    if True:
        import os
        app = qw.QApplication.instance()
        if not app:
            app = qw.QApplication( [])

        gg = modelBrowser()
        gg.main()
        gg.show()
        gg.move(0,0)

        gg.raise_()
        print 222
        try:
            sys.exit(app.exec_())
        except: pass
        print 333
    if False:
        mlf = makeUploadFiles(1)
        mlf.createRotatePic()