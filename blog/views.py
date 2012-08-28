#coding=utf-8

# Create your views here.

from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.template import loader,Context  
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
from myblog.blog.models import *
from django.shortcuts import render_to_response,get_list_or_404  
from myblog.blog.forms import MessageForm

   
def Archive_Blog(request,object_id):  
    blog_detail = Article.objects.filter(id=object_id) 
    blog_image = ArticlePic.objects.filter(article=object_id) 
    
    if request.method == 'POST':
        form = MessageForm(request.POST)#Form类是通过MessageForm方法填充表单的值的，这里是直接从request里获得提交的表单值。这里如果用户提交错误，则form中就会包含错误信息，在render时就能在提交错误的字段中提示错误信息。
        if form.is_valid():
            title = form.cleaned_data['title']	    ###cleaned_data为form类的属性，可以将valid的数据转换为在定义form时的对应的python类型
            content = form.cleaned_data['content']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_model = Comment(title = title,name = name, content = content, email = email, article_id = object_id )
            message_model.save()
            return HttpResponseRedirect('//')    #####???????????最后返回一个 HttpResponseRedirect 对象，作用是重定向到 /message/ 页，防止用户刷新导致重复提交数据。
    else:
        form = MessageForm()  ##?????????????如果页面没有用户发送的提交信号POST，则保持form为空，或者说重定向页面后，清空form的值，防止用户重复提交
	
    messages = Comment.objects.filter(article=object_id).order_by('-time')  ##定义一个Comment表的数据列实例，命名为messages  !?这里为什么是article，而不是article_id  由此可以猜想，在views视图函数里所需要用到的表的数据属性名时，应该和models里所用的属性名一致，而并非是真正的数据库里的名称，这应该是django故意设计来方便于代码与数据库完全独立用的。
    paginator = Paginator(messages,6)  ##以下对留言最分页处理
    try:
        page = int(request.GET.get('page','1'))
    except Valueerrors:
        page = 1
    try:
        message_per_page = paginator.page(page)
    except(EmptyPage,InvalidPage):
        message_per_page = paginator.page(paginator.num_pages)

    return render_to_response('blog.html',{'blog_detail':blog_detail,'blog_image':blog_image,'form':form,
        'message_per_page':message_per_page})
        
        

def Paginate_Blog(request):
    blog = Article.objects.all().order_by('-time')  #定义一个blog变量用于保存数据库里的Article表里的数据项，并按时间逆序排列
    paginator = Paginator(blog,5)  #定义一个Paginator类的实例paginator，并传入blog变量作为需要分页显示的数据列表，5为每页显示的数据项条数
    try:
    	page = int(request.GET.get('page','1'))  #定义整型变量page，通过request对象属性GET的get方法，获得页面请求信息里所包含的页码数，赋予page  ！！get(key,default=None)，返回键值key对应的值；如果key没有在字典里，则返回default参数的值，默认为None
        if page < 1:  #当page值未非正数时，将其设置为1，以免页码出错  ## 这里的页码分页仍然有一定的问题，如果手动在URL处输入页码数，当所录入页码并不存在时，应跳转404页
            page=1  
    except ValueError: #此处从同学拷贝来的代码有误。正确变量名写法应该如本代码 ValueError
    	page = 1  #后期可修改一下，使页面跳转404页
    try:
    	blog_per_page = paginator.page(page)  #将上面的整型变量page作为参数传入paginator的page()方法并返回一个名为blog_per_page的Page对象，该对象的参数表示的是页码序号，如给出的页号不存在，抛出InvalidPage异常。
    except(EmptyPage,InvalidPage):
    	blog_per_page = paginator.page(paginator.num_pages)  #如果抛出InvalidPage异常，则通过paginator的num_pages将页面的总页数作为参数，换句话说，就是传入页面最后一页页码
    return render_to_response('blog_list.html',{'blog_per_page':blog_per_page})






