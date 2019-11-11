from ghost.models import BRoast
from django import forms

class AddBRoast(forms.Form):
    boast_or_roast = forms.BooleanField
    content        = forms.CharField(widget=forms.Textarea)