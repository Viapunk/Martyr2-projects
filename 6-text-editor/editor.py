# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        
        Form.setSizePolicy(sizePolicy)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.Button_open = QtGui.QPushButton(Form)
        self.Button_open.setObjectName(_fromUtf8("Button_open"))
        self.horizontalLayout.addWidget(self.Button_open)
        
        self.Button_save = QtGui.QPushButton(Form)
        self.Button_save.setObjectName(_fromUtf8("Button_save"))
        
        self.horizontalLayout.addWidget(self.Button_save)
        
        self.Button_quit = QtGui.QPushButton(Form)
        self.Button_quit.setObjectName(_fromUtf8("Button_quit"))
        
        self.horizontalLayout.addWidget(self.Button_quit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.Editor = QtGui.QPlainTextEdit(Form)
        self.Editor.setObjectName(_fromUtf8("Editor"))
        
        self.verticalLayout.addWidget(self.Editor)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Button_open.clicked.connect(self.OpenTextFile)
        self.Button_quit.clicked.connect(self.Close_Application)
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Button_open.setText(_translate("Form", "Open", None))
        self.Button_save.setText(_translate("Form", "Save", None))
        self.Button_quit.setText(_translate("Form", "Quit", None))


    def OpenTextFile(self):
        dialog = QtGui.QFileDialog()
        dialog.setWindowTitle("Choose a file to open")
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        dialog.setNameFilter("Text (*.txt);; All files (*.*)")
        dialog.setViewMode(QtGui.QFileDialog.Detail)
        filename = QtCore.QStringList()
        if(dialog.exec_()):
            filename = dialog.selectedFiles()
        plain_text = open(filename[0]).read()
        self.Editor.setPlainText(plain_text)
        
    
    def Close_Application(self):
        choice = QtGui.QMessageBox.question(Form ,'Quit application','Do you want to quit?', QtGui.QMessageBox.Yes
                | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            QtGui.QApplication.quit()
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
