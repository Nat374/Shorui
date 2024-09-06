from PyQt6 import QtCore

def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Shorui"))
    self.document_list.headerItem().setText(0, _translate("MainWindow", "Documents"))
    __sortingEnabled = self.document_list.isSortingEnabled()
    self.document_list.setSortingEnabled(False)
    self.name_document.setPlaceholderText(_translate("MainWindow", "Name your document"))
    self.label.setText(_translate("MainWindow", "Recently opened document(s)"))
    self.label_2.setText(_translate("MainWindow", "All documents"))
    self.open_folder.setText(_translate("MainWidnow", "Open folder"))
    #main_window.setWindowTitle(_translate("main_window", "main_window"))

lang = {
    "create_folder": "Type the name of the new folder/category", 
    "text_field_empty": "The name is empty", 
    "error_already_exist": "This file already exist",
    "errror_select_folder": "Please select a folder in the documents list"
    }

def retranslateUi_settings(self, main_window):
    _translate = QtCore.QCoreApplication.translate
    self.main_window.setWindowTitle("Settings")
    self.title_doc.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">New Document</span></p></body></html>"))
    self.empty_doc.setText(_translate("main_window", "Empty Document"))
    self.template_doc.setText(_translate("main_window", "Use a template (template.odt)"))
    self.title_folder.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">Document(s) Folder</span></p></body></html>"))
    self.folder_selector.setText(_translate("main_window", "Change Folder"))
    from main import settings
    from os import getcwd
    self.current_folder.setText(_translate("main_window", "Current folder for all documents: " + settings["root"]))
    self.title_doc_name.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">Document Name</span></p></body></html>"))
    self.include_date.setText(_translate("main_window", "Include date"))
    self.title_ui.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">Interface</span></p></body></html>"))
    self.credit.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:13pt;\"><b>EasyDoc 1.0 - Made by Nathan Gronier</span></p></body></html>"))
    self.theme_label.setText(_translate("main_window", "Theme"))
    self.language_title.setText(_translate("main_window", "Language"))
    self.language_ComboBox.setItemText(0, _translate("main_window", "English"))
    self.language_ComboBox.setItemText(1, _translate("main_window", "Français"))
        
