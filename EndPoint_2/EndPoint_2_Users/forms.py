from django import forms
from models import Userdatabase


class IdForms(forms.ModelForm):
    class Meta:
        model = Userdatabase
        fields = ('id', 'username', 'email', 'profession', 'city', 'state')
