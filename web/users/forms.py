from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile, Test

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','email',
                'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
    
        #fast way to do it
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'gender', 'age', 'phone',
                'addressLine1', 'addressLine2', 'pin']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
    
        #fast way to do it
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class TestForm(ModelForm):
    
    class Meta:
        model = Test
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
    
        #fast way to do it
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})