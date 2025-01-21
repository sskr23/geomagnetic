import pytest
import geomagnetic.geomagnetic as gmag


def test_get_vector():
    mgfld = gmag.Geomagneticfield()
    with pytest.raises(ValueError):
        mgfld.get_vector()


def test_get_field():
    mgfld = gmag.Geomagneticfield()
    with pytest.raises(ValueError):
        mgfld.get_field()


def test_show_field():
    mgfld = gmag.Geomagneticfield()
    with pytest.raises(ValueError):
        mgfld.show_field()

def test_show_modelname():
    mgfld = gmag.Geomagneticfield()
    with pytest.raises(ValueError):
        mgfld.show_modelname()

