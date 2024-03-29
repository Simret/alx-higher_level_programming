#!/usr/bin/python3
"""A module that multiplies 2 matricies using numpy module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """A method that multiplies 2 matrix that is given
        Args:
            m_a: input first matrix
            m_b: input second matrix
        Returns:
            return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
