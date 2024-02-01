from django.urls import path
from . import views
app_name='flowerapp'


urlpatterns = [

    path('',views.index,name='index'),
    path('flower/<int:flower_id>/',views.detail,name='detail'),
    path('add/',views.add_flower,name='add_flower'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]
