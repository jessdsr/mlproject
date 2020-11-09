# -*- coding: UTF-8 -*-

# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
    assert haversine(48.865, 2.380, 48.235, 2.393) == 70.00696965697475
