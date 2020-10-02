from django.forms import ModelForm
from detail.models import UserDetails

class UserModelForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['title', 'notes', 'gender']
