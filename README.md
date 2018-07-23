scrapbox.nvim
==================================================

[![Build Status](https://travis-ci.org/FGtatsuro/scrapbox.nvim.svg?branch=master)](https://travis-ci.org/FGtatsuro/scrapbox.nvim)

Neovim plugin to access Scrapbox(<https://scrapbox.io/>).

Requirements
------------

The dependencies on other softwares/libraries for this project. 
This software may work even if these requirements aren't met, but the behavior on that case can't be supported officially.

- Neovim (>= 0.3.x)
- Python (>= 3.7.x)

How to
------

1. Start Neovim with `SCRAPBOX_PROJECT_URL` as an environment variable.

```bash
SCRAPBOX_PROJECT_URL=<YOUR_PROJECT_URL> nvim
```

2. Access a scrapbox page via `ScrapboxAccessPage` command.
   The page with given name is opend via Webbrowser.

```
# In Neovim
:ScrapboxAccessPage vim
```

Development
-----------

1. Start Neovim with a config file to load a plugin of this project.

```bash
# FYI: https://github.com/neovim/python-client/blob/master/docs/usage/remote-plugins.rst
$ nvim -u tests/vimrc
```

2. Update the remote plugin manifest, and check futures of your plugin.

```
# In Neovim
:UpdateRemotePlugins
:(Run plugin's command/function/mapping and so on)
```
