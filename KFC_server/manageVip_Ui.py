from PyQt5.Qt import *
import os

class ManageVip_Ui(QDialog):
    '''这是vip充值窗口'''
    
    def newWindowUI(self, dialog):
        dialog.resize(800,500)
        self.dialog = dialog
        self.button()
        self.lineEdit()
        # self.background_show()
        self.tab_winget()
    
    def button(self):
        self.button1 = QPushButton(self.dialog)
        self.button1.setGeometry(QRect(770, 10, 20, 20))
        self.button1.setText("×")
        self.button1.clicked.connect(self.dialog.close)    

        self.button2 = QPushButton(self.dialog)
        self.button2.setGeometry(QRect(30, 130,180, 50))
        self.button2.setText("查询记录")

        self.button3 = QPushButton(self.dialog)
        self.button3.setGeometry(QRect(30, 210,180, 50))
        self.button3.setText("会员充值")

        self.button4 = QPushButton(self.dialog)
        self.button4.setGeometry(QRect(30, 290,180, 50))
        self.button4.setText("会员注销")

        self.button4 = QPushButton(self.dialog)
        self.button4.setGeometry(QRect(30, 370,180, 50))
        self.button4.setText("信息打印")

    def lineEdit(self):       
        self.lineEdit_1 = QLineEdit(self.dialog)
        self.lineEdit_1.setGeometry(30, 80, 180, 30)
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setMaxLength(17)
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setEchoMode(QLineEdit.Normal)
        self.lineEdit_1.setAlignment(Qt.AlignCenter)
        self.lineEdit_1.setDragEnabled(False)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.lineEdit_1.setObjectName("lineEdit")
        self.lineEdit_1.setPlaceholderText('会员手机号')

        


    def background_show(self):
        self.path= (os.path.dirname(__file__)).replace('\\','/') 
        #添加窗口背景图片
        palette1 = QPalette() 
        palette1.setBrush(self.dialog.backgroundRole(), QBrush(QPixmap('%s/Images/regist.jpg'%self.path)))
        self.dialog.setPalette(palette1)

    def tab_winget(self):
        self.tableWidget = QTableWidget(self.dialog)
        self.tableWidget.setGeometry(QRect(230, 50, 550, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)# 设置列数
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['会员名称','消费金额',"充值金额",'剩余金额','时间'])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)# 设置禁止编辑
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)# 设置整行选中
        self.tableWidget.horizontalHeader().setStretchLastSection(True)# 设置填满窗口
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.verticalHeader().setVisible(False)# 隐藏左边表头
        self.tableWidget.horizontalHeader()
        self.tableWidget.setColumnWidth(0,95)
        self.tableWidget.setColumnWidth(1,80)
        self.tableWidget.setColumnWidth(2,80)
        self.tableWidget.setColumnWidth(3,80)
        self.tableWidget.setColumnWidth(4,200)
        
        

    