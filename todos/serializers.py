from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'priority', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Title is required")
        if len(value) > 120:
            raise serializers.ValidationError("Title must be 120 characters or less")
        return value.strip()

    def validate_description(self, value):
        if value and len(value) > 500:
            raise serializers.ValidationError("Description must be 500 characters or less")
        return value

    def validate_priority(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Priority must be between 1 and 5")
        return value


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority']
        extra_kwargs = {
            'description': {'required': False, 'allow_blank': True},
            'priority': {'required': False, 'default': 3},
        }

    def validate_title(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Title is required")
        if len(value) > 120:
            raise serializers.ValidationError("Title must be 120 characters or less")
        return value.strip()

    def validate_description(self, value):
        if value and len(value) > 500:
            raise serializers.ValidationError("Description must be 500 characters or less")
        return value

    def validate_priority(self, value):
        if value is None:
            return 3
        if value < 1 or value > 5:
            raise serializers.ValidationError("Priority must be between 1 and 5")
        return value
