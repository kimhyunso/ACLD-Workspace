from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Agent, Department, Employee, Log, Report
from .server_image import Server
from django.http import HttpResponse
import json
from django.views.decorators.http import require_http_methods



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


clients = []  # SSE 클라이언트 저장용 리스트

@require_http_methods(['GET'])
def sse_stream(request):
    response = HttpResponse(content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['Connection'] = 'keep-alive'

    clients.append(response)  # SSE 클라이언트를 리스트에 추가

    return response

@csrf_exempt
def send_html_to_clients(request):
    # HTML 데이터 처리 로직
    html = "<h1>Hello, SSE!</h1>"
    
    # HTML 데이터를 SSE 이벤트 형식으로 전송
    sse_data = f"data: {html}\n\n"
    return HttpResponse(sse_data, content_type='text/event-stream')
