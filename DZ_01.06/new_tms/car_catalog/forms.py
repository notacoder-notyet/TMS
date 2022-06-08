from django.forms import ModelForm

from .models import CarBaseModel, CarBrand, CarModel, Engine

class CarBrandForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'


class EngineForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'