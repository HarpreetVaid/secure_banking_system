from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Account

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(label="Username",write_only=True)
    password = serializers.CharField(label="Password",style={'input_type': 'password'},trim_whitespace=False,write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
        
        attrs['user'] = user
        return attrs

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountBalanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance']

    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance