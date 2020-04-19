from django.shortcuts import render, redirect, HttpResponse
from .models import Show

def index(request):
    return redirect('/shows')

def shows(request):  
    all_shows = Show.objects.all()
    context = {
        "shows": all_shows
    }
    
    return render(request, "index.html", context)

###########################
# DISPLAY ADD SHOW TEMPLATE
###########################
def new_show(request):
    
    return render(request, "new.html")

###########################
# ADD SHOW TO DB
###########################
def add_new_show(request):
    new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], release=request.POST["release"], desc = request.POST["desc"])
    id = new_show.id
    return redirect(f"/shows/{id}")

###########################
# DISPLAY SHOW INFO
###########################
def display_show(request, id):
    
    new_show = Show.objects.get(id=id)
    context = {
        "show": new_show
    }
    
    return render(request, "show.html", context)


###########################
# EDIT SHOW ENTRY
###########################
def edit_show(request, id):
    show = Show.objects.get(id=id)
    context= {
        "show": show
    }
    return render(request, "edit.html", context)

###########################
# SUBMIT EDIT
###########################
def update(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release = request.POST['release']
    show.desc = request.POST['desc']
    show.save()
    return redirect(f"/shows/{id}")

###########################
# REMOVE SHOW FROM DB
###########################
def delete(request, id):
    
    show = Show.objects.get(id=id)
    show.delete()
    
    return redirect("/shows")
# def new(request):
#     return render(request, 'new.html')

# def edit(request, id):
#     context = {
#         'show': Show.objects.get(id=id)
#     }
#     return render(request, 'edit.html',context)


# def shows(request, id):
#     if id > 0 :
#         context = {
#             'show': Show.objects.get(id=id)
#         }
#         return render(request, 'show.html',context)
#     else:    
#         context = {
#         'show': Show.objects.all()
#         }
#         return render(request, 'index.html', context)

# def create(request):
#     new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['release'], desc=request.POST['desc'])
#     id = new_show.id
#     print(new_show)
#     return redirect (f'/shows/{id}')

# def update(request):
#     return redirect ('shows/')