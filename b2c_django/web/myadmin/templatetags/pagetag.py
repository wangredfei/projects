from django import template
register = template.Library()
# 自定义过滤器
# @register.filter
# def kong_upper(val):
#     print ('val from template:',val)
#     return val.upper()

# 自定义标签
from django.utils.html import format_html
@register.simple_tag
def showpage(count,request): 
    kv=""
    for i in request.GET:
        if i != 'p':
            kv+='&'+i+'='+request.GET[i]
    # print(kv)
    count= int(count)
    p=int(request.GET.get("p",1))

    begin=p-4
    end=p+5

    #判断当前页数
    if p<6:
        begin=1
        end=10

    if p>count-5:
        begin=count-9
        end=count

    if count<10:
        begin=1
        end=count
    
    page=""    
    page+='<li ><a href="?p=1">首页</a></li>'
    if p <=1:
        page+='<li ><a href="?p='+str(1)+kv+'"><<</a></li>'

    else:
        page+='<li ><a href="?p='+str(p-1)+kv+'"><<</a></li>'

    for i in range(begin,end+1):
        if i==p:
            page+='<li class="am-active"><a href="?p='+str(i)+kv+'">'+str(i)+'</a></li>'
        else:
    
            page+='<li ><a href="?p='+str(i)+kv+'">'+str(i)+'</a></li>'
    if p>=count:
        page+='<li ><a href="?p='+str(count)+kv+'">>></a></li>'
    else:
        page+='<li ><a href="?p='+str(p+1)+kv+'">>></a></li>'

    page+='<li ><a href="?p='+str(count)+'">尾页</a></li>'

        

    return format_html(page)


from django.utils.html import format_html
@register.simple_tag
def sorts(request): 
    ur=""
    for i in request.GET:
        if i != 'j':
           ur+='&'+i+'='+request.GET[i]
    # print(kv)
   
    urls= '<th><a href="?j=1'+ur+'">价格↑</a></th>'
        

    return format_html(urls)





from django.utils.html import format_html
@register.simple_tag
def cheng(num,price):
    num=int(num)
    price=float(price)
    c=num * price
    res="{:.2f}".format(c)

    return res











