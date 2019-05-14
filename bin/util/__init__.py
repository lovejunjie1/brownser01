import os
import sys
import json_pack as json
#o_path = os.getcwd()
#print 'o_Path',o_path

#print '__file__',__file__
#print 'abs',os.path.abspath(__file__)

def getSoftwareConfig():
	theAbsPath = os.path.abspath(__file__)
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

	print 'serv',serv
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

def slot():
    pass


def has():
    pass

def help():
    pass

if __name__ == '__main__':
	getPath()