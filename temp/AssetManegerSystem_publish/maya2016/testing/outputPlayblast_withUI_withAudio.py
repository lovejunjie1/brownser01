'''
    image list play blast tool.with ui and infomations
    thanks for JYB(http://blog.sina.com.cn/matthew0326)
    he give me a lot of help
    iformations include:
        frame
        artist
        project name
        date
        machineID
        logo
    2018-5-30 17:38:11
'''


import os
import maya.cmds as cmds
from PySide import QtCore, QtGui
import subprocess
import time
import getpass


class outputMayaPlayblast():
    translater = "D:/AssetManegerSystem_publish/data/translater.exe"
    __fps = 24
    def setFps(self,val):
        if isinstance(val,int):
            self.__fps = val

    def getPictureName(self, subFolder='', midName='tempCut'):
        tempPath = 'C:\\outputTemp\\AssetManaBox_Local\\'
        if subFolder:
            tempPath = tempPath + subFolder + '\\'
        if not os.path.exists(tempPath):
            os.makedirs(tempPath)
        dirs = os.listdir(tempPath)
        number = str(len(dirs))
        ans = tempPath + midName + number
        return ans

    def frameToMs(self, fm):
        s = float(fm) / float(self.__fps)
        val = int(s * 1000.0)
        return val

    def frameToUnitTime(self, fm):
        s = float(fm) / float(self.__fps)
        # s = 3.45
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)

        hours = str(int(hours)).zfill(2)
        minutes = str(int(minutes)).zfill(2)
        outStr = '%s:%s:%s' % (hours, minutes, seconds)
        return outStr

    def outputPlayblast(self, camShape):
        objExt = cmds.objExists(camShape)
        if not objExt:
            return False
        renderWidth = cmds.getAttr("defaultResolution.width")
        renderHeight = cmds.getAttr("defaultResolution.height")

        startFrame = int(cmds.playbackOptions(q=1, min=1))
        endFrame = int(cmds.playbackOptions(q=1, max=1)) + 1
        keyArray = range(startFrame, endFrame)
        #print 'orignal keyarray : ' + str(keyArray)

        oAttr = cmds.getAttr(camShape + '.overscan')
        cmds.setAttr(camShape + '.overscan', 1.0)
        camName = str(camShape)
        if 'Shape' in camShape:
            camName = camShape[0:-5]

        outputPath = self.getPictureName(subFolder=camName)
        outputDir = os.path.dirname(outputPath)
        if not (os.path.exists(outputDir)):
            os.makedirs(outputDir)

        dirs = os.listdir(outputDir)
        if dirs:
            for i in dirs:
                os.remove(outputDir + '\\' + i)


        fullPath = outputDir + '\\' + camName

        # modelName = (cmds.getPanel(wf=True))
        modelName = 'modelPanel4'
        # type = cmds.modelPanel(modelName, e=True, cam=True)
        cmds.modelEditor(modelName, edit=True, camera=camShape)
        cmds.modelEditor(	modelName,
                            e=1,
                            wireframeOnShaded=False,
                            nurbsCurves=False,
                            imagePlane=False,
                            ikHandles=False,
                            headsUpDisplay=False,
                            handles=False,
                            hairSystems=False,
                            grid=True,
                            follicles=False,
                            dynamics=False,
                            displayTextures=False,
                            deformers=False,
                            dimensions=False,
                            lights=False,
                            joints=False,
                            shadows=False,
                            textureMaxSize = 128)
        cmds.modelEditor(modelName, e=1, displayLights="all", shadows=True)

        pathArray = []
        for i in range(len(keyArray)):
            strNum = str(i).zfill(4)
            realFileName = fullPath + '.' + strNum + '.jpg'
            pathArray.append(realFileName)

        cmds.playblast( st=1, et=1,
                        format='image',
                        frame=keyArray,
                        filename=fullPath,
                        clearCache=1,
                        viewer=0,
                        showOrnaments=1,
                        percent=100,
                        compression='jpg',
                        quality=100,
                        forceOverwrite=1,
                        widthHeight=[renderWidth, renderHeight])

        cmds.setAttr(camShape + '.overscan', oAttr)

        self.allAudios = cmds.ls(type='audio')
        if self.allAudios:
            audioPath = self.combieSceneAudios(startFrame)
            return [pathArray, keyArray, audioPath]
        else:
            return [pathArray, keyArray, '']


    def combieSceneAudios(self, beginFrame):

        outputPath = self.getPictureName(subFolder='combieAudio') + '.wav'
        outputDir = os.path.dirname(outputPath)
        if not (os.path.exists(outputDir)):
            os.makedirs(outputDir)

        emptyDict = {}
        for i in self.allAudios:
            offset = cmds.getAttr(i + '.offset')
            audioPath = cmds.getAttr(i + '.filename')
            if str(offset) in emptyDict.keys():
                emptyDict[str(offset)].append(audioPath)
            else:
                emptyDict.update({str(offset): [audioPath]})

        tempArray = emptyDict.keys()
        sortArray = []
        for ta in tempArray:
            sortArray.append(float(ta))
        sortArray.sort()

        attrArray = []
        inputArray = []
        delayArray = []
        count = 0
        for sa in sortArray:
            dataArray = emptyDict[str(sa)]
            for g in dataArray:
                offsetStr = self.frameToMs(sa - sortArray[0])
                importStr = '-i ' + g
                inputArray.append(importStr)
                attrName = 'aud' + str(count)
                attrArray.append(attrName)
                delayStr = '[%d]adelay=%s|%s[%s]' % (count, offsetStr, offsetStr, attrName)
                delayArray.append(delayStr)
                count += 1

        fullStr = ''
        for a in attrArray:
            subStr = '[%s]' % a
            fullStr += subStr

        endPart = fullStr + 'amix=inputs=' + str(len(attrArray))
        delayArray.append(endPart)

        filterSub = ';'.join(delayArray)
        filterStr = '-filter_complex "' + filterSub + '"'

        importStr = ' '.join(inputArray)

        commandArray = [self.translater, '-y', importStr, filterStr, '-c:v copy', outputPath]
        commandStr = ' '.join(commandArray)

        subprocess.call(commandStr, shell=True)

        if sortArray[0] < beginFrame:
            cutPath = self.cutAudio(beginFrame,outputPath)
            return [0, cutPath]
        else:

            offsetRange = self.frameToMs(sortArray[0] - beginFrame)
            return [offsetRange, outputPath]

    def cutAudio(self, beginFrame, combieVideoPath):
        outputPath = self.getPictureName(subFolder='combieAudio') + '.wav'

        offsetArray = []
        for i in self.allAudios:
            offset = cmds.getAttr(i + '.offset')
            offsetArray.append(offset)

        startFrame = min(offsetArray)
        startTime = ''
        if startFrame < beginFrame:
            startTime = self.frameToUnitTime(beginFrame - startFrame)

        cutCommandArray = [self.translater, '-y -i', combieVideoPath, '-ss', startTime, '-c:v copy', outputPath]

        cutCmd = ' '.join(cutCommandArray)
        subprocess.call(cutCmd, shell=True)
        return outputPath



