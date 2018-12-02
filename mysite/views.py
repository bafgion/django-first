from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'mysite/home.html')

def contact(request):
    return render(request, 'mysite/contact.html')

def news(request):
    return render(request, 'mysite/news.html')


def reset(request):
    return render(request, 'mysite/reset.html')


def reset_user(request):

    name = request.POST["Imya"]
    company = request.POST["Company"]
    email = request.POST["Email"]
    phone = request.POST["Phone"]
    message = request.POST["Message"]

    print(name, company, email, phone, message)

    return HttpResponseRedirect("/")