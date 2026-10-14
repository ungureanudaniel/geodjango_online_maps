import json
from django.contrib.gis.geos import GEOSGeometry
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import (
    TraseeTuristice, LimitaSectoarePNB, TraseeTematice, CladiriAdministrative,
    InfrastructuraAgrement, ZonarePNBHG2011, ZonarePNBv2025, AriiNaturaleOUG2016,
    AriiNaturalePropunereAPNB, Peaks, LimitaAdministrativaJudet,
    LimitaAdministrativaUAT, LimitaPNBv2016, LimitaSitN2K2016, LimitaAdministrativaRomania,
)


class WGS84GeoFeatureSerializer(GeoFeatureModelSerializer):
    """
    GeoFeatureModelSerializer that emits proper GeoJSON dicts in SRID 4326,
    regardless of the source geometry's SRID or the drf-gis version quirks.

    - Converts WKT strings to GeoJSON nested objects
    - Reprojects any non-4326 geometry to 4326
    """
    # Override to_representation to handle WKT strings and reprojection
    def to_representation(self, instance):
        data = super().to_representation(instance) # Get the default representation
        geom = data.get('geometry') # Get the geometry field from the representation

        if isinstance(geom, str):
            try:
                g = GEOSGeometry(geom)
                if g.srid and g.srid != 4326:
                    g = g.clone() # Clone the geometry to avoid modifying the original
                    g.transform(4326) # Transform to WGS84
                data['geometry'] = json.loads(g.geojson)
                # reduce precision for speed
                data['geometry'] = self._round_coords(data['geometry'], precision=6)
            except Exception:
                pass
        elif isinstance(geom, dict):
            pass

        return data

def _round_coords(self, geom, precision):
    if geom['type'] == 'Point':
        geom['coordinates'] = [round(coord, precision) for coord in geom['coordinates']]
    elif geom['type'] in ['LineString', 'MultiPoint']:
        geom['coordinates'] = [[round(coord, precision) for coord in point] for point in geom['coordinates']]
    elif geom['type'] in ['Polygon', 'MultiLineString']:
        geom['coordinates'] = [[[round(coord, precision) for coord in point] for point in ring] for ring in geom['coordinates']]
    elif geom['type'] == 'MultiPolygon':
        geom['coordinates'] = [[[[round(coord, precision) for coord in point] for point in ring] for ring in polygon] for polygon in geom['coordinates']]
    return geom


class TraseeTuristiceSerializer(WGS84GeoFeatureSerializer):
    class Meta:
        model = TraseeTuristice
        geo_field = 'geom'
        fields = ['id', 'denumire_t', 'cod', 'judet', 'shape_leng']


class TraseeTematiceSerializer(WGS84GeoFeatureSerializer):
    class Meta:
        model = TraseeTematice
        geo_field = 'geom'
        fields = ['id', 'denumire_t', 'judet', 'timp', 'distanta_m', 'dificultat', 'distanta']


class CladiriAdministrativeSerializer(WGS84GeoFeatureSerializer):
    class Meta:
        model = CladiriAdministrative
        geo_field = 'geom'
        fields = ['id', 'nume', 'activa', 'tip_constr', 'address', 'phone', 'name']


class InfrastructuraAgrementSerializer(WGS84GeoFeatureSerializer):
    class Meta:
        model = InfrastructuraAgrement
        geo_field = 'geom'
        fields = ['id']


class ZonarePNBHG2011Serializer(WGS84GeoFeatureSerializer):
    class Meta:
        model = ZonarePNBHG2011
        geo_field = 'geom'
        fields = ['id', 'denumire', 'zonare_int', 'shape_area']


class ZonarePNBv2025Serializer(WGS84GeoFeatureSerializer):
    class Meta:
        model = ZonarePNBv2025
        geo_field = 'geom_3857'
        fields = ['id', 'zonare_int', 'area_ha', 'notes']


class SimpleGeomSerializer(WGS84GeoFeatureSerializer):
    """Reusable serializer for geometry-only models (no rich attributes)."""
    class Meta:
        geo_field = 'geom'
        fields = ['id']


class AriiNaturaleOUG2016Serializer(WGS84GeoFeatureSerializer):
    class Meta():
        model = AriiNaturaleOUG2016
        geo_field = 'geom'
        fields = ['id', 'localid', 'text', 'arie', 'tip_anp', 'cod_ro']

class AriiNaturalePropunereAPNBSerializer(WGS84GeoFeatureSerializer):
    class Meta():
        model = AriiNaturalePropunereAPNB
        geo_field = 'geom'
        fields = ['id', 'localid', 'text', 'arie', 'tip_anp', 'cod_ro']

class LimitaAdministrativaJudetSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaAdministrativaJudet
        geo_field = 'geom'
        fields = ['id', 'name', 'shape_area']

class LimitaAdministrativaUATSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaAdministrativaUAT
        geo_field = 'geom'
        fields = ['id', 'name', 'shape_area']

class PeaksSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = Peaks
        geo_field = 'geom'
        fields = ['id', 'name', 'ele']


class LimitaPNBv2016Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaPNBv2016
        geo_field = 'geom'
        fields = ['id', 'name', 'shape_area']


class LimitaSitN2K2016Serializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaSitN2K2016
        geo_field = 'geom'
        fields = ['id', 'name', 'shape_area']

class LimitaSectoarePNBSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaSectoarePNB
        geo_field = 'geom'

class LimitaAdministrativaRomaniaSerializer(SimpleGeomSerializer):
    class Meta(SimpleGeomSerializer.Meta):
        model = LimitaAdministrativaRomania
