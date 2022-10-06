from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def iniciarsesion(request):
    
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        data=request.POST['user_name']
        
        user_name = request.POST['user_name']
        password1 = request.POST['password']
        
       
        usu=User.objects.get(username=user_name)
        usu1=User.objects.filter(password=password1).filter(username=usu)

        print(usu1)
   
        try:
        
            if usu1 is not None:
                
                if (usu.is_superuser==False and usu.is_staff==False):
                    login(request,usu)
                    request.session['superusu']=None
                    request.session['emple']=None
                    request.session['user']=usu.username
                    return redirect( "../catalogo")
                if usu.is_superuser:
                    login(request,usu)
                    request.session['superusu']=usu.is_superuser
                    request.session['emple']=None
                    request.session['user']=usu.username
                    return redirect( "../catalogo")
                if usu.is_staff:
                    login(request,usu)
                    request.session['superusu']=None
                    request.session['emple']=usu.is_staff
                    request.session['user']=usu.username
                    return redirect( "../catalogo")                    
        except usu==None:
            print ("no existe el usuario")
            
                 

    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def cerrarsesion(request):
    del request.session['user']
    logout(request)
    return redirect( "../catalogo")


carlos=0