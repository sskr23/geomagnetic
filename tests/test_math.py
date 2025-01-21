import geomagnetic.math as gmath
import numpy as np


def test_rodriguez_rotation_matrix_z():
    """test rodriguez rotation matrix using pytest"""
    rot_mat = gmath.rodriguez_rotation_matrix(np.array([0, 0, 1]), 90)
    exp_mat = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    assert np.allclose(a=rot_mat, b=exp_mat.T, atol=1e-3, rtol=1e-3)


def test_rodriguez_rotation_matrix_y():
    """test rodriguez rotation matrix using pytest"""
    rot_mat = gmath.rodriguez_rotation_matrix(np.array([0, 1, 0]), 90)
    exp_mat = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
    assert np.allclose(a=rot_mat, b=exp_mat.T, atol=1e-3, rtol=1e-3)


def test_rodriguez_rotation_matrix_x():
    """test rodriguez rotation matrix using pytest"""
    rot_mat = gmath.rodriguez_rotation_matrix(np.array([1, 0, 0]), 90)
    exp_mat = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    assert np.allclose(a=rot_mat, b=exp_mat.T, atol=1e-3, rtol=1e-3)


def test_rodriguez_rotation_matrix():
    """test rodriguez rotation matrix using pytest"""
    rot_mat1 = gmath.rodriguez_rotation_matrix(np.array([0, 0, 1]), 45)
    rot_mat2 = gmath.rodriguez_rotation_matrix(rot_mat1.T[0], 90)
    tot_rot_mat = np.dot(rot_mat2, rot_mat1)
    exp_mat = np.array(
        [
            [1 / np.sqrt(2), 1 / np.sqrt(2), 0],
            [0, 0, 1],
            [1 / np.sqrt(2), -1 / np.sqrt(2), 0],
        ]
    )
    assert np.allclose(a=tot_rot_mat, b=exp_mat.T, atol=1e-3, rtol=1e-3)
    rot_mat3 = gmath.rodriguez_rotation_matrix(tot_rot_mat.T[1], 45)
    tot_rot_mat = np.dot(rot_mat3, tot_rot_mat)
    exp_mat = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    assert np.allclose(a=tot_rot_mat, b=exp_mat.T, atol=1e-3, rtol=1e-3)
    rot_mat4 = gmath.rodriguez_rotation_matrix(tot_rot_mat.T[2], 90)
    tot_rot_mat = np.dot(rot_mat4, tot_rot_mat)
    exp_mat = np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    assert np.allclose(a=tot_rot_mat, b=exp_mat.T, atol=1e-3, rtol=1e-3)
    rot_mat5 = gmath.rodriguez_rotation_matrix(tot_rot_mat.T[1], 90)
    tot_rot_mat = np.dot(rot_mat5, tot_rot_mat)
    exp_mat = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    assert np.allclose(a=tot_rot_mat, b=exp_mat.T, atol=1e-3, rtol=1e-3)
