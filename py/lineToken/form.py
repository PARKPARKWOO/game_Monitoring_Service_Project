from django import forms
from .models import LineToken

class line_update(forms.ModelForm):
    class Meta:
        model = LineToken
        fields = ["line_token", "photo_input", "want_message"]