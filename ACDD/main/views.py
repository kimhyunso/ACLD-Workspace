from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Agent, Dection, Report, Identify, Department, Employee
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models import Count, Q
from django.core.paginator import Paginator
import os, json, psutil, random
from django.db.models.functions import TruncHour, TruncMonth
from datetime import datetime, timedelta
from django.db import connections

@require_http_methods(['GET'])
def home(request):
    context = home_data('HOME')
    return render(request, 'main/home.html', context)

@require_http_methods(['POST'])
def get_updated_data(request):
    context = home_data('REALTIME')
    return JsonResponse(context)

def home_data(isFlag):
    report_list = Report.objects.filter(status=0).order_by('-report_no').select_related(
        'dect_no', 
        'dect_no__emp_no', 
    ).values(
        'dect_no', 
        'status', 
        'create_at',
        'dect_no__emp_no__emp_no', 
        'dect_no__emp_no__emp_name', 
        'dect_no__emp_no__depmt_no__depmt_name',
    )

    for report in report_list:
        employee = report['dect_no__emp_no__emp_no']
        identify = Identify.objects.filter(emp_no=employee).first()
        if identify:
            report['ip'] = identify.ip
            report['mac'] = identify.mac

    dection_list = Dection.objects.filter(status=0).order_by('-dect_no').select_related(
        'emp_no', 
        'emp_no__depmt_no',
    ).values(
        'dect_no', 
        'create_at', 
        'emp_no__emp_no', 
        'emp_no__emp_name', 
        'emp_no__depmt_no__depmt_name',
    )
    
    for dection in dection_list:
        employee = dection['emp_no__emp_no']
        identify = Identify.objects.filter(emp_no=employee).first()
        if identify:
            dection['ip'] = identify.ip
            dection['mac'] = identify.mac

    data = Dection.objects.annotate(month=TruncMonth('create_at')).values('month').annotate(count=Count('dect_no')).values('month', 'count')

    datasets = [0 for i in range(12)]
    labels = [i for i in range(1, 13)]

    for item in data:
        for i in range(1, 13):
            if item['month'].month == i:
                datasets[i-1] = item['count']
                break
    
    dect_count = Dection.objects.all().filter(status=0).aggregate(count=Count('dect_no'))
    report_count = Report.objects.all().filter(status=0).aggregate(count=Count('report_no'))
    report_done_count = Dection.objects.all().filter(status=1).aggregate(count=Count('dect_no'))

    if isFlag == 'REALTIME':
        dection_list = list(dection_list)
        report_list = list(report_list)

        
    rnd_db = random.choice(range(1, 101))
    rnd_network_traffic = random.choice(range(1, 101))
    rnd_use_drive = random.choice(range(1, 101))
    rnd_use_cpu = random.choice(range(1, 101))

    context = {
        'dectionList' : list(dection_list),
        'reportList' : list(report_list),
        'dectionCount' : dect_count['count'],
        'reportCount' : report_count['count'],
        'reportDoneCount' : report_done_count['count'],
        'useCPU' : rnd_use_cpu,
        'useDB' :rnd_db,
        'useDrive' : rnd_use_drive,
        'bytesReceived' : rnd_network_traffic,
        'dataLabels' : labels,
        'datasets' : datasets,
    }

    return context



@require_http_methods(['GET', 'POST'])
def agent(request):
    if request.method == 'GET':

        page = request.GET.get('page', '1')
        search_key = request.GET.get('search_key')
        if search_key == None:
            search_key = ''

        agent_list = (
            Agent.objects
            .filter(
                Q(identifies__emp_no__emp_name__icontains=search_key)|
                Q(agent_no__icontains=search_key)|
                Q(identifies__ip__icontains=search_key)|
                Q(identifies__mac__icontains=search_key)|
                Q(identifies__emp_no__emp_name__icontains=search_key)|
                Q(identifies__emp_no__email__icontains=search_key)|
                Q(identifies__emp_no__rank__icontains=search_key)|
                Q(identifies__emp_no__depmt_no__depmt_name__icontains=search_key)|
                Q(identifies__emp_no__depmt_no__location__icontains=search_key)|
                Q(identifies__emp_no__depmt_no__landline__icontains=search_key)|
                Q(identifies__emp_no__phone_no__icontains=search_key)
            )
            .order_by('-agent_no')
            .prefetch_related('identifies__emp_no__depmt_no')
            .values(
                'agent_no',
                'create_at',
                'status',
                'identifies__ip',
                'identifies__mac',
                'identifies__emp_no__emp_name',
                'identifies__emp_no__email',
                'identifies__emp_no__rank',
                'identifies__emp_no__depmt_no__depmt_name',
                'identifies__emp_no__depmt_no__location',
                'identifies__emp_no__depmt_no__landline',
                'identifies__emp_no__phone_no',
            )
        )


        paginator = Paginator(agent_list, 10)
        page_obj = paginator.get_page(page)

        context = {
            'agent_list' : page_obj,
        }

        return render(request, 'main/agent.html', context)
    else:
        pass

