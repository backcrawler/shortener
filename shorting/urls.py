from django.urls import path
from shorting import views

app_name = 'shorting'

urlpatterns = [
    path('', views.AjaxHomeView.as_view(), name='mainpage'),
    path('<str:shortcode>/', views.redirect_view, name='redirect_view'),
]