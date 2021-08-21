=========
agri_tech
=========


.. image:: https://img.shields.io/pypi/v/agri_tech.svg
        :target: https://pypi.python.org/pypi/agri_tech

.. image:: https://img.shields.io/travis/Kibika/agri_tech.svg
        :target: https://travis-ci.com/Kibika/agri_tech

.. image:: https://readthedocs.org/projects/agri-tech/badge/?version=latest
        :target: https://agri-tech.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/Kibika/agri_tech/shield.svg
     :target: https://pyup.io/repos/github/Kibika/agri_tech/
     :alt: Updates



Loading and using Lidar data


* Free software: MIT license
* Documentation: https://agri-tech.readthedocs.io.


Features
--------

This project creates a package to access Entwine Point Tile(EPT) LiDAR data from AWS and return the data in the format of a geopandas dataframe for ease of analysis.

The first step was to access the USGS data through the public data url "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

A .txt is created for the regions available abd used to create a dropdown where a user can choose the regional data they would like to analyze.
The data used for analysis in this data is from the state of IOWA, witht the label 'IA_FullState'.

The boundaries will be user inputs that depend on the area a user wants to analyze. The boundaries are reprojected before input into the pdal pipeline.

Using the pdal library, we create a pipeline that can be used to access the data inside the ept.jsons. The pipeline uses read.ept to read the file, the second layer filters the dataset depending on classes, we retain classes 2-7 and 9. The classes represent the type of data collected e.g. ground. The third layer writes the data in 3 different formats, the first format is a .laz file, the .laz file is transformed to a .tif. The data is also written to a .geojson in the pipeline.

The .geojson is used to create a geodataframe and the geometry of the dataset is changed to two dimensions, removing the elevation. The elevation is represented as a colum in the final dataframe.

The .tif file is plotted to produce a pixel image of the area. The .tif is also ised to generate the shapefile of the area.

## Installation
The project requires installation of pdal wheel.

pip install agri-tech==0.1.9

## Example
import agri_tech

from agri_tech import agri_tech

method = agri_tech.Lidar()    # calls the Lidar class from the package

method.region()               # allows user to choose the region they would like to analyse

method.ept_json()             # returns the url to the lidar data of the region chosen

method.pipeline(xmin = -93.756155,xmax = -93.747334, ymin = 41.918015, ymax = 41.921429)    # user inputs the coordinates of the area to analyse, the     coordinates used here belong to a farm in Iowa, USA. This method will also apply a crs to the co-ordinates the crs allowed currently is "epsg:4326"

method.run_pipeline()         # reads the lidarr data from the url provided with 'ept_json method, writes and returns .las, .tif and geojson files 

method.geodf('spatial_subset.geojson')     # reads the geojson from 'run_pipeline' and returns a geodataframe

method.plot_raster('spatial_subset.tif')   # plots the .tif file using pixels to show high and low elevations

method.plot3d()                            # returns a 3d plot of the area chosen




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
