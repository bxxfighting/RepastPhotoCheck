from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import repast_ui
import sys
import xlrd
import xlwt
import os
from PIL import Image

class App(QDialog):

    def __init__(self, root=None):
        super(App, self).__init__(root)
        self.ui = repast_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.filename = ''
        self.dirname = ''
        self.savedirname = ''
        self.ui.image_width.setText('800')
        self.ui.image_height.setText('800')

        self.connect(self.ui.choose_file_bn, SIGNAL('clicked()'), self.chooseFile)
        self.connect(self.ui.choose_image_bn, SIGNAL('clicked()'), self.chooseImage)
        self.connect(self.ui.check_image_bn, SIGNAL('clicked()'), self.checkImage)
        self.connect(self.ui.resize_image_bn, SIGNAL('clicked()'), self.resizeImage)
        self.connect(self.ui.choose_save_dir_bn, SIGNAL('clicked()'), self.chooseSaveDir)


    def chooseFile(self):
        fd = QFileDialog(self)
        if fd.exec() == QDialog.Accepted:
            self.filename = fd.selectedFiles()[0]
            self.ui.choose_filename.setText(self.filename)

    def chooseImage(self):
        self.dirname = QFileDialog.getExistingDirectory()
        self.ui.choose_image_dir.setText(self.dirname)

    def chooseSaveDir(self):
        self.savedirname = QFileDialog.getExistingDirectory()
        self.ui.save_dirname.setText(self.savedirname)

    def checkImage(self):
        if self.filename:
            if not os.path.exists(self.filename):
                self.displayMessage('选择的文件不存在')
                return False
        else:
            self.displayMessage('请选择一个excel文件')
            return False
    
        if self.dirname:
            if not os.path.exists(self.dirname):
                self.displayMessage('选择的目录不存在')
                return False
        else:
            self.displayMessage('请选择目录')
            return False

        data = xlrd.open_workbook(self.filename)
        table = data.sheets()[0]
        count = 0
        for name in table.col_values(0):
            image_names = [self.dirname + '/' + name + end for end in ('.jpg', '.JPG', '.jpeg')]
            sign = 0
            for image_name in image_names:
                if os.path.exists(image_name):
                    sign += 1
            if not sign:
                count += 1
                self.ui.no_file_tip.append(name)
        self.ui.no_image_count.setText(str(count)+'张图片匹配失败，详情看下面列表')

    def resizeImage(self):
        if self.dirname:
            if not os.path.exists(self.dirname):
                self.displayMessage('选择的目录不存在')
                return False
        else:
            self.displayMessage('请选择目录')
            return False
        for name in os.listdir(self.dirname):
            img = Image.open(self.dirname + '/' + name)
            img = img.resize(self.getImageSize())
            tempdir = self.savedirname + '/' + 'temp'
            if not os.path.exists(tempdir):
                os.mkdir(tempdir)
            img.save(tempdir + '/' + name, 'JPEG')

    def displayMessage(self, message):
        QMessageBox.warning(self, '警告', message)

    def getImageSize(self):
        width = int(self.ui.image_width.text())
        height = int(self.ui.image_height.text())
        return (width, height)


app = QApplication(sys.argv)
repast = App()
repast.show()
app.exec_()
