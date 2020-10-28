from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_UpdateWindow(object):
    def setup_up(self, UpdateWindow):
        UpdateWindow.setObjectName("UpdateWindow")
        UpdateWindow.resize(395, 212)
        self.label = QtWidgets.QLabel(UpdateWindow)
        self.label.setGeometry(QtCore.QRect(80, 50, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(UpdateWindow)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UpdateWindow)
        self.label_3.setGeometry(QtCore.QRect(180, 80, 55, 16))
        self.label_3.setObjectName("label_3")
        self.updt_btn = QtWidgets.QPushButton(UpdateWindow)
        self.updt_btn.setGeometry(QtCore.QRect(80, 140, 141, 28))
        self.updt_btn.setObjectName("updt_btn")
        self.openGLWidget = QtWidgets.QOpenGLWidget(UpdateWindow)
        self.openGLWidget.setGeometry(QtCore.QRect(-600, 520, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")
        self.status = QtWidgets.QLabel(UpdateWindow)
        self.status.setGeometry(QtCore.QRect(80, 110, 151, 16))
        self.status.setText("")
        self.status.setObjectName("status")

        self.updt_btn.clicked.connect(self.update_load)

        self.retranslateUi(UpdateWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)

    def retranslateUi(self, UpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Form"))
        self.label.setText(_translate("UpdateWindow", "Update Password Generator"))
        self.label_2.setText(_translate("UpdateWindow", "Current Version:"))
        self.label_3.setText(_translate("UpdateWindow", "1.0"))
        self.updt_btn.setText(_translate("UpdateWindow", "Check for Updates"))

    def update_load(self):
        # Here will be the method for updating the application
        # From now we'll use the timer func.
        time.sleep(2.5)
        self.status.setText('No Update Available')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateWindow = QtWidgets.QWidget()
    ui = Ui_UpdateWindow()
    ui.setup_up(UpdateWindow)
    UpdateWindow.show()
    sys.exit(app.exec_())
