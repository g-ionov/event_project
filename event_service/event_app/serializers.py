from rest_framework import serializers

from event_app.models import Organization, Event, User


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for creating organization"""
    class Meta:
        model = Organization
        fields = ('title', 'description', 'address', 'postcode')


class SimpleUserSerializer(serializers.ModelSerializer):
    """Simple serializer for user (only email)"""
    class Meta:
        model = User
        fields = ('email',)


class OrganizationDetailSerializer(serializers.ModelSerializer):
    """Serializer for organization detail"""
    users = SimpleUserSerializer(many=True, read_only=True)
    full_address = serializers.SerializerMethodField()
    class Meta:
        model = Organization
        fields = ('title', 'description', 'full_address', 'users')

    @staticmethod
    def get_full_address(obj):
        return f'{obj.address}, {obj.postcode}'

class SimpleOrganizationSerializer(serializers.ModelSerializer):
    """Simple serializer for event (only title)"""
    class Meta:
        model = Event
        fields = ('title',)


class EventSerializer(serializers.ModelSerializer):
    """Serializer for creating event"""
    organizations = SimpleOrganizationSerializer(many=True, read_only=True, source='organization')
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'image', 'organizations')


class EventCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating event"""
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'image', 'organization')


class EventDetailSerializer(serializers.ModelSerializer):
    """Serializer for event detail"""
    organizations = OrganizationDetailSerializer(many=True, read_only=True, source='organization')
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'image', 'organizations')