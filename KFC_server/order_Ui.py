from PyQt5.Qt import *


class Ui_Order(QMainWindow):
    def initUi(self,widget):
        self.shop_cart = []
        widget.resize(1100,630)
        self.widget = widget
        self.button()
        # self.setStyleSheet("background-color: rgb(244,164,96)")
        self.tab_winget()
        self.label()
        self.lineedit()
        self.food_scroll()
    
    def lineedit(self):
        self.lineEdit_1 = QLineEdit(self.widget)
        self.lineEdit_1.setGeometry(720,420,160,30)

    def tab_winget(self):
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setGeometry(QRect(660, 50, 400, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)# 设置列数
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['商品名称','数量','价格'])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)# 设置禁止编辑
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)# 设置整行选中
        self.tableWidget.horizontalHeader().setStretchLastSection(True)# 设置填满窗口
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)# 隐藏左边表头
        self.tableWidget.horizontalHeader()


    def button(self):
        self.button1 = QPushButton(self.widget)
        self.button1.setGeometry(QRect(1070, 10, 20, 20))
        self.button1.setText("×")
        self.button1.clicked.connect(self.widget.close) 

        self.button2 = QPushButton(self.widget)
        self.button2.setGeometry(QRect(900, 420, 100, 30))
        self.button2.setText("查询")
         

        self.button3 = QPushButton(self.widget)
        self.button3.setGeometry(QRect(800, 480, 100, 40))
        self.button3.setText("会员管理")
         

        self.button33 = QPushButton(self.widget)
        self.button33.setGeometry(QRect(930, 480, 100, 40))
        self.button33.setText("会员注册")
         

        self.button4 = QPushButton(self.widget)
        self.button4.setGeometry(QRect(700, 560, 100, 40))
        self.button4.setText("普通结账")
         

        self.button5 = QPushButton(self.widget)
        self.button5.setGeometry(QRect(850, 560, 100, 40))
        self.button5.setText("会员结账")
         

    def label(self):
        self.label_1 = QLabel(self.widget)
        self.label_1.setText('会员查询')
        self.label_1.setGeometry(QRect(660,430,60,30))

        self.label_2 = QLabel(self.widget)
        self.label_2.setText('总金额')
        self.label_2.setGeometry(QRect(720,380,60,30))

        self.label_3 = QLabel(self.widget)
        self.label_3.setText('余额')
        self.label_3.setGeometry(QRect(680,480,60,30))

        self.label_4 = QLabel(self.widget)
        self.label_4.setText('0.00')
        self.label_4.setGeometry(QRect(730,480,60,30))

        self.label_5 = QLabel(self.widget)
        self.label_5.setText('0.00')
        self.label_5.setGeometry(QRect(800,380,60,30))


    def food_scroll(self):
        '''左侧商品篮控件'''
        self.tab_widget = QTabWidget(self.widget)
        self.tab_widget.setGeometry(10,10,600,600)
        # self.tab_widget.TabShape(self.tab_widget.Rounded)
        # self.tab_widget.setTabPosition(self.tab_widget.West)
        self.tab1 = QScrollArea()
        self.tab2 = QScrollArea()
        self.tab3 = QScrollArea()
        self.tab4 = QScrollArea()
        self.tab5 = QScrollArea()
        self.tab6 = QScrollArea()
        self.tab7 = QScrollArea()

        self.tab1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 一直显示水平滚动条
        self.tab1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示垂直滚动条
        self.tab1_wid = QWidget()
        self.tab1.setWidget(self.tab1_wid)
        self.tab1.setWidgetResizable(True)

        self.tab2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 一直显示水平滚动条
        self.tab2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示垂直滚动条
        self.tab2_wid = QWidget()
        self.tab2.setWidget(self.tab2_wid)
        self.tab2.setWidgetResizable(True)

        self.tab3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 一直显示水平滚动条
        self.tab3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示垂直滚动条
        self.tab3_wid = QWidget()
        self.tab3.setWidget(self.tab3_wid)
        self.tab3.setWidgetResizable(True)

        self.tab4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 一直显示水平滚动条
        self.tab4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示垂直滚动条
        self.tab4_wid = QWidget()
        self.tab4.setWidget(self.tab4_wid)
        self.tab4.setWidgetResizable(True)

        self.tab5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 一直显示水平滚动条
        self.tab5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示垂直滚动条
        self.tab5_wid = QWidget()
        self.tab5.setWidget(self.tab5_wid)
        self.tab5.setWidgetResizable(True)

        self.tab6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 一直显示水平滚动条
        self.tab6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示垂直滚动条
        self.tab6_wid = QWidget()
        self.tab6.setWidget(self.tab6_wid)
        self.tab6.setWidgetResizable(True)

        self.tab7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 一直显示水平滚动条
        self.tab7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 不显示垂直滚动条
        self.tab7_wid = QWidget()
        self.tab7.setWidget(self.tab7_wid)
        self.tab7.setWidgetResizable(True)
  
        self.tab_widget.addTab(self.tab1,"当季主打")
        self.tab_widget.addTab(self.tab2,"美味汉堡")
        self.tab_widget.addTab(self.tab3,"特色烤翅")
        self.tab_widget.addTab(self.tab4,"多彩套餐")
        self.tab_widget.addTab(self.tab5,"巨大的桶")
        self.tab_widget.addTab(self.tab6,"小食配餐")
        self.tab_widget.addTab(self.tab7,"缤纷饮料")
        
        self.tabUI(self.tab1_wid,'当季主打')
        self.tabUI(self.tab2_wid,'美味汉堡')
        self.tabUI(self.tab3_wid,'特色烤翅')
        self.tabUI(self.tab4_wid,'多彩套餐')
        self.tabUI(self.tab5_wid,'巨大的桶')
        self.tabUI(self.tab6_wid,'小食配餐')
        self.tabUI(self.tab7_wid,'缤纷饮料')
    
    def tabUI(self,wid, u):
        
        import os
        self.path= (os.path.dirname(__file__)).replace('\\','/') 
        food_list = os.listdir('%s/food_images/%s'%(self.path,u))
        from math import ceil
        height = ceil(len(food_list)/3)*200+20#计算内容所占高度,控制滚动条
        wid.setMinimumSize(505,height)
        for i in range(len(food_list)):
            self.groupbox_1 = QGroupBox(wid)
            x = i%3
            y = i // 3
            
            self.groupbox_1.setGeometry(10+(x*190),10+(y*200),180,200)
            self.groupbox_1.setStyleSheet("background-color: rgb(255,255,255)")
            self.button_food_1 = QPushButton(self.groupbox_1)
            self.button_food_1.setGeometry(15,15,150,150)
            self.button_food_1.setStyleSheet(
                'QPushButton{border-image: url(%s/food_images/%s/%s)}'%(self.path,u,food_list[i])
                )
            self.button_food_2 = QPushButton(self.groupbox_1)
            self.button_food_2.setText(food_list[i][0:-4]+"元")
            self.button_food_2.setGeometry(0,175,180,20)
            # self.button_food_2.setStyleSheet("background:transparent")
            
            self.button_food_1.clicked.connect(self.button_food_2.clicked)
            self.button_food_2.clicked.connect(lambda : self.MapButton_clicked(self.sender().text()))
        

    def MapButton_clicked(self, food_money):
        
        food_money_list = food_money.split("-")
        
        food_name = food_money_list[0]
        food_money = food_money_list[1]

        self.shop_cart.append([food_name, food_money[0:-1]])
        

        # 创建一个字典用于存储{'name':monry}
        self.shop_cart_d = dict(self.shop_cart)
        # 创建一个字典,用于计数统计
        count_foodcart = {}

        for food in self.shop_cart:
            if food[0]  not in count_foodcart:
                count_foodcart[food[0]] = self.shop_cart.count(food)
        
                
        # 创建一个终极list
        self.shop_cart_end = []
        for name,count in count_foodcart.items():
            money = round(count*float(self.shop_cart_d[name]),1)
            self.shop_cart_end.append([name, count, money])
        

        # 设置行数
        self.tableWidget.setRowCount(len(self.shop_cart_end)+1)
        
        # 添加数据
        for j in range(len(self.shop_cart_end)):
            food_imfo = self.shop_cart_end[j]
            # print(food_imfo)
            for i in range(3):
                # 添加数据
                if i ==2:
                    Item = QTableWidgetItem(str(food_imfo[i])+"元")
                else:
                    Item = QTableWidgetItem(str(food_imfo[i]))
                Item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(j,i,Item)

        # 统计总金额
        sum_money = 0
        for food in self.shop_cart_end:
            sum_money += food[2]
        self.label_5.setText(str(round(sum_money,1))+"元")

        