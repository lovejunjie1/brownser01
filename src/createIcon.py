# -*- coding: utf-8 -*-
import os
import sys
import subprocess, os

def getRootPath():
    loadPath = ''
    for path in sys.path:
        print path+'\\pathfile.browser'
        if os.path.exists(path+'\\pathfile.browser'):
            loadPath = path

    return loadPath

def main(rccPath = 'C:/Python27/Lib/site-packages/PyQt4'):
    rootPath = getRootPath()
    rootPath = rootPath.replace('\\','/')

    if os.path.exists(rootPath + '/src/resources.py'):
        os.remove(rootPath + '/src/resources.py')


    images = os.listdir(rootPath + '/src/icon')
    qss = os.listdir(rootPath + '/src/qss')
    with open(rootPath + '/src/resources.qrc', 'w+') as f:
        f.write(u'<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')

        for item in images:
            f.write(u'<file alias="icon/'+ item +'">icon/'+ item +'</file>\n')

        for item in qss:
            f.write(u'<file alias="qss/'+ item +'">qss/'+ item +'</file>\n')

        f.write(u'</qresource>\n</RCC>')
    spellCommand = rccPath + '/pyrcc4.exe -o %s/src/resources.py %s/src/resources.qrc' % (rootPath,rootPath)
    pipe = subprocess.Popen(spellCommand, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, creationflags=0x08)

    #pipe = os.system()
if __name__ == '__main__':
    testPath = r'C:\gitLab\brownser01'
    if testPath not in sys.path:
        sys.path.append(testPath)
    # maya本身不带rcc，需要自己装一个pyqt或者pyside，把main的rccpath指到那个python里面的目录里
    main()