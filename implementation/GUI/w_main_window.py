# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w_main_window.ui'
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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
from resources import gui_resources_rc

class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(1192, 890)
        icon = QIcon()
        icon.addFile(u":/icon/Ikona.png", QSize(), QIcon.Normal, QIcon.Off)
        w_MainWindow.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(w_MainWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(w_MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.Pomiary = QWidget()
        self.Pomiary.setObjectName(u"Pomiary")
        self.horizontalLayout = QHBoxLayout(self.Pomiary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setHorizontalSpacing(-1)
        self.pb_DetectReference = QPushButton(self.Pomiary)
        self.pb_DetectReference.setObjectName(u"pb_DetectReference")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_DetectReference.sizePolicy().hasHeightForWidth())
        self.pb_DetectReference.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pb_DetectReference, 4, 0, 1, 1)

        self.pb_ChooseImage = QPushButton(self.Pomiary)
        self.pb_ChooseImage.setObjectName(u"pb_ChooseImage")

        self.gridLayout.addWidget(self.pb_ChooseImage, 0, 0, 1, 1)

        self.pb_RotateLeft = QPushButton(self.Pomiary)
        self.pb_RotateLeft.setObjectName(u"pb_RotateLeft")
        font = QFont()
        font.setStrikeOut(False)
        self.pb_RotateLeft.setFont(font)

        self.gridLayout.addWidget(self.pb_RotateLeft, 0, 1, 1, 1)

        self.pb_DetectFacialLandmarks = QPushButton(self.Pomiary)
        self.pb_DetectFacialLandmarks.setObjectName(u"pb_DetectFacialLandmarks")
        sizePolicy.setHeightForWidth(self.pb_DetectFacialLandmarks.sizePolicy().hasHeightForWidth())
        self.pb_DetectFacialLandmarks.setSizePolicy(sizePolicy)
        self.pb_DetectFacialLandmarks.setMinimumSize(QSize(160, 0))

        self.gridLayout.addWidget(self.pb_DetectFacialLandmarks, 4, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.Pomiary)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.le_referenceMM = QLineEdit(self.groupBox_2)
        self.le_referenceMM.setObjectName(u"le_referenceMM")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_referenceMM)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 5)

        self.pb_RotateRight = QPushButton(self.Pomiary)
        self.pb_RotateRight.setObjectName(u"pb_RotateRight")
        self.pb_RotateRight.setFont(font)

        self.gridLayout.addWidget(self.pb_RotateRight, 0, 2, 1, 3)

        self.pb_measure = QPushButton(self.Pomiary)
        self.pb_measure.setObjectName(u"pb_measure")
        sizePolicy.setHeightForWidth(self.pb_measure.sizePolicy().hasHeightForWidth())
        self.pb_measure.setSizePolicy(sizePolicy)
        self.pb_measure.setMinimumSize(QSize(145, 0))

        self.gridLayout.addWidget(self.pb_measure, 4, 2, 1, 3)

        self.groupBox = QGroupBox(self.Pomiary)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(400, 0))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.le_LeftEyeMM = QLineEdit(self.groupBox)
        self.le_LeftEyeMM.setObjectName(u"le_LeftEyeMM")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_LeftEyeMM)

        self.le_RightEyeMM = QLineEdit(self.groupBox)
        self.le_RightEyeMM.setObjectName(u"le_RightEyeMM")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_RightEyeMM)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.le_UpperLipMM = QLineEdit(self.groupBox)
        self.le_UpperLipMM.setObjectName(u"le_UpperLipMM")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_UpperLipMM)


        self.gridLayout.addWidget(self.groupBox, 18, 0, 1, 5)

        self.groupBox_4 = QGroupBox(self.Pomiary)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_5 = QRadioButton(self.groupBox_4)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_3.addWidget(self.radioButton_5, 3, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(200, 400))
        self.label_5.setPixmap(QPixmap(u":/icon/phltrums fasdpn.org .jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 5, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_3.addWidget(self.radioButton_4, 4, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox_4)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 1, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox_4)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_3.addWidget(self.radioButton_3, 2, 2, 1, 2)

        self.radioButton = QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 5, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 19, 0, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.graphicsView = QGraphicsView(self.Pomiary)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout.addWidget(self.graphicsView)

        self.tabWidget.addTab(self.Pomiary, "")
        self.Siatki_centylowe = QWidget()
        self.Siatki_centylowe.setObjectName(u"Siatki_centylowe")
        self.gridLayout_5 = QGridLayout(self.Siatki_centylowe)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_9 = QPushButton(self.Siatki_centylowe)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_5.addWidget(self.pushButton_9, 5, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lineEdit_5 = QLineEdit(self.groupBox_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy4)

        self.gridLayout_10.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_7 = QPushButton(self.groupBox_7)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox_7)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_4.addWidget(self.pushButton_8)


        self.gridLayout_10.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_7, 3, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy4.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy4)

        self.gridLayout_9.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_5 = QPushButton(self.groupBox_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.groupBox_6)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.gridLayout_9.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout_9)


        self.gridLayout_5.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.graphicsView_2 = QGraphicsView(self.Siatki_centylowe)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout_5.addWidget(self.graphicsView_2, 0, 1, 6, 1)

        self.groupBox_5 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.le_UpperLipMMChart = QLineEdit(self.groupBox_5)
        self.le_UpperLipMMChart.setObjectName(u"le_UpperLipMMChart")
        sizePolicy4.setHeightForWidth(self.le_UpperLipMMChart.sizePolicy().hasHeightForWidth())
        self.le_UpperLipMMChart.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.le_UpperLipMMChart, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_5)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.le_RightEyeMMChart = QLineEdit(self.groupBox_3)
        self.le_RightEyeMMChart.setObjectName(u"le_RightEyeMMChart")
        sizePolicy4.setHeightForWidth(self.le_RightEyeMMChart.sizePolicy().hasHeightForWidth())
        self.le_RightEyeMMChart.setSizePolicy(sizePolicy4)

        self.gridLayout_6.addWidget(self.le_RightEyeMMChart, 1, 2, 1, 1)

        self.le_LeftEyeMMChart = QLineEdit(self.groupBox_3)
        self.le_LeftEyeMMChart.setObjectName(u"le_LeftEyeMMChart")
        sizePolicy4.setHeightForWidth(self.le_LeftEyeMMChart.sizePolicy().hasHeightForWidth())
        self.le_LeftEyeMMChart.setSizePolicy(sizePolicy4)

        self.gridLayout_6.addWidget(self.le_LeftEyeMMChart, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_6.addLayout(self.horizontalLayout_2, 3, 0, 1, 3)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.tabWidget.addTab(self.Siatki_centylowe, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 6)

        self.lb_Message = QLabel(w_MainWindow)
        self.lb_Message.setObjectName(u"lb_Message")
        self.lb_Message.setWordWrap(False)

        self.gridLayout_2.addWidget(self.lb_Message, 18, 0, 1, 1)


        self.retranslateUi(w_MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Wspomaganie Diagnostyki FAS", None))
        self.pb_DetectReference.setText(QCoreApplication.translate("w_MainWindow", u"Wykryj referencj\u0119", None))
        self.pb_ChooseImage.setText(QCoreApplication.translate("w_MainWindow", u"Wyb\u00f3r zdj\u0119cia", None))
        self.pb_RotateLeft.setText(QCoreApplication.translate("w_MainWindow", u"Obr\u00f3t w lewo", None))
        self.pb_DetectFacialLandmarks.setText(QCoreApplication.translate("w_MainWindow", u"Wykryj elementy twarzy", None))
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("w_MainWindow", u"Rozmiar referencji w mm", None))
        self.pb_RotateRight.setText(QCoreApplication.translate("w_MainWindow", u"Obr\u00f3t w prawo", None))
        self.pb_measure.setText(QCoreApplication.translate("w_MainWindow", u"Dokonaj pomiar\u00f3w", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_MainWindow", u"Pomiary", None))
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 lewego oka [mm]", None))
        self.label_2.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 prawego oka [mm]", None))
        self.label_4.setText(QCoreApplication.translate("w_MainWindow", u"Wysoko\u015b\u0107 g\u00f3rnej wargi [mm]", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("w_MainWindow", u"Wyb\u00f3r rynienki podnosowej", None))
        self.radioButton_5.setText(QCoreApplication.translate("w_MainWindow", u"3", None))
        self.label_5.setText("")
        self.radioButton_4.setText(QCoreApplication.translate("w_MainWindow", u"2", None))
        self.radioButton_2.setText(QCoreApplication.translate("w_MainWindow", u"5", None))
        self.radioButton_3.setText(QCoreApplication.translate("w_MainWindow", u"4", None))
        self.radioButton.setText(QCoreApplication.translate("w_MainWindow", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pomiary), QCoreApplication.translate("w_MainWindow", u"Pomiary", None))
        self.pushButton_9.setText(QCoreApplication.translate("w_MainWindow", u"Eksport siatek", None))
        self.groupBox_7.setTitle("")
        self.label_10.setText(QCoreApplication.translate("w_MainWindow", u"Waga [kg]", None))
        self.pushButton_7.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 7", None))
        self.pushButton_8.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 8", None))
        self.groupBox_6.setTitle("")
        self.label_9.setText(QCoreApplication.translate("w_MainWindow", u"Wzrost [cm]", None))
        self.pushButton_5.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 5", None))
        self.pushButton_6.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 6", None))
        self.groupBox_5.setTitle("")
        self.label_8.setText(QCoreApplication.translate("w_MainWindow", u"Wysoko\u015b\u0107 g\u00f3rnej wargi [mm]", None))
        self.pushButton_3.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 3", None))
        self.pushButton_4.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 4", None))
        self.groupBox_3.setTitle("")
        self.label_6.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 lewego oka [mm]", None))
        self.label_7.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 prawego oka [mm]", None))
        self.pushButton.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Siatki_centylowe), QCoreApplication.translate("w_MainWindow", u"Siatki centylowe", None))
        self.lb_Message.setText(QCoreApplication.translate("w_MainWindow", u"Komunikaty", None))
    # retranslateUi

