from django.shortcuts import render


def dashBoard(request):
    context = {}
    return render(request, context)

def view(request, view_pk):
    context = {}
    return render(request, context)

def detail(request):
    context = {}
    return render(request, context)

