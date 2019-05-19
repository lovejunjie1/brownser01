import os
import sys
import json_pack as json
#o_path = os.getcwd()
#print 'o_Path',o_path

#print '__file__',__file__
#print 'abs',os.path.abspath(__file__)

def getSoftwareConfig(testPath = ''):
	#C:\gitLab\brownser01\bin\util\__init__.py
	if testPath:
		theAbsPath = testPath
	else:
		theAbsPath = os.path.abspath(__file__)
	#print theAbsPath
	spPath = theAbsPath.split('bin')
	configPath = spPath[0] + '/configs/universeSet.pipeSet'
	ext = os.path.exists(configPath)
	#print 'configPath',configPath,ext
	hey = json.loadJson(configPath)
	return hey

def get():
    pass

def getTypeNameDict():
	theDict = {
	'Charactors':'CHR',
	'Props':'PRP',
	'Sets':'SET',
	'Elements':'ELM'
	}
	return theDict

def getDepNameDict():
	depDict = {
	'Model':'mod',
	'LookDev':'look'
	}
	return depDict

def getPath(dataType='', name='', varient='', dep='', project='',isHistory = False,location='work'):
	if isHistory:
		#D:\testDir\pipPrj\ZZZ\.HistoryInfo\_assets\Charactors\girl\history
		pathRoot = '%(serv)s/%(prj)s/.HistoryInfo/%(bigType)s/%(dataType)s/%(name)s/history'
	
	else:
		#pathRoot = '%(serv)s/%(prj)s/%(bigType)s/%(dataType)s/%(name)s/%(dep)s/%(var)s/Main/%(st)s_%(name)s_%(depst)s.ma'
		pathRoot = '%(serv)s/%(prj)s/%(bigType)s/%(dataType)s/%(name)s/%(dep)s/%(var)s/Main'
	
	bigType = '_shots'
	if dataType in ['Charactors','Props','Sets','Elements']:
		bigType = '_assets'
	keyDict = getTypeNameDict()
	depDict = getDepNameDict()

	mainData = getSoftwareConfig()
	#print mainData
	if location == 'main':
		serv = mainData['general']['pipeMainPath']
	elif location == 'work':
		serv = mainData['general']['pipeWorkPath']
	elif location == 'bak':
		serv = mainData['general']['pipeBakPath']
	elif location == 'local':
		serv = mainData['general']['localCachePath']

	#print 'serv',serv
	print 'dep',dep
	print keyDict
	cbDict = {
		'serv':serv,
		'prj':project,
		'bigType':bigType,
		'dataType':dataType,
		'st':keyDict[dataType],
		'name':name,
		'dep':dep,
		'depst':depDict[dep],
		'var':varient
		}

	rtRoot = pathRoot % cbDict
	return rtRoot

def getPublishSlot(dataType='', name='', varient='', dep='', project=''):
	thePath = getPath(dataType=dataType, name=name, varient=varient, dep=dep, project=project,location='main')
    


def getWorkSlot(dataType='', name='', varient='', dep='', project=''):
	thePath = getPath(dataType=dataType, name=name, varient=varient, dep=dep, project=project,location='work')
	theDir = '/'.join(thePath.split('/')[:-1])

	if not os.path.exists(theDir):
		os.makedirs(theDir)

	returnPath = ''
	dirList = os.listdir(theDir)
	if dirList:
		biggest = 0
		for dl in dirList:
			cbPath = theDir+'/'+dl
			if os.path.isdir(cbPath):
				val = int(dl.split('.')[-1])
				if val > biggest:
					biggest = val
		biggest += 1
		bigStr = str(biggest).zfill(3)
		returnPath = thePath + '.' + bigStr
	else:
		returnPath = thePath + '.001'

	print returnPath
	return returnPath

def help():
    pass

if __name__ == '__main__':
	testDic = {"basic": {"project": "ZZZ", "dataType": "Charactors", "name": "girl", "varient": "defaultVersion", "path": "D:/testDir/pipePrj/ZZZ/_assets/Charactors/girl/LookDev/defaultVersion/Main", "sizeLevel": 1, "dep": "LookDev"}}
	td = testDic['basic']
	getWorkSlot(dataType=td['dataType'],name=td['name'], varient=td['varient'], dep=td['dep'], project=td['project'])