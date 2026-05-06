from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
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


class TraseeTuristiceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TraseeTuristice
        geo_field = 'geom'
        fields = ['id', 'denumire_t', 'cod', 'judet', 'shape_leng']


class TraseeTematiceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TraseeTematice
        geo_field = 'geom'
        fields = ['id', 'denumire_t', 'judet', 'timp', 'distanta_m', 'dificultat', 'distanta']


class CladiriAdministrativeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CladiriAdministrative
        geo_field = 'geom'
        fields = ['id', 'nume', 'activa', 'tip_constr', 'address', 'phone', 'name']


class InfrastructuraAgrementSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = InfrastructuraAgrement
        geo_field = 'geom'
        fields = ['id']


class ZonarePNBHG2011Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = ZonarePNBHG2011
        geo_field = 'geom'
        fields = ['id', 'denumire', 'zonare_int', 'shape_area']


class ZonarePNBv2025Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = ZonarePNBv2025
        geo_field = 'geom_3857'
        fields = ['id', 'zonare_int', 'area_ha', 'notes']


class LimitaRONPA006Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = LimitaRONPA006
        geo_field = 'geom'
        fields = ['id', 'localid', 'characters', 'text', 'arie', 'tip_anp']


class SimpleGeomSerializer(GeoFeatureModelSerializer):
    """Reusable serializer for geometry-only models (no rich attributes)."""
    class Meta:
        geo_field = 'geom'
        fields = ['id']


class LimitaROSCI0013OUG2025Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaROSCI0013OUG2025


class AriiNaturaleOUG2016Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = AriiNaturaleOUG2016


class AriiNaturalePropunereAPNBSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = AriiNaturalePropunereAPNB


class LimitaAdministrativaJudetSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaAdministrativaJudet


class LimitaAdministrativaUATSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaAdministrativaUAT


class LimitaN2K2017Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaN2K2017


class LimitaPNBv2016Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaPNBv2016


class LimitaPNBv2023Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaPNBv2023


class LimitaSitN2K2016Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaSitN2K2016


class LimitaSitN2K2023Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaSitN2K2023


class LimitaSectoarePNBSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaSectoarePNB


class AriiProtejateRomaniaOUGSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = AriiProtejateRomaniaOUG


class ArieNaturalaLege2000Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = ArieNaturalaLege2000


class LimitaZonarePropusa2024Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaZonarePropusa2024


class LimitaAdministrativaRomaniaSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaAdministrativaRomania
