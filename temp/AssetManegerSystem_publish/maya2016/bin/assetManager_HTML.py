# -*- coding: utf-8 -*-
from PySide import QtCore
import os, random

class assetManager_HTML(QtCore.QObject):
    def HTML_CreateEmptyStyle(self, historyPath):
        style = (
            '<style type="text/css">  \n'
            '.iconPicL{position: relative;margin-left: 25px;float: left;} \n'
            '.iconPicR{position: relative;margin-right: 25px;float: right;} \n'
            '.timeDiv{font-family:Verdana;color:white;height:10px;text-align:center;margin:0 auto}   \n'
            '.bubbleDiv{width: 100%;  margin: 0;  border: 0px solid #4a4f58;  }  \n'
            '.bubbleItem{word-break:break-all;font-family:microsoft YaHei;font-size:15px;width: 100%;}  \n'
            '.bubble{max-width: 260px;position: relative;line-height: 20px;padding-left: 10px;padding-top: 0px;padding-bottom: 0px;border-radius: 7px;margin-top: 0px;padding-right: 10px;display: inline-block;} \n'
            '.leftBubble{position: relative;margin-left: 25px;border: 1px solid #00b6b6;background-color: #f8fdfc;}   \n'
            '.leftBubble .bottomLevel{position: absolute;top: 5px;left: -10px;border-top: 10px solid #00b6b6;border-left: 10px solid transparent;}     \n'
            '.leftBubble .topLevel{position: absolute;top: 6px;left: -8px;border-top: 10px solid #f8fdfc;border-left: 10px solid transparent;z-index: 100;  }   \n'
            '.rightBubble{position: relative;margin-right: 25px;float: right;border: 1px solid #aaa;background-color: #f8fdfc;}    \n'
            '.rightBubble .bottomLevel{position: absolute;bottom: 6px;right: -10px;border-bottom: 10px solid #aaa;border-right: 10px solid transparent;}  \n'
            '.rightBubble .topLevel{position: absolute;bottom: 7px;right: -8px;border-bottom: 10px solid #fff;border-right: 10px solid transparent;z-index: 100;}   \n'
            '.clearfix:after {visibility: hidden;display: block;font-size: 0;content: " ";clear: both;height: 0;  } \n'
            'img{max-width:300px;margin:5px 0;}\n'
            '</style>\n'
            '<div class="bubbleDiv">\n'
            '</div>\n'
            )
        reportnew = open(historyPath, 'w')
        reportnew.write(style)
        reportnew.close()
        return style

    def HTML_addMsg(self, htmlpath, message):
        # htmlPath is this type of data.
        # r'Z:\project\pig\asset\PRODUCE\Char\monkeyking\history.html'
        if not os.path.exists(htmlpath):
            self.HTML_CreateEmptyStyle(htmlpath)

        htmlFile = open(htmlpath, 'rt')
        line = []
        tryCount = 0
        inserline = 0
        for i in htmlFile.readlines():
            if (len(i) < 26) and (len(i)>20) and ('<div class="bubbleDiv">' in i):
                inserline = tryCount+1
            else:
                tryCount += 1

            line.append(i.decode('utf-8'))
        htmlFile.close()

        line.insert(inserline, message)
        print 'inserline is ' + str(inserline)
        s=''
        for li in line:
            s += li
        with open(htmlpath,'wt') as reportnew:
            reportnew.write(s.encode('utf-8'))


    def HTML_createMsg(self, contect, user, pictures, side=1, initPath='D:\\figo_tool_box'):
        pic = ''
        if pictures:
            # pictures is a array type data like ['D:\\xxx\\xxx\xxx.png','D:\\xxx\\xxx\xxx.png']
            if len(pictures) >= 3:
                for p in pictures[:3]:
                    fixP = 'file:///' + p
                    pic += '<img src=\"{}\" width=\"100\" height=\"100\" />'.format(fixP)
            else:
                for p in pictures:
                    fixP = 'file:///' + p
                    pic += '<img src=\"{}\" width=\"100\" height=\"100\" />'.format(fixP)

        sentionsA = ''
        sentionsB = ''

        avarterArray = os.listdir(self.iconPath + '\\avarter')
        countstr = ''
        for i in user:
            countstr += str(ord(i))

        random.seed(int(countstr))
        usePic = 'file:///' + self.iconPath + '\\avarter\\' + avarterArray[int(random.random() * len(avarterArray))]

        if side > 0:
            sentionsA = '<div class="bubbleItem clearfix"> <p><div class=timeDiv>'
            sentionsB = '</div></p> <div><img class=iconPicR src="' + usePic + '" width="50" height="50" /></div>  <span class="bubble rightBubble"><strong>['
        elif side < 0:
            sentionsA = '<div class="bubbleItem"> <p><div class=timeDiv>'
            sentionsB = '</div></p>  <div><img class=iconPicL src="' + usePic + '" width="50" height="50" /></div> <span class="bubble leftBubble"><strong>['
        else:
            sentionsA = '<div class="bubbleItem"> <p><div class=timeDiv>'
            sentionsB = '</div></p>   <span class="bubble leftBubble"><strong>['

        message = sentionsA
        message += QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        message += sentionsB
        message += user
        message += ']:</strong><br>'
        message += contect
        message += '<br>'
        message += pic
        message += '<span class="bottomLevel"></span>  <span class="topLevel"></span>  </span>  </div> \n'
        return message