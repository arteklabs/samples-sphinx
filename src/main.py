"""
API Reference
=============

This is the python package for the sphinx demo.

.. toctree::
    :maxdepth: 1

    api/utils
"""
from utils import arithmetic

if __name__ == "__main__":
    print("The division of 1 by 2 is {}".format(arithmetic.divide(1, 2)))
