from django.shortcuts import render


def index(request):
    return render(request,'blog/index.html')

def about(request):
    return render(request,'blog/about.html')

def trending(request):
    return render(request,'blog/trendindpage.html')

def contact(request):
    return render(request,'blog/contacts.html')      

def home(request):
    return render(request,'blog/index.html') 

def signup(request):
    return render(request,'blog/signup.html')   

def login(request):
    return render(request,'blog/login.html')            


