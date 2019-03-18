
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^emails/$',views.emails,name="emails"),

	#首页
	url(r'^$',views.index,name="index"),
	#登录
	url(r'^login/$',views.login,name="login"),
	#退出登录
	url(r"^loginout/$",views.loginout,name="loginout"),
	#注册
	url(r'^register/$',views.register,name="register"),
  	#找回页面
  	url(r'^find/$',views.find,name="find"),
  	#向总价中删除当前商品单价
  	url(r'^deltatels$',views.deltatels,name="deltatels"),
  	#向总价中添加当前商品单价
  	url(r'^addtatels$',views.addtatels,name="addtatels"),
  	#全选时商品总价
  	url(r'^alltatels$',views.alltatels,name="alltatels"),

  	url(r'^nums$',views.nums,name="nums"),


	#列表
	url(r'^lists/(?P<pid>[0-9]+)$',views.lists,name="lists"),
	url(r'^clicknum/$',views.clicknum,name="clicknum"),
	#详情
	url(r'^info/(?P<gid>[0-9]+)$',views.info,name="info"),
	#加入购物车
	url(r'^cart/$',views.cart,name="cart"),
	#购物车列表
	url(r'^cartlist/$',views.vartlist,name="cartlist"),
	#清空购物车列表
	url(r'^cartclear/$',views.cartclear,name="cartclear"),
	#删除购物车商品
	url(r'^delgoods/$',views.delgoods,name="delgoods"),
	#商品减减按钮
	url(r'^subbutton/$',views.subbutton,name="subbutton"),
	#商品加价按钮
	url(r'^addbutton/$',views.addbutton,name="addbutton"),


	#订单提交确认
	url(r'^order/ok/$',views.orderok,name="orderok"),
	#生成订单
	url(r'^order/create/$',views.ordercreate,name="ordercreate"),
	#支付订单
	url(r'^order/buy/$',views.orderbuy,name="orderbuy"),
	#个人订单
	url(r'^order/user/$',views.orderuser,name="orderuser"),
	#个人中心
	url(r'^order/one/$',views.orderone,name="orderone"),

	#商品详情
	url(r'^order/infos/$',views.orderinfos,name="orderinfos"),
	#地址管理
	url(r'^order/add/$',views.orderadd,name="orderadd"),
	#添加地址
	url(r'^order/adds/$',views.orderadds,name="orderadds"),
	#编辑地址
	url(r'^order/edit/$',views.orderedit,name="orderedit"),
	#执行编辑
	url(r'^order/editinsert/$',views.editinsert,name="editinsert"),

]
