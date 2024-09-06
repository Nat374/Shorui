from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QInputDialog, QFileDialog, QWidget, QMainWindow
from PyQt6.QtCore import QSize
import os
import subprocess
import pickle
from shutil import copy2

recent_doc_name = []
recent_doc_path = []


from datetime import date
today = date.today()
date_main_window = today.strftime("%d-%m-%Y")

# Check if data from a previous session is present
if os.path.isfile("asset\\data.pkl") == True:
    with open("asset\\data.pkl", "rb") as f:
        recent_doc_name = pickle.load(f)
        recent_doc_path = pickle.load(f)
        settings = pickle.load(f)               

if os.path.isfile("asset\\data.pkl") == False:
    settings = {
        'theme': "Windowsvista",
        'root': f"{os.getcwd()}\\database",
        'doc_base': "empty",
        'has_date_in_name': True,
        'current_lang': "Français"
    }

print(settings["current_lang"])

if settings["current_lang"] == "Français":
    print("ok")
    from fr import *
else:
    from en import *

if os.path.isdir(settings["root"]) == False:
    os.mkdir(settings["root"])

def change_settings(setting, value):
    settings[setting] = value
    with open('asset\\data.pkl', 'wb') as f:
        pickle.dump(recent_doc_name, f)
        pickle.dump(recent_doc_path, f)
        pickle.dump(settings, f)    

# Because "SyntaxError: f-string: unmatched '['" thanks nuitka
global root
root = settings["root"]

# ==============================================================================
# =           SETTINGS WINDOW                                                  =
# ==============================================================================

from setting import Ui_Settings

# =================================================================================================
# =                MAIN WINDOW                                                                    =
# =================================================================================================

