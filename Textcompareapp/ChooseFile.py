from PyQt5.QtWidgets import QFileDialog


def choose_image(self,button):

    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self,"Choose File", "", "All Files (*);;Text Files (*.txt);; CSV Files(*.csv)",options=options)

    if fileName and button == 1 :
        self.file_path = fileName
        self.lineEdit.setText(self.file_path)

    elif fileName and button == 2 :
        self.file_path = fileName

        self.lineEdit_2.setText(self.file_path)

    if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
        self.compareButton.setEnabled(True)





