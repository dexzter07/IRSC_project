from django import forms

class MyModel2(forms.Form):
   color = forms.CharField(widget=forms.Select)