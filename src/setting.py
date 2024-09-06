from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QInputDialog, QFileDialog, QWidget, QMainWindow
from PyQt6.QtCore import QSize
from functools import partial

class Ui_Settings(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.main_window.setWindowTitle("Settings")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 695, 435))
        self.title_doc = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_doc.setGeometry(QtCore.QRect(20, 20, 601, 21))
        self.empty_doc = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.empty_doc.setGeometry(QtCore.QRect(20, 50, 121, 20))
        self.template_doc = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.template_doc.setGeometry(QtCore.QRect(150, 50, 181, 20))
        self.title_folder = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_folder.setGeometry(QtCore.QRect(20, 90, 601, 21))
        self.folder_selector = QtWidgets.QPushButton(parent=self.centralwidget)
        self.folder_selector.setGeometry(QtCore.QRect(20, 120, 121, 24))
        self.current_folder = QtWidgets.QLabel(parent=self.centralwidget)
        self.current_folder.setGeometry(QtCore.QRect(20, 150, 1000, 16))
        self.title_doc_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_doc_name.setGeometry(QtCore.QRect(20, 190, 601, 21))
        self.credit = QtWidgets.QLabel(parent=self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(20, 395, 601, 25))
        self.include_date = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.include_date.setGeometry(QtCore.QRect(20, 220, 121, 20))
        self.title_ui = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_ui.setGeometry(QtCore.QRect(20, 260, 601, 21))
        self.theme_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.theme_comboBox.setGeometry(QtCore.QRect(20, 310, 121, 22))
        self.theme_comboBox.addItem("Fusion")
        self.theme_comboBox.addItem("Windows")
        self.theme_comboBox.addItem("Windowsvista")
        self.theme_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.theme_label.setGeometry(QtCore.QRect(20, 290, 51, 16))
        self.theme_label.setObjectName("theme_label")
        self.language_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.language_title.setGeometry(QtCore.QRect(20, 340, 81, 16))
        self.language_ComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.language_ComboBox.setGeometry(QtCore.QRect(20, 360, 121, 22))
        self.language_ComboBox.addItem("")
        self.language_ComboBox.addItem("")
        QtCore.QMetaObject.connectSlotsByName(main_window)
        from fr import retranslateUi_settings
        retranslateUi_settings(self, main_window)
        
        from main import settings

        self.theme_comboBox.setCurrentText(settings["theme"])

        if settings["doc_base"] == "empty":
            self.empty_doc.setChecked(True)
        else:
            self.template_doc.setChecked(True)
        
        if settings["has_date_in_name"] == True:
            self.include_date.setChecked(True)

        from main import change_settings

        self.theme_comboBox.currentIndexChanged.connect(
            lambda: change_settings("theme", self.theme_comboBox.currentText())
        )
        
        self.language_ComboBox.currentIndexChanged.connect(
            lambda: change_settings("current_lang", self.language_ComboBox.currentText())
        )

        self.empty_doc.clicked.connect(
            lambda: change_settings("doc_base", "empty")
        )
        
        self.template_doc.clicked.connect(self.useTemplate)
        
        self.include_date.clicked.connect(
            lambda: change_settings("has_date_in_name", self.include_date.isChecked())
        )

        self.folder_selector.clicked.connect(self.changeFolder)

    def changeFolder(self):
        from tkinter import filedialog
        file_path = filedialog.askdirectory()

        from main import change_settings
        change_settings('root', file_path.replace("/", "\\"))

        QMessageBox.warning(None, "Warning", "Please restart the software to apply changes")

    def useTemplate(self):
        from main import change_settings
        change_settings('doc_base', "template")
        
        QMessageBox.warning(None, "Warning", "New document file now be a copy of template.odt, Use this file as a master template")

        from os.path import isfile
        if isfile("template.odt") == False:
            f = open("template.odt", "a")
            f.close()
            print("MADE FILE")
            