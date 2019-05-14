from xml.dom.minidom import Document
import xml

def XML_isElementInPath(self,parentPath,searchString):
    tempArray=[]
    theNode=False
    for pp in parentPath.childNodes:
        tempArray.append(pp.nodeName)
        if searchString==pp.nodeName:
            theNode=pp
    return theNode

def XML_getNiceName(self):
    """
    print os.environ
    for i in os.environ:
        print os.environ[i]
        
    import platform
    platform.node()   
    platform.platform()
    
    import sys, socket
    hostname = socket.gethostname()
    print "Host name:", hostname
    """
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'System\CurrentControlSet\Services\lanmanserver\Parameters')
    
    value = _winreg.QueryValueEx(key,"srvcomment")
    return value[0]

def XML_CreateNode(self,version='high'):
    visNumber=self.visNumber
    geoNumber=self.geoNumber
    message=self.message
    userName=self.XML_getNiceName()
    localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    TransMessage=message.decode('gbk')
    
    doc = Document()  #创建DOM文档对象
    fileMessage = doc.createElement('fileMessage') #创建根元素
    
    submitTime = doc.createElement('time') #时间
    submitUser = doc.createElement('user') #提交人
    submitVisNumber = doc.createElement('visNumber') #已显示数量
    submitGeoNumber = doc.createElement('geoNumber') #geometry数量
    submitVersion = doc.createElement('version') #版本类型
    submitMessage = doc.createElement('message') #备注消息
    
    submitTimeNode=doc.createTextNode(localtime) 
    submitUserNode=doc.createTextNode(userName) 
    submitGeoNumberNode=doc.createTextNode(str(geoNumber)) 
    submitVisNumberNode=doc.createTextNode(str(visNumber)) 
    submitVersionNode=doc.createTextNode(version) 
    submitMessageNode=doc.createTextNode(TransMessage) 
    
    submitTime.appendChild(submitTimeNode)
    submitUser.appendChild(submitUserNode)
    submitVisNumber.appendChild(submitVisNumberNode)
    submitGeoNumber.appendChild(submitGeoNumberNode)
    submitVersion.appendChild(submitVersionNode)
    submitMessage.appendChild(submitMessageNode)

    fileMessage.appendChild(submitUser)
    fileMessage.appendChild(submitVisNumber)
    fileMessage.appendChild(submitGeoNumber)
    fileMessage.appendChild(submitVersion)
    fileMessage.appendChild(submitMessage)
    fileMessage.appendChild(submitTime)
    
    return fileMessage
  
def XML_createRootNode(self,path):
    if path!='':
        doc = Document()  #创建DOM文档对象
        mainTitle = doc.createElement('mainTitle') #根 
        doc.appendChild(mainTitle)
        f = open(path,'w') #path like 'd:/bookstore.xml'
        f.write(doc.toprettyxml(indent = '',encoding="utf-8"))
        f.close()
    else:
        print 'path is empty'

def XML_writeNode(self,node,path):
    if path!='':
        isFileExist=os.path.isfile(path)
        if isFileExist:
            try:
                xml.dom.minidom.parse(path)
            except Exception:
                self.XML_createRootNode(path)
        else:
             self.XML_createRootNode(path)
        readfile= xml.dom.minidom.parse(path)
        root = readfile.documentElement
        root.appendChild(node)
        f = open(path,'w') #path like 'd:/bookstore.xml'
        f.write(root.toprettyxml(indent = '',encoding="utf-8"))
        f.close()
    else:
        print 'path is empty'
    
def XML_readXmlToDict(self,path):
    if path!='':
        readfile= xml.dom.minidom.parse(path)
        root = readfile.documentElement
        
        itemsArray=[]
        for i in root.childNodes:
            if i.nodeType==1:
                itemsArray.append(i)
        
        mainDict=[]
        for count,ia in enumerate(itemsArray):
            theDict={}
            
            for iac in  ia.childNodes:
                tempDict={}
                if iac.nodeType==1:
                    
                    tempDict={iac.nodeName:iac.childNodes[0].data}
                    theDict.update(tempDict)
            print theDict
            mainDict.append(theDict)
        return mainDict
    else:
        print 'path is empty'
        return False