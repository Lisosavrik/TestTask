from django.shortcuts import render, redirect
from .models import Projects
from django.core.paginator import Paginator


def show_projects(request):
    data = Projects.objects.all()

    if (data.count() < 1):
        from .management.commands.update_db import fetch_projects
        fetch_projects()
        data = Projects.objects.all()
    
    paginator = Paginator(data, 100)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/projects.html', {'page_obj': page_obj})


def redirect_to_projects(request):
    return redirect("/projects")