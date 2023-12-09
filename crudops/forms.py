from django import forms
from .models import Programming

class LanguageForm(forms.ModelForm):

    class Meta:
        model = Programming
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'std_code': 'Registration Code',
            'mobile': 'Telephone No.',
            'language': 'Programming Language',
        }

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        self.fields['language'].empty_label = "Select"
        self.fields['mobile'].required = False