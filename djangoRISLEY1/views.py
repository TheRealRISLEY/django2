from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def index(request):
    return render(request, 'index.html')

def newpage(request):
    return render(request, 'page_my.html')