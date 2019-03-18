from django.shortcuts import render
from django.http import HttpResponse
import re

class AdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):


        # 检测当前的请求是否已经登录,如果已经登录,.则放行,如果未登录,则跳转到登录页
        # 获取当前用户的请求路径  /admin/开头  但不是 /admin/login/  /admin/dologin/   /admin/verifycode
        urllist = ['/admin/login/','/admin/dologin/','/admin/user/code/']
        # 判断是否进入了后台,并且不是进入登录页面
        if re.match('/admin/',request.path) and request.path not in urllist:

            # 检测session中是否存在 adminlogin的数据记录
            if request.session.get('_auth_user_id',None) == '':
                # 如果在session没有记录,则证明没有登录,跳转到登录页面
                return HttpResponse('<script>alert("请先登录");location.href="/admin/login";</script>')

        #判断是否有要进入前台需要登录的页面
        urllist=["/order/ok/","/order/create/","/order/buy/","/order/user/"]
        #判断是否进入
        if request.path in urllist:
            #判断是否登录
            if not request.session.get("vipuser",None):
                #如果没有登录则调到登录页面
                return HttpResponse('<script>alert("请先登录");location.href="/login";</script>')

        response = self.get_response(request)
        print(response)
        return response