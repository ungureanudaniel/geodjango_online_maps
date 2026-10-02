# bucegi_park_app/renderers.py
from rest_framework.renderers import JSONRenderer


class GeoJSONRenderer(JSONRenderer):
    """Wrap DRF list output as a GeoJSON FeatureCollection so Leaflet can consume it."""
    media_type = 'application/geo+json'
    format = 'geojson'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Paginated response: {"results": [...]}
        if isinstance(data, dict) and 'results' in data and isinstance(data['results'], list):
            data = {
                'type': 'FeatureCollection',
                'features': data['results'],
            }
        # Plain list response: [{...}, {...}]
        elif isinstance(data, list):
            data = {
                'type': 'FeatureCollection',
                'features': data,
            }
        return super().render(data, accepted_media_type, renderer_context)