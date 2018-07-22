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

    @neovim.command('ScrapboxAccessPage', nargs=1)
    def access_page(self, args):
        title, = args
        self.handler.access_page(title)

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
