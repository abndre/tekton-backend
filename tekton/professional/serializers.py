from rest_framework import serializers
from .models import Professional


class ProfessionalSerializer(serializers.ModelSerializer):

    class Meta:

        model = Professional
        fields = '__all__'
