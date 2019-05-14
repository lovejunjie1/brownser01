def createState(state,artist='xxx',type='state-high'):
    mainStyle='QGroupBox{color:%s;border:5px solid %s;border-radius: 9px;}QGroupBox::title { subcontrol-origin: margin;subcontrol-position: top left;left:10px;top:-3px;margin-left: 0px;padding:0 10px; } '
    stateGrp=QtGui.QGroupBox(type)
    stateGrp.setAttribute(Qt.WA_DeleteOnClose)
    stateGVB=QtGui.QVBoxLayout()
    stateGrp.setLayout(stateGVB)
    
    messageLab=QtGui.QLabel()
    messageLab.setToolTip('statemessage')
    stateGVB.addWidget(messageLab) 
    if state=='waiting':
        stateGrp.setMaximumHeight(80)
        stateGrp.setStyleSheet(mainStyle % ('white','white'))
        
        messageLab.setText('Task created,waiting for Artist')

        actionBtn=QtGui.QPushButton('let me do it')
        actionBtn.setToolTip('actionbutton')
        stateGVB.addWidget(actionBtn) 
        stateGVB.addStretch  (1)       
        
        return stateGrp
    if state=='pre-checking':
        stateGrp.setMaximumHeight(120)
        stateGrp.setStyleSheet(mainStyle % ('#AAAAAA','#AAAAAA'))
        messageLab.setText(artist+' ready to work on it,checking pre-department source')
        
        actionBtn=QtGui.QPushButton('open')
        actionBtn.setToolTip('open pre-department')
        stateGVB.addWidget(actionBtn) 
         
        
        lh=QtGui.QHBoxLayout()
        okBtn=QtGui.QPushButton('ok')
        okBtn.setToolTip('ok pre-department')
        lh.addWidget(okBtn)
        
        replyBtn=QtGui.QPushButton('reply')
        replyBtn.setToolTip('reply pre-department')
        lh.addWidget(replyBtn)
        
        stateGVB.addLayout(lh)
        stateGVB.addStretch  (1) 
        return stateGrp
    if state=='working' :
        stateGrp.setMaximumHeight(80)
        stateGrp.setStyleSheet(mainStyle % ('yellow','yellow'))
        messageLab.setText(artist+' working on this task')
        
        lh=QtGui.QHBoxLayout()
        okBtn=QtGui.QPushButton('upload')
        okBtn.setToolTip('upload')
        lh.addWidget(okBtn)
        
        replyBtn=QtGui.QPushButton('reply')
        replyBtn.setToolTip('read reply')
        lh.addWidget(replyBtn)
        
        stateGVB.addLayout(lh)  
        stateGVB.addStretch  (1) 
        return stateGrp
    if state=='checking':
        stateGrp.setMaximumHeight(120)
        stateGrp.setStyleSheet(mainStyle % ('#ffb666','#ffb666'))
        messageLab.setText('file already upload.wait '+artist+' to check.')
                
        actionBtn=QtGui.QPushButton('open')
        actionBtn.setToolTip('open check file')
        stateGVB.addWidget(actionBtn) 
         
        
        lh=QtGui.QHBoxLayout()
        okBtn=QtGui.QPushButton('ok')
        okBtn.setToolTip('upload check file')
        lh.addWidget(okBtn)
        
        replyBtn=QtGui.QPushButton('reply')
        replyBtn.setToolTip('reply check file')
        lh.addWidget(replyBtn)
        
        stateGVB.addLayout(lh)
        stateGVB.addStretch  (1) 
        return stateGrp
    if state=='modifing' :
        stateGrp.setMaximumHeight(80)
        stateGrp.setStyleSheet(mainStyle % ('red','red'))
        messageLab.setText(artist+' is fixing this task')
        
        lh=QtGui.QHBoxLayout()
        okBtn=QtGui.QPushButton('view Rpl')
        okBtn.setToolTip('view reply document')
        lh.addWidget(okBtn)
        
        replyBtn=QtGui.QPushButton('upload')
        replyBtn.setToolTip('upload fix file')
        lh.addWidget(replyBtn)
        
        stateGVB.addLayout(lh)  
        stateGVB.addStretch  (1) 
        return stateGrp
    if state=='uploaded':
        stateGrp.setMaximumHeight(120)
        stateGrp.setStyleSheet(mainStyle % ('#00AA00','#00AA00'))
        messageLab.setText('file already uploaded')
        
        actionBtn=QtGui.QPushButton('upload new')
        actionBtn.setToolTip('upload new')
        stateGVB.addWidget(actionBtn) 
        stateGVB.addStretch  (1)
        return stateGrp
        
    if state=='nextneed':
        stateGrp.setMaximumHeight(80)
        stateGrp.setStyleSheet(mainStyle % ('red','red'))
        messageLab.setText('next deparment need some fix')
        
        lh=QtGui.QHBoxLayout()
        okBtn=QtGui.QPushButton('upload')
        okBtn.setToolTip('upload need')
        lh.addWidget(okBtn)
        
        replyBtn=QtGui.QPushButton('check need')
        replyBtn.setToolTip('check need')
        lh.addWidget(replyBtn)
        
        stateGVB.addLayout(lh)  
        stateGVB.addStretch  (1) 
        return stateGrp
        
        