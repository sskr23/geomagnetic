import sys
print(sys.path)
from . import geomagnetic as gmag
from . import telescope as gtel
from . import math as gmath
import argparse
import numpy as np
from logging import getLogger, StreamHandler, DEBUG, INFO, Formatter

logger = getLogger(name=__name__)
logger.setLevel(DEBUG)
st_handler = StreamHandler()
st_handler.setFormatter(
    Formatter("(%(name)s) %(funcName)s [%(levelname)s]: %(message)s")
)
# set log level after parsing argument instead
# st_handler.setLevel(INFO)
# logger.addHandler(st_handler)
np.set_printoptions(precision=3)


def interactive(args):
    gmfld = gmag.Geomagneticfield()
    intensity = args.field[0]
    declination = args.field[1]
    inclination = args.field[2]
    pointing = {}
    pointing["elevation"] = args.pointing[0]
    pointing["azimuth"] = args.pointing[1]
    gmfld.set_field(intensity=intensity, dec_deg=declination, inc_deg=inclination)
    gmfld.show_field()
    logger.debug(gmfld.get_field())
    gmath.calculate_field(mag=gmfld.get_vector(), point=pointing, logger=logger)


def auto(args):
    gmfld = gmag.Geomagneticfield(logger)
    gmfld.load_model("./json/TA-BR.json")
    gmfld.show_field()
    telescope = gtel.TelescopePointing(logger)
    telescope.load_telescopes("./json/telescope.json")
    logger.info(telescope.get_telescopes().keys())
    # enter the loop for given telescopes
    for key, value in telescope.get_telescopes().items():
        logger.info(f"########## Start {key} ##########")
        gmath.calculate_field(gmfld.get_vector(), value, logger=logger)


def parse_arguments():
    parser = argparse.ArgumentParser(description="geomagnetic field calculation")
    subparsers = parser.add_subparsers(dest="mode", required=True)

    interactive_parser = subparsers.add_parser(
        "interactive", help="mode for an interactive calculation", aliases=["int", "i"]
    )
    interactive_parser.add_argument(
        "-f",
        "--field",
        required=True,
        type=float,
        nargs=3,
        help="geo-magnetic filed <intensity(nT)> <declination(deg)> <inclination(deg)>",
    )
    interactive_parser.add_argument(
        "-l", "--level", type=int, help="set logging level", default=20
    )

    interactive_parser.add_argument(
        "-p",
        "--pointing",
        required=True,
        type=float,
        nargs=2,
        help="telescope pointing <elevation(deg)> <azimuth(deg)>",
    )
    interactive_parser.set_defaults(handler=interactive)

    auto_parser = subparsers.add_parser(
        "automatic", help="mode for an automatic calculation", aliases=["auto", "a"]
    )
    auto_parser.add_argument(
        "-l", "--level", type=int, help="set log level", default=20
    )
    auto_parser.set_defaults(handler=auto)

    args = parser.parse_args()
    return args


if "__main__" == __name__:
    args = parse_arguments()
    st_handler.setLevel(args.level)
    logger.addHandler(st_handler)
    if hasattr(args, "handler"):
        args.handler(args)
