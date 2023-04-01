from rest_framework import serializers
from .models import Box
from user.serializers import UserSerializer
from rest_framework.exceptions import ValidationError

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Box   
        fields=('id','length','breadth','height','area','volume','created_on','updated_on')
        read_only_fields = ['id','area','volume','created_on','updated_on']

    def create(self, validated_data):
        try:
            box = Box.objects.create(
                length=validated_data.get('length', ''),
                breadth=validated_data.get('breadth', ''),
                height=validated_data.get('height', ''),
                creator=self.context['user']
            )
            return box
        
        except ValidationError as e:
            raise serializers.ValidationError(e)
        
    def to_representation(self, instance):
        rep= super().to_representation(instance)
        rep['creator']=UserSerializer(instance.creator).data
        return rep