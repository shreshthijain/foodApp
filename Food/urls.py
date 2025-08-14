from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'food'
urlpatterns = [
    path("", views.index, name="index"),  
    path("food/", views.item_list, name="item_list"),  
    path("food/delete/<int:id>", views.delete_item, name="delete_item"),
    path("food/details/<int:id>", views.item_details, name="item_details"),
    path("food/add", views.add_item, name = "add_item"),
    path("food/update/<int:id>/", views.update_item, name = "update_item" )
]
