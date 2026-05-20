from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='Sign_In')
def add_student(request):
    form = StudentForm()
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
        return HttpResponse("Something Went Wrong While Creating New Student!!")
    template_name = 'student_app/add_student.html'
    context = {'form':form}
    return render(request,template_name,context)


@login_required(login_url='Sign_In')
def show_student(request):
    objs = Student.objects.all()
    template_name = 'student_app/show_student.html'
    context = {'objs':objs}
    return render(request,template_name,context)


def update_student(request,pk):
    obj = Student.objects.get(stu_id = pk)
    form = StudentForm(instance=obj)
    if(request.method == 'POST'):
        form = StudentForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
        return HttpResponse("Something Went Wrong While Updating Student Details!!")
    template_name = 'student_app/update_student.html'
    context = {'form':form}
    return render(request,template_name,context)


def delete_student(request,pk):
    obj = Student.objects.get(stu_id = pk)
    if(request.method == 'POST'):
        obj.delete()
        return redirect('Show_Student')
    template_name = 'student_app/delete_student.html'
    context = {'obj':obj}
    return render(request,template_name,context)
