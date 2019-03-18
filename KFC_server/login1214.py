from PyQt5.Qt import *
import os



class Ui_MainWindow(object):
    '''这是登录界面的控件类'''

    def initUI(self, MainWindow):
        self.path= (os.path.dirname(__file__)).replace('\\','/') 
        MainWindow.resize(800,450)
        MainWindow.setWindowTitle("KFC")
        self.parentMainWindow = MainWindow
        self.background_show()
        self.Label()
        self.Button()
        self.LineEdit()
        self.parentMainWindow.setWindowIcon(QIcon('%s/Images/ICON.jpg'%self.path))

    def background_show(self):
        #添加窗口背景图片
        palette1 = QPalette() 
        self.path= (os.path.dirname(__file__)).replace('\\','/') 
        palette1.setBrush(self.parentMainWindow.backgroundRole(), QBrush(QPixmap('%s/Images/KFC.jpg'%self.path)))
        self.parentMainWindow.setPalette(palette1)

    def Label(self):
        self.label1 = QLabel(self.parentMainWindow)
        self.label1.setGeometry(580,160,50,50)
        self.label1.setText("账号")

        self.label2 = QLabel(self.parentMainWindow)
        self.label2.setGeometry(580, 190, 50, 50)
        self.label2.setText("密码")

    def Button(self):
        self.button1 = QPushButton(self.parentMainWindow)
        self.button1.setText("登录")
        self.button1.setGeometry(580,250,90,30)

        self.button2 = QPushButton(self.parentMainWindow)
        self.button2.setText("注册")
        self.button2.setGeometry(680, 250, 90, 30)

        self.Button3 = QPushButton(self.parentMainWindow)
        self.Button3.setGeometry(QRect(770, 10, 20, 20))
        self.Button3.setText("×")
        self.Button3.clicked.connect(self.parentMainWindow.close)

        self.Button4 = QPushButton(self.parentMainWindow)
        self.Button4.setGeometry(QRect(740, 10, 20, 20))
        self.Button4.setText("-")
        self.Button4.clicked.connect(self.parentMainWindow.showMinimized)

    def LineEdit(self):
        self.lineEdit = QLineEdit(self.parentMainWindow)
        self.lineEdit.setGeometry(620, 175, 150, 20)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(17)
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('账户/手机号')

        self.lineEdit_2 = QLineEdit(self.parentMainWindow)
        self.lineEdit_2.setGeometry(620, 205, 150, 20)
        self.lineEdit_2.setMaxLength(17)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText('密码')


    def load_data(self, sp):
        for i in range(1, 11):              #模拟主程序加载过程 
            time.sleep(0.2)                   # 加载数据
            sp.showMessage("加载... {0}%".format(i * 10), Qt.AlignHCenter |Qt.AlignTop, Qt.black)
            qApp.processEvents()  # 允许主进程处理事件
        time.sleep(1)
