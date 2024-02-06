# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Movie Website'
copyright = '2023, The Proton Guy'
author = 'The Proton Guy'
release = 'version 1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'movie.settings' 
os.environ['SECRET_KEY'] = 'django-insecure-2ns(12mi_0-i^lq8z9&*$u90lqt9#x6k*z(*o-kl*izfq7yl)y'
django.setup()
...
extensions = [
 'sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc'
]