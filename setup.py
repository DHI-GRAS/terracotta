from setuptools import setup, find_packages
import os

import versioneer

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as fp:
    install_requires = fp.read()

setup(
    name='terracotta',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='A modern XYZ tile server written in Python',
    author='Philip Graae',
    author_email='phgr@dhigroup.com',
    packages=find_packages(),
    python_requires='>=3.5',
    setup_requires=['numpy'],
    install_requires=install_requires,
    extras_require={
        'test': [
            'pytest>=3.5',
            'pytest-cov',
            'pytest-mypy',
            'pytest-flake8',
            'codecov',
            'attrs>=17.4.0',
            'matplotlib',
            'moto',
            'crick'
        ],
        'aws': [
            'boto3',
            'botocore',
            'awscli',
            'zappa'
        ]
    },
    entry_points='''
        [console_scripts]
        terracotta=terracotta.scripts.cli:cli
    ''',
    include_package_data=True,
    package_data={
        'terracotta': [
            'cmaps/*_rgb.npy',  # colormaps
            'templates/*.html', 'static/*.js', 'static/*.css', 'static/images/*.png'  # preview app
        ]
    }
)
