from rest_framework import serializers
from customapiapp.models import train

class trainserializer(serializers.ModelSerializer):
    class Meta:
        model =train
        fields ='__all__'