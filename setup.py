from setuptools import setup, find_packages
from os.path import join, dirname
import resu

setup(
    name='resu',
    version=resu.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': ['resu = resu.cli:run']
        },
    install_requires=[
        "docopt",
        "PyYAML",
        "jinja2",
        "mako",
        "pdfkit",
        "sphinx",
        "sphinx_rtd_theme"
        ],
    package_data={'resu': [
        'examples/*.*',
        'examples/*/*.*'
        ]}
    )
