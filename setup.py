""" EEA Exhibit Installer
"""
from setuptools import setup, find_packages
import os
from os.path import join

NAME = 'eea.exhibit'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description="Exhibit JS libs",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='exhibit eea plone zope python',
      author='Alin Voinea',
      author_email='alin.voinea@eaudeweb.ro',
      url='http://eggrepo.eea.europa.eu/simple',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
