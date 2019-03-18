
from django.conf.urls import url,include
from .views import userviews,typeviews,goodsviews,authviews

urlpatterns = [

	#后台首页
	url(r'^$',userviews.adminindex,name="admin_user_index"),
	# 后台登录页
	url(r'^login/$',authviews.mylogin,name="admin_login"),
	#退出登录
	url(r'^loginout/$',authviews.myloginout,name="admin_loginout"),
	#验证码
	url(r'^user/code/$',userviews.code,name="admin_user_code"),
    #首页信息
    url(r'^user/home/$',userviews.home,name="admin_home"),

   
    #管理员添加
    url(r'^auth/user/add/$',authviews.useradd,name="auth_useradd"),
    #管理员列表
    url(r'^auth/user/list/$',authviews.userlist,name="auth_userlist"),
    #管理员删除
    url(r'auth/user/del/(?P<uid>[0-9]+)$',authviews.userdel,name="auth_userdel"),
    #管理组添加
    url(r'^auth/group/add/$',authviews.groupadd,name="auth_groupadd"),
    #管理组列表
    url(r'^auth/group/list/$',authviews.grouplist,name="auth_grouplist"),
    #编辑组
    url(r'^auth/group/edit/(?P<gid>[0-9]+)$',authviews.groupedit,name="auth_groupedit"),



   	#用户
    url(r'^user/add/$',userviews.useradd,name="admin_user_add"),
    url(r'^user/insert/$',userviews.userinsert,name="admin_user_insert"),
    url(r'^user/list/$',userviews.userlist,name="admin_user_list"),
    url(r'^user/del/(?P<uid>[0-9]+)$',userviews.userdel,name="admin_user_del"),
    url(r'^user/edit/(?P<uid>[0-9]+)$',userviews.useredit,name="admin_user_edit"),
    url(r'^user/update/$',userviews.userupdate,name="admin_user_update"),
    url(r'^user/ajax/$',userviews.userajax,name="admin_user_ajax"),


    #类型
    url(r'^type/add$',typeviews.typeadd,name="admin_type_add"),
    url(r'^type/insert$',typeviews.typeinsert,name="admin_type_insert"),
    url(r'^type/list$',typeviews.typelist,name="admin_type_list"),
    url(r'^type/edit/(?P<tid>[0-9]+)$',typeviews.typeedit,name="admin_type_edit"),
    url(r'^type/update/$',typeviews.typeupdate,name="admin_type_update"),
    url(r'^type/del/$',typeviews.typedel,name="admin_type_del"),


    #商品
    url(r'^goods/add/$',goodsviews.goodsadd,name="admin_goods_add"),
    url(r'^goods/insert/$',goodsviews.goodsinsert,name="admin_goods_insert"),
    url(r'^goods/list/$',goodsviews.goodslist,name="admin_goods_list"),
    url(r'^goods/del/$',goodsviews.goodsdel,name="admin_goods_del"),
    url(r'^goods/edit/(?P<gid>[0-9]+)$',goodsviews.goodsedit,name="admin_goods_edit"),
    url(r'^goods/update/$',goodsviews.goodsupdate,name="admin_goods_update"),
    url(r'^goods/status/$',goodsviews.status,name="admin_goods_status"),


    #订单管理
    # url(r"^order/order/$",goodsviews.order,name="admin_order_order"),
    #订单发货
    url(r'^order/fagoods/(?P<oid>[0-9]+)$',goodsviews.fagoods,name="admin_order_fagoods"),
    #订单管理2
    url(r'^order/orders/',goodsviews.orders,name="admin_order_orders"),
    #订单查看
    url(r'^order/orderlook/(?P<aid>[0-9]+)$',goodsviews.orderlook,name="admin_order_orderlook"),
    #订单状态
    url(r'^order/statu/$',goodsviews.statu,name="admin_order_statu"),
]