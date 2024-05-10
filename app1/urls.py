from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.login_page,name='login'),
    path('reg/',views.register_page,name='register'),

]