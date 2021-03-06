#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christopher J. Friedline'
SITENAME = u'Christopher J. Friedline, Ph.D.'
SITESUBTITLE = u"will blog for tenure..."
SITEURL = 'http://chris.friedline.net'

READERS = {'html': None}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Blogroll
LINKS = (
    ('Eckert Lab', 'http://eckertlab.blogspot.com/'),
    ('Rivera Lab', 'http://riveralab.bio.vcu.edu/'),
    ('VCU Biology', 'http://www.biology.vcu.edu'),
    ('Evol.Fri', 'http://evolfri.blogspot.com'),
    ('Software Carpentry', 'http://www.software-carpentry.org'),
    ('The Tree of Life', 'http://phylogenomics.blogspot.com'),
    ('Living in an Ivory Basement', 'http://ivory.idyll.org/blog'),
    ('The Loom', 'http://phenomena.nationalgeographic.com/blog/the-loom/'),
    ('Dechronization', 'http://treethinkers.blogspot.com'),
    ('TreeThinkers', 'http://treethinkers.org/blog/'),
    ("Haldane's Sieve", 'http://haldanessieve.org'),)

# Social widget
SOCIAL = (('Bitbucket', 'http://www.bitbucket.org/cfriedline'),
          ('Github', 'http://github.com/cfriedline'),
          ('Twitter', 'http://twitter.com/noituloveand'),
          ('LinkedIn', 'http://www.linkedin.com/in/friedline'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TYPOGRIFY = True

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_PAGES_ON_MENU = False

DEFAULT_CATEGORY = u'Blog'

MENUITEMS = (('About', '/pages/about.html'),
             ('Funding', '/pages/funding.html'),
             ('Publications', '/pages/publications.html'),
             ('Contact', '/pages/contact.html'))

PDF_GENERATOR = False

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

TWITTER_USERNAME = u'noituloveand'

GOOGLE_ANALYTICS = u'UA-42131442-1'

THEME = "../pelican-themes/pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = ['sitemap', 'related_posts', 'latex', 'tag_cloud', 'i18n_subsites']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}

STATIC_PATHS = ['extra/CNAME',
                'images',
                'extra/favicon.ico',
                'extra/keybase.txt']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/keybase.txt': {'path': 'keybase.txt'}
}

BOOTSTRAP_THEME = "simplex"

# CUSTOM_CSS = "theme/css/custom.css"

DISPLAY_BREADCRUMBS = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

DISPLAY_TAGS_INLINE = True

CC_LICENSE = "CC-BY"

ADDTHIS_PROFILE = "ra-53d5b428043a2c47"

TWITTER_WIDGET_ID = "493588924690747392"

TWITTER_CARDS = True

# GITHUB_USER = "cfriedline"

# GITHUB_REPO_COUNT = 5

DISPLAY_CATEGORIES_ON_SIDEBAR = False

PYGMENTS_STYLE = "solarizeddark"

RELATED_POSTS_MAX = 5

TAG_CLOUD_STEPS = 4

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
