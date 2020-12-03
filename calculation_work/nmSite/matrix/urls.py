from django.urls import path

from . import views

app_name = 'matrix'
urlpatterns = [
    path('', views.get_settings, name='get_settings'),
    path('your_name/', views.get_settings, name='post_settings'),
    # path('count_field/<int:n>/', views.get_name, name='count_field'),
]
