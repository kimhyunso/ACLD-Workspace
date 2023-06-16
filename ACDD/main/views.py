from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Agent, Dection, Report, Identify, Department, Employee
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models import Count
import os

def home(request):
    dection_list = Dection.objects.all().filter(status=0).order_by('-dect_no')
    report_list = Report.objects.all().filter(status=0).order_by('-report_no')

    dect_count = Dection.objects.all().filter(status=0).aggregate(count=Count('dect_no'))
    report_count = Report.objects.all().filter(status=0).aggregate(count=Count('report_no'))
    report_done_count = Dection.objects.all().filter(status=1).aggregate(count=Count('dect_no'))


    context = {
        'dection_list' : dection_list,
        'report_list' : report_list,
        'dect_count' : dect_count['count'],
        'report_count' : report_count['count'],
        'report_done_count' : report_done_count['count'],
    }
    return render(request, 'app/home.html', context)


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
        dempt_list = Department.objects.all()
        context = {
            'dempt_list' : dempt_list,
        }
        return render(request, 'app/addEmp.html', context)
    else:
        if 'file_csv' in request.FILES:
            csv_file = request.FILES['file_csv']
            employee_csv_folder = 'employee_csv'
            employee_csv_path = os.path.join(employee_csv_folder, csv_file.name)
            csv_filename = fs.save(employee_csv_path, csv_file)
            return JsonResponse({'success': True})

        emp_name =request.POST.get('emp_name')
        rank = request.POST.get('rank')
        emp_no = request.POST.get('emp_no')
        MAC = request.POST.get('MAC')
        IP = request.POST.get('IP')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        depmt_no = request.POST.get('depmt_no')

        emp_img = request.FILES['empt_img']
        fs = FileSystemStorage()

        employee_folder = 'employee' 
        employee_path = os.path.join(employee_folder, f'{emp_no}_{emp_img.name}')
        filename = fs.save(employee_path, emp_img)

        employee = Employee()
        department = Department.objects.get(depmt_no=depmt_no)

        employee.emp_name = emp_name
        employee.emp_no = emp_no
        employee.depmt_no = department
        employee.rank = rank
        employee.phone_no = phone_no
        employee.email = email
        employee.emp_img_path = os.path.join(settings.MEDIA_ROOT, f'{emp_no}_{emp_img.name}')
        employee.save()

        agent = Agent()
        agent.agent_no = emp_no
        agent.status = 0
        agent.save()

        identify = Identify()
        employee = Employee.objects.get(emp_no=emp_no)
        agent = Agent.objects.get(agent_no=emp_no)

        identify.emp_no = employee
        identify.agent_no = agent
        identify.ip = IP
        identify.mac = MAC
        identify.save()
        return JsonResponse({'success': True})

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

        # dempt_list = Department.objects.all()
        # depmt_name_list = serializers.serialize('json', department)
        return JsonResponse(reqData)


        




