from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ..  models import *
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
# Create your views here.


			
#首页
def adminindex(request):
	
	return render(request,'myadmin/index.html')

#home ajax
def home(request):
	u=(len(Users.objects.all()))
	t=(len(Types.objects.all()))
	g=(len(Goods.objects.all()))
	info={"u":u,"t":t,"g":g}
	return JsonResponse(info)


#填写表单
@permission_required("myadmin.insert_users",raise_exception = True)
def useradd(request):
	return render(request,"myadmin/user/add.html")

#将信息插入数据库
@permission_required("myadmin.insert_users",raise_exception = True)
def userinsert(request):
	print(request.POST.get("xx"))
	res=upload(request)
	#判断返回值是否是合法路径
	if not res:
		return HttpResponse('<script>alert("上传的文件类型不正确,只能上传图片类型");location.href="'+reverse('admin_user_add')+'"</script>')
    

	# 执行添加
	ob=Users()
	ob.username=request.POST.get("username")
	ob.password= make_password(request.POST['password'], None, 'pbkdf2_sha256')
	ob.email=request.POST.get("email")
	ob.phone=request.POST.get("phone")
	ob.age=request.POST.get("age")
	ob.sex=request.POST.get("xx")
	ob.picurl = res
	ob.save()
	return HttpResponse('<script>alert("添加成功");location.href="'+reverse('admin_user_list')+'"</script>')


#列表页
@permission_required("myadmin.show_users",raise_exception = True)
def userlist(request):
	#搜索类型
	types=request.GET.get("type","")
	#搜索值
	v=request.GET.get("keywords","")
	#搜索状态
	statuslist={"正常":0,"禁用":1,"管理员":2}
	#判断搜索类型
	if types=="all":
		data=Users.objects.filter(Q(username__contains=v)|Q(email__contains=v)|Q(age__contains=v)|Q(sex__contains=v)|Q(status__contains=v))
	elif types=="username":
		data=Users.objects.filter(username__contains=v)
	elif types=="email":
		data=Users.objects.filter(email__contains=v)
	elif types=="age":
		data=Users.objects.filter(age__contains=v)
	elif types=="sex":
		data=Users.objects.filter(sex__contains=v)

	elif types=="status":
		data=Users.objects.filter(status__contains=statuslist.get(v,"aabbcc"))
	#没有搜索条件 返回全部
	else:
		data=Users.objects.exclude(status=3)

	


	# 数据分页类
	from django.core.paginator import Paginator
	# 实例化分页类 第一个参数是查询后的信息 第二个是要展示数据的条数
	paginator = Paginator(data,10)
	#页数
	p=int(request.GET.get("p",1))
	# 获取分页数据对象[{id:1},{id:2}]  [{id:3},{id:4}]
	goodslist= paginator.page(p)
	
	# 获取当前页的页码数 (1,177)
	num = paginator.page_range


	res={"info":goodslist,"page":num}
	return render(request,'myadmin/user/list.html',res)

#逻辑删除操作
@permission_required("myadmin.del_users",raise_exception = True)

def userdel(request,uid):	
	ob=Users.objects.get(id=uid)
	ob.status=3
	ob.save()

	return HttpResponse('<script>alert("删除成功");location.href="/admin/user/list/"</script>')

#编辑页面
@permission_required("myadmin.edit_users",raise_exception = True)
def useredit(request,uid):
	ob=Users.objects.get(id=uid)
	# print(ob.id)

	return render(request,"myadmin/user/edit.html",{"ob":ob})


#更新数据
@permission_required("myadmin.edit_users",raise_exception = True)
def userupdate(request):


		ob=Users.objects.get(id = request.POST['uid'])
		ob.username=request.POST['username']
		ob.password=request.POST['password']
		ob.email=request.POST['email']
		ob.phone=request.POST['phone']
		ob.age=request.POST['age']
		ob.sex=request.POST['xx']
		print(ob.id)
		# 判断是否有文件上传
		if request.	FILES.get('picurl',None):
			 # 判断是否使用的默认图
			if ob.picurl != '/static/pics/default/default.jpg':
				import os
				os.remove('.'+ob.picurl)

			ob.picurl =  upload(request)


	    # 执行更新
		ob.save()
		return HttpResponse('<script>alert("修改成功");location.href="/admin/user/list/"</script>')

#执行状态修改
def userajax(request):

	ob=Users.objects.get(id=request.GET["uid"])
	print(ob)
	ob.status=request.GET.get("val")
	ob.save()
	return HttpResponse('')



#上传图片
def upload(request):
	if not request.FILES.get("picurl"):
		return '/static/pics/default/default.jpg'
 	

	import random,time
	#定义文件随机数
	
	time='{time}{sui}.'.format(sui=random.randrange(1000,9999),time=int(time.time()))

	#取后缀名
	res=(str(request.FILES.get("picurl")).split(".")).pop()

	path="/static/pics/"+time+res

	if res.upper() not in ["BMP","JPG","JPEG","PNG","GIF"]:
		return False
	#打开文件
	fs=open('.'+path,"wb+")
	#分片写入
	for i  in  request.FILES.get("picurl").chunks():
		fs.write(i)
	#关闭文件
	fs.close()

	return path



def code(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')








