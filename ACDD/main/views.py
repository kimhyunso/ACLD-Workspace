from django.shortcuts import render


def home(request):
    return render(request, "app/home.html")

# def detail(request):
#     return render(request, "app/detail.html")


def detail(request):
    # 더미 데이터 생성
    return render(request, 'app/detail.html')



