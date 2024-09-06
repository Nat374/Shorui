from PyQt6 import QtCore

def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "EasyDoc Manager [BUILD NON-PUBLIC (PROTOTYPE)]"))
    self.document_list.headerItem().setText(0, _translate("MainWindow", "Documents"))
    __sortingEnabled = self.document_list.isSortingEnabled()
    self.document_list.setSortingEnabled(False)
    self.name_document.setPlaceholderText(_translate("MainWindow", "Nommer votre document."))
    self.label.setText(_translate("MainWindow", "Documents récents"))
    self.label_2.setText(_translate("MainWindow", "Liste des documents"))
    self.open_folder.setText(_translate("MainWidnow", "Ouvir le dossier"))
    #main_window.setWindowTitle(_translate("main_window", "main_window"))


lang = {
    "create_doc_errror":"Le fichier existe déjà", 
    "create_folder": "Entrer le nom de la catégorie/dossier", 
    "text_field_empty": "Le nom du fichier est vide", 
    "error_already_exist": "Le fichier existe déjà",
    "errror_select_folder": "Veuillez sélectionner un dossier dans la liste des documents"
    }

def retranslateUi_settings(self, main_window):
    _translate = QtCore.QCoreApplication.translate
    self.main_window.setWindowTitle("Settings")
    self.title_doc.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">Nouveaux document</span></p></body></html>"))
    self.empty_doc.setText(_translate("main_window", "Document Vide"))
    self.template_doc.setText(_translate("main_window", "Utiliser une template (template.odt)"))
    self.title_folder.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">Nouveaux document Folder</span></p></body></html>"))
    self.folder_selector.setText(_translate("main_window", "Changer le dossier"))
    from main import settings
    from os import getcwd
    self.current_folder.setText(_translate("main_window", "Dossier de stockage des documents: " + settings["root"]))
    self.title_doc_name.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">Nom des ducuments</span></p></body></html>"))
    self.include_date.setText(_translate("main_window", "Inclure la date"))
    self.title_ui.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:12pt;\">Interface</span></p></body></html>"))
    self.credit.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:13pt;\"><b>EasyDoc 1.0 - Crée par Nathan Gronier</span></p></body></html>"))
    self.theme_label.setText(_translate("main_window", "Theme"))
    self.language_title.setText(_translate("main_window", "Language"))
    self.language_ComboBox.setItemText(0, _translate("main_window", "English"))
    self.language_ComboBox.setItemText(1, _translate("main_window", "Français"))
        