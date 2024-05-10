from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from implementation.GUI.Point import Point


class Scene(qtw.QGraphicsScene):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.reference_points = []
        self.reference_lines = []
        self.lip_points = []
        self.lip_line = None
        self.left_eye_points = []
        self.left_eye_line = None
        self.right_eye_points = []
        self.right_eye_line = None

        self.radius = 5
        self.point_pen = qtg.QPen()
        self.point_pen.setColor(qtg.QColor(0xFF0000))
        self.point_pen.setWidth(self.radius)

        self.stroke_width = 1
        self.line_pen = qtg.QPen()
        self.line_pen.setColor(qtg.QColor(0xFF0000))
        self.line_pen.setWidth(self.stroke_width)

    def rotate_the_image_left(self):
        pass
        # img = cv2.imread(self.image_path)
        # rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # cv2.imwrite(self.image_path, rotated_img)
        # self.updatePhoto()

    def rotate_the_image_right(self):
        pass
        # img = cv2.imread(self.image_path)
        # rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        # cv2.imwrite(self.image_path, rotated_img)
        # self.updatePhoto()

    def reset(self, items):
        # if a user clicks multiple times "detect reference" we need to make sure we don't draw excessive points
        for item in items:
            self.removeItem(item)
        items.clear()

    def draw_reference(self, reference_coords):
        self.reset(self.reference_points)
        # draw points
        for i in range(4):
            x = reference_coords[i][0]
            y = reference_coords[i][1]
            point = Point(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
            point.setPen(self.point_pen)
            self.addItem(point)
            self.reference_points.append(point)

        self.draw_reference_lines()

    def draw_reference_lines(self):
        self.reset(self.reference_lines)

        for i in range(4):
            next_i = (i + 1) % 4
            x1 = self.reference_points[i].real_x()
            y1 = self.reference_points[i].real_y()
            x2 = self.reference_points[next_i].real_x()
            y2 = self.reference_points[next_i].real_y()

            line = qtw.QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(self.line_pen)
            self.addItem(line)
            self.reference_lines.append(line)
