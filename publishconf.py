#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

# from pelicanconf import *

SITEURL = 'https://chris.friedline.net'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = u'blog-cfriedline'

DISQUS_DISPLAY_COUNTS = True

GOOGLE_ANALYTICS = u'UA-42131442-1'

TIMEZONE = 'America/New_York'

STATIC_PATHS = ['extra/CNAME',
                'images',
                'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
