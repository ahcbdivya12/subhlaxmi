from django.urls import path

from service import views as service_views

urlpatterns = [
    
    path('',service_views.signin ),
    path('form',service_views.form ),
    path('table',service_views.table ),
    path('home',service_views.service_index ),

    path('book',service_views.service_book ),

    path('logout',service_views.LogoutPage),

    path('service_inquiry',service_views.service_inquiry ),

 path('service_invoice/<int:column_id>/',service_views.service_invoice),
    

    path('admin_users',service_views.admin_users),

]