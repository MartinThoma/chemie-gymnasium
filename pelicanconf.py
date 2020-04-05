#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Martin Thoma'
SITENAME = 'Chemie lernen'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'), )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/themoosemind'),
          ('Email', 'mailto:info@martin-thoma.de'),
          ('Github', 'https://github.com/MartinThoma'),
          ('Stackoverflow',
           'http://stackoverflow.com/users/562769/martin-thoma'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = './chemie-theme'

DIRECT_TEMPLATES = (('index', '404'))

STATIC_PATHS = ['bilder',
                'doc']
