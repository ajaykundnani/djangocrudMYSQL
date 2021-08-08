from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='adding'),
    path('edit/<int:id>/',views.edit,name='editing'),
    path('delete/<int:id>/',views.delete,name='deleting')
   
 ]