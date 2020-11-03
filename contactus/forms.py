from django import forms



class ContactForm(forms.Form):

    name = forms.CharField(max_length=100, required = True ,widget=forms.TextInput(attrs={'pattern':"[A-Za-z' ']+"}))
    email = forms.EmailField(max_length=20)
    phone= forms.CharField(max_length=10,required=False, widget=forms.TextInput(attrs={'pattern': '[0-9]{10}'}))
    description = forms.CharField(max_length=200, min_length=20, required=True, widget= forms.Textarea())
