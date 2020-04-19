from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

def index(request):
    return redirect('/shows')

def shows(request):  
    all_shows = Show.objects.all()
    context = {
        "shows": all_shows
    }
    
    return render(request, "index.html", context)


def new_show(request):
    
    return render(request, "new.html")


def add_new_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], release=request.POST["release"], desc = request.POST["desc"])
        id = new_show.id
    return redirect(f"/shows/{id}")


def display_show(request, id):
    
    new_show = Show.objects.get(id=id)
    context = {
        "show": new_show
    }
    
    return render(request, "show.html", context)



def edit_show(request, id):
    show = Show.objects.get(id=id)
    context= {
        "show": show
    }
    return render(request, "edit.html", context)


def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release = request.POST['release']
        show.desc = request.POST['desc']
        show.save()
        return redirect(f"/shows/{id}")


def delete(request, id):
    
    show = Show.objects.get(id=id)
    show.delete()
    
    return redirect("/shows")