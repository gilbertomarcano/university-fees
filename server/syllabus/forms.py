from django import forms

class SubjectForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()