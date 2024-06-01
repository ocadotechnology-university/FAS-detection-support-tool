from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from implementation.GUI.point import Point


class Scene(qtw.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.reference_points = []
        self.lines = []
        self.lip_points = []
        self.left_eye_points = []
        self.right_eye_points = []

        self.radius = 7
        self.point_pen = qtg.QPen()
        self.point_pen.setColor(qtg.QColor(0xD9D9D9))
        self.point_pen.setWidth(self.radius)

        self.stroke_width = 7
        self.line_pen = qtg.QPen()
        self.line_pen.setColor(qtg.QColor(0xD9D9D9))
        self.line_pen.setWidth(self.stroke_width)

    def reset(self, items):
        # if a user clicks multiple times "detect ..." we need to make sure we don't draw excessive points
        for item in items:
            self.removeItem(item)
        items.clear()

    def draw_points(self, points_list, new_coords, tooltip):
        self.reset(points_list)
        for i in range(len(new_coords)):
            x = new_coords[i][0]
            y = new_coords[i][1]
            point = Point(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
            point.setPen(self.point_pen)
            self.addItem(point)
            points_list.append(point)
            point.setToolTip(tooltip)
        self.draw_lines()

    def draw_reference(self, reference_coords):
        self.draw_points(self.reference_points, reference_coords, "Referencja")

    def draw_left_eye(self, coords):
        self.draw_points(self.left_eye_points, coords, "Lewe oko")

    def draw_right_eye(self, coords):
        self.draw_points(self.right_eye_points, coords, "Prawe oko")

    def draw_upper_lip(self, coords):
        self.draw_points(self.lip_points, coords,"Górna warga")

    def sub_draw_lines(self, point_list):
        length = len(point_list)
        for i in range(length):
            next_i = (i + 1) % length
            x1 = point_list[i].real_x()
            y1 = point_list[i].real_y()
            x2 = point_list[next_i].real_x()
            y2 = point_list[next_i].real_y()

            line = qtw.QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(self.line_pen)
            self.addItem(line)
            self.lines.append(line)

    def draw_lines(self):
        # reference lines
        self.reset(self.lines)
        if self.reference_points:
            self.sub_draw_lines(self.reference_points)
        if self.left_eye_points:
            self.sub_draw_lines(self.left_eye_points)
        if self.right_eye_points:
            self.sub_draw_lines(self.right_eye_points)
        if self.lip_points:
            self.sub_draw_lines(self.lip_points)

    def clear_canva_state(self):  # wyczyść kanwę
        self.reference_points = []
        self.lines = []
        self.lip_points = []
        self.left_eye_points = []
        self.right_eye_points = []

    # def set_radius_and_stroke(self):
    #     width = (self.width())
    #     height = (self.height())
    #     x = min (width,height)
    #     self.radius = x * 0.01
    #     self.stroke_width = x * 0.005
