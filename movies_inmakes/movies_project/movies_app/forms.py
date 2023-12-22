from django import forms
from .models import Movie  # Import your Movie model

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'img']  # List the fields you want in the form
