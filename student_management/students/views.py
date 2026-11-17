from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            return render(
                request,
                'students/login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'students/login.html')


# USER LOGOUT
def user_logout(request):
    logout(request)
    return redirect('login')    

# USER REGISTRATION
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('student_list')

    else:

        form = UserCreationForm()

    return render(
        request,
        'students/register.html',
        {'form': form}
    )

# UPDATE STUDENT
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'students/student_update.html',
        {'form': form}
    )


# DELETE STUDENT
def student_delete(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.delete()
        messages.success(request, 'Student deleted successfully!')

        return redirect('student_list')

    return render(
        request,
        'students/student_delete.html',
        {'student': student}
    )
# CREATE STUDENT
def student_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')

    else:

        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )

# READ ALL STUDENTS
def student_list(request):

    students = Student.objects.all().order_by('-id')

    context = {
        'students': students
    }

    return render(
        request,
        'students/student_list.html',
        context
    )

def home(request):

    students = ["Arun", "Bala", "Kumar", "Ravi"]

    context = {
        'students': students,
        'is_available': True
    }

    return render(request, 'students/home.html', context)


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    return render(request, 'students/contact.html')


def services(request):
    return render(request, 'students/services.html')


def student_form(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('student_list')

    else:

        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )

def api_student_page(request):
    return render(
        request,
        'students/student_list.html'
    )