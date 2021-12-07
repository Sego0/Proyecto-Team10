from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, get_user_model

user = get_user_model()

class UsuarioLoginFormulario(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean (self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user= authenticate(username=username, password= password)
			if not user:
				raise forms.ValidationError("Este usuario no existe")
			if not user.check_password(password):
				raise forms.ValidationError("Esta contraseña es incorrecta")
			if not user.is_active:
				raise forms.ValidationError("Este usuario no está activo")
		
		return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)

class RegistroFormulario(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta:
		model = user

		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2'

		]