from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from myadmin.models import *
from django.contrib.auth.hashers import make_password, check_password

#信息查询
def infos():
	ob=Types.objects.exclude(pid=0)
	return ob

# #email()
def emails(request):
	from django.core.mail import send_mail
 
	send_mail('Subject here', 'Here is the message.', '2310649541@qq.com',['1833832525@qq.com'], fail_silently=False)


	return HttpResponse("123")


#首页
def index(request):
	#查寻所有的顶级分类
	data=Types.objects.filter(pid=0)
	for i in data: #便利出的是每个顶级分类
		i.sub=Types.objects.filter(pid=i.id)#将每个二级分类临时插入到顶级分类的对象中
		for ii in i.sub:#便利二级分类　
			ii.sub=Goods.objects.filter(typeid=ii.id)[0:6]#将查询到的商品临时插到二级商品的对象中

	# print(data[0].sub[0])

	#调用查询函数　将返回的分类数据给ｉｎｄｅｘ
	info={"ob":infos(),"glist":data}

	return render(request,'home/index.html',info)


# 注册页
def register(request):
	if request.method == 'GET':
		return render(request,'home/register.html')
	elif request.method == 'POST':
		name=Users.objects.filter(username=request.POST["username"])
		if request.POST["code"].lower() != request.session["verifycode"].lower():
			return HttpResponse("<script>alert('验证码不正确');location.href='/register'</script>")
		if  name:
			return HttpResponse("<script>alert('用户已注册');location.href='/register'</script>")
		else:
			ob=Users()
			ob.username=request.POST["username"]
			ob.password=make_password(request.POST['password'], None, 'pbkdf2_sha256')
			ob.email=request.POST["email"]
			ob.save()
			return HttpResponse("<script>alert('注册成功');location.href='/login'</script>")

#找回密码页面
def find(request):
	if request.method=="GET":
		return render(request,'home/find.html')	
	elif request.method=="POST":
		#接收邮箱
		email=request.POST["email"]
	
		#接收账户名
		username=request.POST["username"]
		print(email,username)	
		ob=Users.objects.filter(username=username).filter(email=email)
		print(ob)

		if ob:
			db=Users.objects.get(username=request.POST['username'])

			db.password=make_password(request.POST["password"],None,"pbkdf2_sha256")
			db.save()
			return HttpResponse("<script>alert('修改成功');location.href='/login'</script>")

		else:
			return HttpResponse("<script>alert('用户或不存在,请重新输入');location.href='/find'</script>")



#登录页
def login(request):
	#判断是否是get请求方式　GET返回登录页面
	if request.method=="GET":
		return render(request,'home/login.html')
	#判断是否是ｐｏｓｔ请求方式post则进行处理
	elif request.method=="POST":
		# name=request.POST["username"]
		#判断验证码是否正确
		if request.POST["code"].lower() != request.session["verifycode"].lower():
			return HttpResponse("<script>alert('验证码不正确');location.href='/login'</script>")
		#获取数据检测用户名密码是否匹配
		ob=Users.objects.filter(username=request.POST["username"])
		#检测是否有当前请求的用户
		if ob:
			#匹配密码是否正确
			if check_password(request.POST["password"],ob[0].password):

				request.session["vipuser"]={"name":ob[0].username,"pic":ob[0].picurl,"uid":ob[0].id}
				request.session.set_expiry(0)
				# return render(request,'home/index.html')
				return HttpResponse('<script>location.href="'+reverse('index')+'"</script>')
			
	
		return HttpResponse("<script>alert('用户名或密码不正确');location.href='/login'</script>")

#退出登录
def loginout(request):
	del request.session["vipuser"]
	return HttpResponse("<script>alert('退出登录成功');location.href='/'</script>")




#列表页
def lists(request,pid):
	#根据id查询当前选择分类 {sub:[][][],goods:[][][]}
	ob=Types.objects.get(id=pid)
	#判断是否是一级分类
	if ob.pid==0:
		data=ob
		#获取子类
		data.sub=Types.objects.filter(pid=ob.id)

		#定义一个空列表获取二级分类的id
		ids=[]
		for i in data.sub:
			ids.append(i.id)
		#查询父级id是ids里的id的商品
		data.goods=Goods.objects.filter(typeid__in=ids)
		
		
	#不是一级分类
	else:
		#获取二级分类的父级
		data=Types.objects.get(id=ob.pid)
		#获取当前分类的商品
		data.goods=Goods.objects.filter(typeid=ob.id)
		#获取当前一级分类下的所有二级分类 包括当前二级分类
		data.sub=Types.objects.filter(pid=data.id)
		#将当前二级分类传入对象
		data.obj=ob
	

	#分配数据
	info={"data":data,"ob":infos()}
	return render(request,"home/lists.html",info)


