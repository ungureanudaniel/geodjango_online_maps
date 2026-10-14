import requests
from django.contrib.gis.db.models.functions import Transform
from django.http import HttpResponse
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny

from .models import (
    Peaks, TraseeTuristice, TraseeTematice, CladiriAdministrative,
    InfrastructuraAgrement, ZonarePNBHG2011, ZonarePNBv2025, AriiNaturaleOUG2016,
    AriiNaturalePropunereAPNB, LimitaAdministrativaJudet,
    LimitaAdministrativaUAT, LimitaPNBv2016, LimitaSitN2K2016,
    LimitaSectoarePNB, LimitaAdministrativaRomania,
)
from .serializers import (
    TraseeTuristiceSerializer, TraseeTematiceSerializer,
    CladiriAdministrativeSerializer, InfrastructuraAgrementSerializer,
    ZonarePNBHG2011Serializer, ZonarePNBv2025Serializer,
    AriiNaturaleOUG2016Serializer, AriiNaturalePropunereAPNBSerializer,
    LimitaAdministrativaJudetSerializer, LimitaAdministrativaUATSerializer, LimitaPNBv2016Serializer,
    LimitaSitN2K2016Serializer,
    LimitaSectoarePNBSerializer, PeaksSerializer,
    LimitaAdministrativaRomaniaSerializer,
)

WGS84 = 4326

@method_decorator(cache_page(60 * 15), name='dispatch')
class GeoReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Base viewset: read-only, public, reprojects geom to WGS84 for Leaflet.
    Subclasses must set: model, serializer_class, geom_field (default 'geom'),
    and optionally srid (default 3844 — skip Transform when srid=0).
    """
    permission_classes = [AllowAny]
    geom_field = 'geom'
    srid = 3844

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.srid not in (0, WGS84):
            qs = qs.annotate(geom_3857=Transform(self.geom_field, WGS84))
        return qs


class TraseeTuristiceViewSet(GeoReadOnlyViewSet):
    model = TraseeTuristice
    serializer_class = TraseeTuristiceSerializer
    srid = 0 


class TraseeTematiceViewSet(GeoReadOnlyViewSet):
    model = TraseeTematice
    serializer_class = TraseeTematiceSerializer


class PeaksViewSet(GeoReadOnlyViewSet):
    model = Peaks
    serializer_class = PeaksSerializer


class CladiriAdministrativeViewSet(GeoReadOnlyViewSet):
    model = CladiriAdministrative
    serializer_class = CladiriAdministrativeSerializer


class InfrastructuraAgrementViewSet(GeoReadOnlyViewSet):
    model = InfrastructuraAgrement
    serializer_class = InfrastructuraAgrementSerializer


class ZonarePNBHG2011ViewSet(GeoReadOnlyViewSet):
    model = ZonarePNBHG2011
    serializer_class = ZonarePNBHG2011Serializer


class ZonarePNBv2025ViewSet(GeoReadOnlyViewSet):
    model = ZonarePNBv2025
    serializer_class = ZonarePNBv2025Serializer


class AriiNaturaleOUG2016ViewSet(GeoReadOnlyViewSet):
    model = AriiNaturaleOUG2016
    serializer_class = AriiNaturaleOUG2016Serializer


class AriiNaturalePropunereAPNBViewSet(GeoReadOnlyViewSet):
    model = AriiNaturalePropunereAPNB
    serializer_class = AriiNaturalePropunereAPNBSerializer
    # srid = 0


class LimitaAdministrativaJudetViewSet(GeoReadOnlyViewSet):
    model = LimitaAdministrativaJudet
    serializer_class = LimitaAdministrativaJudetSerializer


class LimitaAdministrativaUATViewSet(GeoReadOnlyViewSet):
    model = LimitaAdministrativaUAT
    serializer_class = LimitaAdministrativaUATSerializer
    srid = 0


class LimitaPNBv2016ViewSet(GeoReadOnlyViewSet):
    model = LimitaPNBv2016
    serializer_class = LimitaPNBv2016Serializer


class LimitaSitN2K2016ViewSet(GeoReadOnlyViewSet):
    model = LimitaSitN2K2016
    serializer_class = LimitaSitN2K2016Serializer


class LimitaSectoarePNBViewSet(GeoReadOnlyViewSet):
    model = LimitaSectoarePNB
    serializer_class = LimitaSectoarePNBSerializer


class LimitaAdministrativaRomaniaViewSet(GeoReadOnlyViewSet):
    model = LimitaAdministrativaRomania
    serializer_class = LimitaAdministrativaRomaniaSerializer
    srid = 0