from django import forms
from .models import Patient
from django.core.validators import validate_email

class PatientRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'שם פרטי'
        self.fields['last_name'].label = 'שם משפחה'
        self.fields['password'].help_text = "<li>הסיסמה לא יכולה להכיל מידע האישי.</li>" \
                                            "<li>הסיסמה חייבת להכיל לפחות 8 תווים.</li>" \
                                            "<li>הסיסמה חייבת להכיל אותיות ומספרים.</li>"
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['password'].required = True
        self.fields['phone_number'].required = True

    #
    # first_name = forms.CharField(required=True, max_length=255)
    # last_name = forms.CharField(required=True, max_length=255)
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)

    # style the fields

    class Meta:
        model = Patient

        fields = ('first_name', 'last_name', 'email',
                  'password', 'phone_number')

        labels = {
            'first_name': "שם פרטי",
            'last_name': "שם משפחה",
            'email': "אימייל",
            'password': "סיסמא",
            'phone_number': "מספר טלפון",
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }