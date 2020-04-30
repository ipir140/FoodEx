from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('user/login',views.userLogin,name='userLogin'),
    path('register-restaurant/',views.registerRestaurant,name='register-restaurant'),
    path('user/dashboard/',views.userDashboard,name='dashboard1'),
    path('user/dashboard/bookings',views.userBookings,name='userbookings'),
    path('user/accountsetting/',views.userAccountSetting,name='userAccountSetting'),
    path('restaurant/<int:pk>/orders',views.restaurantOrders,name='restaurantOrdersboard')
]