from django import forms
from authapp.models import StreamUser
from authapp.forms import StreamUserEditForm
from myapp.models import ListOfCountries
from myapp.models import Accommodation


# Форма редактирования параметров пользователя
class StreamUserAdminEditForm(StreamUserEditForm):
    class Meta:
        model = StreamUser
        fields = '__all__'


# Форма редактирования параметров стран
class ListOfCountriesEditForm(forms.ModelForm):
    class Meta:
        model = ListOfCountries
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''


# Форма редактирования параметров услуг компании
class AccommodationEditForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''