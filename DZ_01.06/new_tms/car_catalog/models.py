from datetime import datetime

from django.db import models

class CarBaseModel(models.Model):
    CHOICES = (
        ('US', 'United States'),
        ('FR', 'France'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('SW', 'Sweden'),
    )
    name = models.CharField(max_length=50)
    made_in = models.CharField(max_length=50, choices=CHOICES)
    model_years = models.DateField()

    def year_release(self):
        return self.model_yearsstrftime('%Y')


class CarBrand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    founded = models.DateField(auto_now=False, auto_now_add=False)
    headquaters = models.CharField(max_length=50)
    logo = models.FileField(upload_to='uploads/logo_brand', null=True, blank=True)

    def __str__(self):
        return self.name


class Engine(CarBaseModel):
    FUEL_TYPE = (
        ('El', 'Electric'),
        ('D', 'Diesel'),
        ('GAS', 'Gasoline'),
        ('NG', 'Natural gas'),
        ('H', 'Hybrid'),
    )
    displacement = models.CharField(max_length=5) #Хотел сделать красиво стрелочками с ограничением от 0.8л - 7.3л например, но не придумал как
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE)
    torque = models.CharField(max_length=20) # Тоже хотелось поставить IntegerField, но не придумал как оставить автоматически окончание RPM
    power = models.CharField(max_length=20) #Тоже самое
    fuel_consumption = models.CharField(max_length=20) # Тоже. Хотел сделать чтоб юзер вводил средний расход 7, а в БД записывалось бы как 7л/100км например

    def __str__(self):
        return self.name


class CarModel(CarBaseModel):
    CHOICES_LAYOUT = (
        ('FWD', 'Front-wheel drive'),
        ('RWD', 'Rear-wheel drive'),
        ('4WD', 'Four-wheel drive'),
    )
    CHOICES_BODY_STYLE = (
        ('CAB','Cabriolet'),
        ('COU','Coupe'),
        ('HB','Hatchback'),
        ('S','Sedan'),
        ('SW','Station wagon'),
        ('MVP','Minivan'),
        ('PT','Pickup truck'),
        ('T', 'Truck')
    )
    CHOICES_CLASIFICATION = (
        ('A', 'City car'),
        ('B', 'Supemini'),
        ('C', 'Compact'),
        ('D', 'Mid-size'),
        ('E', 'Executiv'),
        ('F', 'Luxary'),
        ('S', 'Sport'),
        ('M', 'MPV'),
        ('J', 'SUV'),
    )
    brand = models.ForeignKey(CarBrand, related_name='brands', on_delete=models.CASCADE)
    engine = models.ManyToManyField(Engine, related_name='engines')
    layout = models.CharField(max_length=20, choices=CHOICES_LAYOUT)
    body_style = models.CharField(max_length=20, choices=CHOICES_BODY_STYLE)
    clasification = models.CharField(max_length=10, choices=CHOICES_CLASIFICATION)
    photo = models.FileField(upload_to='uploads/photo_models', null=True, blank=True)

    def __str__(self):
        return self.name