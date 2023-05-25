from django import forms
from .models import nudge_model

class nudge_form(forms.ModelForm):
    class Meta:
        model = nudge_model
        fields = ['name', 'image', 'tagline', 'schedule', 'description', 'moderator', 'category', 'sub_category', 'rigor_rank']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),  # Restrict file selection to images
        }
