import pysm
import pysm.units as u


def test_read_map_unit():
    m = pysm.read_map("pysm_2/dust_temp.fits", nside=8, field=0, unit="uK_RJ")
    assert u.Unit("uK_RJ") == m.unit


def test_read_map_unit_dimensionless():
    m = pysm.read_map("pysm_2/dust_temp.fits", nside=8, field=0)
    assert u.Unit("") == m.unit
