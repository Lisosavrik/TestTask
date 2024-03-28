from django.shortcuts import render


def show_projects(request):
    return render(request, 'main/projects.html')