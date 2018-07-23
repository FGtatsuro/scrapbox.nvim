#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import webbrowser


class ScrapboxHandler():

    def __init__(self, browser_name='chrome'):
        self.browser = webbrowser.get(browser_name)

    def access_page(self, title):
        self.browser.open(f"{os.environ['SCRAPBOX_PROJECT_URL']}/{title}")

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
