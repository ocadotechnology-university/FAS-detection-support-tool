# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QGraphicsView,
                               QGridLayout, QGroupBox, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem, QWidget)
from resources import GUI_resources_rc


class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(738, 512)
        icon = QIcon()
        icon.addFile(u":/icon/Ikona.png", QSize(), QIcon.Normal, QIcon.Off)
        w_MainWindow.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(w_MainWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_measure = QPushButton(w_MainWindow)
        self.pb_measure.setObjectName(u"pb_measure")

        self.gridLayout.addWidget(self.pb_measure, 10, 0, 1, 2)

        self.pushButton_6 = QPushButton(w_MainWindow)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font = QFont()
        font.setStrikeOut(True)
        self.pushButton_6.setFont(font)

        self.gridLayout.addWidget(self.pushButton_6, 6, 0, 1, 1)

        self.groupBox_2 = QGroupBox(w_MainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.le_referenceMM = QLineEdit(self.groupBox_2)
        self.le_referenceMM.setObjectName(u"le_referenceMM")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_referenceMM)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.groupBox = QGroupBox(w_MainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_LeftEyeMM = QLineEdit(self.groupBox)
        self.le_LeftEyeMM.setObjectName(u"le_LeftEyeMM")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_LeftEyeMM)

        self.le_RightEyeMM = QLineEdit(self.groupBox)
        self.le_RightEyeMM.setObjectName(u"le_RightEyeMM")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_RightEyeMM)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.le_UpperLipMM = QLineEdit(self.groupBox)
        self.le_UpperLipMM.setObjectName(u"le_UpperLipMM")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_UpperLipMM)

        self.gridLayout.addWidget(self.groupBox, 11, 0, 1, 2)

        self.pb_DetectReference = QPushButton(w_MainWindow)
        self.pb_DetectReference.setObjectName(u"pb_DetectReference")

        self.gridLayout.addWidget(self.pb_DetectReference, 4, 0, 1, 1)

        self.pushButton = QPushButton(w_MainWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setFlat(False)

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        self.pushButton_7 = QPushButton(w_MainWindow)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)

        self.gridLayout.addWidget(self.pushButton_7, 7, 1, 1, 1)

        self.pb_DetectFacialLandmarks = QPushButton(w_MainWindow)
        self.pb_DetectFacialLandmarks.setObjectName(u"pb_DetectFacialLandmarks")

        self.gridLayout.addWidget(self.pb_DetectFacialLandmarks, 5, 0, 1, 2)

        self.pushButton_8 = QPushButton(w_MainWindow)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)

        self.gridLayout.addWidget(self.pushButton_8, 7, 0, 1, 1)

        self.pushButton_5 = QPushButton(w_MainWindow)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.gridLayout.addWidget(self.pushButton_5, 6, 1, 1, 1)

        self.pb_ChooseImage = QPushButton(w_MainWindow)
        self.pb_ChooseImage.setObjectName(u"pb_ChooseImage")

        self.gridLayout.addWidget(self.pb_ChooseImage, 0, 0, 1, 2)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)

        self.pb_RotateRight = QPushButton(w_MainWindow)
        self.pb_RotateRight.setObjectName(u"pb_RotateRight")
        self.pb_RotateRight.setFont(font)

        self.gridLayout_2.addWidget(self.pb_RotateRight, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.graphicsView = QGraphicsView(w_MainWindow)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_2.addWidget(self.graphicsView, 1, 1, 3, 4)

        self.lb_Message = QLabel(w_MainWindow)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout_2.addWidget(self.lb_Message, 3, 0, 1, 1)

        self.pb_RotateLeft = QPushButton(w_MainWindow)
        self.pb_RotateLeft.setObjectName(u"pb_RotateLeft")
        self.pb_RotateLeft.setFont(font)

        self.gridLayout_2.addWidget(self.pb_RotateLeft, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.retranslateUi(w_MainWindow)

        QMetaObject.connectSlotsByName(w_MainWindow)

    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Wspomaganie Diagnostyki FAS", None))
        self.pb_measure.setText(QCoreApplication.translate("w_MainWindow", u"Dokonaj pomiar\u00f3w", None))
        self.pushButton_6.setText(QCoreApplication.translate("w_MainWindow", u"Zaznacz lewe oko", None))
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("w_MainWindow", u"Rozmiar referencji w mm", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 lewego oka", None))
        self.label_2.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 prawego oka", None))
        self.label_4.setText(QCoreApplication.translate("w_MainWindow", u"Wysoko\u015b\u0107 g\u00f3rnej wargii", None))
        self.pb_DetectReference.setText(QCoreApplication.translate("w_MainWindow", u"Wykryj referencj\u0119", None))
        self.pushButton.setText(QCoreApplication.translate("w_MainWindow", u"Zaznacz referencj\u0119", None))
        self.pushButton_7.setText(QCoreApplication.translate("w_MainWindow", u"Wyb\u00f3r rynienki podnosowej", None))
        self.pb_DetectFacialLandmarks.setText(
            QCoreApplication.translate("w_MainWindow", u"Wykryj elementy twarzy", None))
        self.pushButton_8.setText(
            QCoreApplication.translate("w_MainWindow", u"Zaznacz g\u00f3rn\u0105 warg\u0119", None))
        self.pushButton_5.setText(QCoreApplication.translate("w_MainWindow", u"Zaznacz prawe oko", None))
        self.pb_ChooseImage.setText(QCoreApplication.translate("w_MainWindow", u"Wyb\u00f3r zdj\u0119cia", None))
        self.pb_RotateRight.setText(QCoreApplication.translate("w_MainWindow", u"Obr\u00f3t w prawo", None))
        self.lb_Message.setText(QCoreApplication.translate("w_MainWindow", u"Komunikaty", None))
        self.pb_RotateLeft.setText(QCoreApplication.translate("w_MainWindow", u"Obr\u00f3t w lewo", None))
    # retranslateUi
