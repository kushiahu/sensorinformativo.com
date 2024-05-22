from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

# class LoginForm(forms.Form):

# 	username = forms.CharField(label="Usuario", max_length=100,
# 		widget=forms.TextInput(attrs={'placeholder':'Usuario o email'}))
# 	password = forms.CharField(label="Password", 
# 		widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Contraseña'}))

# 	error_messages = {
# 		'invalid_login': "Favor de ingresar correctamente el usuario y password",
# 		'inactive': "El usuario esta inactivo.",
# 	}

# 	def clean(self):
# 		username = self.cleaned_data.get('username')
# 		password = self.cleaned_data.get('password')
# 		if username and password:
# 			self.user_cache = authenticate(
# 				username=username,
# 				password=password
# 			)
# 			if self.user_cache is None:
# 				raise forms.ValidationError(
# 					self.error_messages['invalid_login'],
# 					code='invalid_login',
# 				)
# 			else:
# 				self.confirm_login_allowed(self.user_cache)

# 		return self.cleaned_data

# 	def confirm_login_allowed(self, user):
# 		if not user.is_active:
# 			raise forms.ValidationError(
# 				self.error_messages['inactive'],
# 				code='inactive',
# 			)