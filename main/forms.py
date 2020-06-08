from django import forms
from .models import bookmarkModel

class bookmarkForm(forms.ModelForm):
    class Meta:
        model = bookmarkModel
        fields = ['site_name','site_url']