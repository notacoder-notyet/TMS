from django.forms import ModelForm

from .models import CarBrand, CarModel, Engine


class CarBrandForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelForm(ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class EngineForm(ModelForm):
    class Meta:
        model = Engine
        fields = '__all__'