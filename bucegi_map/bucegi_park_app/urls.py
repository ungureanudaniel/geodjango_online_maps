from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# infrastructura_vizitare
router.register(r'trasee-turistice',        views.TraseeTuristiceViewSet,          basename='trasee-turistice')
router.register(r'trasee-tematice',         views.TraseeTematiceViewSet,           basename='trasee-tematice')
router.register(r'cladiri-administrative',  views.CladiriAdministrativeViewSet,    basename='cladiri-administrative')
router.register(r'infrastructura-agrement', views.InfrastructuraAgrementViewSet,   basename='infrastructura-agrement')

# limite
router.register(r'zonare-hg2011',           views.ZonarePNBHG2011ViewSet,          basename='zonare-hg2011')
router.register(r'zonare-v2025',            views.ZonarePNBv2025ViewSet,           basename='zonare-v2025')
router.register(r'arii-naturale-oug2016',   views.AriiNaturaleOUG2016ViewSet,      basename='arii-naturale-oug2016')
router.register(r'arii-naturale-apnb',      views.AriiNaturalePropunereAPNBViewSet,basename='arii-naturale-apnb')
router.register(r'limita-judet',            views.LimitaAdministrativaJudetViewSet,basename='limita-judet')
router.register(r'limita-uat',              views.LimitaAdministrativaUATViewSet,  basename='limita-uat')
router.register(r'limita-pnb-v2016',        views.LimitaPNBv2016ViewSet,           basename='limita-pnb-v2016')
router.register(r'limita-sit-n2k-2016',     views.LimitaSitN2K2016ViewSet,         basename='limita-sit-n2k-2016')
router.register(r'limita-sectoare',         views.LimitaSectoarePNBViewSet,        basename='limita-sectoare')
router.register(r'limita-administrativa-ro',views.LimitaAdministrativaRomaniaViewSet, basename='limita-administrativa-ro')

urlpatterns = [
    path('api/', include(router.urls)),

]
