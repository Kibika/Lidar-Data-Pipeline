#!/usr/bin/env python

"""Tests for `agri_tech` package."""

import pytest

# from agri_tech import agri_tech
from agri_tech.agri_tech import Lidar

from geopandas import GeoDataFrame, GeoSeries, read_file
from geopandas.testing import assert_geodataframe_equal, assert_geoseries_equal




class TestDataFrame:
    def test_df_init(self):
        lidar = Lidar()
        assert type(lidar.geodf('spatial_subset.geojson')) is GeoDataFrame
        
    def test_geo_colname(self):
        lidar = Lidar()
        assert lidar.geodf('Agritech/agri_tech/agri_tech/spatial_subset.geojson')._geometry_column_name == "geometry"
