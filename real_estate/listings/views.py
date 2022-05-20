from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    print('hii there')
    return render(request,'home.html') 
    # return HttpResponse("hellow there")