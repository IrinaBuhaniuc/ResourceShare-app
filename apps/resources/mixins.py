from rest_framework.exceptions import PermissionDenied


DEFAULT_CATEGORY_ID = 1


# <idea>Mixin
class DenyDeletionOfDefaultCategoryMixin():
    # We want to get the category's id we are abut to delete
    # We want to compare it with the DEFAULT_CATEGORY_ID
    # If True, we want raise an exception
    
    # This is the method use for Listing
    def get_queryset(self):
        queryset = super().get_queryset()
        if ( not hasattr(self, "action") or self.action == 'destroy'):
            pk = self.kwargs['pk']
            deleted_queryset = queryset.get(pk=pk)
            if deleted_queryset.pk == DEFAULT_CATEGORY_ID:
                # raise an exception
                raise PermissionDenied(f'Not allowed to delete category with id {pk}')
        
        # never forget to return queryset
        return queryset
    
    # def get_object(self) # is expected to return a single object
    
class FilterOutAdminResourcesMixin():
    
    def get_queryset(self):
        queryset = super().get_queryset().exclude(user_id__is_superuser__exact=True)
        # breakpoint()
        # if ( not hasattr(self, "action") or self.action == 'list'):
        #     pk = self.kwargs['pk']
        #     listed_queryset = queryset.get(pk=pk)
        #     if deleted_queryset.pk == DEFAULT_CATEGORY_ID:
        #         # raise an exception
        #         raise PermissionDenied(f'Not allowed to delete category with id {pk}')
        
        # never forget to return queryset
        return queryset       

    
            