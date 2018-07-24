#!/usr/bin/env python
# -*- coding: utf-8 -*-

import neovim

from scrapbox.scrapbox import ScrapboxHandler


@neovim.plugin
class ScrapboxPlugin():

    def __init__(self, nvim):
        self.nvim = nvim
        self.handler = ScrapboxHandler()

    @neovim.command('ScrapboxTestCommand')
    def test_command(self):
        self.nvim.command('echo "TestCommand"')

    @neovim.command('ScrapboxAccessPage', nargs='+')
    def access_page(self, args):
        title = args[0]
        body = None
        if len(args) == 2:
            body = args[1]
        self.handler.access_page(title, body)

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
