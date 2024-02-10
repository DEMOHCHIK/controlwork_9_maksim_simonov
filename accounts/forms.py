from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'avatar', 'gender',
            'phone_number',
            'user_information')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('phone_number',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.startswith('+996') or not len(phone_number) == 16:
            raise forms.ValidationError(
                'Неправильный формат номера телефона. Пожалуйста, введите номер в формате: +996 XXX XXX XXX')
        return phone_number
