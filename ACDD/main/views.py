from django.shortcuts import render
from django.http import JsonResponse 
from django.views.decorators.http import require_http_methods
import json
from .models import Agent, Dection, Report, identify, Department, Employee

def home(request):
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
        emp_name = reqData['emp_name']
        rank = reqData['rank']
        emp_no = reqData['emp_no']
        MAC = reqData['MAC']
        IP = reqData['IP']
        phone_no = reqData['phone_no']
        email = reqData['email']
        depmt_no = reqData['depmt_no']
        employee = Employee()

        department = Department.objects.get(depmt_no=depmt_no)

        employee.emp_name = emp_name
        employee.emp_no = emp_no
        employee.depmt_no = department
        employee.rank = rank
        employee.phone_no = phone_no
        employee.email = email
        employee.save()

        return JsonResponse(reqData)
    


@require_http_methods(['POST', 'GET'])
def addDepart(request):
    if request.method == 'GET':
        return render(request, 'app/addDepart.html')
    else:
        reqData = json.loads(request.body)
        landline = reqData['landline']
        location = reqData['location']
        demp_name = reqData['demp_name']

        department = Department()
        department.landline = landline
        department.location = location
        department.depmt_name = demp_name
        department.save()
        
        return JsonResponse(reqData)

        
        
       



