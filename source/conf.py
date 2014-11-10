# -*- coding: utf-8 -*-
#

import sys
import os

# -- General configuration ------------------------------------------------

sys.path.append( os.path.abspath( '_themes/tesi' ) )

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.bibtex',
    'numfig', 'numsec'
]

number_figures = True
figure_caption_prefix = 'Figura'

todo_include_todos = True

templates_path = [ '_templates' ]
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
project = u'Tesi'
copyright = u'2014, Paolino Paperino'
version = '1.0'
release = '1.0'
language = 'it'
exclude_patterns = []
keep_warnings = True
default_role = 'code'
nitpicky = True
pygments_style = 'bw'

# -- Options for HTML output ----------------------------------------------

html_theme = 'tesi'
html_theme_path = [ '_themes' ]
html_use_smartypants = True
html_show_sourcelink = False
htmlhelp_basename = 'Tesi'
html_domain_indices = False
html_use_index = False
html_secnumber_suffix = " "

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
  'papersize': 'a4paper',
  'pointsize': '12pt',
  'babel': r'\usepackage[italian]{babel}',
  'fncychap': r'\usepackage[Sonny]{fncychap}',
  'fontpkg': r'\usepackage{times}',
  'inputenc': r'\usepackage[utf8]{inputenc}',
  'fontenc': r'\usepackage[T1]{fontenc}',
  'preamble': r'\fancypagestyle{normal}{\fancyhead[LE,RO]{}} \usepackage{setspace} \onehalfspacing',
  'maketitle': r'',
  'shorthandoff': r''
}

latex_documents = [
  ( 'index', 'Tesi.tex', u'Titolo della Tesi', u'Paolino Paperino', 'manual', True ),
]

latex_domain_indices = False
latex_use_modindex = False

latex_additional_files = [ 'frontespizio.tex_', 'images/minerva.jpg' ]

