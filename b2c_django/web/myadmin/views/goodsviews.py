from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ..  models import *
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import permission_required




@permission_required("myadmin.insert_goods",raise_exception = True)
def goodsadd(request):

	from . typeviews import order

	info={"tlist":order(request)}

	return render(request,'myadmin/goods/add.html',info)

@permission_required("myadmin.insert_goods",raise_exception = True)
def goodsinsert(request):
	if not request.FILES.get("pic",None):
		return HttpResponse("<script>alert('请选择上传图片');location.href='"+reverse("admin_goods_add")+"'</script>") 

	ob=Goods()
	ob.typeid=Types.objects.get(id=request.POST["typeid"])
	ob.title=request.POST["title"]
	ob.price=request.POST["price"]
	ob.storage=request.POST["storage"]
	ob.pic=upload(request)
	ob.info=request.POST["info"]
	ob.save()
	return HttpResponse('<script>alert("添加成功");location.href="/admin/goods/list/"</script>')


@permission_required("myadmin.show_goods",raise_exception = True)
def goodslist(request):
	#获取是否排序

	#接收所搜索参数
	keywords=request.GET.get("keywords",None)
	j=request.GET.get("j",None)
	# 接收区间搜索值
	begin=request.GET.get("begin","")
	end=request.GET.get("end","")

	
	# 判断是否有搜索条件
	if  keywords and j :
		ob= Goods.objects.filter(title__contains=keywords).order_by("price")
	
	elif keywords:
		ob=Goods.objects.filter(title__contains=keywords)


	elif j :
		ob=Goods.objects.order_by("price")
	
	elif begin and end=="":
		ob=Goods.objects.filter(price__gte=begin)
	elif end and begin=="":
		ob=Goods.objects.filter(price__lte=end)
	elif end and begin:
		ob=Goods.objects.filter(Q(price__gte=begin),Q(price__lte=end))
	
	else:
		ob=Goods.objects.all()


	#分页
	from django.core.paginator import Paginator
	# 实例化分页类
	paginator = Paginator(ob,5)
	
	# 获取当前页码
	p=int(request.GET.get('p',1))

	# 获取分页数据对象
	goodslist= paginator.page(p)
	
	
	info={"ob":goodslist}





	return render(request,"myadmin/goods/list.html",info)


@permission_required("myadmin.edit_goods",raise_exception = True)
def goodsedit(request,gid):
	ob=Goods.objects.get(id=gid)
	from . typeviews import order

	info={"ob":ob,"glist":order(request)}
	return render(request,"myadmin/goods/edit.html",info)


@permission_required("myadmin.del_goods",raise_exception = True)
def goodsdel(request):
	ob=Goods.objects.get(id=request.GET["gid"])
	import os
	os.remove('.'+ob.pic)


	ob.delete()

	return JsonResponse({"msg":"OK"})

@permission_required("myadmin.edit_goods",raise_exception = True)
def goodsupdate(request):

	ob=Goods.objects.get(id=request.POST.get("gid"))
	try:
		ob.typeid=Types.objects.get(id=request.POST["typeid"])
		ob.price=request.POST["price"]
		ob.title=request.POST["title"]
		ob.storage=request.POST["storage"]
		ob.info=request.POST["info"]
		ob.title=request.POST["title"]
		# print(request.FILES['pic'])
		# 判断是否有文件上传
		if request.FILES.get("pic",None):
		 	# 判断是否使用的默认图
			if ob.pic != '/static/pics/default/default.jpg':
				import os
				os.remove('.'+ob.pic)

			ob.pic =  upload(request)
	    # 执行更新
		ob.save()
		res="<script>alert('修改成功');location.href='"+reverse("admin_goods_list")+"'</script>"
	except:
		res="<script>alert('修改成功');location.href='admin/goods/edit/"+ob.id+"'</script>"

	return HttpResponse(res)

#状态
def status(request):
	ob=Goods.objects.get(id=request.GET["uid"])
	ob.status=int(request.GET["val"])
	ob.save()
	return HttpResponse("")

#上传图片
def upload(request):

	if not request.FILES.get("pic"):
		return '/static/pics/default/default.jpg'
 	

	import random,time
	#定义文件随机数
	
	time='{time}{sui}.'.format(sui=random.randrange(1000,9999),time=int(time.time()))

	#取后缀名
	res=(str(request.FILES.get("pic")).split(".")).pop()


	path="/static/pics/goods/"+time+res

	if res.upper() not in ["BMP","JPG","JPEG","PNG","GIF"]:
		return False
	#打开文件
	fs=open('.'+path,"wb+")
	#分片写入
	for i  in  request.FILES.get("pic").chunks():
		fs.write(i)
	#关闭文件
	fs.close()

	return path


#订单发货
def fagoods(request,oid):
	
	if request.method=="GET":
		return render(request,'myadmin/goods/fagoods.html')
	elif request.method=="POST":

		
	
		# 查找发货的订单
		order=Order.objects.get(id=oid)
		order.status=3
		# 提交表单
		order.wuliu=request.POST.get("wuliu")
		order.oddnum=request.POST.get("oddnum")
		order.save()
		return HttpResponse("<script>alert('发货成功');location.href='"+reverse("admin_order_orders")+"'</script>")

#订单管理2
def orders(request):
	# 接收所搜索参数
	statu=request.GET.get("type","0")
	if statu=="0":
		#查询所有订单
		orderss=Order.objects.all()
	elif statu=="1":
		#查询未付款的订单
		orderss=Order.objects.filter(status=1)
	elif statu=="2":
		#查询代发货的订单
		orderss=Order.objects.filter(status=2)
	elif statu=="3":
		#查询已发货的订单
		orderss=Order.objects.filter(status=3)



	#分页
	from django.core.paginator import Paginator
	# 实例化分页类
	paginator = Paginator(orderss,5)
	
	# 获取当前页码
	p=int(request.GET.get('p',1))

	# 获取分页数据对象
	orderlist= paginator.page(p)
	
	#分配数据	
	info={"ob":orderlist}


	return render(request,'myadmin/goods/order.html',info)



#订单查看
def orderlook(request,aid):
	#接收订单号
	ob=Order.objects.filter(id=aid)
	info={"order":ob}

	return render(request,'myadmin/goods/orderlook.html',info)


# #订单状态修改
def statu(request):
	status=request.GET["v"]
	print(status)
	ids=int(request.GET["i"])
	#查找订单
	ob=Order.objects.get(id=ids)
	ob.status=status
	ob.save()
	return HttpResponse("ok")





