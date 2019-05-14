
def HTML_CreateEmptyStyle(path):
    style=(
        '<style type="text/css">  \n' 
        '.iconPicL{position: relative;margin-left: 25px;float: left;} \n'
        '.iconPicR{position: relative;margin-right: 25px;float: right;} \n'
        '.timeDiv{font-family:Verdana;color:white;height:10px;text-align:center;margin:0 auto}   \n' 
        '.bubbleDiv{width: 100%;  margin: 0;  border: 0px solid #4a4f58;  }  \n'    
        '.bubbleItem{word-break:break-all;font-family:microsoft YaHei;font-size:15px;width: 100%;}  \n'    
        '.bubble{max-width: 355px;position: relative;line-height: 20px;padding-left: 10px;padding-top: 0px;padding-bottom: 0px;border-radius: 7px;margin-top: 0px;padding-right: 10px;display: inline-block;} \n'     
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
    reportnew = open(path, 'w')  
    reportnew.write(style)  
    reportnew.close() 
    return style



def HTML_addMsg(htmlpath,message):
    htmlFile = open(htmlpath,'r')
    line = []  
    for i in htmlFile.readlines():  
        line.append(i)
    htmlFile.close()
    
    line.insert(-1,message)
    
    s = ''.join(line)  
    reportnew = open(htmlpath, 'w')  
    reportnew.write(s)  
    reportnew.close() 
    
def HTML_createMsg(contect,user,pictures,side=1): 
    pic='' 
    if pictures:
        for p in pictures:
            pic+='<img src=\"{}\" width=\"100\" height=\"100\" />'.format(p)
    sentionsA=''
    sentionsB=''
    usePic='' #getAvertarFromUser(user)
    if not usePic:
        usePic=r'D:\figo_tool_box\icon\lifeStyle18.png'
    if side>0:
        sentionsA='<div class="bubbleItem clearfix"> <p><div class=timeDiv>'
        sentionsB='</div></p> <div><img class=iconPicR src="'+usePic+'" width="50" height="50" /></div>  <span class="bubble rightBubble"><strong>['
    elif side<0:
        sentionsA='<div class="bubbleItem"> <p><div class=timeDiv>'
        sentionsB='</div></p>  <div><img class=iconPicL src="'+usePic+'" width="50" height="50" /></div> <span class="bubble leftBubble"><strong>['
    else:
        sentionsA='<div class="bubbleItem"> <p><div class=timeDiv>'
        sentionsB='</div></p>   <span class="bubble leftBubble"><strong>['   
            
            
    message=sentionsA
    message+=QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
    message+=sentionsB
    message+=user
    message+=']:</strong><br>'
    message+=contect
    message+='<br>'
    message+=pic
    message+='<span class="bottomLevel"></span>  <span class="topLevel"></span>  </span>  </div> \n'
    return message

#HTML_CreateEmptyStyle('d:/ccc.html')

#msg=HTML_createMsg('ttasdasdttxt','haap',["E:\pic1.png","E:\pic2.png"],side=-1)

#HTML_addMsg('d:/ccc.html',msg)