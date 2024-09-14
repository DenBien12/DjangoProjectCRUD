from django.urls import path
from . import views

urlpatterns =[
   path('', views.recipes),
   path('update_receipe/<id>', views.update_recipe, name='update_recipe'),
   path('delete_receipe/<id>', views.delete_recipe, name='delete_recipe'),
]