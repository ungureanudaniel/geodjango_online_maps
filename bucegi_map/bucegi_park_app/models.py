from django.contrib.gis.db import models


# ─────────────────────────────────────────────
# Schema: infrastructura_vizitare
# ─────────────────────────────────────────────

class TraseeTuristice(models.Model):
    """Hiking / tourist trails — MultiLineString, no SRID defined in DB."""
    geom = models.MultiLineStringField(srid=0)
    objectid = models.IntegerField(null=True, blank=True)
    denumire_t = models.CharField(max_length=254, null=True, blank=True)
    cod = models.IntegerField(null=True, blank=True)
    judet = models.CharField(max_length=50, null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'infrastructura_vizitare\".\"trasee_turistice_pnb'
        verbose_name = "Traseu turistic"
        verbose_name_plural = "Trasee turistice PNB"


class TraseeTematice(models.Model):
    """Thematic trails — MultiLineString, EPSG:3844."""
    geom = models.MultiLineStringField(srid=3844)
    objectid = models.IntegerField(null=True, blank=True)
    denumire_t = models.CharField(max_length=254, null=True, blank=True)
    judet = models.CharField(max_length=50, null=True, blank=True)
    timp = models.CharField(max_length=50, null=True, blank=True)
    distanta_m = models.FloatField(null=True, blank=True)
    dificultat = models.CharField(max_length=50, null=True, blank=True)
    distanta = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'infrastructura_vizitare\".\"trasee_tematice_pnb'
        verbose_name = "Traseu tematic"
        verbose_name_plural = "Trasee tematice PNB"


class CladiriAdministrative(models.Model):
    """APNB administrative buildings — Point, EPSG:3844."""
    geom = models.PointField(srid=3844)
    fid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nume = models.CharField(max_length=100, null=True, blank=True, db_column='Nume')
    activa = models.CharField(max_length=2, null=True, blank=True, db_column='Activa')
    latitudine = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True, db_column='Latitudine')
    longitudin = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True, db_column='Longitudin')
    tip_constr = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True, db_column='Name')

    class Meta:
        managed = False
        db_table = 'infrastructura_vizitare\".\"Cladiri administrative APNB'
        verbose_name = "Clădire administrativă"
        verbose_name_plural = "Clădiri administrative APNB"


class InfrastructuraAgrement(models.Model):
    """Recreation infrastructure — MultiLineString, EPSG:3844."""
    geom = models.MultiLineStringField(srid=3844)

    class Meta:
        managed = False
        db_table = 'infrastructura_vizitare\".\"infrastructura_agrement'
        verbose_name = "Infrastructură agrement"
        verbose_name_plural = "Infrastructură agrement"


# ─────────────────────────────────────────────
# Schema: limite
# ─────────────────────────────────────────────

class ZonarePNBHG2011(models.Model):
    """Park zoning per HG 187/2011 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)
    fid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shape_leng = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True, db_column='Shape_Leng')
    shape_area = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True, db_column='Shape_Area')
    denumire = models.CharField(max_length=200, null=True, blank=True, db_column='DENUMIRE')
    zonare_int = models.CharField(max_length=50, null=True, blank=True, db_column='ZONARE_INT')

    class Meta:
        managed = False
        db_table = 'limite\".\"ZONARE_PNB_HG187_2011'
        verbose_name = "Zonare PNB HG 187/2011"
        verbose_name_plural = "Zonare PNB HG 187/2011"


class ZonarePNBv2025(models.Model):
    """Park zoning proposal 2025 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)
    zonare_int = models.CharField(max_length=10, null=True, blank=True)
    area_ha = models.FloatField(null=True, blank=True, db_column='Area_ha')
    notes = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'limite\".\"Zonare_PNB_v2025'
        verbose_name = "Zonare PNB v2025"
        verbose_name_plural = "Zonare PNB v2025"


