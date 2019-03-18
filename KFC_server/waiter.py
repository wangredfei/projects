import os
import sys
import time
from hashlib import sha1

import pymysql
from PyQt5.Qt import *

from regist_Ui import *
from registVip_Ui import *
from login_Ui import *
from order_Ui import *
from manageVip_Ui import *


class WindowSet():
    '''放一些屏幕相关的设置'''

    def center(self):# 移动到屏幕中间
        '''用于居中'''
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕的大小
        size = self.geometry()  # 获取窗口的大小
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def nochange(self):
        self.setFixedSize(self.width(), self.height())   #禁止窗口拉伸
        self.setWindowFlags(Qt.FramelessWindowHint)  #取消窗口边框


class Login_window(WindowSet,QMainWindow):
    '''登录窗口的类'''
    def __init__(self):
        super().__init__()
        self.main_ui = Ui_MainWindow()
        self.main_ui.initUI(self)
           # 连接按钮
        login_button = self.main_ui.button1 # 登录按钮
        regist_button = self.main_ui.button2 # 注册按钮
        login_button.clicked.connect(self.login_mot)
        regist_button.clicked.connect(self.regist_mot)

    def person(self):
        self.nochange()
        self.center()
        splash = QSplashScreen(QPixmap('%s/Images/statu.jpg'%path))
        splash.show()                           # 显示启动界面
        qApp.processEvents() 
        login_window.load_data(splash)           # 加载数据
        login_window.show()
        splash.finish(login_window)              # 隐藏启动界面
    
    def regist_mot(self):
        self.newWindow = Regist()
        self.newWindow.show()
        self.newWindow.exec_()
        
    def order_mot(self):
        self.order = Order(self.waitername)
        self.order.show()
        self.close()

    def login_mot(self):
        cur = sqlh.cursor()
        login_name = self.main_ui.lineEdit.text()
        login_password = self.main_ui.lineEdit_2.text()
        # print(login_password)
        sel = 'select password from waiter where a_name=%s'
        cur.execute(sel,[login_name])
        result = cur.fetchall()
        # print(result)
        s = sha1()
        s.update(login_password.encode('utf8'))
        pwd2 = s.hexdigest()
        if len(result)  == 0:
            QMessageBox.information(login_window,'错误','用户名错误',QMessageBox.Ok)
            
        elif result[0][0] == pwd2:
            QMessageBox.information(login_window,'成功','登录成功',QMessageBox.Ok)
            self.waitername = login_name
            self.order_mot() 
        else:
            QMessageBox.information(login_window,'错误','密码错误',QMessageBox.Ok)
            
        sqlh.commit()
        cur.close()
     
    def load_data(self, sp):
        for i in range(1, 11):              #模拟主程序加载过程 
            time.sleep(0.2)                   # 加载数据
            sp.showMessage("加载... {0}%".format(i * 10), Qt.AlignHCenter |Qt.AlignTop, Qt.black)
            qApp.processEvents()  # 允许主进程处理事件
        time.sleep(1)


class Regist(WindowSet, QDialog):
    '''登录窗口中注册的类'''
    def __init__(self):
        super().__init__()
        self.connect_wid()

    def connect_wid(self):        
        regist_ui = Regist_Ui()
        regist_ui.newWindowUI(self)
        # 信息框
        self.lineEdit = regist_ui.lineEdit
        self.lineEdit_1 = regist_ui.lineEdit_1
        self.lineEdit_2 = regist_ui.lineEdit_2
        # 注册按钮
        self.button2 = regist_ui.button2
        self.button2.clicked.connect(self.regist_mot2)

        self.center()
        self.nochange()

    def regist_mot2(self):
        cur = sqlh.cursor()
        name = self.lineEdit.text()
        phonenum = self.lineEdit_1.text()
        password = self.lineEdit_2.text()
        # print(name,phonenum,password)
        if not name or not phonenum or not password:
            # print("不能为空")
            QMessageBox.information(self,'错误','不能为空',QMessageBox.Ok)

        else:    
            sele = 'select a_name from waiter where a_name=%s'
            cur.execute(sele,[name])
            r= cur.fetchall()
            if r :
                # print('用户名已经存在')
                QMessageBox.information(self,'失败','该用户已存在',QMessageBox.Ok)                
            else:
                s = sha1()
                s.update(password.encode('utf8'))
                password = s.hexdigest()
                ins = 'insert into waiter(a_name,a_phonenum,password) values(%s,%s,%s)'
                cur.execute(ins,[name,phonenum,password])
                try:
                    sqlh.commit()
                except:
                    QMessageBox.information(self,'失败','该手机号已经注册',QMessageBox.Ok)                

                cur.close()
                # print('恭喜你，注册成功')
                QMessageBox.information(self,'成功','注册成功',QMessageBox.Ok)
                self.close()


