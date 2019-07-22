from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from myapp.models import Banner,kecheng,wenti,teacher,jieshao,xiangqing,teachers,dagang,kejian  #导入轮播图模型类
# Create your views here.
def index(request):

    #取到轮播图的数据
    banner_list = Banner.objects.all()

    #取到课程的数据
    kecheng_list = kecheng.objects.all()

    # 取到问题讨论的数据
    wenti_list = wenti.objects.all()

    #取到教师的数据
    teacher_list = teacher.objects.all()
    return render(request,'index.html',locals())

def kcjs(request):    #课程介绍页
    jieshao_list = jieshao.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(jieshao_list, per_page=1, request=request)

    jieshao_list = p.page(page)

    return render(request,'课程介绍.html',locals())

def xq(request):   #课程介绍详情
    xiangqing_list = xiangqing.objects.all()

    return render(request,'课程介绍详情.html',locals())

def tea(request):  #教师页
    teachers_list = teachers.objects.all()
    return render(request,'教师队伍.html',locals())

def dg(request):  #教学大纲
    title_list = dagang.objects.all()
    return render(request,'教学大纲.html',locals())
def kj(request):  #教学课件
    kj_list = kejian.objects.all()
    return render(request,'教学课件.html',locals())



