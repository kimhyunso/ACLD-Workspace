from django.shortcuts import render
from django.http import JsonResponse 
from django.views.decorators.http import require_http_methods
import json
from .models import Agent, Dection, Report, identify, Department, Employee

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

def detail(request):
    return render(request, 'app/detail.html')

def agent(request):
    return render(request, 'app/agent.html')

# def log(request):
#     return render(request, 'app/log.html')



# def log_detail(request):
#     return render(request, 'app/log_detail.html')


# def report(request):
#     return render(request, 'app/report.html')


# def report_detail(request):
#     return render(request, 'app/report_detail.html')

def chart(request):
    return render(request, 'app/chart.html')

def employee(request):
    return render(request, 'app/employee.html')

@require_http_methods(['POST', 'GET'])
def addEmp(request):
    if request.method == 'GET':
        return render(request, 'app/addEmp.html')
    else:
        reqData = json.loads(request.body)
        demp_name = reqData['demp_name']
        emp_name = reqData['emp_name']
        rank = reqData['rank']
        emp_no = reqData['emp_no']
        MAC = reqData['MAC']
        IP = reqData['IP']
        phone_no = reqData['phone_no']
        landline = reqData['landline']
        email = reqData['email']
        location = reqData['location']
        department = Department()
        employee = Employee()

        department['depmt_name'] = demp_name
        department['landline'] = landline
        department['location'] = location

        employee['emp_no'] = emp_no
        employee['depmt_no'] = emp_no
        employee['emp_name'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no
        employee['emp_no'] = emp_no


        return JsonResponse(reqData)

@require_http_methods(['POST', 'GET'])
def addDepart(request):
    if request.method == 'GET':
        return render(request, 'app/addDepart.html')
    else:
        reqData = json.loads(request.body)
        
        
       



