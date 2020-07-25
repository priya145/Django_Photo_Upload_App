from django import forms

from .models import Photo


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ( 'document', )