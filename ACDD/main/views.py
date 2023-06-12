from django.shortcuts import render
from .models import Agent, Department, Employee, Log, Report
from .server_image import Server
import json

def home(request):
    # Cam.objects.filter(name='홍길동')

    # # 'select * from cam where name = "홍길동"'

    # try:
    #     cur = conn.cursor()
    #     sql = 'select * from cam where name = "홍길동"'
    #     cur.
    # except Exception as e:
    #     print(e)
   
    return render(request, 'app/home.html')


def log(request):
    return render(request, 'app/log.html')



def log_detail(request):
    return render(request, 'app/log_detail.html')


def report(request):
    return render(request, 'app/report.html')


def report_detail(request):
    return render(request, 'app/report_detail.html')

def chart(request):
    return render(request, 'app/chart.html')

def employee(request):

    return render(request, 'app/employee.html')
