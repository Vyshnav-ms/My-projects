from django.contrib import admin
from .models import Student, Department, Course, Purpose, Material

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Purpose)
admin.site.register(Material)


