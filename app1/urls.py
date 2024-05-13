from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.login_page,name='login'),
    path('reg/',views.register_page,name='register'),
    path('main/',views.main_page,name='main'),
    path('logout/',views.login_page,name='logout'),
    path('task/<int:task_id>',views.tsak_page,name='task'),
    path('add/',views.add_page,name='add'),
    path('modify/<int:task_id>',views.modify_page,name='modify')

]