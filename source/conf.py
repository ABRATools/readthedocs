# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'ABRATools'
copyright = '2025, A.B.R.A.'
author = 'A.B.R.A.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_copybutton','sphinx_favicon','sphinx_last_updated_by_git','notfound.extension','sphinx-prompt']

templates_path = ['_templates']
exclude_patterns = []

favicons = [
   {
      "rel": "icon",
      "href": "img/terminal-solid.svg",  # use a local file in _static
   },
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
  'cssfiles': ['_static/css/custom.css'],
  'navigation_depth': 2
}
html_show_sourcelink=False
html_copy_source=False
html_show_sphinx=False

def setup(app):
    app.add_css_file('css/custom.css')