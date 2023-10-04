from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import viewsets
from .models import Resources, Category
from . import serializers, mixins


@api_view([ 'GET'])
def list_resources(request):
    queryset = (
        Resources.objects.select_related('user_id','cat_id')
        .prefetch_related('tag')
        .all()
        )
    # response= [
    #     {
    #         "title": query.title,
    #         "link": query.link,
    #         "user": {
    #             "id": query.user_id.id,
    #             "username": query.user_id.username,
    #             },
    #         "category": query.cat_id.cat,
    #         "tags": query.all_tags()
    #     }
    #     for query in queryset
    # ]
    response = serializers.ResourceModelSerializer(queryset,many=True)
    # Transform to JSON before returning
    return Response(response.data)


@api_view(['GET'])
def list_category(response):
    categories = Category.objects.all()
    
    # response=[
    #     {
    #         "id": category.id,
    #         "name": category.cat
    #     }
    #     for category in categories
    # ]
    response = serializers.CategoryModelSerializer(categories, many=True)
    
    # Transform to JSON before returning
    return Response(response.data)


class ListResource(ListAPIView):
    queryset = (
        Resources.objects.select_related('user_id','cat_id')
        .prefetch_related('tag')
        .all()
        )
    serializer_class = serializers.ResourceModelSerializer
    
class ListCategory(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer
    
class DetailResource(RetrieveAPIView):
    lookup_field = "id" # by default. the look_up field is `pk`
    queryset = (
        Resources.objects.select_related('user_id','cat_id')
        .prefetch_related('tag')
        .all()
        )
    serializer_class = serializers.ResourceModelSerializer
    
# ViewSets can permit us to perform the CRUD operations in one class based view.

class ResourceViewSets(mixins.FilterOutAdminResourcesMixin, viewsets.ModelViewSet): # <model-name>ViewSets
    queryset = (
        Resources.objects.select_related('user_id','cat_id')
        .prefetch_related('tag')
        .all()
        )
    serializer_class = serializers.ResourceModelSerializer
    
    
class CategoryViewSets(mixins.DenyDeletionOfDefaultCategoryMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer
    
    
class DeleteCategory(mixins.DenyDeletionOfDefaultCategoryMixin, DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer