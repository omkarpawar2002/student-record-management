from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("User Created Successfully")
        return HttpResponse("Error While Creating User!!")
    template_name = 'student_auth_app/sign_up.html'
    context = {'form':form}
    return render(request,template_name,context)


def sign_in(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('Show_Student')
        return HttpResponse("Sign In Failed!!")
    template_name = 'student_auth_app/sign_in.html'
    context = {}
    return render(request,template_name,context)

def sign_out(request):
    logout(request)
    return redirect('Sign_In')