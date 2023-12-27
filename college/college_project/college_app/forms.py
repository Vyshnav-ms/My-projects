# forms.py

from django import forms
from .models import Student, Department, Course, Material, Purpose

class StudentForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.none())  # Initialize as an empty queryset

    purpose = forms.ModelChoiceField(queryset=Purpose.objects.all())
    materials_provide = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()  # Ensure course field starts with an empty queryset

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