#收藏量
def clicknum(request):
	#接收gid
	gid=request.GET["gid"]
	#查询
	ob=Goods.objects.get(id=gid)
	ob.clicknum=ob.clicknum+1
	click=ob.clicknum
	ob.save()
	return JsonResponse({ "click":click })


#详情页
def info(request,gid):
	#查询gid所对应的商品
	data=Goods.objects.get(id=gid)

	#分配数据
	info={"ob":infos(),"data":data}
	return render(request,"home/info.html",info)



#加入加入购物车
def cart(request):
	#接收数量
	num=request.GET["num"]
	#接受商品id
	gid=request.GET["gid"]

	#查询session信息
	data=request.session.get("cart",{})
	#查询商品信息
	ob=Goods.objects.get(id=gid)
	#判断当前加入的商品是否在session中
	if gid in data:
		#存在则将数量加加
		data[gid]["num"]+=int(num)

	else:
		#不存在则向session中加入
		data[gid]={"gid":gid,"num":int(num),"price":str(ob.price),"title":ob.title,"pic":ob.pic}
	
	#修改data信息
	request.session["cart"]=data

	return JsonResponse({"msg":"加入成功"})

#购物车列表
def vartlist(request):

	try:
		info={"ob":infos(),"num":nums(request),"totals":totalss(request)}
		return render(request,"home/cart.html",info)
	except:
		return render(request,"home/cart.html",{"ob":infos()})


#清空购物车列表
def cartclear(request):
	del request.session["cart"]


	return HttpResponse("<script>alert('清空成功');location.href='"+reverse("cartlist") +"'</script>")


#订单确认页
def orderok(request):
	if request.method=="GET":
		#接收选择的商品id
		ids=request.GET["ids"].split(",")
		#查询ｓｅｓｓｉｏｎ信息
		ses=request.session.get("cart")
		# 定义一个新的session
		orderdata={}
		#循环cart找到商品数量　商品ID
		for i in ses:
			if i in ids:
				orderdata[i]=ses[i]
		# 将orderdata存入session
		request.session["order"]=orderdata

		# 查询订单总金额
		num=0
		totals=0
		for i in ses:
			if i in ids:
				totals+=ses[i]["num"]*float(ses[i]["price"])
				num+=ses[i]["num"]

		#获取当前用户所有的地址
		ob=Address.objects.filter(uid=request.session["vipuser"]["uid"])

		info={"ob":infos(),"total":'%.2f'%totals,"num":num,"address":ob}

		return render(request,'home/orderok.html',info)
	elif request.method=="POST":
		# 接受传过来的参数
		ob=Address()

		ob.uid = Users.objects.get(id=request.session["vipuser"]["uid"]) 
		ob.aname  = request.POST.get("aname")
		ob.aphone = request.POST.get("aphone")
		ob.adds   = request.POST.get("adds")
		

		ob.status = request.POST.get("status",0)
		#状态修改
		s =request.POST.get("status",0)
		if s == "1":
			obs = Address.objects.filter(status=1,uid=request.session["vipuser"]["uid"])
			for i in obs:
				i.status=0
				i.save()

		ob.status = s
		ob.save()
	
	return HttpResponse("<script>alert('添加成功');location.href='/order/ok/?ids="+request.GET["ids"]+"'</script>")
	



#生成订单
def ordercreate(request):

	#接收购买的商品session
	order=request.session["order"]
	print(order)
	#接收总价 
	totalprice=0
	#接收总商品数
	totalnum=0
	if order:
		#循环计算总价和总商品数
		for i in order:
			#计算总价
			p=float(order[i]["price"])*int(order[i]["num"])
			totalprice+=p
			totalnum+=int(order[i]["num"])
		#创建订单
		ob=Order()
		import time ,random
		ob.id=int(time.time())+random.randrange(1000,9999)
		ob.uid=Users.objects.get(id=request.session["vipuser"]["uid"])
		ob.address=Address.objects.get(id=request.POST["addressid"])
		ob.totalprice=totalprice
		ob.totalnum=totalnum
		ob.status=1
		ob.save()

		#读取购物车数据
		cart=request.session["cart"]

		#创建商品详情信息表
		for i in order:
			oi=OrderInfo() 
			oi.orderid=ob
			# 获取当前购买的商品对象
			g=Goods.objects.get(id=order[i]["gid"])
			oi.gid=g
			oi.num=order[i]["num"]
			oi.price=order[i]["price"]
			oi.save()
			del cart[i]
			#修改购买数量和库存量
			g.num +=  order[i]['num']
			g.storage -= order[i]['num']
			g.save()


	        #将删除后的cart重新赋值
			request.session["cart"]=cart
	        #删除order数据
			request.session["order"]={}

	    #跳转到支付页面
		return HttpResponse('<script>alert("订单创建成功,请立即支付");location.href="/order/buy/?orderid='+str(ob.id)+'"</script>')
	else:
		return	HttpResponse('<script>alert("请选择要购买的商品");location.href="'+reverse("cartlist") +'"</script>')


