from django import forms
from .models import TASK

# Define a form class named 'new_form' that inherits from 'forms.ModelForm'
class new_form(forms.ModelForm):
    # Define the form's properties and behavior within the 'Meta' class
    class Meta:
        # Specify the model associated with the form
        model = TASK
        
        # Define the fields from the model that should be included in the form
        fields = ['title', 'description']

        # Define widgets to customize the HTML rendering of form fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
        }
