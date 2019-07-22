from django.db import models

# Create your models here.

#轮播图的模型类
class Banner(models.Model):
    #图片标题
    title = models.CharField(verbose_name="标题",max_length=64)
    # 图片路径
    cover = models.ImageField(verbose_name="轮播图",upload_to='static/imgs/banner/')
    #图片链接
    link_url = models.URLField(verbose_name="图片链接",max_length=256)
    #图片索引
    idx = models.IntegerField(verbose_name="索引")
    is_active = models.BooleanField(verbose_name="是否激活",default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

class kecheng(models.Model):
    cover = models.ImageField(verbose_name="课程介绍图片",upload_to='static/imgs/kecheng')
    title = models.CharField(verbose_name="课程标题",max_length=64,default="")
    # content = models.TextField(verbose_name="课程内容")

    class Meta:
        verbose_name = "课程介绍"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class wenti(models.Model):
    title = models.CharField(verbose_name="具体问题",max_length=256,default='')
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    # cover = models.ImageField(upload_to='static/imgs/wenti/',verbose_name="炮制数据库")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "问题讨论"
        verbose_name_plural = verbose_name

class teacher(models.Model):
    cover = models.ImageField(upload_to='static/imgs/teacher',verbose_name="教师图片")
    name = models.CharField(max_length=64,verbose_name="教师名字")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "教师认证"
        verbose_name_plural = verbose_name

# 课程介绍页数据
class jieshao(models.Model):
    cover = models.ImageField(upload_to='static/imgs/jieshao',verbose_name='课程介绍图片')
    title = models.CharField(max_length=64,verbose_name="书籍标题")
    content = models.TextField(verbose_name="书籍简介")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "课程介绍列表"
        verbose_name_plural = verbose_name


#课程介绍详情
class xiangqing(models.Model):
    cover = models.ImageField(upload_to='static/imgs/xiangqing',verbose_name="课程介绍详情图片")
    content = models.TextField(verbose_name="课程介绍详情内容")
    title = models.CharField(max_length=64,verbose_name="课程介绍详情标题")

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = "课程介绍详情"
        verbose_name_plural = verbose_name

class teachers(models.Model): #教师列表页
    cover = models.ImageField(upload_to='static/imgs/teachers',verbose_name="教师列表图片")
    name = models.CharField(max_length=64,verbose_name="教师名字")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "教师列表"
        verbose_name_plural = verbose_name

class dagang(models.Model):  #教学大纲
    title = models.CharField(max_length=64,verbose_name="教学大纲目录")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "教学大纲"
        verbose_name_plural = verbose_name
class kejian(models.Model):   #教学课件
    title = models.CharField(max_length=64,verbose_name="教学课件标题")
    cover = models.ImageField(upload_to='static/imgs/kejian',verbose_name="教学课件图片")
    content = models.TextField(verbose_name="教学课件内容")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "教学课件"
        verbose_name_plural = verbose_name

