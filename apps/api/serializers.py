from rest_framework import serializers
from django.contrib.auth.models import User
from apps.client.models import Clients
from apps.product.models import Products
from apps.bill.models import Bills
#Comvertir de Json a información en python. 
#Sería el model.py de la api 


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id','document', 'first_name', 'last_name', 'email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'description','attribute1','attribute2','attribute3','attribute4']

class ProductBills(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ['id', 'name', 'client_id','company_name','nit','code','product']

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('email')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len( users ) != 0:
            raise serializers.ValidationError("Usuario existente, ingrese uno diferente")
        else:
            return data

            