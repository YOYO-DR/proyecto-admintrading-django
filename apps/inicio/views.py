from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def principal(request):
  context={
    'titulo':'Principal'
  }
  return render(request, 'principal.html',context)

def iniciarsesion(request):
  #si el metodo es get le paso el formulario
  if request.method=='GET':
    context={
    'titulo':'Iniciar sesión',
    'form':AuthenticationForm
  }
    return render(request, 'iniciarsesion.html',context)
  #si es post, verifico los datos
  elif request.method=='POST':
    #busco si el usuario existe
    user=User.objects.filter(username=request.POST['username'])
    if user:
      #si existe, verifico que la contraseña sea correcta
      user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
      if user==None:
        #si es incorrecta, le mando el error
        context={
    'titulo':'Iniciar sesión',
    'form':AuthenticationForm,
    'error':'Contraseña incorrecta'
  }
        return render(request, 'iniciarsesion.html',context)
      else:
        #si es correcta, inicio sesion y lo redirecciono a la pagina principal
        login(request,user)
        return redirect('principal')
    else:
      #si no existe, le mando el error
      context={
    'titulo':'Iniciar sesión',
    'form':AuthenticationForm,
    'error':'El usuario no existe'
  }
      return render(request, 'iniciarsesion.html',context)

def registro(request):
  if request.method=='GET':
    context={
    'titulo':'Registrarse',
    'form':UserCreationForm
  }
    return render(request, 'registro.html',context)
  if request.method=='POST':
    veriUser=User.objects.filter(username=request.POST['username'])
    #si el usuario existe, le digo que ya existe
    if veriUser:
      context={
          'titulo':'Registrarse',
          'form':UserCreationForm,
          'error':'El usuario ya existe'
        }
      return render(request, 'registro.html',context)
    #si no existe, procedo a crear el usuario
    else:
      #si las contraseñas no son iguales, le digo que no son iguales
      if not request.POST['password1']==request.POST['password2']:
        context={
          'titulo':'Registrarse',
          'form':UserCreationForm,
          'error':'Las contraseñas no coinciden'
        }
        return render(request, 'registro.html',context)
      #si son iguales, procedo a crear al usuario
      else:
        #con un try controlo si succede algun error
        try:
          user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
          user.save()
          login(request,user)
          return redirect('principal')
        except:
          context={
          'titulo':'Registrarse',
          'form':UserCreationForm,
          'error':'Hubo un error registrando al usuario, vuelve a intentar'
        }
        return render(request, 'registro.html',context)

@login_required
def cerrarsesion(request):
  logout(request)
  return redirect('principal')