
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from estate.users import views as user_views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('real_estate/', include('real_estate.urls')),
    path('register/', user_views.register, name='register'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
