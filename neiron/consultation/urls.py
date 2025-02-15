from django.urls import path
from .views import HomeView, ConsultationView, SuccessView

urlpatterns = [
    path('consultation/<slug:slug>/', ConsultationView.as_view(), name='consultation'),
    path('success', SuccessView.as_view(),name='success_page'),

    path('', HomeView.as_view(), name='home'),
]