from django.urls import path

from .views import *

app_name = 'category'

urlpatterns = [

    # LIST

    path('', CategoryListView.as_view(), name = 'categoryList'),

    # CREATE

    path('new/', new_category, name = 'categoryCreate'),

    # DELETE

    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name = 'categoryDelete'),
]