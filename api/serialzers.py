from rest_framework import serializers
from rest_framework.settings import DEFAULTS
from .models import  CustomUser,Business,Appointments,Feedback,TimeSlots




class BusinessSerializer(serializers.ModelSerializer):
    owner=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Business
        fields = '__all__'
    
    # def update(self, instance, validated_data):
    #     instance.id=validated_data.get('id',instance.id)

    #     return super().update(instance, validated_data)

# class CountrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = ('name','code','phone','symbol','currency')

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class FeedBackSerialzer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Feedback
        fields = '__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Appointments
        fields = '__all__'




class TimeSlotSerialzier(serializers.ModelSerializer):
    # created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = TimeSlots
        fields = '__all__'