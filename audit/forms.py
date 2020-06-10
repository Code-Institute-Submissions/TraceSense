from django import forms
from .models import gmp_questions, areas

class GMPQuestions(forms.ModelForm):
    class Meta:
        model = gmp_questions
        fields = ('question',) 
        
            
class AreaForm(forms.ModelForm):
    class Meta:
        model = areas
        fields = ('code','name',)
        