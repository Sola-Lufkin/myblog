#coding=utf-8

# Create your views here.

from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.template import loader,Context  
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
from myblog.message.models import *
from django.shortcuts import render_to_response,get_list_or_404  
from myblog.message.forms import CommentForm


def Message_Index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']	    
            content = form.cleaned_data['content']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_model = Message(title = title,name = name, content = content, email = email)
            message_model.save()
            return HttpResponseRedirect('/message/')  ##该处代码用于从定位   这里的意思是 表单发送后重新定位到 http://127.0.0.1:8000/message/
    else:
        form = CommentForm()  ##?????????????
	
    messages = Message.objects.all().order_by('-time')  ##定义一个Message表的数据列实例，命名为messages
    paginator = Paginator(messages,3)  ##以下对留言最分页处理
    try:
        page = int(request.GET.get('page','1'))
    except Valueerrors:
        page = 1
    try:
        message_per_page = paginator.page(page)
    except(EmptyPage,InvalidPage):
        message_per_page = paginator.page(paginator.num_pages)

    return render_to_response('message.html',{'form':form,
        'message_per_page':message_per_page})




def ContactMe_Index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']	    
            content = form.cleaned_data['content']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_model = Message(title = title,name = name, content = content, email = email)
            message_model.save()
            return HttpResponseRedirect('/#contactme')  ##该处代码用于从定位   这里的意思是 表单发送后重新定位到 http://127.0.0.1:8000/message/
    else:
        form = CommentForm()  ##?????????????
        
        return render_to_response('index.html',{'form':form})
        
        
        
        
