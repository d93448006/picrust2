#!/usr/bin/env python

from setuptools import setup
from glob import glob

__copyright__ = "Copyright 2018-2022, The PICRUSt Project"
__license__ = "GPL"
__version__ = "2.5.1"
__maintainer__ = "Gavin Douglas"

long_description = ("Please visit the google group if you have questions: "
                    "https://groups.google.com/forum/#!forum/picrust-users. "
                    "Paper: Douglas et al. 2020. PICRUSt2 for prediction of "
                    "metagenome functions. Nature Biotechnology. doi: "
                    "10.1038/s41587-020-0548-6."
                    )

setup(name='PICRUSt2',
      version=__version__,
      description=('PICRUSt: Phylogenetic Investigation of Communities by '
                   'Reconstruction of Unobserved States'),
      maintainer=__maintainer__,
      url='https://github.com/picrust/picrust2/wiki',
      packages=['picrust2'],
      scripts=glob('scripts/*py'),
      install_requires=['numpy',
			'h5py',
                        'joblib',
                        'biom-format'],
      package_data={'picrust2':
                    ['MinPath/MinPath12hmp.py',
                     'Rscripts/*R']},
      long_description=long_description)
