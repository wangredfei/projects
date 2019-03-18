from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ..  models import *
from django.urls import reverse
from django.contrib.auth.decorators import permission_required



@permission_required("myadmin.insert_types",raise_exception = True)
def typeadd(request):
	ob=Types.objects.all()
	info={"infos":ob}
	return render(request,"myadmin/types/add.html" , info)

@permission_required("myadmin.insert_types",raise_exception = True)
def typeinsert(request):
	#获取pid的值
	pid=request.POST['pid']
	ob=Types()
	ob.name=request.POST["name"]
	ob.pid=pid
	#判断是否是顶级分类
	if pid=='0':

		ob.path='0,'

	else:

		#查找顶级路径加上顶级id拼接
		paths=Types.objects.get(id=pid)
		ob.path=str(paths.path)+str(pid)+','

	ob.save()
	res=("<script>alert('添加成功');location.href='/admin/type/list'</script>")		

	# res=("<script>alert('添加失败');location.href='/admin/type/add'</script>")

	return HttpResponse(res)

@permission_required("myadmin.show_types",raise_exception = True)
def typelist(request):
	#接受参数
	name=request.GET.get("keywords")
	#判断是否有参数
	if name:

		pid=Types.objects.filter(name=name)

		if pid:

			vid=pid[0].id
			ob=Types.objects.filter(pid=vid)
			for i in ob :
				num=int(len(i.path)/2-1)
				i.name=num*("|--")+i.name
				if i.pid==0:
					i.pname="顶级分类"
				else :
					i.pname=Types.objects.get(id=i.pid).name

		else:

			ob=order(request)
	
	else:

		#没有搜索参数返回全部
		# ob=Types.objects.all()
		#调用排序函数
		ob=order(request)

	info={"ob":ob}

	# 数据分页类
	from django.core.paginator import Paginator
    # 实例化分页类  参数1 查询的数据,参数2 每页要显示的数据
	paginator = Paginator(ob,5)

    # 当前页码
	p = request.GET.get("p",1)

    # 根据当前页码获取当前页应该显示的数据
	userlist = paginator.page(p)

    # 获取当前页的页码数 
	num = paginator.page_range

	info={"ob":userlist,"pagenum":num}
	return render(request,"myadmin/types/list.html",info)



#定义排序函数 并让子类名称前加空格区分
def order(request):
	# 根据extra排序
	# select *,concat(path,id) as paths from myadmin_types order by paths;
	ob=Types.objects.extra(select={"paths":"concat(path,id)"}).order_by("paths")
	
	for i in ob:
		#获取path的长度
		n=int(len(i.path)/2-1)
		i.name=n*("|--")+i.name

		if i.pid==0:
			i.pname="顶级分类"
		else :
			i.pname=Types.objects.get(id=i.pid).name

	return ob


#返回编辑页面
@permission_required("myadmin.edit_types",raise_exception = True)
def typeedit(request,tid):
	ob=Types.objects.get(id=tid)
	info={"ob":ob,"alist":order(request)}
	# print(ob.pid)	


	return render(request,'myadmin/types/edit.html', info)


@permission_required("myadmin.edit_types",raise_exception = True)
def typeupdate(request):
	try:
		#获取id
		uid=request.POST.get("uid")
		#查询
		ob=Types.objects.get(id=uid)
		#执行修改
		ob.name=request.POST['name']
		ob.save()

		res=("<script>alert('修改成功');location.href='/admin/type/list'</script>")		
	except:
		res=("<script>alert('修改失败');location.href='/admin/type/edit'</script>")

	return HttpResponse(res)


@permission_required("myadmin.del_types",raise_exception = True)
def typedel(request):
	# 获取当前类下是否有分类
	obs=Types.objects.filter(pid=request.GET["vid"]).count()
	#判断
	if obs:
		#有子类
		return JsonResponse({'status':1,"msg":"当前类下还有子类,不能删除"})
	
	else:
		# 没有子类 执行删除
		ob=Types.objects.get(id=request.GET["vid"])
		ob.delete()
		return JsonResponse({'status':0,"msg":"删除成功"})





	

