from django import forms 
class Review_form(forms.Form):
    name = forms.CharField(max_length=25)
    mail = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=10)
    review = forms.CharField(widget=forms.Textarea)
    