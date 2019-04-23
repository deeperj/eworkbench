from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'certificationvalidity', api.CertificationValidityViewSet)
router.register(r'programperformance', api.ProgramPerformanceViewSet)
router.register(r'weather', api.WeatherViewSet)
router.register(r'agrodocument', api.AgroDocumentViewSet)
router.register(r'farm', api.FarmViewSet)
router.register(r'certificate', api.CertificateViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for CertificationValidity
    path('agro_app/certificationvalidity/', views.CertificationValidityListView.as_view(), name='agro_app_certificationvalidity_list'),
    path('agro_app/certificationvalidity/create/', views.CertificationValidityCreateView.as_view(), name='agro_app_certificationvalidity_create'),
    path('agro_app/certificationvalidity/detail/<int:pk>/', views.CertificationValidityDetailView.as_view(), name='agro_app_certificationvalidity_detail'),
    path('agro_app/certificationvalidity/update/<int:pk>/', views.CertificationValidityUpdateView.as_view(), name='agro_app_certificationvalidity_update'),
)

urlpatterns += (
    # urls for ProgramPerformance
    path('agro_app/programperformance/', views.ProgramPerformanceListView.as_view(), name='agro_app_programperformance_list'),
    path('agro_app/programperformance/create/', views.ProgramPerformanceCreateView.as_view(), name='agro_app_programperformance_create'),
    path('agro_app/programperformance/detail/<int:pk>/', views.ProgramPerformanceDetailView.as_view(), name='agro_app_programperformance_detail'),
    path('agro_app/programperformance/update/<int:pk>/', views.ProgramPerformanceUpdateView.as_view(), name='agro_app_programperformance_update'),
)

urlpatterns += (
    # urls for Weather
    path('agro_app/weather/', views.WeatherListView.as_view(), name='agro_app_weather_list'),
    path('agro_app/weather/create/', views.WeatherCreateView.as_view(), name='agro_app_weather_create'),
    path('agro_app/weather/detail/<int:pk>/', views.WeatherDetailView.as_view(), name='agro_app_weather_detail'),
    path('agro_app/weather/update/<int:pk>/', views.WeatherUpdateView.as_view(), name='agro_app_weather_update'),
)

urlpatterns += (
    # urls for AgroDocument
    path('agro_app/agrodocument/', views.AgroDocumentListView.as_view(), name='agro_app_agrodocument_list'),
    path('agro_app/agrodocument/create/', views.AgroDocumentCreateView.as_view(), name='agro_app_agrodocument_create'),
    path('agro_app/agrodocument/detail/<int:pk>/', views.AgroDocumentDetailView.as_view(), name='agro_app_agrodocument_detail'),
    path('agro_app/agrodocument/update/<int:pk>/', views.AgroDocumentUpdateView.as_view(), name='agro_app_agrodocument_update'),
)

urlpatterns += (
    # urls for Farm
    path('agro_app/farm/', views.FarmListView.as_view(), name='agro_app_farm_list'),
    path('agro_app/farm/create/', views.FarmCreateView.as_view(), name='agro_app_farm_create'),
    path('agro_app/farm/detail/<int:pk>/', views.FarmDetailView.as_view(), name='agro_app_farm_detail'),
    path('agro_app/farm/update/<int:pk>/', views.FarmUpdateView.as_view(), name='agro_app_farm_update'),
)

urlpatterns += (
    # urls for Certificate
    path('agro_app/certificate/', views.CertificateListView.as_view(), name='agro_app_certificate_list'),
    path('agro_app/certificate/create/', views.CertificateCreateView.as_view(), name='agro_app_certificate_create'),
    path('agro_app/certificate/detail/<slug:slug>/', views.CertificateDetailView.as_view(), name='agro_app_certificate_detail'),
    path('agro_app/certificate/update/<slug:slug>/', views.CertificateUpdateView.as_view(), name='agro_app_certificate_update'),
)

