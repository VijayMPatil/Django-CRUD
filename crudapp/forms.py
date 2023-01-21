from .models import Employee,position
from django import forms

class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('full_name','mobile','emp_code','position')
        labels = {
            'full_name':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeRegisterForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False    
