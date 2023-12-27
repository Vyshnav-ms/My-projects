# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm
from .models import Course
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def student_form_view(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted')

    return render(request, 'forms.html', {'form': form})


def get_courses(request, department_id):
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)