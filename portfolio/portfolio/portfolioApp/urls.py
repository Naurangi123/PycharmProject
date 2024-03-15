from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout,name='logout'),
    path('project',views.project,name='project'),
    path('project_detail/<int:pk>', views.project_detail, name='project_detail'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('add_record/',views.add_record,name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),


]
