import pymysql
db = pymysql.connect('localhost','root','123456',charset='utf8')
cur = db.cursor()
def createdb():
    cur.execute("create database kfc")
    cur.execute('use kfc')
    db.commit()
def vip():
    cur.execute('create table vip(id int primary key auto_increment,\
        name varchar(20) not null, password varchar(40) not null,\
        phonenum varchar(20) not null unique,money int not null,time timestamp)')
    db.commit()

def food():
    cur.execute('create table food(f_id int,f_name varchar(20) not null,\
            f_money varchar(20) not null,\
            fcount int,ftime timestamp)')
    db.commit()

def sell():
    cur.execute("create table sell(id int primary key auto_increment,\
            s_name varchar(40) default 'passerby',phonenum int default 0,\
            time timestamp,csum float(6,1) default 0,spsum float(6,1) default 0\
            ,r_money float(6,1) default 0)")
    db.commit()
def waiter():
    cur.execute("create table waiter(id int primary key auto_increment,\
    a_name varchar(20) not null,\
    password varchar(40) not null,\
    a_phonenum varchar(20) not null unique,time timestamp)")
    db.commit()

createdb()
vip()
food()
sell()
waiter()
db.close()
print('数据库和表创建成功')