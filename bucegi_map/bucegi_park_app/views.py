from django.contrib.gis.db.models.functions import Transform
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import (
    TraseeTuristice, TraseeTematice, CladiriAdministrative,
    InfrastructuraAgrement, ZonarePNBHG2011, ZonarePNBv2025,
    LimitaRONPA006, LimitaROSCI0013OUG2025, AriiNaturaleOUG2016,
    AriiNaturalePropunereAPNB, LimitaAdministrativaJudet,
    LimitaAdministrativaUAT, LimitaN2K2017, LimitaPNBv2016,
    LimitaPNBv2023, LimitaSitN2K2016, LimitaSitN2K2023,
    LimitaSectoarePNB, AriiProtejateRomaniaOUG, ArieNaturalaLege2000,
    LimitaZonarePropusa2024, LimitaAdministrativaRomania,
)
from .serializers import (
    TraseeTuristiceSerializer, TraseeTematiceSerializer,
    CladiriAdministrativeSerializer, InfrastructuraAgrementSerializer,
    ZonarePNBHG2011Serializer, ZonarePNBv2025Serializer,
    LimitaRONPA006Serializer, LimitaROSCI0013OUG2025Serializer,
    AriiNaturaleOUG2016Serializer, AriiNaturalePropunereAPNBSerializer,
    LimitaAdministrativaJudetSerializer, LimitaAdministrativaUATSerializer,
    LimitaN2K2017Serializer, LimitaPNBv2016Serializer, LimitaPNBv2023Serializer,
    LimitaSitN2K2016Serializer, LimitaSitN2K2023Serializer,
    LimitaSectoarePNBSerializer, AriiProtejateRomaniaOUGSerializer,
    ArieNaturalaLege2000Serializer, LimitaZonarePropusa2024Serializer,
    LimitaAdministrativaRomaniaSerializer,
)

WGS84 = 4326


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


# ── infrastructura_vizitare ──────────────────────────────────────────────────

class TraseeTuristiceViewSet(GeoReadOnlyViewSet):
    model = TraseeTuristice
    serializer_class = TraseeTuristiceSerializer
    srid = 0  # undefined in DB — serve as-is (likely already ~WGS84)


class TraseeTematiceViewSet(GeoReadOnlyViewSet):
    model = TraseeTematice
    serializer_class = TraseeTematiceSerializer


class CladiriAdministrativeViewSet(GeoReadOnlyViewSet):
    model = CladiriAdministrative
    serializer_class = CladiriAdministrativeSerializer


class InfrastructuraAgrementViewSet(GeoReadOnlyViewSet):
    model = InfrastructuraAgrement
    serializer_class = InfrastructuraAgrementSerializer


# ── limite ───────────────────────────────────────────────────────────────────

class ZonarePNBHG2011ViewSet(GeoReadOnlyViewSet):
    model = ZonarePNBHG2011
    serializer_class = ZonarePNBHG2011Serializer


class ZonarePNBv2025ViewSet(GeoReadOnlyViewSet):
    model = ZonarePNBv2025
    serializer_class = ZonarePNBv2025Serializer


class LimitaRONPA006ViewSet(GeoReadOnlyViewSet):
    model = LimitaRONPA006
    serializer_class = LimitaRONPA006Serializer


class LimitaROSCI0013OUG2025ViewSet(GeoReadOnlyViewSet):
    model = LimitaROSCI0013OUG2025
    serializer_class = LimitaROSCI0013OUG2025Serializer


class AriiNaturaleOUG2016ViewSet(GeoReadOnlyViewSet):
    model = AriiNaturaleOUG2016
    serializer_class = AriiNaturaleOUG2016Serializer


class AriiNaturalePropunereAPNBViewSet(GeoReadOnlyViewSet):
    model = AriiNaturalePropunereAPNB
    serializer_class = AriiNaturalePropunereAPNBSerializer
    srid = 0


class LimitaAdministrativaJudetViewSet(GeoReadOnlyViewSet):
    model = LimitaAdministrativaJudet
    serializer_class = LimitaAdministrativaJudetSerializer


class LimitaAdministrativaUATViewSet(GeoReadOnlyViewSet):
    model = LimitaAdministrativaUAT
    serializer_class = LimitaAdministrativaUATSerializer
    srid = 0


class LimitaN2K2017ViewSet(GeoReadOnlyViewSet):
    model = LimitaN2K2017
    serializer_class = LimitaN2K2017Serializer


class LimitaPNBv2016ViewSet(GeoReadOnlyViewSet):
    model = LimitaPNBv2016
    serializer_class = LimitaPNBv2016Serializer


class LimitaPNBv2023ViewSet(GeoReadOnlyViewSet):
    model = LimitaPNBv2023
    serializer_class = LimitaPNBv2023Serializer
    srid = 0


class LimitaSitN2K2016ViewSet(GeoReadOnlyViewSet):
    model = LimitaSitN2K2016
    serializer_class = LimitaSitN2K2016Serializer


class LimitaSitN2K2023ViewSet(GeoReadOnlyViewSet):
    model = LimitaSitN2K2023
    serializer_class = LimitaSitN2K2023Serializer
    srid = 0


class LimitaSectoarePNBViewSet(GeoReadOnlyViewSet):
    model = LimitaSectoarePNB
    serializer_class = LimitaSectoarePNBSerializer


class AriiProtejateRomaniaOUGViewSet(GeoReadOnlyViewSet):
    model = AriiProtejateRomaniaOUG
    serializer_class = AriiProtejateRomaniaOUGSerializer


class ArieNaturalaLege2000ViewSet(GeoReadOnlyViewSet):
    model = ArieNaturalaLege2000
    serializer_class = ArieNaturalaLege2000Serializer


class LimitaZonarePropusa2024ViewSet(GeoReadOnlyViewSet):
    model = LimitaZonarePropusa2024
    serializer_class = LimitaZonarePropusa2024Serializer
    srid = 0


class LimitaAdministrativaRomaniaViewSet(GeoReadOnlyViewSet):
    model = LimitaAdministrativaRomania
    serializer_class = LimitaAdministrativaRomaniaSerializer
    srid = 0
