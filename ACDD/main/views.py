from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def detail(request):
    return render(request, 'app/detail.html')



def processing(request):
    return render(request, 'app/processing.html')


def agree(request):
    return render(request, 'app/agree.html')


def disagree(request):
    return render(request, 'app/disagree.html')