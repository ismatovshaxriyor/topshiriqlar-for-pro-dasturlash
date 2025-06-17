from django.urls import path
from .views import main, customers_list

urlpatterns = [
    path('signup/', main, name="register"),
    path('list/', customers_list, name="customers-list")
]

