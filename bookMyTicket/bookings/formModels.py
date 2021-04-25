from django.forms import ModelForm
from .models import *


class City_Form(ModelForm):
    class Meta:
        model = City
        fields = '__all__'