#支付页面
def orderbuy(request):
	if request.method=="GET":
		# 接收地址id
		oid = request.GET.get("orderid")

		#查询
		od=Order.objects.get(id=oid)
		info = {"od":od,"ob":infos()}

		return render(request,'home/orderbuy.html',info)
	elif request.method=="POST":
		oid=request.POST.get("orderid")
		ob=Order.objects.get(id=oid)
		ob.status=2
		ob.save()
		return HttpResponse('<script>alert("支付成功");location.href="'+reverse("index") +'"</script>')

#个人中心
def orderuser(request):
	#接受p
	p=request.GET.get("p","0")
	#全部订单
	if p=="0":
		#订单查询
		order=Order.objects.filter(uid=request.session["vipuser"]["uid"])
		# for i in order:
			# id     = i.uid.id
			# 添加时间
			#addtime = i.addtime
			#购买总金额
			# i.totalprice

			#商品详情表
			# ord=OrderInfo.objects.filter(orderid=i.id)
			# for i in ord:
			# 	print(i.num,i.price,i.gid.title)
		info={"order":order,"ob":infos()}
		return render(request,"home/orderuser.html",info)
	#待付款
	elif p=="1":
		#订单查询
		order=Order.objects.filter(uid=request.session["vipuser"]["uid"],status=1)
		info={"order":order,"ob":infos()}
		return render(request,"home/orderuser.html",info)

	#代发货
	elif p=="2":
		#订单查询
		order=Order.objects.filter(uid=request.session["vipuser"]["uid"],status=2)
		info={"order":order,"ob":infos()}
		return render(request,"home/orderuser.html",info)

	#已发货
	elif p=="3":
		#订单查询
		order=Order.objects.filter(uid=request.session["vipuser"]["uid"],status=3)
		info={"order":order,"ob":infos()}
		return render(request,"home/orderuser.html",info)

#个人中心
def orderone(request):
	# 查询订单
	wei=len(Order.objects.filter(uid=request.session["vipuser"]["uid"],status=1))
	dai=len(Order.objects.filter(uid=request.session["vipuser"]["uid"],status=2))
	info={"wei":wei,"dai":dai,"ob":infos()}

	return render(request,"home/orderone.html",info)

#商品详情
def orderinfos(request):
	#接传来的参数
	id=request.GET.get("id")
	# 查询商品数据
	order=Order.objects.get(id=id)
	# 查询商品详情
	info=OrderInfo.objects.filter(orderid=id)
	
	# 订单状态
	status=order.status
	if status==1:
		status="订单状态：未付款"
	elif status==2:
		status="订单状态：待发货"
	elif status==3:
		status="订单状态：已发货"
	elif status==4:
		status="订单状态：已取消"
	elif status==5:
		status="订单状态：其他"
	#收货地址
	adds=order.address.adds
	#收货姓名
	name=order.address.aname
	#付款金额
	money=order.totalprice
	titlelist=[]
	#快递单号
	oddnum=order.oddnum
	#物流
	wuliu=order.wuliu
	# 购买商品
	for i in info:
		titlelist.append(i.gid.title)

	ding={"wuliu":wuliu,"oddnum":oddnum,"status":status,"adds":adds,"titlelist":titlelist,"aname":name,"money":money}

	return JsonResponse({"order":ding})

#地址管理
def orderadd(request):
	# 获取session里的uid
	uid=request.session["vipuser"]["uid"]
	#查询地址
	ob=Address.objects.filter(uid=uid)
	
	if request.method== "GET":
		#分配地址
		info={"ob":ob}	
		return render(request,'home/orderadd.html',info)
	
	elif request.method=="POST":
		#接收aid
		aid=int(request.POST.get("aid"))
		#查询当前用户所有的地址
		for i in ob:
			
			if i.id == aid:
				i.status=1
				
			else:
				i.status=0
			
			i.save()

		return HttpResponse("ok")

