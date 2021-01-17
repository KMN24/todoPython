from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list}) # в test.html отпавляется "todo_list"

def second(request):
    return HttpResponse("test2 page")