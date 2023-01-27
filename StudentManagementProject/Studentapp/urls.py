from django.urls import path

from Studentapp import views

urlpatterns=[
    path('reg',views.reg_fun,name='reg'),# it will redirect to register.html page
    path('regdata',views.regdata_fun), #it will create superuser account
    path('',views.log_fun,name='log'), # it will display login.html page
    path('logdata',views.logdata_fun),#it will read the data and verify  # user is supeer user and redirect to homr.html
    path('home',views.home_fun,name='home'),#it will redirect to home.html
    path('add_students',views.addstudent_fun,name='add'),#it will redirect to addstudent.html
    path("readdata",views.readdata_fun),#it will insert records into studenttable
    path('display',views.display_fun,name='dis'),#it will redirect to display html page
    path('update/<int:id>',views.update_fun,name='up'),#it will redirect to update page
    path('delete/<int:id>',views.delete_fun,name='del'),# it will delete the  data
    path('log_out',views.log_out_fun,name='log_out')# it will logout from the user account
]
