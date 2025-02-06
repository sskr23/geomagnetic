# Geomagnetic field calculator

This document provides a brief description of Python module for a geomagnetic field calculation.

## How to use

There are two ways to use the module as script.

### Automatic mode

In the automatic mode, the script calculates geomagnetic field component with respect to FAST telescopes automatically.
Details of telescopes and geomagnetic filed models can be given in advance as json files.

```python
python -m geomagnetic automatic/auto/a 
```

- ./json/telescope.json
  
```json
{
    "FAST@TA-1":{
        "azimuth": 89.7,
        "elevation": 15.1
    }
}
```
one can define telescopes in `telescope.json`.
`azimuth` and `elevation` are supposed to be in degree.

- ./json/TA-BR.json

You can download any magnetic field model from the web and put in ./json directory.
The default file name is `TA-BR.json`

### Interactive mode
 
```python
python -m geomagnetic interactive/int/i -f <intensity(nT)> <declination(deg)> <inclination(deg)> -p <elevation(deg)> <azimuth(deg)>
```

the module can be used as interactive calculator for geomagnetic field calculation.
For the details of definitions of each parameters, see technical document in `./docs` 

### How to use geomagnetic module in your script

```python
import geomagnetic.geomagnetic as gmag
import geomagnetic.math as gmath
# Create Geomagneticfield object
gmfld = gmag.Geomagneticfield()
# Give a field information to the object
gmfld.set_field(intensity=intensity,dec_deg=declination,inc_deg=inclination)
# Prepare telescope pointing
pointing = {}
pointing["elevation"] = elevation
pointing["azimuth"] = azimuth
# Calculate
mag_vec, new_axis = gmath.calculate_field(mag=geomag.get_vector(),point=pointing)
```

One can use the module thier script, see jupyter notebook for detailed implementation.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sskr23/geomagnetic/main)

## Geomagnetic filed model

One can download the model as json file on the web.

[here](https://www.ncei.noaa.gov/products/world-magnetic-model)

You need some quantities such as longitute, latitude, elevation, and date of the location you would like to know the field.

## Requirements

- numpy
- pytest (for debug. python -m pytest)

## Planned updates

- Check for input parameter range, especially for angle
- minor fix on logging
- more detaied docstring 
- package installation for jupyter on the web



