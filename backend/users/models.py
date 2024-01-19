from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    username = None         # uses none due to login wanting to be handled by email not username

    USERNAME_FIELD = 'name' 
    REQUIRED_FIELDS = [name, password]
    
from rest_framework import serializers
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'name','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # set everything but password
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance