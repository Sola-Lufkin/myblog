#coding:utf-8
from django import forms

class MessageForm(forms.Form):
    title = forms.CharField(label = '标题',max_length =30,required = True)  ##required字段表示该字段是必须填写的
    content = forms.CharField(label = '内容',widget=forms.Textarea)
    name = forms.CharField(label = '姓名',max_length=40,required = True)
    email = forms.EmailField(label = '邮箱',required=False)