class Order(WindowSet, QWidget):
    '''点餐主界面'''
    def __init__(self, waitername):
        super().__init__()
        self.connect_wid()
        self.waitername = waitername

    def connect_wid(self):
        self.order_ui = Ui_Order()
        self.order_ui.initUi(self)
        self.center()
        self.nochange()
        # 注册按钮
        registVip_button = self.order_ui.button33 
        registVip_button.clicked.connect(self.regist_mot)
        # 查询按钮
        selectVip_button = self.order_ui.button2
        selectVip_button.clicked.connect(self.selectVip_mot)
        # 会员管理
        manage_button = self.order_ui.button3
        manage_button.clicked.connect(self.manageVip_mot)
        # 普通结账
        com_pay = self.order_ui.button4
        com_pay.clicked.connect(self.compay_mot)
        # 会员结账
        vip_pay = self.order_ui.button5
        vip_pay.clicked.connect(self.vippay_mot)


    def regist_mot(self):
        '''注册函数'''
        self.newWindow = RegistVip()
        self.newWindow.show()
        self.newWindow.exec_()

    def manageVip_mot(self):
        '''调用会员界面'''
        self.manage = ManageVip()
        self.manage.show()
        self.manage.exec_()

    def selectVip_mot(self):
        '''查询函数'''
        phonenum = self.order_ui.lineEdit_1.text()
        
        if not phonenum:
            QMessageBox.information(self,'错误','不能为空',QMessageBox.Ok)
            
            return -1 
        cur = sqlh.cursor()
        query='select money from vip where phonenum=%s'#vip客户点餐
        cur.execute(query,[phonenum])
        r = cur.fetchall()
       
        if not r:
            QMessageBox.information(self,'提示','还不是会员,请注册',QMessageBox.Ok)
        else :
            self.order_ui.label_4.setText(str(r[0][0])+"元")
        sqlh.commit()
        cur.close()

    def compay_mot(self):
        # 消费金额
        consum_money = self.order_ui.label_5.text() 
        # 商品列表
        consum_cart = self.order_ui.shop_cart_end
        # print(self.order_ui.shop_cart_end)
        # 存入数据库
        cur = sqlh.cursor()
        res = QMessageBox.question(self,
                        "请确认", "共消费%s元"%consum_money, 
                        QMessageBox.Ok|QMessageBox.No,
                        QMessageBox.Ok)
        print(res)
        if res == 65536:
            return
        
        query = "insert into sell(s_name , csum) values(%s,%s);"
        cur.execute(query, [ self.waitername, consum_money[:-1]])
        sqlh.commit()
        cur.close()
        # 每次结账清除
        self.order_ui.shop_cart.clear()
        self.order_ui.tableWidget.clear()
        self.order_ui.tableWidget.setHorizontalHeaderLabels(['商品名称','数量','价格'])
    
    def vippay_mot(self):
        res = self.selectVip_mot()
        if res == -1:
            return
        cur = sqlh.cursor()
        # 会员手机号
        phonenum = self.order_ui.lineEdit_1.text()
  
        # 查询余额
        query='select money from vip where phonenum=%s'
        cur.execute(query,[phonenum])
        r = cur.fetchall()
        spsum = r[0][0]

        

        # 查询名字用于存入销售表
        query='select name from vip where phonenum=%s'
        cur.execute(query,[phonenum])
        r = cur.fetchall()
        name = r[0][0]

        # 消费金额
        consum_money = self.order_ui.label_5.text()[:-1]
        # print(consum_money)
        consum_moneyVip = round(float(consum_money)*0.88,1)
        # print(consum_moneyVip)

        # 判断金额是否大于 消费金额, 如果剩余金额大于则可直接消费并且扣除卡内余额
        if spsum >= consum_moneyVip:
            spsum2 = spsum - consum_moneyVip
            query2 = "update vip set money = %s where phonenum = %s"
            cur.execute(query2, [spsum2, phonenum])
            res = QMessageBox.information(self,'请确认','打完折%s,剩余%s'%(consum_moneyVip,spsum2),QMessageBox.Ok|QMessageBox.No)
            print(res)
            if res == 65536:
                return

            # 存入销售表
            query = "insert into sell(s_name,phonenum,csum,spsum) values(%s,%s,%s,%s);"
            cur.execute(query, [name, phonenum,consum_moneyVip,spsum2])
        else:
            cash = round(consum_moneyVip - spsum, 1)
            query2 = "update vip  set money = 0 where phonenum = %s"
            cur.execute(query2, [ phonenum])
            res = QMessageBox.information(self,'请确认','打完折%s,卡内余额0元,应付现金%s'%(spsum,cash),QMessageBox.Ok|QMessageBox.No)
            if res ==  65536:
                return
            # 存入数据库
            query = "insert into sell(s_name,phonenum,csum,spsum) values(%s,%s,%s,0);"
            cur.execute(query, [name, phonenum,consum_moneyVip])
            
        # # 商品列表
        # consum_cart = self.order_ui.shop_cart_end
        # print(self.order_ui.shop_cart_end)
       
        
        sqlh.commit()
        cur.close()
        # 每次结账清除
        self.order_ui.lineEdit_1.setText("")
        self.order_ui.label_4.setText("0.00")
        self.order_ui.label_5.setText("0.00")
        self.order_ui.shop_cart.clear()
        self.order_ui.tableWidget.clear()
        self.order_ui.tableWidget.setHorizontalHeaderLabels(['商品名称','数量','价格'])


