# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(783, 489)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.central_stackedWidget = QtGui.QStackedWidget(Dialog)
        self.central_stackedWidget.setObjectName("central_stackedWidget")
        self.submit_page = QtGui.QWidget()
        self.submit_page.setObjectName("submit_page")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.submit_page)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.items_title_label = QtGui.QLabel(self.submit_page)
        self.items_title_label.setStyleSheet("#items_title_label {\n"
"font-size: 14px\n"
"}")
        self.items_title_label.setIndent(4)
        self.items_title_label.setObjectName("items_title_label")
        self.verticalLayout_7.addWidget(self.items_title_label)
        self.renders_stacked_widget = QtGui.QStackedWidget(self.submit_page)
        self.renders_stacked_widget.setStyleSheet("")
        self.renders_stacked_widget.setObjectName("renders_stacked_widget")
        self.renders_page = QtGui.QWidget()
        self.renders_page.setObjectName("renders_page")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.renders_page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.task_scroll = QtGui.QScrollArea(self.renders_page)
        self.task_scroll.setStyleSheet("#task_scroll {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.task_scroll.setWidgetResizable(True)
        self.task_scroll.setObjectName("task_scroll")
        self.contents = QtGui.QWidget()
        self.contents.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.contents.setObjectName("contents")
        self.task_scroll.setWidget(self.contents)
        self.horizontalLayout_7.addWidget(self.task_scroll)
        self.renders_stacked_widget.addWidget(self.renders_page)
        self.no_renders_page = QtGui.QWidget()
        self.no_renders_page.setStyleSheet("")
        self.no_renders_page.setObjectName("no_renders_page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.no_renders_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.no_renders_frame = QtGui.QFrame(self.no_renders_page)
        self.no_renders_frame.setStyleSheet("#no_publishes_frame {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.no_renders_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.no_renders_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.no_renders_frame.setObjectName("no_renders_frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.no_renders_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtGui.QSpacerItem(0, 88, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.label_6 = QtGui.QLabel(self.no_renders_frame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtGui.QSpacerItem(0, 88, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.no_renders_frame)
        self.renders_stacked_widget.addWidget(self.no_renders_page)
        self.verticalLayout_7.addWidget(self.renders_stacked_widget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_title_label = QtGui.QLabel(self.submit_page)
        self.info_title_label.setStyleSheet("#info_title_label {\n"
"font-size: 14px\n"
"}")
        self.info_title_label.setIndent(4)
        self.info_title_label.setObjectName("info_title_label")
        self.verticalLayout.addWidget(self.info_title_label)
        self.groupBox = QtGui.QGroupBox(self.submit_page)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.cancel_btn = QtGui.QPushButton(self.submit_page)
        self.cancel_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.submit_btn = QtGui.QPushButton(self.submit_page)
        self.submit_btn.setObjectName("submit_btn")
        self.horizontalLayout.addWidget(self.submit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.central_stackedWidget.addWidget(self.submit_page)
        self.progress_page = QtGui.QWidget()
        self.progress_page.setObjectName("progress_page")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.progress_page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem7 = QtGui.QSpacerItem(20, 97, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.title = QtGui.QLabel(self.progress_page)
        self.title.setStyleSheet("#title {\n"
"font-size: 24px;\n"
"}")
        self.title.setObjectName("title")
        self.verticalLayout_9.addWidget(self.title)
        self.progress_details = QtGui.QLabel(self.progress_page)
        self.progress_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progress_details.setWordWrap(False)
        self.progress_details.setObjectName("progress_details")
        self.verticalLayout_9.addWidget(self.progress_details)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(3, 3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.central_stackedWidget.addWidget(self.progress_page)
        self.success_page = QtGui.QWidget()
        self.success_page.setObjectName("success_page")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.success_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem10 = QtGui.QSpacerItem(20, 134, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.status_icon = QtGui.QLabel(self.success_page)
        self.status_icon.setMinimumSize(QtCore.QSize(80, 80))
        self.status_icon.setMaximumSize(QtCore.QSize(80, 80))
        self.status_icon.setBaseSize(QtCore.QSize(32, 32))
        self.status_icon.setText("")
        self.status_icon.setPixmap(QtGui.QPixmap(":/res/success.png"))
        self.status_icon.setScaledContents(False)
        self.status_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.status_icon.setObjectName("status_icon")
        self.verticalLayout_5.addWidget(self.status_icon)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.success_status_title = QtGui.QLabel(self.success_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.success_status_title.setFont(font)
        self.success_status_title.setStyleSheet("")
        self.success_status_title.setObjectName("success_status_title")
        self.verticalLayout_6.addWidget(self.success_status_title)
        self.success_details = QtGui.QLabel(self.success_page)
        self.success_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.success_details.setWordWrap(True)
        self.success_details.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.success_details.setObjectName("success_details")
        self.verticalLayout_6.addWidget(self.success_details)
        self.verticalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.horizontalLayout_6.setStretch(2, 3)
        self.horizontalLayout_6.setStretch(3, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        spacerItem14 = QtGui.QSpacerItem(20, 134, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem14)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.success_close_btn = QtGui.QPushButton(self.success_page)
        self.success_close_btn.setObjectName("success_close_btn")
        self.horizontalLayout_5.addWidget(self.success_close_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.central_stackedWidget.addWidget(self.success_page)
        self.failure_page = QtGui.QWidget()
        self.failure_page.setObjectName("failure_page")
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.failure_page)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        spacerItem16 = QtGui.QSpacerItem(20, 134, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(spacerItem16)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem17)
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.status_icon_3 = QtGui.QLabel(self.failure_page)
        self.status_icon_3.setMinimumSize(QtCore.QSize(80, 80))
        self.status_icon_3.setMaximumSize(QtCore.QSize(80, 80))
        self.status_icon_3.setBaseSize(QtCore.QSize(32, 32))
        self.status_icon_3.setText("")
        self.status_icon_3.setPixmap(QtGui.QPixmap(":/res/failure.png"))
        self.status_icon_3.setScaledContents(False)
        self.status_icon_3.setAlignment(QtCore.Qt.AlignCenter)
        self.status_icon_3.setObjectName("status_icon_3")
        self.verticalLayout_17.addWidget(self.status_icon_3)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem18)
        self.horizontalLayout_15.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.failure_status_title = QtGui.QLabel(self.failure_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.failure_status_title.setFont(font)
        self.failure_status_title.setStyleSheet("")
        self.failure_status_title.setObjectName("failure_status_title")
        self.verticalLayout_18.addWidget(self.failure_status_title)
        self.failure_details = QtGui.QLabel(self.failure_page)
        self.failure_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.failure_details.setWordWrap(True)
        self.failure_details.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.failure_details.setObjectName("failure_details")
        self.verticalLayout_18.addWidget(self.failure_details)
        self.verticalLayout_18.setStretch(1, 1)
        self.horizontalLayout_15.addLayout(self.verticalLayout_18)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.horizontalLayout_15.setStretch(2, 3)
        self.horizontalLayout_15.setStretch(3, 1)
        self.verticalLayout_19.addLayout(self.horizontalLayout_15)
        spacerItem20 = QtGui.QSpacerItem(20, 134, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(spacerItem20)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem21)
        self.failure_close_btn = QtGui.QPushButton(self.failure_page)
        self.failure_close_btn.setObjectName("failure_close_btn")
        self.horizontalLayout_14.addWidget(self.failure_close_btn)
        self.verticalLayout_19.addLayout(self.horizontalLayout_14)
        self.central_stackedWidget.addWidget(self.failure_page)
        self.horizontalLayout_2.addWidget(self.central_stackedWidget)

        self.retranslateUi(Dialog)
        self.central_stackedWidget.setCurrentIndex(0)
        self.renders_stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Tank Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.items_title_label.setText(QtGui.QApplication.translate("Dialog", "Choose Items to Submit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic;\">This render does not have any optional items to choose from.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.info_title_label.setText(QtGui.QApplication.translate("Dialog", "Job Attributes:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.submit_btn.setText(QtGui.QApplication.translate("Dialog", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("Dialog", "Submitting...", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_details.setText(QtGui.QApplication.translate("Dialog", "Please wait while submitting to the render farm.", None, QtGui.QApplication.UnicodeUTF8))
        self.success_status_title.setText(QtGui.QApplication.translate("Dialog", "Success!", None, QtGui.QApplication.UnicodeUTF8))
        self.success_details.setText(QtGui.QApplication.translate("Dialog", "Submission was successfully sent to the render farm.", None, QtGui.QApplication.UnicodeUTF8))
        self.success_close_btn.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.failure_status_title.setText(QtGui.QApplication.translate("Dialog", "Failure!", None, QtGui.QApplication.UnicodeUTF8))
        self.failure_details.setText(QtGui.QApplication.translate("Dialog", "Details...", None, QtGui.QApplication.UnicodeUTF8))
        self.failure_close_btn.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
