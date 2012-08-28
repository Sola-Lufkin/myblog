#coding:utf-8
from django import forms

class CommentForm(forms.Form):    #######为了将message的表单和blog里commment的表单区分开，我将它们分别命了名，但是注意的是，
                                  #######由于不小心，message的表单类命成了CommentForm,而不blog的comment却为MessageForm
    title = forms.CharField(label = '标题',max_length =30,required = True)  ##required字段表示该字段是必须填写的
    name = forms.CharField(label = '姓名',max_length=40,required = True)
    email = forms.EmailField(label = '邮箱',required=False)
    content = forms.CharField(label = '内容',widget=forms.Textarea)
    
    

