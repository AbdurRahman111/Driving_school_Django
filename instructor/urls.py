
from django.urls import path
from . import views
urlpatterns = [
    path('login-instructor', views.login_func_instructor, name='login_func_instructor'),
    path('home-instructor', views.home_instructor, name='home_instructor'),
    path('my_lessons', views.my_lessons, name='my_lessons'),
    path('instructor_profile', views.instructor_profile, name='instructor_profile'),
    path('order_details/<int:pk>', views.order_details, name='order_details'),
    path('cancel_order', views.make_cancel_order, name='make_cancel_order'),

]
