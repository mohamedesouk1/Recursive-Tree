import numpy as np
import PySide2.QtWidgets as qtw
import PySide2.QtGui as qtgui
from PySide2.QtCore import Qt,QPoint,QLineF,QPropertyAnimation,QTimeLine
import sys

class Tree:
    t_girth=30 # todo take argument from user
    final_color=[255,0,239,255] # todo take argument from user
    t_color=qtgui.QColor(255,255,255,255)
    trunk=200

class branch(Tree):
    def __init__(self,begin,end):
        self.begin=begin
        self.end=end
        self.drawn=False
        self.color=self.t_color
        self.girth=self.t_girth
        
    # todo add animation       
    def print_branch(self,painter):
        painter.setPen(qtgui.QPen(self.color, self.girth, Qt.SolidLine))
        painter.drawLine(*self.begin,*self.end)
        # self.line=QLineF(*self.begin,*self.end)
        # anim_line=painter.drawLine(self.line)
        # timeline=QTimeLine(100)
        # timeline.valueChanged.connect(self.time_line_change)
        # timeline.setDirection(QTimeLine.Forward)
        # timeline.start()
     
    def time_line_change(self,val):
        print(val)
        end=self.line.pointAt(val)
        return QLineF(self.line.p1(),end)
        #painter.drawPath(path)
            
    def create_branch(self,num_branch):
        
        self.drawn=True
        direction=np.subtract(self.end,self.begin)*0.7
        temp_branches=[]
        Tree.t_girth=Tree.t_girth*0.9
        old_color=list(Tree.t_color.getRgb())
        color=[old_color[i]-7*(255-c)/(Tree.trunk*0.7) if old_color[i]-7*(255-c)/(Tree.trunk*0.7)>0 else 0 for i,c in enumerate(Tree.final_color)]
        Tree.t_color=qtgui.QColor(*color)
        for i in range(num_branch):
            angle=(-90+(180/(2*num_branch))+(180/num_branch)*i)  
            theta = np.deg2rad(angle)
            rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
            rot_dir=(np.dot(rot,direction))
            t_branch=branch(self.end,self.end+rot_dir)   
            temp_branches.append(t_branch)
        return temp_branches
        
        
        
class Window(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree :)")
        self.trunk=200
        # size of window 
        self.xbound=1000
        self.ybound=600
        self.num_branch=2 # todo take argument from user
        self.girth=30 # todo take argument from user
        self.final_color=[255,0,239,255] # todo take argument from user
        self.tree=[]
        self.tree.append(branch(np.array([self.xbound//2,self.ybound]),np.array([self.xbound//2,self.ybound-self.trunk])))

        self.label = qtw.QLabel()
        canvas = qtgui.QPixmap(self.xbound, self.ybound)
        canvas.fill(Qt.black)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        
        painter = qtgui.QPainter(self.label.pixmap())
        painter.setPen(qtgui.QPen(Qt.white, self.girth, Qt.SolidLine))

        for i in range(len(self.tree)):
            self.tree[i].print_branch(painter)
        painter.end()
        
    def mousePressEvent(self, event: qtgui.QMouseEvent): 
        if event.buttons(): 
            for i in range(len(self.tree)):
                if not self.tree[i].drawn:
                    self.tree.extend(self.tree[i].create_branch(self.num_branch)) 
                    self.draw_something()
            self.repaint()




def main():
    #create app
    app=qtw.QApplication(sys.argv)

    #create window
    window=Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
        