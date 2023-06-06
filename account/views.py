from django.shortcuts import render,redirect
from account.models import AccountModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.http import Http404

def check_password(password):
    if len(password)>=8:
        return True
    return False
 
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            if not check_password(password):
                messages.info(request,"Password must be at least 8 symbols")
            else:
                    User.objects.create_user(
                        username=username,
                        password=password,
                    )
        else:
            messages.info(request,"Username has been taken")

    return render(request,'signup.html')
#----------------------------------------------------------------------------
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username,password=password)
        if User is not None:
            login(request,user)
            messages.success(request,"You logged in")
            return redirect("home")
        else :
            if not User.objects.filter(username=username).exists():
                messages.info(request, "Please, enter correct username")
            else:
                messages.info(request,"Please, enter correct password")

    return render(request,'login.html')
#--------------------------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect("login")
#----------------------------------------------------------------------------
def changepassword(request):
    if request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        username = request.POST.get("username")
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")

        user = User.objects.get(username=username)

        if newpassword1 == newpassword2:
            user.set_password(newpassword1)
            user.save()
            messages.success(request,"Password changed")
            return redirect("login")
    return render(request,'changepassword.html')
#-----------------------------------------------------------------
def settings(request):
    if not request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")

        if firstname:
            request.user.first_name = firstname 
            request.user.save()
        if lastname:
            request.user.last_name = lastname
            request.user.save()
        if username:
            request.user.username = username
            request.user.save()
        if oldpassword and newpassword:
            request.user.password = newpassword
            request.user.set_password(newpassword)
            request.user.save()
                
    return render(request,'settings.html')



