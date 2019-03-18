from PyQt5.Qt import *
import os

class RegistVip_Ui(QDialog):
    '''这是管理员的注册'''
    
    def newWindowUI(self, dialog):
        dialog.resize(300,500)
        self.dialog = dialog
        self.button()
        self.lineEdit()
        self.background_show()
    
    def button(self):
        self.button1 = QPushButton(self.dialog)
        self.button1.setGeometry(QRect(270, 10, 20, 20))
        self.button1.setText("×")
        self.button1.clicked.connect(self.dialog.close)    

        self.button2 = QPushButton(self.dialog)
        self.button2.setGeometry(QRect(110, 420,80, 20))
        self.button2.setText("注册")

    def lineEdit(self):
        self.lineEdit = QLineEdit(self.dialog)
        self.lineEdit.setGeometry(75, 215, 150, 30)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(17)
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('姓名')
        
        self.lineEdit_1 = QLineEdit(self.dialog)
        self.lineEdit_1.setGeometry(75, 255, 150, 30)
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setMaxLength(17)
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setEchoMode(QLineEdit.Normal)
        self.lineEdit_1.setAlignment(Qt.AlignCenter)
        self.lineEdit_1.setDragEnabled(False)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.lineEdit_1.setObjectName("lineEdit")
        self.lineEdit_1.setPlaceholderText('手机号')

        self.lineEdit_3 = QLineEdit(self.dialog)
        self.lineEdit_3.setGeometry(75, 295, 150, 30)
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(17)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QLineEdit.Normal)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit")
        self.lineEdit_3.setPlaceholderText('金额')
        

        self.lineEdit_2 = QLineEdit(self.dialog)
        self.lineEdit_2.setGeometry(75, 335, 150, 30)
        self.lineEdit_2.setMaxLength(17)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText('密码')


    def background_show(self):
        self.path= (os.path.dirname(__file__)).replace('\\','/') 
        #添加窗口背景图片
        palette1 = QPalette() 
        palette1.setBrush(self.dialog.backgroundRole(), QBrush(QPixmap('%s/Images/regist.jpg'%self.path)))
        self.dialog.setPalette(palette1)

    