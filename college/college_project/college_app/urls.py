from django.urls import path
from . import views

app_name = 'college_app'

urlpatterns = [

    path('',views.home,name='home'),
    path('studentform/', views.student_form_view, name='student_form_view'),
    path('get_courses/<int:department_id>/', views.get_courses, name='get_courses'),
    # ... other URL patterns ...
]