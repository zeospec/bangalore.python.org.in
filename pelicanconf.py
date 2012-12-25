#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = u"kracekumar"
SITENAME = u"BangPypers"
SITEURL = 'http://bangalore.python.org.in'

#TIMEZONE = 'Asia/Kolkatta'

ARTICLE_URL = "blog/{date:%Y}/{date:%M}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%M}/{date:%d}/{slug}/index.html"

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
         )

# Social widget
SOCIAL = (('FaceBook Page', 'https://www.facebook.com/pages/BangPypers/160541007325160'),
          ('Twitter', '#'),
          ('BangPypers - Mailing List', 'http://mail.python.org/mailman/listinfo/bangpypers'),
          ('Meetup', '#'),)

# Using full path to make the generation work even when it is triggered from some other dir.
root = os.path.dirname(__file__)
THEME = os.path.join(root, 'theme')

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
DEFAULT_PAGINATION = 10
GITHUB_URL = "https://github.com/ipss/bangalore.python.org.in"
DISQUS_SITENAME = "bangpypers"
GOOGLE_ANALYTICS = "UA-36630036-1"