def detail(request):
    page = request.GET.get('page', '1')
    search_key = request.GET.get('search_key')

    if search_key == None:
        search_key = ''
    
    if search_key == '미처리':
        search_key = 0
    elif search_key == '처리완료':
        search_key = 1
    elif search_key == '대기중':
        search_key = 2

    dection_list = Dection.objects.order_by('-dect_no').filter(
        Q(emp_no__emp_no__icontains=search_key)|
        Q(emp_no__emp_name__icontains=search_key)|
        Q(emp_no__depmt_no__depmt_name__icontains=search_key)|
        Q(dect_no__icontains=search_key)|
        Q(status__icontains=search_key)|
        Q(create_at__icontains=search_key)
    ).select_related('emp_no', 'emp_no__depmt_no').values(
        'dect_no', 
        'create_at', 
        'status',
        'emp_no__emp_no', 
        'emp_no__emp_name', 
        'emp_no__depmt_no__depmt_name'
    )

    for dection in dection_list:
        employee = dection['emp_no__emp_no']
        identify = Identify.objects.filter(emp_no=employee).first()
        if identify:
            dection['ip'] = identify.ip
            dection['mac'] = identify.mac

    paginator = Paginator(dection_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'dection_list' : page_obj,
    }

    return render(request, 'main/detail.html', context)


@require_http_methods(['GET', 'POST'])
def process(request, dect_no):
    if request.method == 'GET':
        dect_one = Dection.objects.select_related('emp_no', 'emp_no__depmt_no').values(
            'dect_no', 
            'create_at', 
            'cam_path', 
            'emp_no', 
            'status', 
            'screen_path', 
            'emp_no__emp_img_path', 
            'emp_no__emp_no', 
            'emp_no__emp_name', 
            'emp_no__rank', 
            'emp_no__depmt_no__depmt_name', 
            'emp_no__email',
            'emp_no__phone_no', 
            'emp_no__depmt_no__location', 
            'emp_no__depmt_no__landline',
        ).get(dect_no=dect_no)
        identify = Identify.objects.get(emp_no=dect_one['emp_no'])

        report_list = Report.objects.filter(dect_no=dect_no).values(
            'report_no', 'create_at', 'content', 'status'
        )

        context = {
            'dect_one' : dect_one,
            'report_list' : report_list,
            'identify' : identify,
        }
        return render(request, 'main/process.html', context)
    else:
        data = json.loads(request.body)
        status = int(data['result'])
        dect = Dection.objects.get(dect_no=dect_no)

        if status != 3:
            dection = Dection.objects.filter(dect_no=dect_no).update(status=status)

        if status == 1:
            Report.objects.filter(dect_no=dect_no).update(status=status)
        elif status == 2:
            create_report(dect)
        elif status == 3:
            report = Report.objects.get(dect_no=dect_no)
            report.status = 1
            report.save()
            create_report(dect)

        return JsonResponse({'sucess' : 200})
    


def create_report(dect):
    contents = []
    report = Report()
    report.dect_no = dect

    with open(settings.MEDIA_ROOT + '/context.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line == '\n':
                continue
            contents.append(line)
    
    rnd_content = random.choice(contents)
    report.content = rnd_content
    report.status = 0
    report.save()


def employee(request):
    return render(request, 'main/employee.html')

@require_http_methods(['POST', 'GET'])
def addEmp(request):
    if request.method == 'GET':
        dempt_list = Department.objects.all()
        context = {
            'dempt_list' : dempt_list,
        }
        return render(request, 'main/addEmp.html', context)
    else:
        error_message = "파일형식이 잘못되었습니다"
        context = {
            'message' : error_message,
        }
        STATUS = 400
        fs = FileSystemStorage()


        if 'file_csv' in request.FILES:
            csv_file = request.FILES['fileCSV']
            allowed_extensions = ['csv', 'xlsx']
            file_extension = csv_file.name.split('.')[-1].lower()

            if file_extension not in allowed_extensions:
                return JsonResponse(context, status=STATUS)
    
            employee_csv_folder = 'employee_csv'
            employee_csv_path = os.path.join(employee_csv_folder, csv_file.name)
            csv_filename = fs.save(employee_csv_path, csv_file)
            return JsonResponse({'success': True})

        emp_img = request.FILES['emptImage']
        allowed_extensions = ['png', 'jpg', 'jpeg', 'bmp']
        file_extension = emp_img.name.split('.')[-1].lower()

        if file_extension not in allowed_extensions:
            return JsonResponse(context, status=STATUS)

        emp_name =request.POST.get('empName')
        rank = request.POST.get('rank')
        emp_no = request.POST.get('empNo')
        phone_no = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        depmt_no = request.POST.get('depmtNo')

        employee_folder = 'employee' 
        employee_path = employee_folder + '/' + f'{emp_no}_{emp_img.name}'
        filename = fs.save(employee_path, emp_img)

        
        department = Department.objects.get(depmt_no=depmt_no)
        emp_img_path = os.path.join(settings.MEDIA_URL, employee_path)
        emp_no = Employee.objects.create(emp_name=emp_name, emp_no=emp_no, depmt_no=department, rank=rank, phone_no=phone_no, email=email, emp_img_path=emp_img_path)
        agent_no = Agent.objects.create(status=0)
        

        identify = Identify()
        identify.emp_no = Employee.objects.last()
        identify.agent_no = Agent.objects.last()
        identify.save()

        return JsonResponse({'success': True})

@require_http_methods(['POST', 'GET'])
def addDepart(request):
    if request.method == 'GET':
        return render(request, 'main/addDepart.html')
    else:
        reqData = json.loads(request.body)
        landline = reqData['landLine']
        location = reqData['location']
        demp_name = reqData['dempName']

        department = Department()
        department.landline = landline
        department.location = location
        department.depmt_name = demp_name
        department.save()

        return JsonResponse(reqData)


        




