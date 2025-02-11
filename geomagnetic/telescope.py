#import geomagnetic.util as gutil
#from geomagnetic import load_json
from . import util as gutil

class TelescopePointing:

    def __init__(self, logger=None):
        self._logger = logger
        self._dic_tel = None

    def load_telescopes(self, telname="./json/telescope.json"):
        # add angle style check and range check, in ver 2.
        try:
            self._dic_tel = gutil.load_json(telname)
        except FileNotFoundError as fnf_error:
            if self._logger is not None:
                self._logger.exception(fnf_error)
            else:
                print(f"Error: {fnf_error}")
        except PermissionError as perm_error:
            if self._logger is not None:
                self._logger.exception(perm_error)
            else:
                print(f"Error: {perm_error}")
        except Exception as e:
            if self._logger is not None:
                self._logger.exception(e)
            else:
                print(f"Error: {e}")

    def set_telescope(self, telname, azimuth, elevation):
        if self._dic_tel is None:
            self._dic_tel = {}
            self._dic_tel.setdefault(
                telname, {"azimuth": azimuth, "elevation": elevation}
            )
        elif telname in self._dic_tel.keys():
            raise IndexError(f"{telname} is already in the telescope list.")
        else:
            self._dic_tel.setdefault(
                telname, {"azimuth": azimuth, "elevation": elevation}
            )

    def get_telescopes(self):
        if self._dic_tel is None:
            raise ValueError("no telescope information found.")
        else:
            return self._dic_tel
