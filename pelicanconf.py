#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Patrick Rodriguez'
SITENAME = 'stratospark'
SITEURL = ''
SITETITLE = 'stratospark'
SITESUBTITLE = 'programming for fun.'
SITEDESCRIPTION = 'programming for fun.'
SITELOGO = 'images/avatar.jpg'
FAVICON = 'images/favicon.ico'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

# Blogroll
LINKS = (('#1: Training Food Classifier with Keras/Tensorflow', '/deep-learning-applied-food-classification-deep-learning-keras.html'),
         ('#2: Multiprocess Image Augmentation', '/multiprocess-image-augmentation-keras.html'),
         ('#3: Serverless Uploads with AWS Lambda', '/secure-serverless-file-uploads-with-aws-lambda-s3-zappa.html'))

# Social widget
SOCIAL = (('github', 'https://github.com/stratospark'),
          ('twitter', 'https://twitter.com/stratospark'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = 'flex'

IPYNB_IGNORE_CSS = True
IPYNB_USE_META_SUMMARY = True

DISQUS_SITENAME = "stratospark"
