
def getAssetManagerPath():
    version = 'maya2016'
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
