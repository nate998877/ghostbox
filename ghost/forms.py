from ghost.models import BRoast
from django import forms

class Add_BRoast(forms.Form):
    boast_or_roast = forms.ChoiceField(choices = ((True,"Boast"), (False,"Roast")),
                            initial='Boast', widget=forms.Select(), required=True)
    # boast_or_roast = forms.ChoiceField(required=False)
    content        = forms.CharField(widget=forms.Textarea)