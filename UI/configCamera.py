# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self):
        self.qDialog = QtWidgets.QDialog()
        self.setupUi(self.qDialog)
        self.init()

    def init(self):
        self.qDialog.setFixedSize(self.qDialog.size())
        self.qDialog.setWindowTitle("相机配置界面") 
           
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(271, 519)
        self.label_exposeur_time = QtWidgets.QLabel(Dialog)
        self.label_exposeur_time.setGeometry(QtCore.QRect(10, 290, 141, 31))
        self.label_exposeur_time.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_exposeur_time.setObjectName("label_exposeur_time")
        self.lineEdit_exposeur_time = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_exposeur_time.setGeometry(QtCore.QRect(160, 290, 101, 31))
        self.lineEdit_exposeur_time.setObjectName("lineEdit_exposeur_time")
        self.label_gain = QtWidgets.QLabel(Dialog)
        self.label_gain.setGeometry(QtCore.QRect(10, 330, 141, 31))
        self.label_gain.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_gain.setObjectName("label_gain")
        self.lineEdit_gain = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_gain.setGeometry(QtCore.QRect(160, 330, 101, 31))
        self.lineEdit_gain.setObjectName("lineEdit_gain")
        self.label_frame_rate = QtWidgets.QLabel(Dialog)
        self.label_frame_rate.setGeometry(QtCore.QRect(10, 370, 141, 31))
        self.label_frame_rate.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_frame_rate.setObjectName("label_frame_rate")
        self.lineEdit_frame_rate = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_frame_rate.setGeometry(QtCore.QRect(160, 370, 101, 31))
        self.lineEdit_frame_rate.setObjectName("lineEdit_frame_rate")
        self.pushButton_set_parameter = QtWidgets.QPushButton(Dialog)
        self.pushButton_set_parameter.setGeometry(QtCore.QRect(140, 430, 111, 28))
        self.pushButton_set_parameter.setObjectName("pushButton_set_parameter")
        self.pushButton_open_device = QtWidgets.QPushButton(Dialog)
        self.pushButton_open_device.setGeometry(QtCore.QRect(10, 80, 121, 28))
        self.pushButton_open_device.setObjectName("pushButton_open_device")
        self.pushButton_close_device = QtWidgets.QPushButton(Dialog)
        self.pushButton_close_device.setGeometry(QtCore.QRect(150, 80, 111, 28))
        self.pushButton_close_device.setObjectName("pushButton_close_device")
        self.pushButton_start_grap = QtWidgets.QPushButton(Dialog)
        self.pushButton_start_grap.setGeometry(QtCore.QRect(10, 120, 121, 28))
        self.pushButton_start_grap.setObjectName("pushButton_start_grap")
        self.pushButton_stop_grap = QtWidgets.QPushButton(Dialog)
        self.pushButton_stop_grap.setGeometry(QtCore.QRect(150, 120, 111, 28))
        self.pushButton_stop_grap.setObjectName("pushButton_stop_grap")
        self.pushButton_save_jpg = QtWidgets.QPushButton(Dialog)
        self.pushButton_save_jpg.setGeometry(QtCore.QRect(150, 160, 111, 28))
        self.pushButton_save_jpg.setObjectName("pushButton_save_jpg")
        self.pushButton_save_bmp = QtWidgets.QPushButton(Dialog)
        self.pushButton_save_bmp.setGeometry(QtCore.QRect(10, 160, 121, 28))
        self.pushButton_save_bmp.setObjectName("pushButton_save_bmp")
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setGeometry(QtCore.QRect(60, 470, 121, 28))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_set_IPV4_IP = QtWidgets.QPushButton(Dialog)
        self.pushButton_set_IPV4_IP.setGeometry(QtCore.QRect(10, 40, 121, 28))
        self.pushButton_set_IPV4_IP.setObjectName("pushButton_set_IPV4_IP")
        self.pushButton_set_camera_IP = QtWidgets.QPushButton(Dialog)
        self.pushButton_set_camera_IP.setGeometry(QtCore.QRect(150, 40, 111, 28))
        self.pushButton_set_camera_IP.setObjectName("pushButton_set_camera_IP")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label.setObjectName("label")
        self.pushButton_open_video = QtWidgets.QPushButton(Dialog)
        self.pushButton_open_video.setGeometry(QtCore.QRect(10, 200, 121, 28))
        self.pushButton_open_video.setObjectName("pushButton_open_video")
        self.pushButton_start_infer = QtWidgets.QPushButton(Dialog)
        self.pushButton_start_infer.setGeometry(QtCore.QRect(10, 240, 121, 28))
        self.pushButton_start_infer.setObjectName("pushButton_start_infer")
        self.pushButton_stop_infer = QtWidgets.QPushButton(Dialog)
        self.pushButton_stop_infer.setGeometry(QtCore.QRect(150, 240, 111, 28))
        self.pushButton_stop_infer.setObjectName("pushButton_stop_infer")
        self.pushButton_load_model = QtWidgets.QPushButton(Dialog)
        self.pushButton_load_model.setGeometry(QtCore.QRect(150, 200, 111, 28))
        self.pushButton_load_model.setObjectName("pushButton_load_model")
        self.pushButton_get_parameter = QtWidgets.QPushButton(Dialog)
        self.pushButton_get_parameter.setGeometry(QtCore.QRect(10, 430, 111, 28))
        self.pushButton_get_parameter.setObjectName("pushButton_get_parameter")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_exposeur_time.setText(_translate("Dialog", "Exposure Time"))
        self.label_gain.setText(_translate("Dialog", "Gain"))
        self.label_frame_rate.setText(_translate("Dialog", "Frame Rate"))
        self.pushButton_set_parameter.setText(_translate("Dialog", "Set Parameter"))
        self.pushButton_open_device.setText(_translate("Dialog", "Open Device"))
        self.pushButton_close_device.setText(_translate("Dialog", "Close Device"))
        self.pushButton_start_grap.setText(_translate("Dialog", "Start Grapping"))
        self.pushButton_stop_grap.setText(_translate("Dialog", "Stop Grapping"))
        self.pushButton_save_jpg.setText(_translate("Dialog", "Save as JPG"))
        self.pushButton_save_bmp.setText(_translate("Dialog", "Save as BMP"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))
        self.pushButton_set_IPV4_IP.setText(_translate("Dialog", "Set IPV4 IP"))
        self.pushButton_set_camera_IP.setText(_translate("Dialog", "Set Camera IP"))
        self.label.setText(_translate("Dialog", "相机设置"))
        self.pushButton_open_video.setText(_translate("Dialog", "打开相机"))
        self.pushButton_start_infer.setText(_translate("Dialog", "开始预测"))
        self.pushButton_stop_infer.setText(_translate("Dialog", "停止预测"))
        self.pushButton_load_model.setText(_translate("Dialog", "选择模型"))
        self.pushButton_get_parameter.setText(_translate("Dialog", "Get Parameter"))
