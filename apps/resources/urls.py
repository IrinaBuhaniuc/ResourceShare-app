from django.urls import path
from rest_framework import routers
#from .views import home_page
from . import views, api_views

router = routers.SimpleRouter()
router.register('api/v3/resource', api_views.ResourceViewSets)
router.register('api/v3/category', api_views.CategoryViewSets)

api_urlpatterns = [
    path('api/v1/resource/', api_views.list_resources, name='list-resources'),
    path('api/v1/category/', api_views.list_category, name='list-category'),
    path('api/v2/resource/', api_views.ListResource.as_view(), name='list-resources-class'),
    path('api/v2/category/', api_views.ListCategory.as_view(), name='list-category-class') ,
    path('api/v2/resource/<int:id>', api_views.DetailResource.as_view(), name='detail-resource'),
    path('api/v2/category/<int:pk>/', api_views.DeleteCategory.as_view(), name='delete-resource-class')
]

urlpatterns = [
    path('', views.home_page, name= 'home-page'),
    path('resources/<int:id>', views.resource_detail, name='resources-detail'),
    path('resources/post/', views.resource_post, name='resource-post'),
    *api_urlpatterns,
    *router.urls,
]