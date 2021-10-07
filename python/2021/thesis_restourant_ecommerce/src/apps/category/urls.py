from django.urls import path

from .views import CategoryListView, CategoryCreateView

app_name = 'category'

urlpatterns = [
    # List

    path('', CategoryListView.as_view(), name = 'categorylist'),

    # Create

    path('create/', CategoryCreateView.as_view(), name = 'categorycreate')
]
