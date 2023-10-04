from rest_framework import serializers
from . import models
from apps.user.serializers import UserModelSerializer


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cat = serializers.CharField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()
    
class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()

class ResourceSerializer(serializers.Serializer): # <model-name>Serializer
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    link = serializers.URLField()
    # user = UserSerializer()
    cat_id = CategorySerializer()
    tag = TagSerializer(many=True)

class CategoryModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields = (
            "id",
            "cat",
            "created_at",
            "modified_at"
        )

class TagModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tag
        fields = '__all__' # special string to serialize all model's attribute 
        # fields = (
        #     "id",
        #     "name",
        #     "created_at",
        #     "modified_at"
        # )
        # exclude = (
        #     "created_at",
        #     "modified_at"
        # )
   
class ResourceModelSerializer(serializers.ModelSerializer):
    cat_id = CategoryModelSerializer()
    tag = TagModelSerializer(many = True)
    user_id = UserModelSerializer()
    
    class Meta:
        model = models.Resources
        # two options
        # Specify the fields we want our serializer to serialize
        # Omit fields that our serializer shouldn't serialize
        
        # v1 fields we want to serialize
        fields = (
            "id",
            "title",
            "description",
            "link",
            "user_id",
            "cat_id",
            "tag"
        )