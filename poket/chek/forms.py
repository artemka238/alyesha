from django import forms
from chek.models import Review 
class Review_form(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name","mail","rating","review"]

    