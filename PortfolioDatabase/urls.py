from . import views
from django.urls import path

app_name = 'port_db'
urlpatterns = [
    path('', views.home, name='home'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('hobbies/<int:hobby_id>/', views.hobby_detail, name='hobby_detail'),
    path('portfolio/<int:project_id>/', views.project_detail, name='portfolio_detail')
]