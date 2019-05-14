class FistClass():
    def CreateArrow(self,arrowName):
        arrow=cmds.curve(d=1,p=((2,0,-2),(4,0,0),(2,0,2),(2,0,1),(0,0,1),(0,0,-1),(2,0,-1),(2,0,-2)),n=arrowName)
        cmds.transformLimits(arrow,tx=(0,1),etx=(1,1))
        grp=cmds.group(arrow,n=arrow+'_grp')
        SDK=cmds.group(grp,n=arrow+'_SDK')
        Zero=cmds.group(SDK,n=arrow+'_Zero')
    
        cmds.setAttr(arrow+'.ty',l=1,k=0,channelBox=0)
        cmds.setAttr(arrow+'.tz',l=1,k=0,channelBox=0)
        
        cmds.setAttr(arrow+'.rx',l=1,k=0,channelBox=0)
        cmds.setAttr(arrow+'.ry',l=1,k=0,channelBox=0)
        cmds.setAttr(arrow+'.rz',l=1,k=0,channelBox=0)
        
        cmds.setAttr(arrow+'.sx',l=1,k=0,channelBox=0)
        cmds.setAttr(arrow+'.sy',l=1,k=0,channelBox=0)
        cmds.setAttr(arrow+'.sz',l=1,k=0,channelBox=0)
        
        cmds.setAttr(arrow+'.v',l=1,k=0,channelBox=0)
        return Zero
    
    
    def createFistCtrl(self):
        Larrow=self.CreateArrow('l_arrow_ctrl')
        lmatrix=cmds.xform('Wrist_L',q=1,ws=1,m=1)
        cmds.xform(Larrow,ws=1,m=lmatrix)
        cmds.rotate( '90deg', 0, '180deg', Larrow,r=1,os=1 )
        cmds.move( 0, '-1in', 0, Larrow,relative=True,os=1)
        cmds.parent(Larrow,'Fingers_L')
        
        Rarrow=self.CreateArrow('r_arrow_ctrl')
        rmatrix=cmds.xform('Wrist_R',q=1,ws=1,m=1)
        cmds.xform(Rarrow,ws=1,m=rmatrix)
        cmds.rotate( '90deg', 0, 0, Rarrow,r=1,os=1 )
        cmds.move( 0, '1in', 0, Rarrow,relative=True,os=1)
        cmds.parent(Rarrow,'Fingers_R') 
    
FS = FistClass()
FS.createFistCtrl()