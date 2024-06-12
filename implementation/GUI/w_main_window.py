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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDateEdit, QFormLayout,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)
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
        self.lb_Message = QLabel(w_MainWindow)
        self.lb_Message.setObjectName(u"lb_Message")
        self.lb_Message.setWordWrap(False)

        self.gridLayout_2.addWidget(self.lb_Message, 18, 0, 1, 1)

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
        self.pb_RotateLeft = QPushButton(self.Pomiary)
        self.pb_RotateLeft.setObjectName(u"pb_RotateLeft")
        font = QFont()
        font.setStrikeOut(False)
        self.pb_RotateLeft.setFont(font)

        self.gridLayout.addWidget(self.pb_RotateLeft, 0, 1, 1, 1)

        self.pb_RotateRight = QPushButton(self.Pomiary)
        self.pb_RotateRight.setObjectName(u"pb_RotateRight")
        self.pb_RotateRight.setFont(font)

        self.gridLayout.addWidget(self.pb_RotateRight, 0, 2, 1, 3)

        self.groupBox_4 = QGroupBox(self.Pomiary)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.rb2 = QRadioButton(self.groupBox_4)
        self.rb2.setObjectName(u"rb2")

        self.gridLayout_3.addWidget(self.rb2, 4, 2, 1, 1)

        self.rb4 = QRadioButton(self.groupBox_4)
        self.rb4.setObjectName(u"rb4")

        self.gridLayout_3.addWidget(self.rb4, 2, 2, 1, 2)

        self.rb5 = QRadioButton(self.groupBox_4)
        self.rb5.setObjectName(u"rb5")

        self.gridLayout_3.addWidget(self.rb5, 1, 2, 1, 1)

        self.rb3 = QRadioButton(self.groupBox_4)
        self.rb3.setObjectName(u"rb3")

        self.gridLayout_3.addWidget(self.rb3, 3, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(200, 400))
        self.label_5.setPixmap(QPixmap(u":/icon/phltrums fasdpn.org .jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 5, 1)

        self.rb1 = QRadioButton(self.groupBox_4)
        self.rb1.setObjectName(u"rb1")

        self.gridLayout_3.addWidget(self.rb1, 5, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 20, 0, 1, 5)

        self.groupBox_2 = QGroupBox(self.Pomiary)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.le_referenceMM = QLineEdit(self.groupBox_2)
        self.le_referenceMM.setObjectName(u"le_referenceMM")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_referenceMM)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 5)

        self.pb_DetectReference = QPushButton(self.Pomiary)
        self.pb_DetectReference.setObjectName(u"pb_DetectReference")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_DetectReference.sizePolicy().hasHeightForWidth())
        self.pb_DetectReference.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pb_DetectReference, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 22, 0, 1, 5)

        self.pb_measure = QPushButton(self.Pomiary)
        self.pb_measure.setObjectName(u"pb_measure")
        sizePolicy2.setHeightForWidth(self.pb_measure.sizePolicy().hasHeightForWidth())
        self.pb_measure.setSizePolicy(sizePolicy2)
        self.pb_measure.setMinimumSize(QSize(145, 0))

        self.gridLayout.addWidget(self.pb_measure, 4, 2, 1, 3)

        self.pb_DetectFacialLandmarks = QPushButton(self.Pomiary)
        self.pb_DetectFacialLandmarks.setObjectName(u"pb_DetectFacialLandmarks")
        sizePolicy2.setHeightForWidth(self.pb_DetectFacialLandmarks.sizePolicy().hasHeightForWidth())
        self.pb_DetectFacialLandmarks.setSizePolicy(sizePolicy2)
        self.pb_DetectFacialLandmarks.setMinimumSize(QSize(160, 0))

        self.gridLayout.addWidget(self.pb_DetectFacialLandmarks, 4, 1, 1, 1)

        self.pb_ChooseImage = QPushButton(self.Pomiary)
        self.pb_ChooseImage.setObjectName(u"pb_ChooseImage")

        self.gridLayout.addWidget(self.pb_ChooseImage, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.Pomiary)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMinimumSize(QSize(400, 0))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.le_LeftEyeMM = QLineEdit(self.groupBox)
        self.le_LeftEyeMM.setObjectName(u"le_LeftEyeMM")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_LeftEyeMM)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.le_RightEyeMM = QLineEdit(self.groupBox)
        self.le_RightEyeMM.setObjectName(u"le_RightEyeMM")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_RightEyeMM)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.le_UpperLipMM = QLineEdit(self.groupBox)
        self.le_UpperLipMM.setObjectName(u"le_UpperLipMM")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_UpperLipMM)


        self.gridLayout.addWidget(self.groupBox, 19, 0, 1, 5)

        self.pb_MeasurementRaport = QPushButton(self.Pomiary)
        self.pb_MeasurementRaport.setObjectName(u"pb_MeasurementRaport")

        self.gridLayout.addWidget(self.pb_MeasurementRaport, 21, 0, 1, 5)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.photoGraphicsView = QGraphicsView(self.Pomiary)
        self.photoGraphicsView.setObjectName(u"photoGraphicsView")
        self.photoGraphicsView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout.addWidget(self.photoGraphicsView)

        self.tabWidget.addTab(self.Pomiary, "")
        self.Siatki_centylowe = QWidget()
        self.Siatki_centylowe.setObjectName(u"Siatki_centylowe")
        self.horizontalLayout_7 = QHBoxLayout(self.Siatki_centylowe)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_8 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.groupBox_8.setMinimumSize(QSize(0, 0))
        self.groupBox_8.setMaximumSize(QSize(400, 16777215))
        self.formLayout_3 = QFormLayout(self.groupBox_8)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_11 = QLabel(self.groupBox_8)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.de_birth = QDateEdit(self.groupBox_8)
        self.de_birth.setObjectName(u"de_birth")
        self.de_birth.setMinimumDateTime(QDateTime(QDate(1900, 9, 13), QTime(23, 0, 0)))
        self.de_birth.setCalendarPopup(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.de_birth)

        self.label_16 = QLabel(self.groupBox_8)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.de_measurement = QDateEdit(self.groupBox_8)
        self.de_measurement.setObjectName(u"de_measurement")
        self.de_measurement.setMinimumDate(QDate(1900, 9, 14))
        self.de_measurement.setCalendarPopup(True)
        self.de_measurement.setDate(QDate(2024, 1, 1))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.de_measurement)


        self.verticalLayout_5.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.HeadCircumferenceCMChart = QLineEdit(self.groupBox_5)
        self.HeadCircumferenceCMChart.setObjectName(u"HeadCircumferenceCMChart")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.HeadCircumferenceCMChart.sizePolicy().hasHeightForWidth())
        self.HeadCircumferenceCMChart.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.HeadCircumferenceCMChart, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_HeadCircumferenceWHO = QPushButton(self.groupBox_5)
        self.pb_HeadCircumferenceWHO.setObjectName(u"pb_HeadCircumferenceWHO")

        self.horizontalLayout_3.addWidget(self.pb_HeadCircumferenceWHO)

        self.pb_chart4 = QPushButton(self.groupBox_5)
        self.pb_chart4.setObjectName(u"pb_chart4")

        self.horizontalLayout_3.addWidget(self.pb_chart4)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.le_Height = QLineEdit(self.groupBox_6)
        self.le_Height.setObjectName(u"le_Height")
        sizePolicy4.setHeightForWidth(self.le_Height.sizePolicy().hasHeightForWidth())
        self.le_Height.setSizePolicy(sizePolicy4)

        self.gridLayout_9.addWidget(self.le_Height, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pb_HeightWHO = QPushButton(self.groupBox_6)
        self.pb_HeightWHO.setObjectName(u"pb_HeightWHO")

        self.horizontalLayout_5.addWidget(self.pb_HeightWHO)

        self.pb_chart6 = QPushButton(self.groupBox_6)
        self.pb_chart6.setObjectName(u"pb_chart6")

        self.horizontalLayout_5.addWidget(self.pb_chart6)


        self.gridLayout_9.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout_9)


        self.verticalLayout_5.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.Siatki_centylowe)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_WeightWHO = QPushButton(self.groupBox_7)
        self.pb_WeightWHO.setObjectName(u"pb_WeightWHO")

        self.horizontalLayout_4.addWidget(self.pb_WeightWHO)

        self.pb_chart8 = QPushButton(self.groupBox_7)
        self.pb_chart8.setObjectName(u"pb_chart8")

        self.horizontalLayout_4.addWidget(self.pb_chart8)


        self.gridLayout_10.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)

        self.le_Weight = QLineEdit(self.groupBox_7)
        self.le_Weight.setObjectName(u"le_Weight")
        sizePolicy4.setHeightForWidth(self.le_Weight.sizePolicy().hasHeightForWidth())
        self.le_Weight.setSizePolicy(sizePolicy4)

        self.gridLayout_10.addWidget(self.le_Weight, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.pb_exportCharts = QPushButton(self.Siatki_centylowe)
        self.pb_exportCharts.setObjectName(u"pb_exportCharts")
        self.pb_exportCharts.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_5.addWidget(self.pb_exportCharts)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.the_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.the_spacer)

        self.tabWidget.addTab(self.Siatki_centylowe, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 6)

        QWidget.setTabOrder(self.pb_ChooseImage, self.pb_RotateLeft)
        QWidget.setTabOrder(self.pb_RotateLeft, self.pb_RotateRight)
        QWidget.setTabOrder(self.pb_RotateRight, self.le_referenceMM)
        QWidget.setTabOrder(self.le_referenceMM, self.pb_DetectReference)
        QWidget.setTabOrder(self.pb_DetectReference, self.pb_DetectFacialLandmarks)
        QWidget.setTabOrder(self.pb_DetectFacialLandmarks, self.pb_measure)
        QWidget.setTabOrder(self.pb_measure, self.le_LeftEyeMM)
        QWidget.setTabOrder(self.le_LeftEyeMM, self.le_RightEyeMM)
        QWidget.setTabOrder(self.le_RightEyeMM, self.le_UpperLipMM)
        QWidget.setTabOrder(self.le_UpperLipMM, self.rb5)
        QWidget.setTabOrder(self.rb5, self.rb4)
        QWidget.setTabOrder(self.rb4, self.rb3)
        QWidget.setTabOrder(self.rb3, self.rb2)
        QWidget.setTabOrder(self.rb2, self.rb1)
        QWidget.setTabOrder(self.rb1, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.HeadCircumferenceCMChart)
        QWidget.setTabOrder(self.HeadCircumferenceCMChart, self.pb_HeadCircumferenceWHO)
        QWidget.setTabOrder(self.pb_HeadCircumferenceWHO, self.pb_chart4)
        QWidget.setTabOrder(self.pb_chart4, self.le_Height)
        QWidget.setTabOrder(self.le_Height, self.pb_HeightWHO)
        QWidget.setTabOrder(self.pb_HeightWHO, self.pb_chart6)
        QWidget.setTabOrder(self.pb_chart6, self.le_Weight)
        QWidget.setTabOrder(self.le_Weight, self.pb_WeightWHO)
        QWidget.setTabOrder(self.pb_WeightWHO, self.pb_chart8)
        QWidget.setTabOrder(self.pb_chart8, self.photoGraphicsView)

        self.retranslateUi(w_MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Wspomaganie Diagnostyki FAS", None))
        self.lb_Message.setText(QCoreApplication.translate("w_MainWindow", u"Komunikaty", None))
        self.pb_RotateLeft.setText(QCoreApplication.translate("w_MainWindow", u"Obr\u00f3t w lewo", None))
        self.pb_RotateRight.setText(QCoreApplication.translate("w_MainWindow", u"Obr\u00f3t w prawo", None))
        self.groupBox_4.setTitle("")
        self.rb2.setText(QCoreApplication.translate("w_MainWindow", u"2", None))
        self.rb4.setText(QCoreApplication.translate("w_MainWindow", u"4", None))
        self.rb5.setText(QCoreApplication.translate("w_MainWindow", u"5", None))
        self.rb3.setText(QCoreApplication.translate("w_MainWindow", u"3", None))
        self.label_5.setText("")
        self.rb1.setText(QCoreApplication.translate("w_MainWindow", u"1", None))
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("w_MainWindow", u"Rozmiar referencji w mm:", None))
        self.pb_DetectReference.setText(QCoreApplication.translate("w_MainWindow", u"Wykryj referencj\u0119", None))
        self.pb_measure.setText(QCoreApplication.translate("w_MainWindow", u"Dokonaj pomiar\u00f3w", None))
        self.pb_DetectFacialLandmarks.setText(QCoreApplication.translate("w_MainWindow", u"Wykryj elementy twarzy", None))
        self.pb_ChooseImage.setText(QCoreApplication.translate("w_MainWindow", u"Wyb\u00f3r zdj\u0119cia", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 lewego oka [mm]:", None))
        self.label_2.setText(QCoreApplication.translate("w_MainWindow", u"Szeroko\u015b\u0107 prawego oka [mm]:", None))
        self.label_4.setText(QCoreApplication.translate("w_MainWindow", u"Wysoko\u015b\u0107 g\u00f3rnej wargi [mm]:", None))
        self.pb_MeasurementRaport.setText(QCoreApplication.translate("w_MainWindow", u"Generowanie raportu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pomiary), QCoreApplication.translate("w_MainWindow", u"Pomiary", None))
        self.groupBox_8.setTitle("")
        self.label_11.setText(QCoreApplication.translate("w_MainWindow", u"Data urodzenia:", None))
        self.label_16.setText(QCoreApplication.translate("w_MainWindow", u"Data pomiaru:", None))
        self.groupBox_5.setTitle("")
        self.label_8.setText(QCoreApplication.translate("w_MainWindow", u"Obw\u00f3d g\u0142owy [cm]", None))
        self.pb_HeadCircumferenceWHO.setText(QCoreApplication.translate("w_MainWindow", u"Siatka WHO do 24. miesi\u0105ca", None))
        self.pb_chart4.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 4", None))
        self.groupBox_6.setTitle("")
        self.label_9.setText(QCoreApplication.translate("w_MainWindow", u"Wzrost [cm]:", None))
        self.pb_HeightWHO.setText(QCoreApplication.translate("w_MainWindow", u"Siatka WHO do 24. miesi\u0105ca", None))
        self.pb_chart6.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 6", None))
        self.groupBox_7.setTitle("")
        self.pb_WeightWHO.setText(QCoreApplication.translate("w_MainWindow", u"Siatka WHO do 24. miesi\u0105ca", None))
        self.pb_chart8.setText(QCoreApplication.translate("w_MainWindow", u"Siatka 8", None))
        self.label_10.setText(QCoreApplication.translate("w_MainWindow", u"Waga [kg]:", None))
        self.pb_exportCharts.setText(QCoreApplication.translate("w_MainWindow", u"Generowanie raportu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Siatki_centylowe), QCoreApplication.translate("w_MainWindow", u"Siatki centylowe", None))
    # retranslateUi

