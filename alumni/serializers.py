from rest_framework import serializers
from alumni.models import Alumni, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'number', 'country']


class AlumniSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses')
        alumni = Alumni.objects.create(**validated_data)

        for address_data in addresses_data:
            address = Address.objects.create(alumni=alumni, **address_data)
            alumni.addresses.add(address)
        return alumni

    class Meta:
        model = Alumni
        fields = ['name', 'addresses']