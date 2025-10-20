from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        required=True
    )
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        
        if username and User.objects.filter(username=username).exists():
            self.add_error('username', "This username is already taken.")
            
        if email and User.objects.filter(email=email).exists():
            self.add_error('email', "This email has already been used.")
            
        return cleaned_data
        
        
        
        
#option way yto make the fields required
'''
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','password1','password2']
        
    def __init__(self, *args,**kwargs):
        super(RegistrationForm, self).__init__(*args,**kwargs)
        for field in self.fields.value():
            field.required = True
'''