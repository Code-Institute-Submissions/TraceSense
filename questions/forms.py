from django import forms
from .models import Gmp_questions

class GMPQuestions(forms.ModelForm):
    class Meta:
        model = Gmp_questions
        fields = ('question',) 
        
        widgets = {
            'question': forms.TextInput(attrs={"class": "form-control"})
        }
            

        