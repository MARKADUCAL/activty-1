from django.urls import path
from .views import index, dashboard, base_view  # Add base_view

app_name = "portfolio"

urlpatterns = [
    path('', base_view, name='base'),  # Make base.html the main page
    path('portfolio/', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]