from django.urls import  path
from .views import ( BaseView , AboutView,HomeView)

urlpatterns={
    path('',BaseView.as_view(),name='base'),
    path('about',AboutView.as_view(),name='about'),
    path('home',HomeView.as_view(),name='home')


}