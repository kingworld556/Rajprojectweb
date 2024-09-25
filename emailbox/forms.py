from django import forms

class Emailform(forms.Form):
    subject=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    recipient=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Recipient'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))
    