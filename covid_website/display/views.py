from django.shortcuts import render


# Create your views here.
def hospitail_detail(request):
    return render(request,'hospitail_detail.html')
def survey(request):
    return render (request,'survey.html')
def index(request):
    return render(request,'index.html')
def login (request):
    return render (request,'login.html')
def signup (request):
    return render (request,'signup.html')