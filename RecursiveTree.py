import PySide2.QtWidgets as qtw
import PySide2.QtGui as qtgui
from PySide2.QtCore import Qt,QPoint
import sys


# Todo: make arguments parser and windows compatibility
# import argparse
# import platform
# #parser=argparse.ArgumentParser(description="Draws a Tree recursively")
# #parser.add_argument()



class Window(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree :)")
        self.trunk=200
        # size of window 
        self.xbound=1000
        self.ybound=600
        self.num_branch=2 # todo take argument from user
        self.girth=50 # todo take argument from user
        self.final_color=[255,0,239,255] # todo take argument from user
        self.label = qtw.QLabel()
        canvas = qtgui.QPixmap(self.xbound, self.ybound)
        canvas.fill(Qt.black)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = qtgui.QPainter(self.label.pixmap())
        painter.setPen(qtgui.QPen(Qt.white, self.girth, Qt.SolidLine))
        
        painter.translate(QPoint(self.xbound//2,self.ybound))
        self.tree(painter,self.trunk)
        painter.end()
        
        
        
    def tree(self,painter,len):
        if len>=1:
            painter.drawLine(0,0,0, -len) # @param x1 y1 x2 y2 
            painter.translate(QPoint(0,-len))
            for i in range(self.num_branch):
                painter.save()

                painter.rotate(-90+(180/(2*self.num_branch))+(180/self.num_branch)*i)


                old_color=list(painter.pen().color().getRgb())
                color=[old_color[i]-7*(255-c)/(self.trunk/1.6) if old_color[i]-7*(255-c)/(self.trunk/1.6)>0 else 0 for i,c in enumerate(self.final_color)]
                painter.setPen(qtgui.QPen(qtgui.QColor(*color), painter.pen().width()//1.6, Qt.SolidLine))

                self.tree(painter,len//1.6)

                painter.restore()



def main():
    #create app
    app=qtw.QApplication(sys.argv)

    #create window
    window=Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()