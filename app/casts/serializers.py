"""
Serializers for the casts app
"""
from casts.models import (
    Cast,
    Award,
    AwardReceived
)
from rest_framework import serializers


class AwardSerializer(serializers.ModelSerializer):
    """
    Serializer for the Award Model
    """
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Award
        exclude = ["date_added", "date_modified"]
        read_only_field = ["id"]


class CastSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cast model.
    """
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Cast
        exclude = ["date_added", "date_modified"]
        read_only_fields = ["id", "movies"]

    def to_presentation(self, instance):
        """
        Override the to_representation method to include
        detailed awards info during GET requests.
        """
        return_value = super().to_representation(instance)
        return_value['awards'] = AwardSerializer(
            instance.awards, many=True).data
        return return_value


class CastUpdateSerializer(CastSerializer):
    awards = serializers.PrimaryKeyRelatedField(
        queryset=Award.objects.all(),
        many=True, required=False
    )

    class Meta:
        model = Cast
        exclude = ["date_added", "date_modified"]
        read_only_fields = ["id"]


class MinimalCastSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cast model.
    """
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Cast
        fields = ["id", "name", "url"]


class AwardReceivedSerializer(serializers.ModelSerializer):
    """
    Serializer for the AwardReceived Model
    """
    url = serializers.CharField(source="get_absolute_url", read_only=True)
    recipient = serializers.PrimaryKeyRelatedField(
        queryset=Cast.objects.all(),
        required=True
    )
    award = serializers.PrimaryKeyRelatedField(
        queryset=Award.objects.all(),
        required=True
    )

    def to_representation(self, instance):
        """
        Override the to_representation method to include
        detailed recipient and award info during GET requests.
        """
        return_value = super().to_representation(instance)
        return_value['recipient'] = MinimalCastSerializer(
            instance.recipient).data
        return_value['award'] = AwardSerializer(
            instance.award).data
        return return_value

    class Meta:
        model = AwardReceived
        exclude = ["date_added", "date_modified"]
