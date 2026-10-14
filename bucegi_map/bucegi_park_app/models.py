from django.contrib.gis.db import models


# ─────────────────────────────────────────────
# used schema is 'webmap'
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
        db_table = 'webmap\".\"trasee_turistice_pnb'
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
        db_table = 'webmap\".\"trasee_tematice_pnb'
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
        db_table = 'webmap\".\"cladiri_administrative'
        verbose_name = "Clădire administrativă"
        verbose_name_plural = "Clădiri administrative APNB"


class InfrastructuraAgrement(models.Model):
    """Recreation infrastructure — MultiLineString, EPSG:3844."""
    geom = models.MultiLineStringField(srid=3844)

    class Meta:
        managed = False
        db_table = 'webmap\".\"infrastructura_agrement'
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
        db_table = 'webmap\".\"ZONARE_PNB_HG187_2011'
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
        db_table = 'webmap\".\"zonare_pnb_v2025'
        verbose_name = "Zonare PNB v2025"
        verbose_name_plural = "Zonare PNB v2025"


class AriiNaturaleOUG2016(models.Model):
    """Protected areas per OUG 49/2016 — MultiPolygon, EPSG:3844."""
    localid = models.CharField(max_length=9, db_column='localId', blank=True, null=True)
    cod_ro = models.CharField(max_length=15, db_column='cod_RO', blank=True, null=True)
    text = models.CharField(max_length=254, blank=True, null=True)
    arie = models.FloatField(db_column='Arie', blank=True, null=True)
    tip_anp = models.CharField(max_length=100, db_column='Tip_anp', blank=True, null=True)
    characters = models.CharField(max_length=95, db_column='CharacterS', blank=True, null=True)
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'webmap\".\"arii_naturale_protejate_oug49_2016'
        verbose_name = "Arii naturale protejate OUG 49/2016"


class AriiNaturalePropunereAPNB(models.Model):
    """Protected areas per APNB proposal — MultiPolygon, EPSG:3844."""
    localid = models.CharField(max_length=9, db_column='localId', blank=True, null=True)
    cod_ro = models.CharField(max_length=15, db_column='cod_RO', blank=True, null=True)
    text = models.CharField(max_length=254, blank=True, null=True)
    arie = models.FloatField(db_column='Arie', blank=True, null=True)
    tip_anp = models.CharField(max_length=100, db_column='Tip_anp', blank=True, null=True)
    nr_ord = models.CharField(max_length=5, db_column='NR_ORD', blank=True, null=True)
    characters = models.CharField(max_length=95, db_column='CharacterS', blank=True, null=True)
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'webmap\".\"rezervatii_propuse_pnb_v2'
        verbose_name = "Arii naturale protejate, conf. propunere APNB"


class LimitaAdministrativaJudet(models.Model):
    """County administrative boundary — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)
    name = models.CharField(max_length=100, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'webmap\".\"limita_administrativa_judet'
        verbose_name = "Limita administrativă Județ PN Bucegi"


class LimitaAdministrativaUAT(models.Model):
    """UAT administrative boundary — MultiPolygon, SRID=0."""
    geom = models.MultiPolygonField(srid=0)
    name = models.CharField(max_length=100, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    
    class Meta:
        managed = False
        db_table = 'webmap\".\"limita_administrativa_uat'
        verbose_name = "Limita administrativă UAT PN Bucegi"


class LimitaPNBv2016(models.Model):
    """Park boundary v2016 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)
    text = models.CharField(max_length=254, null=True, blank=True)
    arie = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'webmap\".\"limita_parc_oug_49_2016'
        verbose_name = "Limita PN BUCEGI OUG 49/2016"


class Peaks(models.Model):
    """Mountain peaks — Point, EPSG:3844."""
    geom = models.PointField(srid=3844)
    name = models.CharField(max_length=100, null=True, blank=True)
    ele = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'webmap\".\"peaks'
        verbose_name = "Vârf montan"
        verbose_name_plural = "Vârfuri montane"

class LimitaSitN2K2016(models.Model):
    """Natura 2000 site boundary 2016 — MultiLineString, EPSG:3844."""
    geom = models.MultiLineStringField(srid=3844)
    localid = models.CharField(max_length=20, null=True, blank=True)
    arie = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'webmap\".\"limita_sit_n2k_rosci0013'
        verbose_name = "Limita Sit N2K ROSCI0013 v2016"


class LimitaSectoarePNB(models.Model):
    """Park sectors boundary 2021 — MultiPolygon, EPSG:3844."""
    geom = models.MultiPolygonField(srid=3844)

    class Meta:
        managed = False
        db_table = 'webmap\".\"limite_sectoare_pnb_v2021'
        verbose_name = "Limita sectoare PNB v2021"


class LimitaAdministrativaRomania(models.Model):
    """Romania administrative boundary — MultiLineString, SRID=0."""
    geom = models.MultiLineStringField(srid=0)

    class Meta:
        managed = False
        db_table = 'webmap\".\"limita_administrativa_romania'
        verbose_name = "Limita administrativă România"
