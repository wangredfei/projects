from django.db import models

# Create your models here.

#用户模型
class Users(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=77)
	email=models.CharField(max_length=100,null=True)
	phone=models.CharField(max_length=20,null=True)
	sex=models.CharField(max_length=3,null=True)
	age=models.IntegerField(null=True)
	picurl=models.CharField(max_length=100,default="/static/pics/default/default.jpg")
	status=models.IntegerField(default=0)#0正常 1禁用
	addtime=models.DateTimeField(auto_now_add=True)
	def __str__(self):

		return self.username

	class Meta:
		permissions = (
			("show_users", "查看会员管理"),
			("insert_users", "添加会员管理"),
			("edit_users", "修改会员管理"),
			("del_users", "删除会员管理"),
		)

#分类模型
class Types(models.Model):
	name=models.CharField(max_length=50)
	pid=models.IntegerField()
	path=models.CharField(max_length=50)
	def __str__(self):

		return self.name
	class Meta:
		permissions = (
			("show_types", "查看商品分类管理"),
			("insert_types", "添加商品分类管理"),
			("edit_types", "修改商品分类管理"),
			("del_types", "删除商品分类管理"),
		)



#商品模型
class Goods(models.Model):
	typeid=models.ForeignKey(to="Types",to_field="id")
	title=models.CharField(max_length=255)
	price=models.DecimalField(max_digits=8,decimal_places=2)
	storage=models.IntegerField()
	pic=models.CharField(max_length=50)
	info=models.TextField()
	num=models.IntegerField(default=0)
	clicknum=models.IntegerField(default=0)
	status=models.IntegerField(default=1)#1:新品2：热销3：下架
	addtime=models.DateTimeField(auto_now_add=True)
	def __str__(self):

		return self.title
	class Meta:
		permissions = (
			("show_goods", "查看商品管理"),
			("insert_goods", "添加商品管理"),
			("edit_goods", "修改商品管理"),
			("del_goods", "删除商品管理"),
		)

#地址模型
class Address(models.Model):
	#用户id
	uid=models.ForeignKey(to='Users',to_field="id")
	aname=models.CharField(max_length=20)
	adds=models.CharField(max_length=255)
	aphone=models.CharField(max_length=11)
	#是否为默认1 默认
	status=models.IntegerField(default=0)

	class Meta:
		permissions = (
			("show_address", "查看地址管理"),
			("insert_address", "添加地址管理"),
			("edit_address", "修改地址管理"),
			("del_address", "删除地址管理"),
		)


# 订单表
class Order(models.Model):

	uid =models.ForeignKey("Users",to_field="id")
	address = models.ForeignKey('Address',to_field='id')
	totalprice = models.FloatField()
	totalnum = models.IntegerField()
	# 1 未付款 2已付款,待发货,3已发货,待收货,4已完成,5已取消
	status = models.IntegerField()
	addtime = models.DateTimeField(auto_now_add=True)
	wuliu=models.CharField(max_length=255, null=True)
	oddnum=models.CharField(max_length=255,null=True)


	class Meta:
		permissions = (
			("show_order", "查看订单管理"),
			("insert_order", "添加订单管理"),
			("edit_order", "修改订单管理"),
			("del_order", "删除订单管理"),
		)





# 订单详情
class OrderInfo(models.Model):
	orderid = models.ForeignKey('Order',to_field="id")
	gid =  models.ForeignKey('Goods',to_field="id")
	num = models.IntegerField()
	price = models.FloatField()



	