# List all the folders (type/category)
class Ui_MainWindow(QMainWindow):
    def setupUi(self, parent=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 406)
        
        # Set window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("asset\\icon.png"))
        MainWindow.setWindowIcon(icon)
        # Define central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Label for the recent file and files list widget(s)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 60, 161, 16))
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 161, 16))
        
        # List of all document(s)
        self.document_list = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.document_list.setGeometry(QtCore.QRect(10, 80, 451, 321))
        self.document_list.addTopLevelItem
        self.populate_tree(root)
        self.document_list.doubleClicked.connect(self.open_file)
        
        # List of recent document(s)
        self.recent_doc = Q
        tWidgets.QListWidget(parent=self.centralwidget)
        self.recent_doc.setGeometry(QtCore.QRect(470, 80, 311, 321))
        self.recent_doc.addItems(recent_doc_name)
        self.recent_doc.doubleClicked.connect(self.open_recent_file)

        # New folder / type button
        self.new_folder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.new_folder.setGeometry(QtCore.QRect(350, 10, 55, 41))
        xMyIcon = QtGui.QPixmap("asset\\folder.png");
        self.new_folder.setIcon(QtGui.QIcon(xMyIcon))
        self.new_folder.setIconSize(QSize(26,26))    
        self.new_folder.clicked.connect(self.create_folder)  

        # Upload file button
        self.upload_document = QtWidgets.QPushButton(parent=self.centralwidget)
        self.upload_document.setGeometry(QtCore.QRect(409, 10, 55, 41))
        rMyIcon = QtGui.QPixmap("asset\\upload.png");
        self.upload_document.setIcon(QtGui.QIcon(rMyIcon))
        self.upload_document.setIconSize(QSize(26,26))    
        self.upload_document.clicked.connect(self.fupload_document)    

        # Settings button
        self.open_settings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.open_settings.setGeometry(QtCore.QRect(470, 10, 55, 41))
        rMyIcon = QtGui.QPixmap("asset\\setting.png");
        self.open_settings.setIcon(QtGui.QIcon(rMyIcon))
        self.open_settings.setIconSize(QSize(26,26))    
        self.open_settings.clicked.connect(self.open_settings_cmd)    

        # New document button (data gathered from the following elements:)
        self.new_document = QtWidgets.QPushButton(parent=self.centralwidget)
        self.new_document.setGeometry(QtCore.QRect(290, 10, 55, 41))
        rMyIcon = QtGui.QPixmap("asset\\page.png");
        self.new_document.setIcon(QtGui.QIcon(rMyIcon))
        self.new_document.setIconSize(QSize(26,26))    
        self.new_document.clicked.connect(self.create_document)    

        # Selector / ComboBox for the type when creating a document
        self.document_type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.document_type.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.folder_list_combbobox_populate()

        # Document name input
        self.name_document = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_document.setGeometry(QtCore.QRect(110, 10, 171, 41))

        # Open folder button (open the folder containing all the files)
        self.open_folder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.open_folder.setGeometry(QtCore.QRect(685, 10, 90, 41))
        #self.open_folder.setText("Open Folder")
        self.open_folder.clicked.connect(self.open_folder_cmd)

        
        # Called when the program is closed - save all data (view function for details)
        self.centralwidget.destroyed.connect(self.save_data)

        retranslateUi(self, MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

    # Add the category / folder in the ComboBox of folder (when creating document)
    def folder_list_combbobox_populate(self):
        global folder_names
        self.document_type.clear()

        folder_names = []
        for item in os.listdir(root):
            if os.path.isdir(os.path.join(root, item)):
                folder_names.append(item)

        self.document_type.addItems(folder_names)

    # Open a dialog to ask the user for the name of the new folder / category
    def create_folder(self):
        text, ok = QtWidgets.QInputDialog.getText(None, 'Create New Category', lang["create_folder"])
        if ok:
            os.mkdir(root + "\\" + text)
            
            # Reload the UI to show new elements
            self.populate_tree(root)
            self.folder_list_combbobox_populate()

    # Open a prompt for the user to copy a file to a catogory (if you need to add external file(s))
    def fupload_document(self):
        from tkinter import filedialog
        file_path = filedialog.askopenfilename()

        try:            
            # Check if the select item is a folder not a file (to avoir copy to root)
            
            folder = self.document_list.currentItem().text(0)
            folder_names.index(folder)
            
            copy2(file_path, f"{root}\\{folder}")
            # Reload the files to show changes
            self.populate_tree(root)
        except:
            QMessageBox.warning(None, "Error when copying document.", lang["errror_select_folder"])
            return
                    
    # Open the folder with all the files from the software to the user (for edits)
    def open_folder_cmd(self):
        subprocess.Popen(rf'explorer "{root}"') 

    def open_settings_cmd(self):
        global w
        w = Ui_Settings(self)
        w.show()

    def open_file(self):
        item = self.document_list.currentItem()
        name = item.text(0)
        # Check if the selected file is a child (= has a parent) if not its a parent so it should not be opened
        try: 
            parent = item.parent().text(0)

            self.open(name, parent)
        except:
            pass

    # Open a file when double clicked in the recent files widget
    def open_recent_file(self):
        # Get the selected file in the recent file(s) widget
        index = recent_doc_name.index(self.recent_doc.currentItem().text())
        subprocess.Popen(rf'explorer "{recent_doc_path[index]}"')

    # Save all the data (recent documents) when the software is closed to be used when re-opened (LINE 24-27)
    def save_data(self):
        with open('asset\\data.pkl', 'wb') as f:
            pickle.dump(recent_doc_name, f)
            pickle.dump(recent_doc_path, f)
            pickle.dump(settings, f)    
                
    # Create a document when used click the [+ File] button 
    def create_document(self):
        type = self.document_type.currentText()
        name = self.name_document.text()

        # Check if the name is not empty 
        if name == "":
            QMessageBox.warning(None, "Error when creating document.", lang["text_field_empty"])
            return
        
        if settings["has_date_in_name"] == True:
            file = f"{root}/{type}/{name} - {date_main_window}.odt"
        else:
            file = f"{root}/{type}/{name}.odt"

        # Check if the file already exist
        if os.path.isfile(file):
            QMessageBox.warning(None, "Error when creating document.", lang["error_already_exist"])
            return
        
        # Save the new file to open it to user
        if settings["doc_base"] == "empty":
            f = open(file, "a")
            f.close()
        else:
            if settings["has_date_in_name"] == True:
                file_name = f"{name} - {date_main_window}.odt"
            else:
                file_name = f"{name}.odt"
            
            copy2(f"{os.getcwd()}\\template.odt", f"{root}\\{type}")
            os.rename(f"{root}\\{type}\\template.odt", f"{root}\\{type}\\{file_name}")


        if settings["has_date_in_name"] == True:
            self.open(f"{name} - {date_main_window}.odt", type)
        else:
            self.open(f"{name}.odt", type)
        # Reload the files list to show the new document
        self.populate_tree(root) 

    # Open a file
    # ITEM NAME = The name of the file (like: my file 27-08-24.odt)
    # PARENT = The folder containing the file to open 
    def open(self, itm_name, parent):
        file = (f"{root}\\{parent}\\{itm_name}").replace("/", "\\")
        subprocess.Popen(rf'explorer "{file}"')
        # Add document to recent list on top (index 0)
        recent_doc_name.insert(0, f"{itm_name} ({parent})")
        recent_doc_path.insert(0, file)

        # Check if the recent list is not to long
        if len(recent_doc_name) >= 17:
            recent_doc_name.pop(16)
            recent_doc_path.pop(16)
            self.recent_doc.takeItem(16)


        self.recent_doc.insertItem(0, f"{itm_name} ({parent})")

    # Scan the folder containing all the files to add it the the files list widget
    # DIRECTORY = Folder to scan
    def populate_tree(self, directory):
        self.document_list.clear()
        for root, dirs, files in os.walk(directory):
            if root == directory:
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    dir_item = QtWidgets.QTreeWidgetItem([dir])
                    self.document_list.addTopLevelItem(dir_item)
                    for file in os.listdir(dir_path):
                        file_item = QtWidgets.QTreeWidgetItem([file])
                        dir_item.addChild(file_item)

    # Restanlate the UI
    # TODO: Make it load from a json file other lanagues ?
    #RestanlateUI(self, MainWindow)


# ============================================
# =              STARTUP                     =
# ============================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(settings['theme'])
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
