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





Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
