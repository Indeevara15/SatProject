from django.urls import path

from SatApp import views

urlpatterns = [
    path('',views.insert_fun),
    path('insertdata',views.insertdata_fun,name='insertdata'),
    path('viewdata',views.viewdata_fun,name='viewdata'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('del/<int:id>',views.del_fun,name='del')
]