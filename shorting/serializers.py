from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Link
from .utils import custom_url_validator


class FormSerializer(serializers.ModelSerializer):
    def validate_url(self, url):
        if not custom_url_validator(url):
            raise ValidationError('Please provide valid URL adress!')
        return url

    class Meta:
        model = Link
        fields = ['url', 'short_url']