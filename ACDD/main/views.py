from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def detail(request):
    return render(request, 'detail.html')



def processing(request):
    return render(request, 'processing.html')


def agree(request):
    return render(request, 'agree.html')


def disagree(request):
    return render(request, 'disagree.html')