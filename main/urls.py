from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('structure/', views.structure, name='structure'),
    path('services/', views.services, name='services'),
    path('news/', views.news, name='news'),
    path('contacts/', views.contacts, name='contacts'),

    # ✅ новые страницы “Подробнее”
    path('services/diagnostics/', views.service_diagnostics, name='service_diagnostics'),
    path('services/molecular/', views.service_molecular, name='service_molecular'),
    path('services/monitoring/', views.service_monitoring, name='service_monitoring'),
    path('services/training/', views.service_training, name='service_training'),

    path('documents/', views.documents, name='documents'),
]
