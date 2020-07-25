from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from user import views as user_views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('', user_views.home ,name="home"),
    path('signup_view/', user_views.signup_view , name="signup"),
    path('user_login/', user_views.user_login, name='login'),
    
    path('signup_view/activation_sent.html', user_views.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', user_views.activate, name='activate'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        user_views.activate, name='activate'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'
         ),
         name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('base_layout/', user_views.base_layout, name='base_layout'),

    
]