import geomagnetic.util as gutil
import pytest


def test_load_json():
    with pytest.raises(FileNotFoundError):
        gutil.load_json("hoge.json")
