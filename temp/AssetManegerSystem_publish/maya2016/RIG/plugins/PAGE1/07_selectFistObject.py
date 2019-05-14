

#  ////////////////////////////////////////////////////////////////////
#  //                          _ooOoo_                               //
#  //                         o8888888o                              //
#  //                         88" . "88                              //
#  //                         (| ^_^ |)                              //
#  //                         O\  =  /O                              //
#  //                      ____/`---'\____                           //
#  //                    .'  \\|     |//  `.                         //
#  //                   /  \\|||  :  |||//  \                        //
#  //                  /  _||||| -:- |||||-  \                       //
#  //                  |   | \\\  -  /// |   |                       //
#  //                  | \_|  ''\---/''  |   |                       //
#  //                  \  .-\__  `-`  ___/-. /                       //
#  //                ___`. .'  /--.--\  `. . ___                     //
#  //              ."" '<  `.___\_<|>_/___.'  >'"".                  //
#  //            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 //
#  //            \  \ `-.   \_ __\ /__ _/   .-` /  /                 //
#  //      ========`-.____`-.___\_____/___.-`____.-'========         //
#  //                           `=---='                              //
#  //      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        //
#  //            		                                       	     //
#  ////////////////////////////////////////////////////////////////////

from PySide import QtGui
from PySide import QtCore

class showChoose(QtGui.QWidget):
    
    def showUI(self):
        Qmsg = QtGui.QMessageBox(self)
        Qmsg.setWindowTitle("choose")
        Lbtn = Qmsg.addButton('left',QtGui.QMessageBox.ActionRole)  
        Rbtn = Qmsg.addButton('right',QtGui.QMessageBox.ActionRole)     
        cancelButton = Qmsg.addButton("cancel",QtGui.QMessageBox.ActionRole)        
        Qmsg.setText('do you want to select ....  side?')  
        Qmsg.exec_()    
    
        reply=Qmsg.clickedButton()                  
        if reply == Lbtn:
            self.mirrorFistAction(mod='LR',isSel=True)
        elif reply == Rbtn:
            self.mirrorFistAction(mod='RL',isSel=True)
        else:
            print 'cancel'
    
    #=======================
    
    def mirrorFistAction(self,mod='LR',isSel=False):
        if mod=='LR':
            frm='L'
            to='R'
        else:
            frm='R'
            to='L'
        data=['FKExtraPinkyFinger1_',
        'FKExtraPinkyFinger2_',
        'FKExtraPinkyFinger3_',
        
        'FKExtraRingFinger1_',
        'FKExtraRingFinger2_',
        'FKExtraRingFinger3_',
        
        'FKExtraMiddleFinger1_',
        'FKExtraMiddleFinger2_',
        'FKExtraMiddleFinger3_',
        
        'FKExtraIndexFinger1_',
        'FKExtraIndexFinger2_',
        'FKExtraIndexFinger3_',
        
        'FKExtraThumbFinger1_',
        'FKExtraThumbFinger2_',
        'FKExtraThumbFinger3_']
        if isSel:
            cmds.select(cl=1)
            for d in data:
                cmds.select(d+mod[0],add=1)
        else:
            for d in data:
                mirrorHandpos(d+frm,d+to)
        
theC = showChoose()
theC.setWindowFlags(Qt.WindowStaysOnTopHint)
theC.showUI()





