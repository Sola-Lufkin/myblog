#coding:utf-8
from django import template
from django.template.defaultfilters import stringfilter

####作为合法的标签库，模块需要包含一个名为register的模块级变量。这个变量是template.Library的实例，是所有注册标签和过滤器的数据结构
register = template.Library()

@register.filter
@stringfilter

def truncate_zh(value,arg):
	"""
	Truncate a string including chinese characters.
	Argument: Numbers of characters to truncate after.
	"""
	try:
		number = arg
		if int(number) < len(value):
			return value[0:int(number)] + '. . . . . .'
		else:
			return value
	except:
		return value



