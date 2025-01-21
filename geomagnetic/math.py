import numpy as np
import geomagnetic.util as gutil


def rodriguez_rotation_matrix(vector, ang_deg):
    """calculate a 2-D rotation matrix around given vector

    Args:
       vector (float): a vector, rotational axis
       ang_deg (float): rotational angle in degree
    Returns:
       rot_matrix (np.ndarray): a 3-D matrix for a specific rotation
    """
    # add zero vector removal, add type check numpy
    if vector.shape[0] != 3:
        raise ValueError("input is not 3-d vector")
    else:
        axis = vector / np.linalg.norm(vector)
        ang_rad = np.deg2rad(ang_deg)
        ax, ay, az = axis
        K = np.array(
            [
                [0, az, -ay],
                [-az, 0, ax],
                [ay, -ax, 0],
            ]
        )
        id_array = np.identity(3)
        rot_matrix = (
            id_array + np.sin(ang_rad) * K.T + (1 - np.cos(ang_rad)) * np.dot(K.T, K.T)
        )
        return rot_matrix


def calculate_field(mag, point, logger=None):
    """
    default base matrix is ([e1,e2,e3]).T
    """
    ele_deg, az_deg = point["elevation"], point["azimuth"]
    gutil.out_info(f"Telescope pointing: {ele_deg} deg, {az_deg} deg", logger)
    # 1st rotation, around z-axis
    nz = np.identity(3).T[2]
    gutil.out_debug(f"normal vector for the 1st rotation: {nz}", logger)
    rot_mat = rodriguez_rotation_matrix(nz, az_deg)
    n_new = np.dot(rot_mat, np.identity(3))
    gutil.out_debug(f"rotation matrix for the 1st rotation:\n{n_new}", logger)
    # if you want to check by eye, no need to transpose
    # adding that, if you want to take inner product, no need to transpose
    # but if you want to pick up column vector, you need to transpose
    # 2nd rotation, around an updated x-axis
    n_new_x = n_new.T[0]
    gutil.out_debug(f"normal vector for the 2nd rotation: {n_new_x}", logger)
    rot_2 = rodriguez_rotation_matrix(n_new_x, ele_deg - 90)
    gutil.out_debug(f"rotation matrix for the 2nd rotation:\n{rot_2}", logger)
    n_gen = np.dot(rot_2, n_new)
    gutil.out_info(f"camera x axis: {n_gen.T[0]}", logger)
    gutil.out_info(f"camera y axis: {n_gen.T[1]}", logger)
    gutil.out_info(f"camera z axis: {n_gen.T[2]}", logger)
    gutil.out_info(f"geo magnetic filed: {mag}", logger)
    mag_gen = np.dot(n_gen.T, mag)
    gutil.out_info(f"geo magnetic field for the telescope: {mag_gen}", logger)
    # print(np.dot(n_gen.T[0],mag),np.dot(n_gen.T[1],mag),np.dot(n_gen.T[2],mag))
    return mag_gen, n_gen
