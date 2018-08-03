#!/usr/bin/env python
# -*- coding: utf-8 -*-

import neovim

from scrapbox.scrapbox import ScrapboxHandler


@neovim.plugin
class ScrapboxPlugin():

    def __init__(self, nvim):
        self.nvim = nvim
        # Note: In initialization phase(=in __init__ method), Neovim APIs mayn't be used properly.
        self.handler = ScrapboxHandler(self.nvim)

    @neovim.command('ScrapboxAccessPage', nargs='1', range='%')
    def access_page(self, args, range):
        title = args[0]
        start, end = range
        # range starts 1, but Neovim API to get lines accept 0 origin.
        body = '\n'.join(self.nvim.current.buffer[slice(start - 1, end)])
        self.handler.access_page(title, body)

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
