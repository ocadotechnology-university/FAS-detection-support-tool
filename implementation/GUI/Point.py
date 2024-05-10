
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg


class Point(qtw.QGraphicsEllipseItem):
    def __init__(self,*args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setFlag(qtw.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        scene = self.scene()
        # print(self.rect().x())
        # print(self.rect().y())
        # print(self.pos().x())
        # print(self.y())

        print(scene)
        if scene:
            print("xd")
            scene.draw_lines()
            print(f"{self.x()=}")
            print(f"{self.pos().x()=}")
            print(f"{self.rect().x()=}")
            print(f"{self.rect().center().x()=}")
            print(f"{self.rect().getCoords()=}")

    def real_x(self):
        return self.rect().center().x()+self.x()

    def real_y(self):
        return self.rect().center().y()+self.y()

    def get_real_coords(self):
        return [self.real_x(),self.real_y()]






