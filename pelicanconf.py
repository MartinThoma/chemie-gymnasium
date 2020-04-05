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

DIRECT_TEMPLATES = (('index', '404', 'impressum', 'links', 'projekt'))

STATIC_PATHS = ['bilder',
                'doc']

ARTICLE_URL = '{slug}.htm'
ARTICLE_SAVE_AS = '{slug}.htm'
PAGE_URL = '{slug}.htm'
PAGE_SAVE_AS = '{slug}.htm'

PLUGIN_PATHS = ['./pelican-toc',
                './pelican-sitemap',
                ]
PLUGINS = ['toc',
           'sitemap',
           'pelican_alias',
           ]


SITEMAP = {
    'exclude': ['tag/', 'category/',
                'tags.html', 'archives.html', 'categories.html'],
    'format': 'xml'
}

TOC = {'TOC_HEADERS': '^h[2-3]',
       'TOC_RUN': 'true'}

