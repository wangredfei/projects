from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ..  models import *
from django.urls import reverse
from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth import authenticate,login,logout 












#管理员添加
def useradd(request):

	#判断是请求页面或提交
	if request.method == "GET":

		#查询所有组
		per=Group.objects.all()
		info={"per":per}
		return render(request,"myadmin/auth/add.html",info)
	elif request.method == "POST":
		s=request.POST.get("super","")
		
		
		if s:
			ob=User.objects.create_superuser(request.POST["username"],request.POST["email"],request.POST["password"])
		
		else:
			ob=User.objects.create_user(request.POST["username"],request.POST["email"],request.POST["password"])	

		ob.save()
		# 判断是否有选权限组
		prms=request.POST.getlist("prms",None)
		if prms:
			ob.groups.set(prms)
			ob.save()

		return HttpResponse("<script>alert('成功');location.href='"+reverse("auth_userlist")+"'</script>")




#管理元列表
def userlist(request):

	ob=User.objects.all()

	return render(request,'myadmin/auth/list.html',{"ob":ob})


# 管理员删除
def userdel(request,uid):

    ob = User.objects.get(id=uid)
    ob.delete()
    return HttpResponse('<script>location.href="/admin/auth/user/list"</script>')

#添加组
def groupadd(request):
	if request.method == "GET":
		per=Permission.objects.exclude(name__istartswith="Can")
		return render(request,"myadmin/group/add.html",{"per":per})

	elif request.method == "POST":
		# 获取选择的所有权限
		l=request.POST.getlist("prms",None)

		# 创建组
		g = Group(name=request.POST['username'])
		g.save()

	
	
		# 判断是否需要给组添加权限
		if l:
			# 给组分配权限
			g.permissions.set(l)
			g.save()


			return HttpResponse("<script>alert('成功');location.href='"+reverse("auth_grouplist")+"'</script>")


#组列表
def grouplist(request):
	g=Group.objects.all()


	return render(request,"myadmin/group/list.html",{"ob":g})

#组编辑
def groupedit(request,gid):
	# 查询组
	ginfo=Group.objects.get(id=gid)

	if request.method =="GET":	
		per=Permission.objects.exclude(group=ginfo).exclude(name__istartswith="Can")

		info={"ginfo":ginfo,"per":per}
		
		return render(request,"myadmin/group/edit.html",info)
	

	elif request.method == "POST":

		#接受发来的参数
		prms=request.POST.getlist("prms",None)
		print(prms)
		#修改组名
		ginfo.name=request.POST["name"]
		#清空当前组的权限
		ginfo.permissions.clear()
		if prms:
			ginfo.permissions.set(prms)

		ginfo.save()

		return HttpResponse("<script>alert('成功');location.href='"+reverse("auth_grouplist")+"'</script>")

#登录页
def mylogin(request):
	if request.method=="GET":

		return render(request,'myadmin/login.html')
	elif  request.method=="POST":

		#检测验证码是否正确
		if request.POST["code"].lower() != request.session["verifycode"].lower():
			return HttpResponse("<script>alert('验证码不正确');location.href='/admin/login'</script>")

		#使用django 提公的后台验证方法
		username=request.POST["username"]
		password=request.POST["password"]
		user = authenticate(request,username=username,password=password)
	
		if user:
			login(request,user)
	
			return render(request,'myadmin/index.html')
		return HttpResponse("<script>alert('用户名不存在或密码不正确');location.href='/admin/login'</script>")

	# 	ob=Users.objects.filter(username=request.POST["username"])
	# 	# 真则表示有这条数据
	# 		#判断密码是否正确
	# 		if check_password(request.POST['password'],ob[0].password):
			
	# 			#密码正确 判断是否是管理员权限
	# 			if ob[0].status==2:
	# 				request.session["AdminUser"]={"username":ob[0].username,"pic":ob[0].picurl}
	# 				request.session.set_expiry(0)
	# 			else:
	# 				return HttpResponse("<script>alert('您没有权限登录');location.href='/admin/login'</script>")
			
			
#退出登录	
def myloginout(request):
	# del request.session['AdminUser']
	logout(request)
	return HttpResponse("<script>alert('退出成功');location.href='/admin/login'</script>")