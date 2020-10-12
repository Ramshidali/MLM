from django.urls import path
from . import views

app_name = 'mlmm'

urlpatterns = [
    path ('',views.index,name='index'),
    path ('login/',views.index,name='index'),
    path ('registration_page/',views.register_page,name='register_page'),
    path ('register/',views.register,name='register'),
    path ('signin/',views.signin,name='signin')
]