import numpy as np
import geomagnetic.util as gutil


class Geomagneticfield:
    """class to hold geo-magneticfield"""

    def __init__(self, logger=None):
        self._logger = logger
        self._dec_deg = None
        self._inc_deg = None
        self._intensity = None
        self._int_horizontal = None
        self._int_vertical = None
        self._int_x = None
        self._int_y = None
        self._int_z = None
        self._modelname = None

    def set_field(self, intensity, dec_deg, inc_deg):
        """set magnetic vector

        Args:
            intensity: total intensity of the geo magnetic field in nT
            dec_deg: declination angle in degree, mes clockwise from true north to the horizontal component of the field vec
            inc_deg: inclination angle in degree, mes from horizontal plane to field vector, positive downwards
        """
        # add angle range check in ver 2.
        self._dec_deg = dec_deg
        self._inc_deg = inc_deg
        self._intensity = intensity
        self._int_horizontal = intensity * np.cos(np.deg2rad(inc_deg))
        self._int_vertical = intensity * np.sin(np.deg2rad(inc_deg))
        self._int_x = self._int_horizontal * np.sin(np.deg2rad(dec_deg))
        self._int_y = self._int_horizontal * np.cos(np.deg2rad(dec_deg))
        self._int_z = -self._int_vertical

    def get_vector(self, isgeo=True):
        if (self._int_x is None) or (self._int_y is None) or (self._int_z is None):
            raise ValueError(
                "Magnetic field values are not properly set. Check the initialization."
            )
        else:
            return np.array([self._int_x, self._int_y, self._int_z])

    def get_field(self):
        if (
            (self._dec_deg is None)
            or (self._inc_deg is None)
            or (self._intensity is None)
        ):
            raise ValueError(
                "Magnetic field values are not properly set. Check the initialization."
            )
        else:
            return self._dec_deg, self._inc_deg, self._intensity

    def show_field(self):
        if (
            (self._dec_deg is None)
            or (self._inc_deg is None)
            or (self._intensity is None)
        ):
            raise ValueError(
                "Magnetic field values are not properly set. Check the initialization."
            )
        else:
            gutil.out_info(
                f"Intensity: {self._intensity} nT, Declination: {self._dec_deg} deg, Inclination: {self._inc_deg} deg",
                self._logger,
            )

    def show_modelname(self):
        if self._modelname is None:
            raise ValueError("No model name has been set. Check your inout.")
        else:
            gutil.out_info(f"Model: {self._modelname}")

    def load_model(self, modelname):
        try:
            self._dic_model = gutil.load_json(modelname)
            res_dict = self._dic_model["result"][0]
            # unt_dict = self._dic_model["units"]
            self.set_field(
                intensity=res_dict["totalintensity"],
                dec_deg=res_dict["declination"],
                inc_deg=res_dict["inclination"],
            )
            self._modelname = self._dic_model["model"]
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
