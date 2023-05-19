"""
utils.arithmetic
================

this is the module for arithmetic

.. autofunction:: divide(a, b, c=1)
"""


def divide(a, b, c=1):
    """divide two numbers

    Parameters
    ----------
    a : _type_
        _description_
    b : _type_
        _description_
    c : int, optional
        _description_, by default 1

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    ZeroDivisionError
        _description_
    """
    result = 0
    if b == 0:
        raise ZeroDivisionError
    else:
        result = a / b
    return result
