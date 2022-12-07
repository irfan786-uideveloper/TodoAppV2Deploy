from django.shortcuts import redirect, render

from .models import TodolistItem
# Create your views here.

def todoapp(request):

    todoitems=TodolistItem.objects.all

    return render(request,"todolist.html",{'item':todoitems})

def addtodo(request):

    x=request.POST['content']

    newitem=TodolistItem(content=x)

    newitem.save()

    return redirect('/')

def delete(request,id):

    y=TodolistItem.objects.get(id=id)

    y.delete()

    return redirect('/')

