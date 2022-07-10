from rest_framework import serializers

from .models import GlobalTask, Objectives


class GlobalTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GlobalTask
        fields = '__all__'


class ObjectivesSerializer(serializers.ModelSerializer):
    # executor = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Objectives
        fields = '__all__'