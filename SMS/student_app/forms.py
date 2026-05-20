from django import forms
from .models import Student

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

course_choices = [
    ('PYTHON', 'PYTHON'),
    ('JAVASCRIPT', 'JAVASCRIPT'),
    ('JAVA', 'JAVA'),
    ('C_PLUS_PLUS', 'C++'),
    ('TYPESCRIPT', 'TYPESCRIPT')
]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'stu_id':forms.NumberInput(attrs={
                'placeholder':'E.g.,101'
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Joe'
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Biden'
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'course_purchase':forms.Select(choices=course_choices),
            'mobile_no':forms.TextInput(attrs={
                'placeholder':'+91 XXXXX XXXXX'
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com'
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password'
            })
        }