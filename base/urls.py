from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocate_list),
    path('add_advocate/', views.advocate_add),
    path('advocates/<str:username>/', views.advocate_details),

]
