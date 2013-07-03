#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christopher J. Friedline'
SITENAME = u'Christopher J. Friedline, Ph.D.'
SITESUBTITLE = u"A postdoc's tale..."
SITEURL = 'http://chris.friedline.net'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Blogroll
LINKS =  (
('Eckert Lab', 'http://eckertlab.blogspot.com/'),
('Rivera Lab', 'http://riveralab.bio.vcu.edu/'),
('VCU Biology', 'http://www.biology.vcu.edu'),
('Evol.Fri', 'http://evolfri.blogspot.com'),
('The Tree of Life', 'http://phylogenomics.blogspot.com'),
('Living in an Ivory Basement', 'http://ivory.idyll.org/blog'),
('The Loom', 'http://phenomena.nationalgeographic.com/blog/the-loom/'),
('Not Exactly Rocket Science', 'http://phenomena.nationalgeographic.com/blog/not-exactly-rocket-science/'),
('Dechronization', 'http://treethinkers.blogspot.com'),
('TreeThinkers', 'http://treethinkers.org/blog/'),
)

# Social widget
SOCIAL = (
('Bitbucket', 'http://www.bitbucket.org/cfriedline'),
('Github', 'http://github.com/cfriedline'),
('Twitter', 'http://twitter.com/noituloveand'),
('Facebook', 'http://www.facebook.com/cfriedline'),
('LinkedIn', 'http://www.linkedin.com/in/friedline'),
)            
            
            
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TYPOGRIFY = True

DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_CATEGORY = u'Blog'

MENUITEMS = (('Home', "/"),)

PDF_GENERATOR = False

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

DISQUS_SITENAME = u'blog-cfriedline'

TWITTER_USERNAME = u'noituloveand'

GOOGLE_ANALYTICS = u'UA-42131442-1'

THEME = "themes/notmyidea-cjf"

PLUGIN_PATH = '/Users/chris/src/pelican-plugins'
PLUGINS=['sitemap',]

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

FILES_TO_COPY = (
('extra/CNAME', 'CNAME'),
('extra/google34b2553a47731679.html', 'google34b2553a47731679.html'),
)

