#!/usr/bin/env python
# -*- coding: utf-8 -*-

import neovim


@neovim.plugin
class ScrapboxPlugin():

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('ScrapboxTestCommand')
    def test_command(self):
        self.nvim.command('echo "TestCommand"')

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
