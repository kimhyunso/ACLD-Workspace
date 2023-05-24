from django.shortcuts import render, redirect, get_list_or_404
from django.conf import settings 
from .models import Part, User
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required




@require_http_methods(['GET'])
def view(request, part_pk):
    context = {
        'user' : get_list_or_404(User, pk=part_pk)
    }
    return render(request, context)


@require_http_methods(['GET'])
def detail(request):
    Part.objects.filter()
    context = {}
    return render(request, context)

