from django import forms
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
                                       AuthenticationForm)
from .models import StreamUser, StreamUserProfile


class StreamUserRegisterForm(UserCreationForm):
    class Meta:
        model = StreamUser
        fields = (
            'username', 'first_name', 'password1',
            'password2', 'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data


class StreamUserEditForm(UserChangeForm):

    class Meta:
        model = StreamUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar',
                  'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
        if field_name == 'password':
            field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("ВЫ слишком молоды!")

        return data


class StreamUserLoginForm(AuthenticationForm):
    class Meta:
        model = StreamUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(StreamUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StreamUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = StreamUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(StreamUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