class LimitaRONPA006(models.Model):
    """Official RONPA006 park boundary OUG49/2016 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)
    localid = models.CharField(max_length=9, null=True, blank=True)
    characters = models.CharField(max_length=95, null=True, blank=True)
    text = models.CharField(max_length=254, null=True, blank=True)
    arie = models.FloatField(null=True, blank=True)
    tip_anp = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita_RONPA006_OUG49_2016_v2025'
        verbose_name = "Limita RONPA006 OUG49/2016 v2025"
        verbose_name_plural = "Limite RONPA006 OUG49/2016 v2025"


class LimitaROSCI0013OUG2025(models.Model):
    """ROSCI0013 Natura 2000 boundary OUG49/2016 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita ROSCI0013 OUG49-2016 v2025'
        verbose_name = "Limita ROSCI0013 OUG49-2016 v2025"


class AriiNaturaleOUG2016(models.Model):
    """Protected areas per OUG 49/2016 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Arii naturale protejate, conform OUG 49/2016'
        verbose_name = "Arii naturale protejate OUG 49/2016"


class AriiNaturalePropunereAPNB(models.Model):
    """Protected areas per APNB proposal — MultiPolygon, EPSG:3844 (SRID=0 in DB)."""
    geom = models.MultiPolygonField(srid=0)

    class Meta:
        managed = False
        db_table = 'limite\".\"Arii naturale protejate, conform propunere APNB'
        verbose_name = "Arii naturale protejate propunere APNB"


class LimitaAdministrativaJudet(models.Model):
    """County administrative boundary — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita administrativa Judet - PN BUCEGI'
        verbose_name = "Limita administrativă Județ PN Bucegi"


class LimitaAdministrativaUAT(models.Model):
    """UAT administrative boundary — MultiPolygon, SRID=0."""
    geom = models.MultiPolygonField(srid=0)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita administrativa UAT - PN BUCEGI'
        verbose_name = "Limita administrativă UAT PN Bucegi"


class LimitaN2K2017(models.Model):
    """Natura 2000 boundary 2017 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita N2K 2017'
        verbose_name = "Limita N2K 2017"


class LimitaPNBv2016(models.Model):
    """Park boundary v2016 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita PN BUCEGI v2016'
        verbose_name = "Limita PN BUCEGI v2016"


class LimitaPNBv2023(models.Model):
    """Park boundary v2023 — MultiLineString, SRID=0."""
    geom = models.MultiLineStringField(srid=0)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita PN BUCEGI v2023'
        verbose_name = "Limita PN BUCEGI v2023"


class LimitaSitN2K2016(models.Model):
    """Natura 2000 site boundary 2016 — MultiLineString, EPSG:3844."""
    geom = models.MultiLineStringField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita Sit N2K ROSCI0013 v2016'
        verbose_name = "Limita Sit N2K ROSCI0013 v2016"


class LimitaSitN2K2023(models.Model):
    """Natura 2000 site boundary 2023 — MultiLineString, SRID=0."""
    geom = models.MultiLineStringField(srid=0)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita Sit N2K ROSCI0013 v2023'
        verbose_name = "Limita Sit N2K ROSCI0013 v2023"


class LimitaSectoarePNB(models.Model):
    """Park sectors boundary 2021 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita sectoare PNB v2021'
        verbose_name = "Limita sectoare PNB v2021"


class AriiProtejateRomaniaOUG(models.Model):
    """All protected areas Romania OUG49/2016 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"ARII_PROTEJATE_ROMANIA_OUG492016_EPSG_3844'
        verbose_name = "Arii protejate România OUG49/2016"


class ArieNaturalaLege2000(models.Model):
    """Protected area per Law 5/2000 — Point, EPSG:3844."""
    geom = models.PointField(srid=3844)

    class Meta:
        managed = False
        db_table = 'limite\".\"Arie naturală protejată, conform Legii nr. 5 / 2000:'
        verbose_name = "Arie naturală protejată Legea 5/2000"


class LimitaZonarePropusa2024(models.Model):
    """Proposed zoning boundary 2024 — MultiPolygon, SRID=0."""
    geom = models.MultiPolygonField(srid=0)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita zonare propusa PNB v2024'
        verbose_name = "Limita zonare propusă PNB v2024"


class LimitaAdministrativaRomania(models.Model):
    """Romania administrative boundary — MultiLineString, SRID=0."""
    geom = models.MultiLineStringField(srid=0)

    class Meta:
        managed = False
        db_table = 'limite\".\"Limita administrativa Romania'
        verbose_name = "Limita administrativă România"
