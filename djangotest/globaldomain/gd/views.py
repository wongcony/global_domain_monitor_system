from django.shortcuts import render,render_to_response
from django.template import Template,Context
from django.http import HttpResponse
from gd.models import resultdb
# Create your views here.
def search(request):
	return render_to_response('search.html')
def domain_search_button(request):
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		results=resultdb.objects.filter(Domain=q)
		return render_to_response('/djangotest/globaldomain/gd/domain_search_result.html',{'results':results})
	else:
		message='you submit an empty form'
		return HttpResponse(message)
def ip_search_button(request):
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		results=resultdb.objects.filter(Result=q)
		return render_to_response('/djangotest/globaldomain/gd/ip_search_result.html',{'results':results})
	else:
		message='you submit an empty form'
		return HttpResponse(message)
