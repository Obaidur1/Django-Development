from django.forms import ModelForm
from .models import Property, PropertyImages


class AddPropertyForm(ModelForm):
    model = ModelForm
    fields = "__all__"