#添加地址
def orderadds(request):
	if request.GET.get("aname")and request.GET.get("adds")and request.GET.get("aphone"):
		#获取当前登录的用户
		uob=Users.objects.get(id=request.session["vipuser"]["uid"])
		ob=Address()
		ob.aname=request.GET.get("aname",None)
		ob.adds=request.GET.get("adds",None)
		ob.aphone=request.GET.get("aphone",None)
		#判断地址是否是默认地址
		if request.GET["status"]=="1":
			# 获取session里的uid
			uid=request.session["vipuser"]["uid"]
			##查询当前用户所有的地址
			aob=Address.objects.filter(uid=uid)
			for i in aob:
				i.status=0
				i.save()
		ob.status=1
		ob.uid=uob
		ob.save()

		return HttpResponse("<script>alert('添加成功');location.href='"+reverse(orderadd)+"'</script>")
	else:
		return HttpResponse("<script>alert('添加失败，请完整填写信息');location.href='"+reverse(orderadd)+"'</script>")


#修改地址
def orderedit(request):
	# 接收aid
	aid=request.GET["aid"]
	#查询地址对象
	ob=Address.objects.get(id=aid)
	info={"aname":ob.aname,"adds":ob.adds,"aphone":ob.aphone}
	return JsonResponse(info)


#执行编辑
def editinsert(request):
	# 接受edit 判断是编辑还是删除
	edit=request.GET.get("edit")
	#接受地址id
	aid=int(request.GET.get("aid"))

	ob=Address.objects.get(id=aid)
	
	if edit=="1":
		# 执行删除
		ob.delete()
	elif edit=="2":
		# 执行修改
		ob.aname=request.GET["aname"]
		ob.adds=request.GET["adds"]
		ob.aphone=request.GET["aphone"]
		ob.save()


	return HttpResponse("<script>location.href='"+reverse(orderadd)+"'</script>")
	

#删除购物车单个商品
def delgoods(request):
	gid=request.GET["gid"]
	# del request.session["cart"][gid]
	data= request.session.get("cart")
	del data[gid]
	request.session["cart"]=data
	
	return JsonResponse({"msg":"ok","nums":nums(request),"totals":totalss(request)})


#商品减减
def subbutton(request):
	#获取当前操作的商品id
	gid=request.GET["gid"]
	#查询session
	data=request.session.get("cart")
	if data[gid]["num"] <= 1:
		num=data[gid]["num"]
		price=float(data[gid]["price"])
		total=num*price
		
		return JsonResponse({"num":num ,"total":'%.2f'%total,"nums":nums(request),"totals":totalss(request)})
	else:
		data[gid]["num"]=int(data[gid]["num"])-1
		request.session["cart"]=data
		num=int(data[gid]["num"])
		price=float(data[gid]["price"])
		total=num*price
		return JsonResponse({"num":num,"total":'%.2f'%total,"nums":nums(request),"totals":totalss(request)})

#商品加加
def addbutton(request):
	#获取当前操作的商品id
	gid=request.GET["gid"]
	#查询session
	data=request.session.get("cart")
	data[gid]["num"]=int(data[gid]["num"])+1
	request.session["cart"]=data
	num=int(data[gid]["num"])
	price=float(data[gid]["price"])
	total=num*price

	return JsonResponse({"num":num,"total":'%.2f'%total,"nums":nums(request),"totals":totalss(request)})

#计算总价中排除未选中的商品小计
def deltatels(request):
	
	return JsonResponse({"totalss":totals(request)})

#向总价中添加单个商品小计
def addtatels(request):

	return JsonResponse({"totalss":totals(request)})

#全选时返回的总价
def alltatels(request):

	return JsonResponse({"totalss":totalss(request)})



#计算单个总价函数
def totals(request):
	gid=request.POST.getlist("gid")
	
	res=request.session.get("cart")
	totals=0
	for i in res:
		if i in gid:
			pass
		else:
			totals+=res[i]["num"]*float(res[i]["price"])
	return '%.2f'%totals




#计算总价函数
def totalss(request):
	res=request.session.get("cart")
	#计算总价钱的标志位
	total=0
	for i in res:
		#计算总价
		total+=res[i]["num"]*float(res[i]["price"])
	return '%.2f'%total
#计算总商品数函数
def nums(request):
	res=request.session.get("cart")
	print(res)
	#计算总产品数量的标志位
	num=0
	for i in res:
		#计算购物车有多少商品
		num+=res[i]["num"]
	return num

	