class sequenceToMov():

    def __init__(self):
        self.__camName = 'sq00_sc00_sh0000_000f_000f_fps00'
        self.__translaterPath = 'D:\\AssetManegerSystem_publish\\data\\translater.exe'
        self.__sequence = 'sq00'
        self.__scene = 'sc00'
        self.__shot = 'shot0000'
        self.__startframe = '100f'
        self.__endframe = '200f'
        self.__fps = 'fps24'

        self.__output = 'C:/outputTemp'
        if not(os.path.exists(self.__output)):
            os.makedirs(self.__output)
        self.__inputFormat = self.__camName + '.%04d.'
        self.__artist = 'artist'
        self.__project = 'project'
        self.__comment = ''
        self.__department = 'department'
        self.__iconPath = 'D:\\AssetManegerSystem_publish\\icon\\logo.png'

        self.__nowFrame = int(self.__startframe[:-1])
        self.__audio = ''
        self.__audioOffset = 0

    def setAudio(self, st, data):
        if isinstance(data, str) and isinstance(st, int):
            if os.path.exists(data):
                self.__audio = data
                self.__audioOffset = st
        else:
            print 'section 1 must be [int],section 2 must be [str]'

    def setSequence(self, data):
        if isinstance(data, int):
            spName = self.__camName.split('_')
            spName[0] = 'sq' + str(data)
            self.__sequence = spName[0]
            self.__camName = '_'.join(spName)
        else:
            print 'input data is not int type'

    def setScene(self, data):
        if isinstance(data, int):
            spName = self.__camName.split('_')
            spName[1] = 'sc' + str(data)
            self.__scene = spName[0]
            self.__camName = '_'.join(spName)
        else:
            print 'input data is not int type'

    def setShot(self, data):
        if isinstance(data, int):
            spName = self.__camName.split('_')
            spName[2] = 'shot' + str(data)
            self.__shot = spName[2]
            self.__camName = '_'.join(spName)
        else:
            print 'input data is not int type'

    def setStartframe(self, data):
        if isinstance(data, int):
            spName = self.__camName.split('_')
            spName[3] = str(data) + 'f'
            self.__startframe = spName[3]
            self.__nowFrame = data
            self.__camName = '_'.join(spName)
        else:
            print 'input data is not int type'

    def setEndframe(self, data):
        if isinstance(data, int):
            spName = self.__camName.split('_')
            spName[4] = str(data) + 'f'
            self.__endframe = spName[4]
            self.__camName = '_'.join(spName)
        else:
            print 'input data is not int type'

    def setFps(self, data):
        if isinstance(data, int):
            spName = self.__camName.split('_')
            spName[0] = 'fps' + str(data)
            self.__fps = spName[0]
            self.__camName = '_'.join(spName)
        else:
            print 'input data is not int type'

    def setOutput(self, data):
        if isinstance(data, str):
            self.__output = str(data)
            if not(os.path.exists(self.__output)):
                os.makedirs(self.__output)

    def setCameraName(self, data):
        if isinstance(data, str):
            spName = data.split('_')
            if len(spName) == 6:
                checkArray = []
                if 'sq' in spName[0] and len(spName[0]) == 4:
                    self.__sequence = spName[0]
                    checkArray.append(1)
                else:
                    print 'sq wrong'
                    return False

                if 'sc' in spName[1] and len(spName[1]) == 4:
                    self.__scene = spName[1]
                    checkArray.append(1)
                else:
                    print 'sc wrong'
                    return False

                if 'sh' in spName[2] and len(spName[2]) == 6:
                    self.__shot = spName[2]
                    checkArray.append(1)
                else:
                    print 'shot wrong'
                    return False

                if 'f' in spName[3] and len(spName[3]) == 4:
                    self.__startframe = spName[3]
                    self.__nowFrame = int(self.__startframe[:-1])
                    checkArray.append(1)
                else:
                    print 'startframe wrong'
                    return False

                if 'f' in spName[4] and len(spName[4]) == 4:
                    self.__endframe = spName[4]
                    checkArray.append(1)
                else:
                    print 'endframe wrong'
                    return False

                if 'fps' in spName[5] and len(spName[5]) == 5:
                    self.__fps = spName[5]
                    checkArray.append(1)
                else:
                    print 'fps wrong'
                    return False

                if len(checkArray) == 6:
                    self.__camName = str(data)
                    self.__inputFormat = self.__camName + '.%04d.'
                else:
                    print 'wrong element of camera name'
            else:
                print 'wrong lenth of camera name'

    def setArtist(self, data):
        nameStr = str(data)
        self.__artist = nameStr

    def setProject(self, data):
        dataStr = str(data)
        self.__project = dataStr

    def setDepartment(self, data):
        dataStr = str(data)
        self.__department = dataStr

    def setComment(self, data):
        dataStr = str(data)
        self.__comment = dataStr

    def setIcon(self, data):
        if os.path.exists(data):
            self.__iconPath = str(data)

    def setTranslater(self, data):
        if '\\' in data:
            data = data.replace('\\', '/')
        self.__translaterPath = data

    def createMovie(self, dataPath, isUI=True):
        dataArray = ''
        if isinstance(dataPath,list):
            dataArray = list(dataPath)
        elif isinstance(dataPath,str):
            dataTemp = os.listdir(dataPath)
            dataArray = []
            if '\\' in dataPath:
                dataPath = dataPath.replace('\\', '/')
            for da in dataTemp:
                dataArray.append(dataPath + '/' + da)

        date = time.strftime("%Y/%m/%d", time.localtime(time.time()))
        # %Y-%m-%d %H:%M:%S

        keyArray = range(int(self.__startframe[0:-1]), int(self.__endframe[0:-1])+1)
        inputPath = os.path.dirname(dataArray[0])
        inputType = dataArray[0].split('.')[-1]

        thePixmap = QtGui.QPixmap(dataArray[0])
        picSize = [thePixmap.width(), thePixmap.height()]

        if isUI:
            startFrame = int(self.__nowFrame)
            for count, i in enumerate(dataArray):
                self.__nowFrame = startFrame + count
                self.createPlayblastUI(i,
                                       date,
                                       imageSize=picSize,
                                       isReplace=True)
        outputMovie = self.__output + '/' + self.__camName + '.mov'
        ffmpegCommand =(self.__translaterPath
                        + ' -y -f image2 -r '
                        + str(self.__fps[3:])
                        + ' -i '
                        + inputPath
                        + '/'
                        + self.__inputFormat
                        + inputType
                        + ' -vcodec libx264 '
                        + outputMovie
                        )
        print ffmpegCommand
        subprocess.call(ffmpegCommand, shell=True)

        if self.__audio:
            outputMovie2 = self.__output + '/' + self.__camName + '_audio.mov'
            delayStr = 'adelay = %d|%d' % (self.__audioOffset, self.__audioOffset)
            ffmpegCommand2 = (self.__translaterPath
                             + ' -y -i '
                             + outputMovie
                             + ' -i '
                             + self.__audio
                             + ' -filter_complex "'
                             + delayStr
                             + '" '
                             + outputMovie2
                              )

            print ffmpegCommand2
            subprocess.call(ffmpegCommand2, shell=True)
            return outputMovie2
        else:
            return outputMovie

    def createPlayblastUI(self, sourceImage, strDate, imageSize=[], font="Microsoft YaHei", isReplace=False):
        #print 'into pUI'
        if os.path.exists(sourceImage):

            pixmap = QtGui.QImage(sourceImage)

            frameWidth = imageSize[0]
            frameHeight = imageSize[1]
            strSize = str(frameWidth) + '*' + str(frameHeight)
            iconPath = self.__iconPath
            cam = self.__camName
            artist = self.__artist
            machine = getpass.getuser()
            frame = self.__nowFrame
            date = strDate
            project = self.__project
            dep = self.__department
            cmt = self.__comment
            # ----------------------
            titleFont = QtGui.QFont()
            titleFont.setFamily(font)
            titleFont.setPointSize(frameHeight * 0.02)

            dataFont = QtGui.QFont()
            dataFont.setFamily(font)
            dataFont.setPointSize(frameHeight * 0.03)

            keyframeFont = QtGui.QFont()
            keyframeFont.setFamily(font)
            keyframeFont.setPointSize(frameHeight * 0.1)

            overlay = QtGui.QImage(iconPath)
            overlay = overlay.scaledToHeight(int(frameHeight * 0.05))
            source = overlay.rect()
            target = QtCore.QRect(0.0, 0.0, frameHeight * 0.1, frameHeight * 0.1)
            source.moveCenter(target.center())

            lineBHt = frameHeight * 0.1
            lineCHt = frameHeight * 0.92

            lineAWd = frameWidth * 0.01
            lineBWd = frameWidth * 0.2
            lineCWd = frameWidth * 0.4
            lineDWd = frameWidth * 0.55
            unitWd = frameWidth * 0.01

            rect1 = QtCore.QRectF(frameWidth * 0.55, 0, unitWd * 4, lineBHt)
            rect2 = QtCore.QRectF(frameWidth * 0.59, 0, unitWd * 40, lineBHt)

            rect3 = QtCore.QRectF(lineAWd, lineCHt, unitWd * 4, frameHeight * 0.08)
            rect4 = QtCore.QRectF(lineAWd + (unitWd * 4), lineCHt, unitWd * 13, frameHeight * 0.08)

            rect5 = QtCore.QRectF(lineBWd, lineCHt, unitWd * 4.5, frameHeight * 0.08)
            rect6 = QtCore.QRectF(lineBWd + (unitWd * 4.5), lineCHt, unitWd * 14, frameHeight * 0.08)

            rect7 = QtCore.QRectF(lineCWd, lineCHt, unitWd * 7, frameHeight * 0.08)
            rect8 = QtCore.QRectF(lineCWd + (unitWd * 7), lineCHt, unitWd * 8, frameHeight * 0.08)

            rect9 = QtCore.QRectF(frameWidth * 0.1, 0, unitWd * 10, lineBHt)
            rect10 = QtCore.QRectF(frameWidth * 0.2, 0, unitWd * 15, lineBHt)

            rect11 = QtCore.QRectF(lineDWd, lineCHt, unitWd * 7.5, frameHeight * 0.08)
            rect12 = QtCore.QRectF(lineDWd + (unitWd * 7.5), lineCHt, unitWd * 20, frameHeight * 0.08)

            rect13 = QtCore.QRectF(frameWidth * 0.4, 0, unitWd * 12, lineBHt)
            rectKeyframe = QtCore.QRectF(frameWidth * 0.85, frameHeight * 0.85, unitWd * 15, frameHeight * 0.15)

            # -----------------------------

            painter = QtGui.QPainter()

            painter.begin(pixmap)
            painter.setOpacity(0.2)
            painter.setPen(QtGui.QColor(255, 255, 255))

            painter.drawLine(0, 0, frameWidth, frameHeight)
            painter.drawLine(0, frameHeight, frameWidth, 0)

            painter.drawLine(0, frameHeight * 0.333, frameWidth, frameHeight * 0.333)
            painter.drawLine(0, frameHeight * 0.666, frameWidth, frameHeight * 0.666)

            painter.drawLine(frameWidth * 0.333, 0, frameWidth * 0.333, frameHeight)
            painter.drawLine(frameWidth * 0.666, 0, frameWidth * 0.666, frameHeight)

            painter.setOpacity(0.4)
            painter.setPen(QtGui.QColor(0, 0, 0))
            painter.setBrush(QtGui.QBrush(Qt.black, Qt.SolidPattern))
            painter.drawRect(0, 0, frameWidth, frameHeight * 0.1)
            painter.drawImage(source.topLeft(), overlay)
            # top
            painter.setOpacity(0.7)
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.setBrush(QtGui.QBrush(Qt.black, Qt.SolidPattern))
            painter.drawRect(0, frameHeight * 0.92, frameWidth * 0.85, frameHeight)
            painter.drawRect(rectKeyframe)
            # buttom
            painter.setOpacity(1)
            painter.setPen(QtGui.QColor(255, 255, 255))

            # painter.drawRect(target)

            painter.setFont(titleFont)
            painter.drawText(rect1, Qt.AlignCenter, "cam : ")
            painter.setFont(dataFont)
            painter.drawText(rect2, Qt.AlignCenter, cam)

            painter.setFont(titleFont)
            painter.drawText(rect3, Qt.AlignCenter, "date : ")
            painter.setFont(dataFont)
            painter.drawText(rect4, Qt.AlignCenter, date)

            painter.setFont(titleFont)
            painter.drawText(rect5, Qt.AlignCenter, "artist : ")
            painter.setFont(dataFont)
            painter.drawText(rect6, Qt.AlignCenter, artist)

            painter.setFont(titleFont)
            painter.drawText(rect7, Qt.AlignCenter, "machine : ")
            painter.setFont(dataFont)
            painter.drawText(rect8, Qt.AlignCenter, machine)

            painter.setFont(titleFont)
            painter.drawText(rect11, Qt.AlignCenter, "comment : ")
            painter.setFont(dataFont)
            painter.drawText(rect12, Qt.AlignCenter, cmt)

            painter.setFont(keyframeFont)
            painter.drawText(rectKeyframe, Qt.AlignCenter, str(frame))

            painter.setFont(dataFont)
            painter.drawText(rect9, Qt.AlignCenter, project)
            painter.drawText(rect10, Qt.AlignCenter, dep)
            painter.drawText(rect13, Qt.AlignCenter, strSize)

            painter.end()
            '''
            if outputPath:
                import re
                bPath = os.path.dirname(sourceImage)
                bName = os.path.basename(sourceImage)

                spSor = re.split('\\|/', bPath)
                spOut = re.split('\\|/', outputPath)

                if spSor == spOut:
                    print 'samePath'
                    # means continue to run isReplace part
                else:
                    spOut.append(bName)
                    newPath = '\\'.join(spOut)
                    pixmap.save(newPath)
                    return newPath
                    print 'finish'
            '''
            if isReplace:
                os.remove(sourceImage)
                pixmap.save(sourceImage)
                return sourceImage
                print 'finish'
            else:
                bName = os.path.basename(sourceImage)
                bPath = os.path.dirname(sourceImage)
                newPath = bPath + '\\ui_' + bName
                pixmap.save(newPath)
                return newPath
                print 'finish'


OMP = outputMayaPlayblast()
ans2 = OMP.outputPlayblast('sq01_sc01_sh0010_100f_230f_fps24Shape')
print ans2


CTM = sequenceToMov()
CTM.setCameraName('sq01_sc01_sh0010_100f_230f_fps24')
CTM.setAudio(ans2[2][0], ans2[2][1])
CTM.createMovie(ans2[0],isUI=True)




