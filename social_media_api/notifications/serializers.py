from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    target = serializers.SerializerMethodField()
    
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'read']
        read_only_fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp']
    
    def get_target(self, obj):
        if obj.target:
            return str(obj.target)
        return None