from django.urls import path
from .views import *

urlpatterns = [
    path('', BondsList.as_view(), name='bondslist'),
    path('create', BondCreateAPI.as_view(), name='bondcreate'),
    
]
