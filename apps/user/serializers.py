from rest_framework import serializers
from .models import User

class UserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        # fields = ('id', 
        #           'username', 
        #           'email', 
        #           'title', 
        #           'first_name', 
        #           'last_name'
        #           )
        # extra_kwargs = {'password': {'write_only': True}}
        # read_only_fields = ['id']
        
        
class UserUpdateModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ('id', 
                  'username', 
        )