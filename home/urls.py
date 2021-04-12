
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'), # home
    path('all_lessons', views.all_lessons, name='all_lessons'), # all lesson
    path('product_search', views.product_search, name='product_search'), # for searching products
    path('profile', views.profile, name='profile'), # user profile
    path('edit_profile', views.edit_profile, name='edit_profile'),# user profile edit
    path('login-signup', views.signup_login, name='signup_login'), # user signup
    path('login', views.login_func, name='login_func'), # user login
    path('logout_func', views.logout_func, name='logout_func'), # user logout
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'), # product details

    # activation email
    path('email/confirmation/<str:activation_key>/', views.email_confirm, name='email_activation' ), #sending activation email

]
