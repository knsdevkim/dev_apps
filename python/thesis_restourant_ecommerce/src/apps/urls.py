from django.urls import path, include

app_name = 'apps'

urlpatterns = [
    path('category/', include('apps.category.urls', namespace='category')),
    path('product/', include('apps.product.urls', namespace='product')),
    path('media/', include('apps.media.urls', namespace='media')),
]
