import filecmp


class FileCompare():

    def comparision_tool(self):
        self.file_1 = open(self.lineEdit.text(), 'r')
        self.file_2 = open(self.lineEdit_2.text(), 'r')

        file_1 = self.lineEdit.text()
        file_2 = self.lineEdit_2.text()

        file_1_name = file_1.rfind('/')
        file_2_name = file_2.rfind('/')

        file_1_name = file_1[file_1_name+1:]
        file_2_name = file_2[file_2_name+1:]


        self.textBrowser.setText("-----------------------------------")
        self.textBrowser.append("Comparing Files...")
        self.textBrowser.append("-----------------------------------")

        if filecmp.cmp(self.lineEdit.text(),self.lineEdit_2.text()):
            self.textBrowser.append("Similar Files found!!")

        else:
            line_no = 1
            self.read_file1 = self.file_1.readline()
            self.read_file2 = self.file_2.readline()

            while self.read_file1 != '' or self.read_file2 != '':

                f1_line = self.read_file1.rstrip()
                f2_line = self.read_file2.rstrip()

                if f1_line != f2_line:

                    if f2_line == '' and f1_line != '':

                        self.textBrowser.append(file_1_name +"> Line " + str(line_no) + " : " + f1_line)

                    elif f1_line != '':
                        self.textBrowser.append(file_1_name +"> Line " + str(line_no) + " : " + f1_line)

                    if f1_line == '' and f2_line != '':
                        self.textBrowser.append(file_2_name +"> Line " + str(line_no) + " : " + f2_line)

                    elif f2_line != '':
                        self.textBrowser.append(file_2_name +"> Line " + str(line_no) + " : " + f2_line)

                    self.textBrowser.append("")

                self.read_file1 = self.file_1.readline()
                self.read_file2 = self.file_2.readline()

                line_no += 1

        self.file_1.close()
        self.file_2.close()
