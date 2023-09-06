from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text(),

setup(
    name='metadynminer',
    version='0.2.5',
    description="Python package for efficient analysis of HILLS files generated by Plumed metadynamics simulations. ",
    long_description=(this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/Jan8be/metadynminer.py',
    author='Jan Beránek',
    author_email='Jan1.Beranek@vscht.cz',
    license='GPL-3.0',
    packages=['metadynminer'],
    install_requires=['numpy>=1.21.6',
                      'matplotlib>=3.5.3',
                      'pandas>=1.3.5',
                      'pyvista>=0.38.5'
                      ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
)
