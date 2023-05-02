from django.shortcuts import render

def Welcome_view(request):
    name = "Abdulaziz"
    return render(request, 'base.html',{"name": name})

def Course_info(request):
    name = "Abdulaziz"
    return render(request, 'base.html',{"name": name})
