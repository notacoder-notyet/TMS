from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import CarBrandForm, CarModelForm, EngineForm
from .models import CarModel

class IndexView(ListView):
    model = CarModel
    template_name = 'car_catalog/index.html'


class CarBrandView(FormView):
    template_name = 'car_catalog/brand_form.html'
    form_class = CarBrandForm
    success_url = '/'


class CarModelView(FormView):
    template_name = 'car_catalog/model_form.html'
    form_class = CarModelForm
    success_url = '/'


class EngineView(FormView):
    template_name = 'car_catalog/engine_form.html'
    form_class = EngineForm
    success_url = '/'