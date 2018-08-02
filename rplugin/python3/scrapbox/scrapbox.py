#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse

import webbrowser


class ScrapboxHandler():

    def __init__(self, nvim):
        self.nvim = nvim
        self.browser = webbrowser.get('chrome')

    def access_page(self, title, body):
        if 'scrapbox#project_url' not in self.nvim.vars:
            self.nvim.err_write(
                '[scrapbox] This plugin requires g:scrapbox#project_url\n',
                async_=True)
            return
        page_url = f"{self.nvim.vars['scrapbox#project_url']}/{title}"
        if body:
            page_url = f"{page_url}?{urllib.parse.urlencode({'body': body})}"
        self.browser.open(page_url)

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
