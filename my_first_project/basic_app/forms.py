from django import forms

from django.core import validators

from basic_app.models import UserProfileInfo

from django.contrib.auth.models import User


def check_for_z(inp_value):
    if inp_value[0].lower() !='z':
        raise forms.ValidationError("Name NEEDS TO START WITH Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField(label='Enter your email here')
    ver_email = forms.EmailField(label='Enter your Email one more time')
    text =  forms.CharField(widget=forms.Textarea)

    BotCatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    # BotCatcher is a hidden tag which is to catch a Bot which is tryring to jam your browser
    # by putting in false data.
    # this field will not be visble to normal user hence MaxLengthValidator will be 0
    # but Bot operated not with html page, but the inspect mode and set a "value" tag there
    #here, it will be trapped since the length value shall be 0 but bot is assigning this value something and hence it will be trapped

    def clean(self):
        all_data_in_clean = super().clean()
        Email = all_data_in_clean['email']
        VEmail = all_data_in_clean['ver_email']

        if Email !=VEmail:
            raise forms.ValidationError('Make sure your emails match')
        else:
            print(Email)
            print(VEmail)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','profile_pic')
