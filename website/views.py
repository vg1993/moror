from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse

def Homepage(request):
	t=get_template('/home/ithouse/site/website/website/person/index.html')
	html=t.render()
	return HttpResponse(html)

