import pytest
import geomagnetic.telescope as gtel


def test_set_telescope():
    telescope = gtel.TelescopePointing()
    telescope.set_telescope("TEL1", 0, 0)
    with pytest.raises(IndexError):
        telescope.set_telescope("TEL1", 0, 0)


def test_get_telescope():
    telescope = gtel.TelescopePointing()
    with pytest.raises(ValueError):
        telescope.get_telescopes()
