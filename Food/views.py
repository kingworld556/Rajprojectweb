from django.shortcuts import render, redirect, get_object_or_404
from Food.models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login_page/')
def recipe(request):
    if request.method=="POST":
        data=request.POST
        r_name=data.get('r_name')
        r_description=data.get('r_description')
        r_image=request.FILES.get('r_image')
        r_video = request.FILES.get('r_video')

        Recipe.objects.create(
            r_image=r_image,
            r_description=r_description,
            r_name=r_name,
            r_video=r_video
        )
        return redirect("/recipe/")
    
    queryset=Recipe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(r_name__icontains=request.GET.get('search'))
    context={'recipe':queryset}
    return render(request,"home/recipe.html",context)

@login_required(login_url='/login_page/')
def delete_recipe(request,id):
    recipe=get_object_or_404(Recipe,id=id)
    recipe.delete()
    return redirect('/recipe/')

@login_required(login_url='/login_page/')
def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        r_name=data.get('r_name')
        r_description=data.get('r_description')
        r_image=request.FILES.get('r_image')

        queryset.r_name=r_name
        queryset.r_description=r_description
        
        if r_image:
            queryset.r_image = r_image
        

        queryset.save()
        return redirect("/recipe/")
    context={'recipe':queryset}
    return render(request,"home/recipe_update.html",context)


def register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name =request.POST.get('last_name ')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,"User already taken")
            return redirect('/register/')
        
        user=User.objects.create(
            first_name=first_name,
            last_name =last_name ,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('/register/')
    return render(request,"home/register.html")

def logout_page(request):
    logout(request)
    return redirect('/recipe/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Username and password are required")
            return redirect('/login_page/')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid User")
            return redirect('/login_page/')
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login_page/')
        
        login(request, user)
        return redirect('/recipe/')

    # Handle GET request or other methods
    return render(request, "home/login.html")