class RegistVip(WindowSet, QDialog):
    '''主界面注册的窗口'''
    def __init__(self):
        super().__init__()
        self.connect_wid()
    
    def connect_wid(self):  
        regist_ui = RegistVip_Ui()
        regist_ui.newWindowUI(self)
        self.button2 = regist_ui.button2
        self.button2.clicked.connect(self.regist_mot2)
        self.lineEdit = regist_ui.lineEdit
        self.lineEdit_1 = regist_ui.lineEdit_1
        self.lineEdit_2 = regist_ui.lineEdit_2
        self.lineEdit_3 = regist_ui.lineEdit_3
        self.center()
        self.nochange()
    def regist_mot2(self):
        '''注册按钮'''
        cur = sqlh.cursor()
        name = self.lineEdit.text()
        phonenum = self.lineEdit_1.text()
        password = self.lineEdit_2.text()
        money = self.lineEdit_3.text()
        # print(name,phonenum,password,money)
        if not cur or not phonenum or not password :
            QMessageBox.information(self,'错误','不能为空',QMessageBox.Ok)
        else:    
            sele = 'select name from vip where name=%s'
            cur.execute(sele,[name])
            r= cur.fetchall()
            if r :
                QMessageBox.information(self,'失败','该用户已存在',QMessageBox.Ok)                
            else:
                s = sha1()
                s.update(password.encode('utf8'))
                password = s.hexdigest()
                ins = 'insert into vip(name,phonenum,password,money) values(%s,%s,%s,%s)'
                cur.execute(ins,[name,phonenum,password,money])
                try:
                    sqlh.commit()
                except:
                    QMessageBox.information(self,'失败','手机号已经注册',QMessageBox.Ok)

                # print('恭喜你，注册成功')
                QMessageBox.information(self,'成功','注册成功',QMessageBox.Ok)
                query = "insert into sell(s_name,phonenum,r_money) values(%s,%s,%s);"
                cur.close()
                cur.execute(query, [name, phonenum,money])
                self.close()


class ManageVip(WindowSet, QDialog):
    def __init__(self):
        super().__init__()
        self.connect_wid()
    
    def connect_wid(self):
        # 显示控件
        manage_ui = ManageVip_Ui()
        manage_ui.newWindowUI(self)
        self.center()
        self.nochange()

        # 连接会员手机号
        self.phonenum = manage_ui.lineEdit_1
        # 连接查询记录\会员查询\信息打印\按钮
        self.select_button = manage_ui.button2
        self.select_button.clicked.connect(self.select_mot)
        
        self.recharge_button = manage_ui.button3
        # self.recharge_button.clicked.connect(self.recharge_mot)

        self.printinfo_button = manage_ui.button4
        self.printinfo_button.clicked.connect(self.printinfo_mot)
        
        # 连接表
        self.tableWidget = manage_ui.tableWidget
    def select_mot(self):
        phonenum = self.phonenum.text()
        #判断是否为空
        if not phonenum:
            QMessageBox.information(self,'错误','不能为空',QMessageBox.Ok)
            return
        # 数据库取数据
        cur = sqlh.cursor()
        query='select s_name,csum,r_money,spsum,time from sell where phonenum=%s order by time DESC '
        cur.execute(query,[phonenum])
        self.sellinfos = cur.fetchall()
        # 对取出结果进行判断
        if not self.sellinfos:
            QMessageBox.information(self,'提示','没有消费记录',QMessageBox.Ok)
        else :
            # 设置行增长
            self.tableWidget.setRowCount(len(self.sellinfos)+1)
            for j in range(len(self.sellinfos)):
                sellinfo = self.sellinfos[j]
                # print(sellinfo)
                for i in range(5):
                    # 添加数据
                    if i ==1 or i == 2 or i == 3:
                        Item = QTableWidgetItem(str(sellinfo[i])+"元")
                    else:
                        Item = QTableWidgetItem(str(sellinfo[i]))
                    Item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(j,i,Item)

    # def recharge_mot(self):

    def printinfo_mot(self):
        print(self.sellinfos)


if __name__ == "__main__":
    path= (os.path.dirname(__file__)).replace('\\','/')
    sqlh = pymysql.connect(host='localhost',
                        user='root',
                        password='123456',
                        database='kfc',
                        charset='utf8',
                        port=3306)

    app=QApplication(sys.argv)
    login_window = Login_window()
    login_window.person()
    sys.exit(app.exec_())                   # 进入循环
