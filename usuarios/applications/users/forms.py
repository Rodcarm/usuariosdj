from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=forms.PasswordInput,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name',
            'gender'
        )

    def clean_password2(self):

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        
        if password1 != password2:

            self.add_error('password2','No coincide')

        elif len(password1) < 8:

            self.add_error('password1','Contraseña muy corta')

class LoginForm(forms.Form):

    username = forms.CharField(
        label='usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'usuario'
            }
        )
    )

    password = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña'
            }
        )
    )