from setuptools import setup, find_packages
from os import path
import re

here = path.abspath(path.dirname(__file__))

# get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# resolve relative links to figures
long_description = re.sub(
    r'!\[(.*?)\]\((docs/_figures/.*?)\)',
    r'![\1](https://github.com/DHI-GRAS/terracotta/raw/master/\2)',
    long_description
)

numpy_version = '>=1.15,!=1.17.0'

setup(
    # metadata
    name='terracotta',
    description='A modern XYZ tile server written in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DHI-GRAS/terracotta',
    author='Jonas Sølvsteen',
    author_email='josl@dhigroup.com',
    keywords='xyz tileserver rasterio cloud-optimized-geotiff serverless',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Flask',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    # module
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6',
    use_scm_version={
        'write_to': 'terracotta/_version.py'
    },
    # dependencies
    setup_requires=[
        'setuptools_scm',
        'setuptools_scm_git_archive',
        'numpy%s' % numpy_version
    ],
    install_requires=[
        'apispec>=1.0',
        'apispec-webframeworks',
        'cachetools>=3.1.0',
        'click',
        'flask',
        'flask_cors',
        'marshmallow>=3.0.0',
        'mercantile',
        'numpy%s' % numpy_version,
        'pillow',
        'pyyaml>=3.10',  # downstream dependency of apispec
        'shapely',
        'rasterio>=1.0,<=1.1.8',  # TODO: unpin when performance issues with GDAL3 are fixed
        'shapely',
        'toml',
        'tqdm'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'pytest-mypy',
            'pytest-flake8',
            'pytest-benchmark',
            'attrs>=17.4.0',
            'codecov',
            'colorlog',
            'crick',
            'flake8',
            'matplotlib',
            'moto',
            'aws-xray-sdk',
            'pymysql>=1.0.0'
        ],
        'docs': [
            'sphinx',
            'sphinx_autodoc_typehints',
            'sphinx-click',
            'pymysql<0.10'
        ],
        'recommended': [
            'colorlog',
            'crick',
            'pymysql<0.10'
        ]
    },
    # CLI
    entry_points='''
        [console_scripts]
        terracotta=terracotta.scripts.cli:entrypoint
    ''',
    # package data
    include_package_data=True,
    package_data={
        'terracotta': [
            'cmaps/data/*_rgba.npy',  # colormaps
            'templates/*.html', 'static/*'  # preview app
        ]
    },
)
