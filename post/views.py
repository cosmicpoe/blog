from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	context_dic={'gola':'hola'}

	return render(request,'post/index.html',context_dic);
